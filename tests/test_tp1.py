"""
TP1 : Tests pytest
Valide les 15 exercices
"""

import pytest
from tp1 import (
    resultat_ex1, resultat_ex2, resultat_ex3, resultat_ex4, resultat_ex5,
    resultat_ex6, resultat_ex7, resultat_ex8, resultat_ex9, resultat_ex10,
    resultat_ex11, resultat_ex12, resultat_ex13, resultat_ex14, resultat_ex15
)


class TestTP1:
    """Tests pour TP1 - Introduction à Python"""
    
    def test_ex1_affichage_message(self):
        """Ex1: Afficher un message"""
        assert resultat_ex1 == "Bienvenue dans la formation Python !"
    
    def test_ex2_affichage_plusieurs_lignes(self):
        """Ex2: Afficher plusieurs lignes"""
        expected = """Bonjour !
Bienvenue dans le monde de la programmation Python.
Amusez-vous bien !"""
        assert resultat_ex2 == expected
    
    def test_ex3_addition_simple(self):
        """Ex3: Addition simple (5 + 3 = 8)"""
        assert resultat_ex3 == 8
        assert isinstance(resultat_ex3, int)
    
    def test_ex4_variable_et_message(self):
        """Ex4: Créer et afficher une variable"""
        assert resultat_ex4 == "Bonjour, Alice !"
    
    def test_ex5_concatenation_chaines(self):
        """Ex5: Concaténation de chaînes"""
        assert resultat_ex5 == "Bonjour, Alice Dupont !"
    
    def test_ex6_multiplication(self):
        """Ex6: Multiplier des nombres (7 * 8 = 56)"""
        assert resultat_ex6 == 56
    
    def test_ex7_division_flottante(self):
        """Ex7: Division avec résultat flottant (10 / 3 ≈ 3.333)"""
        assert isinstance(resultat_ex7, float)
        assert 3.3 < resultat_ex7 < 3.34
    
    def test_ex8_modulo(self):
        """Ex8: Calculer le reste (15 % 4 = 3)"""
        assert resultat_ex8 == 3
    
    def test_ex9_conversion_types(self):
        """Ex9: Conversion de types et message"""
        assert resultat_ex9 == "Vous avez 25 ans."
    
    def test_ex10_type_variable(self):
        """Ex10: Afficher le type d'une variable"""
        assert "3.14" in resultat_ex10
        assert "float" in resultat_ex10
    
    def test_ex11_majuscules(self):
        """Ex11: Transformer en majuscules"""
        assert resultat_ex11 == "FORMATION PYTHON"
    
    def test_ex12_longueur_chaine(self):
        """Ex12: Longueur d'une chaîne"""
        assert resultat_ex12 == 16
        assert isinstance(resultat_ex12, int)
    
    def test_ex13_celsius_fahrenheit(self):
        """Ex13: Convertir Celsius en Fahrenheit (0°C = 32°F)"""
        assert resultat_ex13 == 32.0
    
    def test_ex14_operations(self):
        """Ex14: Opérations arithmétiques"""
        assert isinstance(resultat_ex14, dict)
        assert resultat_ex14["addition"] == 17
        assert resultat_ex14["soustraction"] == 7
        assert resultat_ex14["multiplication"] == 60
        assert resultat_ex14["division"] == 2.4
    
    def test_ex15_operations_combinees(self):
        """Ex15: Opérations combinées ((5 + 3) * 2 = 16)"""
        assert resultat_ex15 == 16


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
