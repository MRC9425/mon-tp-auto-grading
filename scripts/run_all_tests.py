"""
run_all_tests.py - Lance les tests pytest pour tous les élèves
Version simplifiée et fonctionnelle
"""

import os
import sys
import subprocess
from pathlib import Path

def run_tests():
    """Lance les tests pour chaque élève"""
    
    print("="*60)
    print("🧪 Lancement des tests pour tous les élèves")
    print("="*60)
    
    eleves_dir = Path("eleves")
    tests_dir = Path("tests")
    
    if not eleves_dir.exists():
        print("❌ Dossier 'eleves' introuvable")
        return False
    
    total_passed = 0
    total_failed = 0
    
    # Parcourir chaque élève
    for student_dir in sorted(eleves_dir.iterdir()):
        if not student_dir.is_dir():
            continue
        
        student_name = student_dir.name
        print(f"\n👤 {student_name}")
        
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
            
            try:
                # Lancer pytest directement
                result = subprocess.run(
                    [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=no", "-q"],
                    capture_output=True,
                    text=True,
                    cwd=str(student_dir),
                    timeout=30
                )
                
                # Parser les résultats
                output = result.stdout + result.stderr
                
                # Compter les tests passés/échoués
                passed = output.count(" PASSED")
                failed = output.count(" FAILED")
                
                total_passed += passed
                total_failed += failed
                
                if result.returncode == 0:
                    print(f"✓ ({passed} tests)")
                else:
                    print(f"⚠️  ({passed}/{passed+failed} tests)")
                    
            except subprocess.TimeoutExpired:
                print("✗ (timeout)")
            except Exception as e:
                print(f"✗ Erreur: {e}")
    
    # Résumé final
    print("\n" + "="*60)
    print("📊 RÉSUMÉ FINAL")
    print("="*60)
    
    total_tests = total_passed + total_failed
    if total_tests > 0:
        percentage = (total_passed / total_tests) * 100
        print(f"Total : {total_passed}/{total_tests} tests ({percentage:.0f}%)")
    else:
        print("Aucun test exécuté")
    
    print("="*60)
    
    return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)