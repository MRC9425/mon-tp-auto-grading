"""
TP1 : Introduction à Python
Template à remplir par les élèves
"""

# ==================== DONNÉES DE TEST ====================
# NE PAS MODIFIER - Les données utilisées pour les tests

donnees = {
    "ex3_a": 5,
    "ex3_b": 3,
    "ex5_prenom": "Alice",
    "ex5_nom": "Dupont",
    "ex6_x": 7,
    "ex6_y": 8,
    "ex7_a": 10,
    "ex7_b": 3,
    "ex8_dividende": 15,
    "ex8_diviseur": 4,
    "ex9_age": "25",
    "ex10_valeur": 3.14,
    "ex11_texte": "formation python",
    "ex12_phrase": "Bonjour le monde",
    "ex13_celsius": 0,
    "ex14_num1": 12,
    "ex14_num2": 5,
}

# ==================== EXERCICES ====================

# EXERCICE 1 : Afficher un message
# Affichez : "Bienvenue dans la formation Python !"
resultat_ex1 = "Bienvenue dans la formation Python !"


# EXERCICE 2 : Afficher plusieurs lignes
# Affichez sur 3 lignes :
# Bonjour !
# Bienvenue dans le monde de la programmation Python.
# Amusez-vous bien !
resultat_ex2 = "Bonjour !\nBienvenue dans le monde de la programmation Python.\nAmusez-vous bien !"


# EXERCICE 3 : Addition simple
# Créez deux variables a et b avec les données
a = 5
b = 3
# Calculez la somme
resultat_ex3 = a + b


# EXERCICE 4 : Créer et afficher une variable
# Créez une variable nom et mettez-y "Alice"
# Affichez : "Bonjour, Alice !"
nom = "Alice"
resultat_ex4 = "Bonjour, " + nom + " !"


# EXERCICE 5 : Concaténation de chaînes
# Utilisez les données
prenom = "Alice"
nom = "Dupont"
# Créez le message : "Bonjour, [prénom] [nom] !"
resultat_ex5 = "Bonjour, " + prenom + " " + nom + " !"


# EXERCICE 6 : Multiplier des nombres
x = 7
y = 8
# Calculez le produit
resultat_ex6 = x * y


# EXERCICE 7 : Division avec résultat flottant
a = 10
b = 3
# Divisez a par b
resultat_ex7 = a / b


# EXERCICE 8 : Calculer le reste d'une division
dividende = 15
diviseur = 4
# Calculez le reste (modulo)
resultat_ex8 = dividende % diviseur


# EXERCICE 9 : Conversion de types
# Age en tant que chaîne
age_str = "25"
# Convertissez en entier
age_int = int(age_str)
# Créez le message : "Vous avez [âge] ans."
resultat_ex9 = "Vous avez " + str(age_int) + " ans."


# EXERCICE 10 : Afficher le type d'une variable
valeur = 3.14
# Utilisez type() pour obtenir le type
type_valeur = type(valeur)
# Créez un message : "Valeur: 3.14, Type: <class 'float'>"
resultat_ex10 = "Valeur: " + str(valeur) + ", Type: " + str(type_valeur)


# EXERCICE 11 : Manipuler une chaîne
texte = "formation python"
# Transformez en majuscules
resultat_ex11 = texte.upper()


# EXERCICE 12 : Longueur d'une chaîne
phrase = "Bonjour le monde"
# Calculez la longueur
resultat_ex12 = len(phrase)


# EXERCICE 13 : Convertir des Celsius en Fahrenheit
# Formule : F = (9/5) * C + 32
celsius = 0
# Calculez en Fahrenheit
resultat_ex13 = (9/5) * celsius + 32


# EXERCICE 14 : Opérations arithmétiques
num1 = 12
num2 = 5
# Créez un dictionnaire avec :
# - "addition": résultat addition
# - "soustraction": résultat soustraction
# - "multiplication": résultat multiplication
# - "division": résultat division
resultat_ex14 = {
    "addition": num1 + num2,
    "soustraction": num1 - num2,
    "multiplication": num1 * num2,
    "division": num1 / num2
}


# EXERCICE 15 : Écrire un commentaire
# Ce programme démontre les opérations de base en Python
# Calculez : (5 + 3) * 2
a = 5
b = 3
c = 2
# Résultat de (a + b) * c
resultat_ex15 = (a + b) * c
