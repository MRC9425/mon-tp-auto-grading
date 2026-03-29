"""
run_all_tests.py - Lance pytest pour tous les élèves
Génère un rapport JSON avec les résultats
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

def run_tests_for_students():
    """Lance les tests pour chaque élève et élève"""
    
    print("="*60)
    print("🧪 Lancement des tests pour tous les élèves")
    print("="*60)
    
    eleves_dir = Path("eleves")
    tests_dir = Path("tests")
    
    if not eleves_dir.exists():
        print("❌ Dossier 'eleves' introuvable")
        return False
    
    if not tests_dir.exists():
        print("❌ Dossier 'tests' introuvable")
        return False
    
    all_results = {
        'timestamp': datetime.now().isoformat(),
        'students': {}
    }
    
    # Parcourir chaque élève
    for student_dir in sorted(eleves_dir.iterdir()):
        if not student_dir.is_dir():
            continue
        
        student_name = student_dir.name
        print(f"\n👤 {student_name}")
        all_results['students'][student_name] = {}
        
        # Parcourir chaque TP
        tp_files = sorted(student_dir.glob("tp*.py"))
        
        for tp_file in tp_files:
            tp_name = tp_file.stem  # tp3, tp4, etc.
            tp_num = tp_name.replace('tp', '')
            
            # Chercher le fichier de test correspondant
            test_file = tests_dir / f"test_{tp_name}.py"
            
            if not test_file.exists():
                print(f"  ⚠️  {tp_name}: Pas de test trouvé")
                continue
            
            print(f"  📝 {tp_name}...", end=" ", flush=True)
            
            # Créer un fichier tp.py temporaire dans le répertoire de l'élève
            temp_tp = student_dir / "tp.py"
            
            try:
                # Copier le fichier pour les tests
                with open(tp_file, 'r') as src:
                    with open(temp_tp, 'w') as dst:
                        dst.write(src.read())
                
                # Lancer pytest
                result = subprocess.run(
                    [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=short"],
                    capture_output=True,
                    text=True,
                    cwd=str(student_dir)
                )
                
                # Parser les résultats
                output = result.stdout + result.stderr
                
                # Compter les tests passés/échoués
                if "passed" in output:
                    # Extraire le nombre de tests
                    import re
                    match = re.search(r'(\d+) passed', output)
                    passed = int(match.group(1)) if match else 0
                else:
                    passed = 0
                
                if "failed" in output:
                    import re
                    match = re.search(r'(\d+) failed', output)
                    failed = int(match.group(1)) if match else 0
                else:
                    failed = 0
                
                all_results['students'][student_name][tp_name] = {
                    'passed': passed,
                    'failed': failed,
                    'total': passed + failed,
                    'return_code': result.returncode
                }
                
                if result.returncode == 0:
                    print(f"✓ ({passed} tests)")
                else:
                    print(f"✗ ({passed}/{passed+failed} tests)")
                
            except Exception as e:
                print(f"✗ Erreur: {e}")
                all_results['students'][student_name][tp_name] = {
                    'error': str(e)
                }
            
            finally:
                # Nettoyer le fichier temporaire
                if temp_tp.exists():
                    temp_tp.unlink()
    
    # Sauvegarder les résultats
    results_file = Path("test_results.json")
    with open(results_file, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n✅ Résultats sauvegardés dans {results_file}")
    
    # Afficher un résumé
    print("\n" + "="*60)
    print("📊 RÉSUMÉ")
    print("="*60)
    
    total_students = len(all_results['students'])
    print(f"Nombre d'élèves : {total_students}")
    
    total_passed = 0
    total_failed = 0
    
    for student, tps in all_results['students'].items():
        student_passed = 0
        student_failed = 0
        
        for tp, result in tps.items():
            if 'passed' in result:
                student_passed += result['passed']
                student_failed += result['failed']
        
        total_passed += student_passed
        total_failed += student_failed
        
        if student_passed + student_failed > 0:
            percentage = (student_passed / (student_passed + student_failed)) * 100
            print(f"  {student:15s} : {student_passed:2d}/{student_passed + student_failed:2d} tests ({percentage:.0f}%)")
    
    print("="*60)
    if total_passed + total_failed > 0:
        total_percentage = (total_passed / (total_passed + total_failed)) * 100
        print(f"Total : {total_passed}/{total_passed + total_failed} tests ({total_percentage:.0f}%)")
    
    return True


if __name__ == "__main__":
    success = run_tests_for_students()
    sys.exit(0 if success else 1)
