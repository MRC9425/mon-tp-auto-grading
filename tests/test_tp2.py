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
        """Ex1: Parcourir une chaîne → liste de caractères"""
        assert resultat_ex1 == ['p', 'y', 't', 'h', 'o', 'n']

    def test_ex2_position_caracteres(self):
        """Ex2: Position des caractères dans 'programmation'
        p(0) r(1) o(2) g(3) r(4) a(5) m(6) m(7) a(8) t(9) i(10) o(11) n(12)
        """
        assert isinstance(resultat_ex2, dict)
        assert len(resultat_ex2) == 13
        assert resultat_ex2[0] == 'p'
        assert resultat_ex2[5] == 'a'   # CORRIGÉ : 'a' pas 'n'
        assert resultat_ex2[12] == 'n'  # 'n' est en position 12

    def test_ex3_code_ascii(self):
        """Ex3: Code ASCII de 'A' = 65"""
        assert resultat_ex3 == 65

    def test_ex4_majuscule_minuscule(self):
        """Ex4: 'B' est une majuscule"""
        assert resultat_ex4 == "majuscule"

    def test_ex5_est_chiffre(self):
        """Ex5: '5' est un chiffre → True"""
        assert resultat_ex5 == True

    def test_ex6_compter_chiffres(self):
        """Ex6: 'Python3 est version 3.11' → 4 chiffres (3, 3, 1, 1)"""
        assert resultat_ex6 == 4

    def test_ex7_somme_chiffres_text(self):
        """Ex7: '1352' → 1 + 3 + 5 + 2 = 11"""
        assert resultat_ex7 == 11

    def test_ex8_construire_nombre(self):
        """Ex8: '42' → 42 (sans int())"""
        assert resultat_ex8 == 42

    def test_ex9_verifier_numerique(self):
        """Ex9: '123abc456' contient des lettres → False"""
        assert resultat_ex9 == False

    def test_ex10_addition_texte(self):
        """Ex10: 12 + 3 = 15"""
        assert resultat_ex10 == 15

    def test_ex11_extraire_chiffres(self):
        """Ex11: 1234 → '1234'"""
        assert resultat_ex11 == "1234"

    def test_ex12_inverser_nombre(self):
        """Ex12: 5678 → 8765"""
        assert resultat_ex12 == 8765

    def test_ex13_calculatrice_simple(self):
        """Ex13: '12+3' → 15"""
        assert resultat_ex13 == 15


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
