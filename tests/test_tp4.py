"""
TP4 : Tests pytest - Boucle while
Valide les 15 exercices
"""

import pytest
from tp4 import (
    resultat_ex1, resultat_ex2, resultat_ex3, resultat_ex4, resultat_ex5,
    resultat_ex6, resultat_ex7, resultat_ex8, resultat_ex9, resultat_ex10,
    resultat_ex11, resultat_ex12, resultat_ex13, resultat_ex14, resultat_ex15
)


class TestTP4:
    """Tests pour TP4 - Boucle while"""

    def test_ex1_compter_jusqua_n(self):
        """Ex1: Compter de 1 à 4 → [1, 2, 3, 4]"""
        assert resultat_ex1 == [1, 2, 3, 4]

    def test_ex2_compte_a_rebours(self):
        """Ex2: Compte à rebours de 4 → [4, 3, 2, 1, 0]"""
        assert resultat_ex2 == [4, 3, 2, 1, 0]

    def test_ex3_somme_1_a_n(self):
        """Ex3: Somme de 1 à 5 = 15"""
        assert resultat_ex3 == 15

    def test_ex4_longueur_sans_len(self):
        """Ex4: Longueur de 'algorithmique' sans len() = 13"""
        assert resultat_ex4 == 13

    def test_ex5_validation_saisie(self):
        """Ex5: [25, 0, 5, 7] → première valide (1-10) = 5 au 3ème essai"""
        assert isinstance(resultat_ex5, dict)
        assert resultat_ex5["valeur"] == 5
        assert resultat_ex5["essais"] == 3

    def test_ex6_chercher_caractere(self):
        """Ex6: 'y' dans 'python' sans in → 'Présent'"""
        assert resultat_ex6 == "Présent"

    def test_ex7_position_caractere(self):
        """Ex7: 'g' dans 'algorithmique' sans find()
        a(0) l(1) g(2) → position 2
        """
        assert resultat_ex7 == 2

    def test_ex8_compter_chiffres(self):
        """Ex8: 'Python3 est version 3.11' → 4 chiffres"""
        assert resultat_ex8 == 4

    def test_ex9_somme_chiffres_entier(self):
        """Ex9: 1234 → 1+2+3+4 = 10"""
        assert resultat_ex9 == 10

    def test_ex10_inverser_entier(self):
        """Ex10: 1234 → 4321"""
        assert resultat_ex10 == 4321

    def test_ex11_nombre_premier(self):
        """Ex11: 7 est premier → True"""
        assert resultat_ex11 == True

    def test_ex12_table_multiplication(self):
        """Ex12: table de 7 → liste de 10 chaînes '7 x N = R'"""
        assert isinstance(resultat_ex12, list)
        assert len(resultat_ex12) == 10
        assert "7 x 1 = 7" in resultat_ex12
        assert "7 x 10 = 70" in resultat_ex12

    def test_ex13_jeu_devinette(self):
        """Ex13: trouver 42 dans [50, 35, 42] → 3 essais"""
        assert resultat_ex13 == 3

    def test_ex14_factorielle(self):
        """Ex14: 5! = 120"""
        assert resultat_ex14 == 120

    def test_ex15_releve_notes(self):
        """Ex15: notes=[14,17,8,25,11,-1] → 4 valides, moy=12.5, max=17, min=8
        Note 25 rejetée (hors 0-20), -1 = fin de liste
        """
        assert isinstance(resultat_ex15, dict)
        assert resultat_ex15["nombre"] == 4
        assert resultat_ex15["moyenne"] == 12.5
        assert resultat_ex15["max"] == 17
        assert resultat_ex15["min"] == 8


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
