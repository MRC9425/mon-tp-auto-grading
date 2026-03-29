"""
save_results.py - Enregistre les résultats des tests dans PostgreSQL
Lance les tests pour chaque élève et enregistre les résultats
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
import psycopg2
from psycopg2 import sql
import importlib.util

# Configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'user': os.getenv('DB_USER', 'tp_user'),
    'password': os.getenv('DB_PASSWORD', 'tp_password'),
    'database': os.getenv('DB_NAME', 'tp_grading'),
}

class TestRunner:
    def __init__(self):
        self.results = {}
        self.conn = None
        
    def connect_db(self):
        """Connecte à PostgreSQL"""
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            return True
        except psycopg2.Error as e:
            print(f"❌ Erreur de connexion BD : {e}")
            return False
    
    def get_or_create_student(self, student_name, cursor):
        """Obtient ou crée un élève dans la BD"""
        try:
            cursor.execute("SELECT id FROM eleves WHERE nom = %s", (student_name,))
            result = cursor.fetchone()
            
            if result:
                return result[0]
            else:
                cursor.execute(
                    "INSERT INTO eleves (nom, email) VALUES (%s, %s) RETURNING id",
                    (student_name, f"{student_name}@cf2m.be")
                )
                return cursor.fetchone()[0]
        except psycopg2.Error as e:
            print(f"❌ Erreur BD : {e}")
            return None
    
    def run_tp_tests(self, student_name, tp_name, tp_path):
        """Lance les tests pour un TP spécifique d'un élève"""
        try:
            # Importer le module du student
            spec = importlib.util.spec_from_file_location(tp_name, tp_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            results = {}
            
            # Vérifier les 15 exercices
            for i in range(1, 16):
                var_name = f"resultat_ex{i}"
                if hasattr(module, var_name):
                    value = getattr(module, var_name)
                    results[i] = {
                        'existe': True,
                        'value': value,
                        'statut': 'PASSED' if value is not None else 'NOT_DONE'
                    }
                else:
                    results[i] = {
                        'existe': False,
                        'value': None,
                        'statut': 'NOT_DONE'
                    }
            
            return results
            
        except Exception as e:
            print(f"⚠️ Erreur lors du test de {student_name}/{tp_name} : {e}")
            return None
    
    def save_to_db(self, student_name, tp_name, results):
        """Enregistre les résultats dans PostgreSQL"""
        if not self.conn or results is None:
            return False
        
        try:
            cursor = self.conn.cursor()
            
            # Obtenir/créer l'élève
            student_id = self.get_or_create_student(student_name, cursor)
            if not student_id:
                return False
            
            # Insérer les résultats pour chaque exercice
            for ex_num, ex_result in results.items():
                cursor.execute("""
                    INSERT INTO resultats 
                    (eleve_id, tp_name, exercice_num, statut, score, details, commit_sha)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT DO NOTHING;
                """, (
                    student_id,
                    tp_name,
                    ex_num,
                    ex_result['statut'],
                    1 if ex_result['statut'] == 'PASSED' else 0,
                    json.dumps(ex_result),
                    os.getenv('GITHUB_SHA', 'local')
                ))
            
            self.conn.commit()
            print(f"  ✓ {student_name}/{tp_name} enregistré")
            return True
            
        except psycopg2.Error as e:
            print(f"  ❌ Erreur BD : {e}")
            self.conn.rollback()
            return False
    
    def run_all_tests(self):
        """Lance tous les tests pour tous les élèves"""
        print("\n" + "="*60)
        print("Lancement des tests pour tous les élèves")
        print("="*60)
        
        if not self.connect_db():
            return False
        
        eleves_dir = Path("eleves")
        if not eleves_dir.exists():
            print("❌ Dossier 'eleves' introuvable")
            return False
        
        # Parcourir chaque élève
        for student_dir in sorted(eleves_dir.iterdir()):
            if not student_dir.is_dir():
                continue
            
            student_name = student_dir.name
            print(f"\n👤 {student_name}")
            
            # Parcourir chaque TP
            for tp_file in sorted(student_dir.glob("tp*.py")):
                tp_name = tp_file.stem  # tp3, tp4, etc.
                
                print(f"  📝 {tp_name}...", end=" ")
                
                # Lancer les tests
                results = self.run_tp_tests(student_name, tp_name, str(tp_file))
                
                if results:
                    # Enregistrer dans la BD
                    if self.save_to_db(student_name, tp_name, results):
                        # Compter les résultats
                        passed = sum(1 for r in results.values() if r['statut'] == 'PASSED')
                        total = len(results)
                        print(f"✓ ({passed}/{total})")
                    else:
                        print("✗ (erreur BD)")
                else:
                    print("✗ (erreur test)")
        
        if self.conn:
            self.conn.close()
        
        print("\n✅ Tests terminés !")
        return True


def main():
    runner = TestRunner()
    success = runner.run_all_tests()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
