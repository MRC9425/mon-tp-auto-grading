"""
TP2 : Tests pytest
Valide les 13 exercices
"""

import pytest
from tp2 import (
    resultat_ex1, resultat_ex2, resultat_ex3, resultat_ex4, resultat_ex5,
    resultat_ex6, resultat_ex7, resultat_ex8, resultat_ex9, resultat_ex10,
    resultat_ex11, resultat_ex12, resultat_ex13
)


class TestTP2:
    """Tests pour TP2 - Manipulation des caractères"""
    
    def test_ex1_parcourir_chaine(self):
        """Ex1: Parcourir une chaîne"""
        assert resultat_ex1 == ['p', 'y', 't', 'h', 'o', 'n']
    
    def test_ex2_position_caracteres(self):
        """Ex2: Position des caractères"""
        assert isinstance(resultat_ex2, dict)
        assert resultat_ex2[0] == 'p'
        assert resultat_ex2[5] == 'n'
        assert len(resultat_ex2) == 13
    
    def test_ex3_code_ascii(self):
        """Ex3: Code ASCII"""
        assert resultat_ex3 == 65  # ord('A')
    
    def test_ex4_majuscule_minuscule(self):
        """Ex4: Majuscule ou minuscule"""
        assert resultat_ex4 == "majuscule"
    
    def test_ex5_est_chiffre(self):
        """Ex5: Est-ce un chiffre ?"""
        assert resultat_ex5 == True
    
    def test_ex6_compter_chiffres(self):
        """Ex6: Compter les chiffres"""
        assert resultat_ex6 == 4  # "Python3 est version 3.11" a 4 chiffres
    
    def test_ex7_somme_chiffres_text(self):
        """Ex7: Somme des chiffres d'un texte"""
        assert resultat_ex7 == 11  # 1 + 3 + 5 + 2
    
    def test_ex8_construire_nombre(self):
        """Ex8: Construire un nombre"""
        assert resultat_ex8 == 42
    
    def test_ex9_verifier_numerique(self):
        """Ex9: Vérifier entrée numérique"""
        assert resultat_ex9 == False  # "123abc456" contient des lettres
    
    def test_ex10_addition_texte(self):
        """Ex10: Addition de nombres texte"""
        assert resultat_ex10 == 15  # 12 + 3
    
    def test_ex11_extraire_chiffres(self):
        """Ex11: Extraire les chiffres"""
        assert resultat_ex11 == "1234"
    
    def test_ex12_inverser_nombre(self):
        """Ex12: Inverser un nombre"""
        assert resultat_ex12 == 8765
    
    def test_ex13_calculatrice_simple(self):
        """Ex13: Calculatrice simple"""
        assert resultat_ex13 == 15  # 12 + 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
