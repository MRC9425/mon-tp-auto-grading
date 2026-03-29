"""
setup_db.py - Initialise la base de données PostgreSQL
Crée les tables et schéma nécessaires
"""

import psycopg2
from psycopg2 import sql
import os
from datetime import datetime

# Configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'user': os.getenv('DB_USER', 'tp_user'),
    'password': os.getenv('DB_PASSWORD', 'tp_password'),
    'database': os.getenv('DB_NAME', 'tp_grading'),
}

def create_tables():
    """Crée les tables de la base de données"""
    
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        print("📊 Création des tables PostgreSQL...")
        
        # Table: eleves
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS eleves (
                id SERIAL PRIMARY KEY,
                nom VARCHAR(100) UNIQUE NOT NULL,
                email VARCHAR(100),
                date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                actif BOOLEAN DEFAULT TRUE
            );
        """)
        print("✓ Table 'eleves' créée")
        
        # Table: resultats
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resultats (
                id SERIAL PRIMARY KEY,
                eleve_id INTEGER NOT NULL REFERENCES eleves(id),
                tp_name VARCHAR(50) NOT NULL,
                exercice_num INTEGER NOT NULL,
                statut VARCHAR(20) NOT NULL, -- PASSED, FAILED, NOT_DONE
                score INTEGER DEFAULT 0,
                details TEXT,
                date_test TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                commit_sha VARCHAR(40),
                branch VARCHAR(100) DEFAULT 'main',
                UNIQUE(eleve_id, tp_name, exercice_num, date_test)
            );
        """)
        print("✓ Table 'resultats' créée")
        
        # Table: tp_metadata
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tp_metadata (
                id SERIAL PRIMARY KEY,
                tp_name VARCHAR(50) UNIQUE NOT NULL,
                nombre_exercices INTEGER,
                description TEXT,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("✓ Table 'tp_metadata' créée")
        
        # Table: statistiques (view materializée)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS statistiques (
                id SERIAL PRIMARY KEY,
                eleve_id INTEGER NOT NULL REFERENCES eleves(id),
                tp_name VARCHAR(50),
                nombre_exos_total INTEGER,
                nombre_exos_passes INTEGER,
                nombre_exos_echoues INTEGER,
                nombre_exos_non_faits INTEGER,
                pourcentage_reussite FLOAT,
                date_calcul TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("✓ Table 'statistiques' créée")
        
        # Index pour les performances
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_resultats_eleve 
            ON resultats(eleve_id);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_resultats_tp 
            ON resultats(tp_name);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_resultats_date 
            ON resultats(date_test);
        """)
        print("✓ Index créés")
        
        # Insérer les TPs de base
        cursor.execute("""
            INSERT INTO tp_metadata (tp_name, nombre_exercices, description)
            VALUES 
                ('tp1', 10, 'Variables et types'),
                ('tp2', 9, 'Chaînes de caractères'),
                ('tp3', 15, 'Algorithmique sur les chaînes'),
                ('tp4', 15, 'Boucles while'),
                ('tp5', 12, 'Listes et structures'),
                ('tp6', 10, 'Dictionnaires'),
                ('tp7', 15, 'Fonctions'),
                ('tp8', 12, 'Fichiers'),
                ('tp9', 10, 'Modules'),
                ('tp10', 8, 'Programmation objet')
            ON CONFLICT (tp_name) DO NOTHING;
        """)
        print("✓ Métadonnées des TPs insérées")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("\n✅ Base de données prête !")
        return True
        
    except psycopg2.Error as e:
        print(f"❌ Erreur PostgreSQL : {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur : {e}")
        return False


if __name__ == "__main__":
    print("="*60)
    print("Setup PostgreSQL pour Auto-Grading")
    print("="*60)
    
    success = create_tables()
    
    if success:
        print("\n🎉 Base de données initialisée avec succès !")
    else:
        print("\n⚠️ Erreur lors de l'initialisation")
