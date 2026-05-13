"""
TP2 : Manipulation des caractères et conversions
Template à remplir par les élèves
"""

# ==================== DONNÉES DE TEST ====================
donnees = {
    "ex1_mot": "python",
    "ex2_mot": "programmation",
    "ex3_char": "A",
    "ex4_lettre": "B",
    "ex5_char": "5",
    "ex6_phrase": "Python3 est version 3.11",
    "ex7_chiffres": "1352",
    "ex8_nombre_text": "42",
    "ex9_texte": "123abc456",
    "ex10_num1": 12,
    "ex10_num2": 3,
    "ex11_nombre": 1234,
    "ex12_nombre": 5678,
    "ex13_expression": "12+3",
}

# ==================== EXERCICES ====================

# EXERCICE 1 : Parcourir une chaîne
# Créez une liste contenant chaque caractère du mot "python"
# Exemple résultat : ['p', 'y', 't', 'h', 'o', 'n']
mot = "python"
resultat_ex1 = list(mot)


# EXERCICE 2 : Position des caractères
# Affichez chaque lettre du mot "programmation" avec sa position
# Exemple résultat : "p:0 r:1 o:2 g:3..." (comme string ou dict)
mot = "programmation"
resultat_ex2 = ""
i = 0
while i < len(mot):
    if i == 0:
        resultat_ex2 = mot[i] + ":" + str(i)
    else:
        resultat_ex2 = resultat_ex2 + " " + mot[i] + ":" + str(i)
    i += 1


# EXERCICE 3 : Codes des caractères
# Retournez le code ASCII d'un caractère avec ord()
char = "A"
# Code ASCII de "A"
resultat_ex3 = ord(char)


# EXERCICE 4 : Majuscule ou minuscule
# Utilisez le code ASCII pour déterminer si c'est majuscule ou minuscule
lettre = "B"
# Retournez "majuscule" ou "minuscule"
code = ord(lettre)
if code >= 65 and code <= 90:
    resultat_ex4 = "majuscule"
else:
    resultat_ex4 = "minuscule"


# EXERCICE 5 : Est-ce un chiffre ?
# Utilisez le code ASCII pour vérifier si c'est un chiffre
char = "5"
# Retournez True ou False
code = ord(char)
if code >= 48 and code <= 57:
    resultat_ex5 = True
else:
    resultat_ex5 = False


# EXERCICE 6 : Compter les chiffres dans un texte
phrase = "Python3 est version 3.11"
# Comptez combien de chiffres (0-9) la phrase contient
# Indice : ord('0') = 48, ord('9') = 57
nb_chiffres = 0
i = 0
while i < len(phrase):
    code = ord(phrase[i])
    if code >= 48 and code <= 57:
        nb_chiffres += 1
    i += 1
resultat_ex6 = nb_chiffres


# EXERCICE 7 : Somme des chiffres d'un texte
chiffres_text = "1352"
# Convertissez chaque caractère chiffre en nombre et additionnez
# "1352" → 1 + 3 + 5 + 2 = 11
total = 0
i = 0
while i < len(chiffres_text):
    total += ord(chiffres_text[i]) - 48
    i += 1
resultat_ex7 = total


# EXERCICE 8 : Construire un nombre
# Lisez un nombre texte caractère par caractère
# Utilisez la formule : resultat = resultat * 10 + chiffre
nombre_text = "42"
# Convertissez "42" en nombre 42 (sans utiliser int())
resultat_ex8 = 0
i = 0
while i < len(nombre_text):
    chiffre = ord(nombre_text[i]) - 48
    resultat_ex8 = resultat_ex8 * 10 + chiffre
    i += 1


# EXERCICE 9 : Vérifier une entrée numérique
texte = "123abc456"
# Vérifiez si le texte ne contient QUE des chiffres
# "123abc456" → False (contient des lettres)
# "123456" → True
resultat_ex9 = True
i = 0
while i < len(texte):
    code = ord(texte[i])
    if code < 48 or code > 57:
        resultat_ex9 = False
    i += 1


# EXERCICE 10 : Mini addition de nombres texte
num1_text = str(12)  # "12"
num2_text = str(3)   # "3"
# Convertissez manuellement en nombres (sans int())
# puis additionnez et retournez le résultat
n1 = 0
i = 0
while i < len(num1_text):
    n1 = n1 * 10 + (ord(num1_text[i]) - 48)
    i += 1
n2 = 0
i = 0
while i < len(num2_text):
    n2 = n2 * 10 + (ord(num2_text[i]) - 48)
    i += 1
resultat_ex10 = n1 + n2


# EXERCICE 11 : Extraire les chiffres d'un nombre
nombre = 1234
# Affichez les chiffres un par un en utilisant % et //
# 1234 → ['1', '2', '3', '4'] ou "1234"
resultat_ex11 = ""
n = nombre
while n > 0:
    resultat_ex11 = str(n % 10) + resultat_ex11
    n = n // 10


# EXERCICE 12 : Inverser un nombre
nombre = 5678
# Affichez le nombre avec chiffres inversés
# 5678 → 8765
inverse = 0
n = nombre
while n > 0:
    inverse = inverse * 10 + n % 10
    n = n // 10
resultat_ex12 = inverse


# EXERCICE 13 : Bonus - Calculatrice simple
expression = "12+3"
# Parsez une expression comme "12+3"
# Identifiez les nombres et l'opérateur
# Retournez le résultat du calcul
# "12+3" → 15
i = 0
while i < len(expression) and ord(expression[i]) >= 48 and ord(expression[i]) <= 57:
    i += 1
operateur = expression[i]
n1 = 0
j = 0
while j < i:
    n1 = n1 * 10 + (ord(expression[j]) - 48)
    j += 1
n2 = 0
j = i + 1
while j < len(expression):
    n2 = n2 * 10 + (ord(expression[j]) - 48)
    j += 1
if operateur == '+':
    resultat_ex13 = n1 + n2
elif operateur == '-':
    resultat_ex13 = n1 - n2
elif operateur == '*':
    resultat_ex13 = n1 * n2
elif operateur == '/':
    resultat_ex13 = n1 / n2
