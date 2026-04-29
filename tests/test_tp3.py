"""
TP3 : Tests pytest
Valide les 15 exercices
"""

import pytest
from tp3 import (
    resultat_ex1, resultat_ex2, resultat_ex3, resultat_ex4, resultat_ex5,
    resultat_ex6, resultat_ex7, resultat_ex8, resultat_ex9, resultat_ex10,
    resultat_ex11, resultat_ex12, resultat_ex13, resultat_ex14, resultat_ex15
)


class TestTP3:
    """Tests pour TP3 - Algorithmique sur les chaînes"""
    
    def test_ex1_parcourir_chaine(self):
        """Ex1: Parcourir une chaîne"""
        assert resultat_ex1 == list("algorithmique")
    
    def test_ex2_compter_lettre(self):
        """Ex2: Compter une lettre"""
        assert resultat_ex2 == 2  # 'a' dans "programmation"
    
    def test_ex3_compter_voyelles(self):
        """Ex3: Compter les voyelles"""
        assert resultat_ex3 == 4  # o, o, u dans "bonjour"
    
    def test_ex4_inverser_chaine(self):
        """Ex4: Inverser une chaîne"""
        assert resultat_ex4 == "olleh"
    
    def test_ex5_palindrome(self):
        """Ex5: Vérifier un palindrome"""
        assert resultat_ex5 == True
    
    def test_ex6_compter_mots(self):
        """Ex6: Compter les mots"""
        assert resultat_ex6 == 4
    
    def test_ex7_supprimer_espaces_extremes(self):
        """Ex7: Supprimer espaces début et fin"""
        assert resultat_ex7 == "Bonjour le monde"
    
    def test_ex8_mot_le_plus_long(self):
        """Ex8: Trouver le mot le plus long"""
        assert len(resultat_ex8) == 7  # "Bonjour" ou "monde"
    
    def test_ex9_supprimer_espaces_multiples(self):
        """Ex9: Supprimer espaces multiples"""
        assert resultat_ex9 == "Bonjour tout le monde"
    
    def test_ex10_inverser_mots(self):
        """Ex10: Inverser les mots"""
        assert resultat_ex10 == "genial est Python"
    
    def test_ex11_supprimer_consecutifs(self):
        """Ex11: Supprimer caractères consécutifs"""
        assert resultat_ex11 == "bonjour"
    
    def test_ex12_compression_chaine(self):
        """Ex12: Compression simple"""
        assert resultat_ex12 == "a3b2c1"
    
    def test_ex13_parentheses_equilibrees(self):
        """Ex13: Vérifier parenthèses équilibrées"""
        assert resultat_ex13 == True
    
    def test_ex14_anagrammes(self):
        """Ex14: Vérifier anagrammes"""
        assert resultat_ex14 == True
    
    def test_ex15_analyseur_phrase(self):
        """Ex15: Analyseur de phrase"""
        assert isinstance(resultat_ex15, dict)
        assert resultat_ex15["nombre_mots"] == 6
        assert resultat_ex15["nombre_caracteres"] == 24  # Sans espaces


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
