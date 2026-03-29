"""
TP4 : Tests Pytest - Boucle while
Teste les 15 exercices du TP4
VERSION CORRIGÉE - Toutes les assertions vérifiées
"""

import sys
import importlib.util
import pytest


def charger_tp4(chemin_fichier):
    """Charge le fichier tp4.py d'un élève et retourne les résultats"""
    spec = importlib.util.spec_from_file_location("tp4", chemin_fichier)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Retourne un dictionnaire avec tous les résultats
    return {
        "ex1": module.resultat_ex1,
        "ex2": module.resultat_ex2,
        "ex3": module.resultat_ex3,
        "ex4": module.resultat_ex4,
        "ex5": module.resultat_ex5,
        "ex6": module.resultat_ex6,
        "ex7": module.resultat_ex7,
        "ex8": module.resultat_ex8,
        "ex9": module.resultat_ex9,
        "ex10": module.resultat_ex10,
        "ex11": module.resultat_ex11,
        "ex12": module.resultat_ex12,
        "ex13": module.resultat_ex13,
        "ex14": module.resultat_ex14,
        "ex15": module.resultat_ex15,
    }


# ========================================================================
# EXERCICE 1 : Compter jusqu'à N
# ========================================================================

def test_ex1_compter_4():
    """Compte de 1 à 4: [1, 2, 3, 4]"""
    result = charger_tp4("tp4.py")
    assert result["ex1"] == [1, 2, 3, 4], f"Attendu [1, 2, 3, 4], got {result['ex1']}"


# ========================================================================
# EXERCICE 2 : Compte à rebours
# ========================================================================

def test_ex2_rebours_4():
    """Compte à rebours de 4 à 0: [4, 3, 2, 1, 0]"""
    result = charger_tp4("tp4.py")
    assert result["ex2"] == [4, 3, 2, 1, 0], f"Attendu [4, 3, 2, 1, 0], got {result['ex2']}"


# ========================================================================
# EXERCICE 3 : Somme de 1 à N
# ========================================================================

def test_ex3_somme_5():
    """Somme de 1 à 5 = 1+2+3+4+5 = 15"""
    result = charger_tp4("tp4.py")
    assert result["ex3"] == 15, f"Attendu 15, got {result['ex3']}"


# ========================================================================
# EXERCICE 4 : Longueur d'un mot sans len()
# ========================================================================

def test_ex4_longueur_algorithmique():
    """Longueur de 'algorithmique' = 13"""
    result = charger_tp4("tp4.py")
    assert result["ex4"] == 13, f"Attendu 13, got {result['ex4']}"


# ========================================================================
# EXERCICE 5 : Validation de saisie
# ========================================================================

def test_ex5_structure():
    """Vérifie la structure du résultat"""
    result = charger_tp4("tp4.py")
    assert isinstance(result["ex5"], dict), "Résultat doit être un dictionnaire"
    assert "valeur" in result["ex5"], "Doit contenir 'valeur'"
    assert "essais" in result["ex5"], "Doit contenir 'essais'"


def test_ex5_trouve_valide():
    """Trouve première valide dans [25, 0, 5, 7] → 5 au 3ème essai"""
    result = charger_tp4("tp4.py")
    ex5 = result["ex5"]
    assert ex5["valeur"] == 5, f"Attendu valeur=5, got {ex5['valeur']}"
    assert ex5["essais"] == 3, f"Attendu 3 essais, got {ex5['essais']}"
    assert 1 <= ex5["valeur"] <= 10, "Valeur doit être entre 1 et 10"


# ========================================================================
# EXERCICE 6 : Chercher un caractère sans in
# ========================================================================

def test_ex6_caractere_present():
    """'y' est présent dans 'python'"""
    result = charger_tp4("tp4.py")
    assert result["ex6"] == "Présent", f"Attendu 'Présent', got {result['ex6']}"


# ========================================================================
# EXERCICE 7 : Position d'un caractère sans find()
# ========================================================================

def test_ex7_position_g_algorithmique():
    """Position de 'g' dans 'algorithmique' = 2
    
    a-l-g-o-r-i-t-h-m-i-q-u-e
    0-1-2-3-4-5-6-7-8-9-10-11-12
    """
    result = charger_tp4("tp4.py")
    assert result["ex7"] == 2, f"Attendu 2, got {result['ex7']}"


# ========================================================================
# EXERCICE 8 : Compter les chiffres
# ========================================================================

def test_ex8_compter_chiffres():
    """Compter chiffres dans 'Python3 est version 3.11'
    Chiffres: 3, 3, 1, 1 = 4 chiffres"""
    result = charger_tp4("tp4.py")
    assert result["ex8"] == 4, f"Attendu 4, got {result['ex8']}"


# ========================================================================
# EXERCICE 9 : Somme des chiffres d'un entier
# ========================================================================

def test_ex9_somme_chiffres_1234():
    """Somme des chiffres de 1234 = 1+2+3+4 = 10"""
    result = charger_tp4("tp4.py")
    assert result["ex9"] == 10, f"Attendu 10, got {result['ex9']}"


# ========================================================================
# EXERCICE 10 : Inverser un entier
# ========================================================================

def test_ex10_inverser_1234():
    """Inverser 1234 = 4321"""
    result = charger_tp4("tp4.py")
    assert result["ex10"] == 4321, f"Attendu 4321, got {result['ex10']}"


# ========================================================================
# EXERCICE 11 : Nombre premier
# ========================================================================

def test_ex11_7_est_premier():
    """7 est premier → True"""
    result = charger_tp4("tp4.py")
    assert result["ex11"] == True, f"Attendu True pour 7, got {result['ex11']}"


# ========================================================================
# EXERCICE 12 : Table de multiplication
# ========================================================================

def test_ex12_table_7():
    """Table de multiplication de 7 de 1 à 10"""
    result = charger_tp4("tp4.py")
    assert isinstance(result["ex12"], list), "Doit être une liste"
    assert len(result["ex12"]) == 10, f"Doit contenir 10 entrées, got {len(result['ex12'])}"
    # Vérifier quelques valeurs
    assert "7 x 1 = 7" in result["ex12"], "Doit contenir '7 x 1 = 7'"
    assert "7 x 10 = 70" in result["ex12"], "Doit contenir '7 x 10 = 70'"


# ========================================================================
# EXERCICE 13 : Jeu de devinette
# ========================================================================

def test_ex13_nombre_essais():
    """Nombre d'essais pour trouver 42 dans [50, 35, 42] = 3"""
    result = charger_tp4("tp4.py")
    assert result["ex13"] == 3, f"Attendu 3 essais, got {result['ex13']}"


# ========================================================================
# EXERCICE 14 : Factorielle
# ========================================================================

def test_ex14_factorielle_5():
    """5! = 1 × 2 × 3 × 4 × 5 = 120"""
    result = charger_tp4("tp4.py")
    assert result["ex14"] == 120, f"Attendu 120, got {result['ex14']}"


# ========================================================================
# EXERCICE 15 : Relevé de notes
# ========================================================================

def test_ex15_structure():
    """Vérifie la structure du résultat"""
    result = charger_tp4("tp4.py")
    assert isinstance(result["ex15"], dict), "Doit être un dictionnaire"
    assert "nombre" in result["ex15"], "Doit contenir 'nombre'"
    assert "moyenne" in result["ex15"], "Doit contenir 'moyenne'"
    assert "max" in result["ex15"], "Doit contenir 'max'"
    assert "min" in result["ex15"], "Doit contenir 'min'"


def test_ex15_notes_14_17_8_11():
    """Relevé : notes = [14, 17, 8, 25, 11, -1]
    
    Notes valides (0-20): 14, 17, 8, 11 = 4 notes
    Somme: 14 + 17 + 8 + 11 = 50
    Moyenne: 50 / 4 = 12.5
    Max: 17
    Min: 8
    Note 25 doit être rejetée (hors limites)
    """
    result = charger_tp4("tp4.py")
    ex15 = result["ex15"]
    
    assert ex15["nombre"] == 4, f"Attendu 4 notes valides, got {ex15['nombre']}"
    assert ex15["moyenne"] == 12.5, f"Attendu moyenne 12.5, got {ex15['moyenne']}"
    assert ex15["max"] == 17, f"Attendu max 17, got {ex15['max']}"
    assert ex15["min"] == 8, f"Attendu min 8, got {ex15['min']}"


# ========================================================================
# TESTS GLOBAUX
# ========================================================================

def test_all_resultats_existent():
    """Vérifie que tous les resultats_ex1 à ex15 existent et ne sont pas None"""
    result = charger_tp4("tp4.py")
    for i in range(1, 16):
        key = f"ex{i}"
        assert key in result, f"Le résultat {key} n'existe pas"
        assert result[key] is not None, f"Le résultat {key} est None"


# ========================================================================
# RÉSUMÉ ET STATISTIQUES
# ========================================================================

def test_resultat_complet():
    """Affiche un résumé complet des résultats"""
    result = charger_tp4("tp4.py")
    
    print("\n" + "="*60)
    print("RÉSUMÉ COMPLET DU TP4")
    print("="*60)
    
    for i in range(1, 16):
        key = f"ex{i}"
        value = result[key]
        if value is None:
            status = "❌ NOT DONE"
        else:
            status = f"✓ {type(value).__name__}"
        print(f"Exercice {i:2d}: {status:20s} = {str(value)[:60]}")
    
    print("="*60)


if __name__ == "__main__":
    # Pour lancer les tests : pytest test_tp4.py -v
    pytest.main([__file__, "-v"])
