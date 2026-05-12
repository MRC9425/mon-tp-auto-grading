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
        """Ex1: 'algorithmique' → liste de caractères"""
        assert resultat_ex1 == list("algorithmique")

    def test_ex2_compter_lettre(self):
        """Ex2: 'a' dans 'programmation' → 2 fois"""
        assert resultat_ex2 == 2

    def test_ex3_compter_voyelles(self):
        """Ex3: voyelles dans 'bonjour' (a,e,i,o,u,y) → o, o, u = 3
        b(0) o(1) n(2) j(3) o(4) u(5) r(6)
        """
        assert resultat_ex3 == 3  # CORRIGÉ : 3 pas 4

    def test_ex4_inverser_chaine(self):
        """Ex4: 'hello' → 'olleh'"""
        assert resultat_ex4 == "olleh"

    def test_ex5_palindrome(self):
        """Ex5: 'radar' est un palindrome → True"""
        assert resultat_ex5 == True

    def test_ex6_compter_mots(self):
        """Ex6: 'Bonjour tout le monde' → 4 mots"""
        assert resultat_ex6 == 4

    def test_ex7_supprimer_espaces_extremes(self):
        """Ex7: '  Bonjour le monde  ' → 'Bonjour le monde'"""
        assert resultat_ex7 == "Bonjour le monde"

    def test_ex8_mot_le_plus_long(self):
        """Ex8: dans 'Bonjour tout le monde' → 'Bonjour' (7 lettres)"""
        assert len(resultat_ex8) == 7

    def test_ex9_supprimer_espaces_multiples(self):
        """Ex9: 'Bonjour  tout   le    monde' → 'Bonjour tout le monde'"""
        assert resultat_ex9 == "Bonjour tout le monde"

    def test_ex10_inverser_mots(self):
        """Ex10: 'Python est genial' → 'genial est Python'"""
        assert resultat_ex10 == "genial est Python"

    def test_ex11_supprimer_consecutifs(self):
        """Ex11: 'booonnjooour' → 'bonjour'"""
        assert resultat_ex11 == "bonjour"

    def test_ex12_compression_chaine(self):
        """Ex12: 'aaabbc' → 'a3b2c1'"""
        assert resultat_ex12 == "a3b2c1"

    def test_ex13_parentheses_equilibrees(self):
        """Ex13: '(a + b) * (c - d)' → True"""
        assert resultat_ex13 == True

    def test_ex14_anagrammes(self):
        """Ex14: 'listen' et 'silent' → True"""
        assert resultat_ex14 == True

    def test_ex15_analyseur_phrase(self):
        """Ex15: 'Bonjour tout le monde avec tous'
        - 6 mots
        - 26 caractères sans espaces : Bonjour(7)+tout(4)+le(2)+monde(5)+avec(4)+tous(4) = 26
        """
        assert isinstance(resultat_ex15, dict)
        assert resultat_ex15["nombre_mots"] == 6
        assert resultat_ex15["nombre_caracteres"] == 26  # CORRIGÉ : 26 pas 24


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
