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
mot = donnees["ex1_mot"]
resultat_ex1 = list(mot)


# EXERCICE 2 : Position des caractères
# Affichez chaque lettre du mot "programmation" avec sa position
# Exemple résultat : "p:0 r:1 o:2 g:3..." (comme string ou dict)
mot = donnees["ex2_mot"]
resultat_ex2 = ""
i = 0
while i < len(mot):
    if i > 0:
        resultat_ex2 = resultat_ex2 + " "
    resultat_ex2 = resultat_ex2 + mot[i] + ":" + str(i)
    i = i + 1



# EXERCICE 3 : Codes des caractères
# Retournez le code ASCII d'un caractère avec ord()
char = donnees["ex3_char"]
# Code ASCII de "A"
resultat_ex3 = ord(char)


# EXERCICE 4 : Majuscule ou minuscule
# Utilisez le code ASCII pour déterminer si c'est majuscule ou minuscule
lettre = donnees["ex4_lettre"]
# Retournez "majuscule" ou "minuscule"
resultat_ex4 = ""
if 65 <= ord(lettre) <= 90:
    resultat_ex4 = "majuscule"
else:
    resultat_ex4 = "minuscule"


# EXERCICE 5 : Est-ce un chiffre ?
# Utilisez le code ASCII pour vérifier si c'est un chiffre
char = donnees["ex5_char"]
# Retournez True ou False
resultat_ex5 = ""
if 48 <= ord(char) <= 57:
    resultat_ex5 = True
else:
    resultat_ex5 = False


# EXERCICE 6 : Compter les chiffres dans un texte
phrase = donnees["ex6_phrase"]
# Comptez combien de chiffres (0-9) la phrase contient
# Indice : ord('0') = 48, ord('9') = 57
resultat_ex6 = 0
i = 0
while i < len(phrase):
    if 48 <= ord(phrase[i]) <= 57:
        resultat_ex6 = resultat_ex6 + 1
    i = i + 1


# EXERCICE 7 : Somme des chiffres d'un texte
chiffres_text = donnees["ex7_chiffres"]
# Convertissez chaque caractère chiffre en nombre et additionnez
# "1352" → 1 + 3 + 5 + 2 = 11
resultat_ex7 = 0
i = 0
while i < len(chiffres_text):
    resultat_ex7 = resultat_ex7 + (ord(chiffres_text[i]) - 48)
    i = i + 1


# EXERCICE 8 : Construire un nombre
# Lisez un nombre texte caractère par caractère
# Utilisez la formule : resultat = resultat * 10 + chiffre
nombre_text = donnees["ex8_nombre_text"]
# Convertissez "42" en nombre 42 (sans utiliser int())
resultat_ex8 = 0
i = 0
while i < len(nombre_text):
    resultat_ex8 = resultat_ex8 * 10 + (ord(nombre_text[i]) - 48)
    i = i + 1


# EXERCICE 9 : Vérifier une entrée numérique
texte = donnees["ex9_texte"]
# Vérifiez si le texte ne contient QUE des chiffres
# "123abc456" → False (contient des lettres)
# "123456" → True
resultat_ex9 = True
i = 0
while i < len(texte):
    if not (48 <= ord(texte[i]) <= 57):
        resultat_ex9 = False
    i = i + 1


# EXERCICE 10 : Mini addition de nombres texte
num1_text = str(donnees["ex10_num1"])  # "12"
num2_text = str(donnees["ex10_num2"])  # "3"
# Convertissez manuellement en nombres (sans int())
# puis additionnez et retournez le résultat
resultat_ex10 = ""
n1 = 0
for c in num1_text:
    n1 = n1 * 10 + (ord(c) - 48)

n2 = 0
for c in num2_text:
    n2 = n2 * 10 + (ord(c) - 48)

resultat_ex10 = n1 + n2


# EXERCICE 11 : Extraire les chiffres d'un nombre
nombre = donnees["ex11_nombre"]
# Affichez les chiffres un par un en utilisant % et //
# 1234 → ['1', '2', '3', '4'] ou "1234"
resultat_ex11 = []
n = nombre
while n > 0:
    resultat_ex11.insert(0, str(n % 10))
    n = n // 10


# EXERCICE 12 : Inverser un nombre
nombre = donnees["ex12_nombre"]
# Affichez le nombre avec chiffres inversés
# 5678 → 8765
resultat_ex12 = 0
n = nombre
while n > 0:
    resultat_ex12 = resultat_ex12 * 10 + n % 10
    n = n // 10

# EXERCICE 13 : Bonus - Calculatrice simple
expression = donnees["ex13_expression"]
# Parsez une expression comme "12+3"
# Identifiez les nombres et l'opérateur
# Retournez le résultat du calcul
# "12+3" → 15
pos_op = 0 
operateur = ""
i = 0 
for c in expression: 
    if c == '+' or c == '-' or c == '*' or c == '/':
        operateur = c
        pos_op = i 
    i += 1

gauche = 0 
i = 0 
for c in expression: 
    if i == pos_op:
        break 
    gauche = gauche * 10 + (ord(c) - 48)
    i += 1 

droite = 0 
i = 0 
for c in expression: 
    if i > pos_op: 
        droite = droite * 10 + (ord(c) - 48)
    i += 1   

if operateur == '+':
    resultat_ex13 = gauche + droite
elif operateur == '-':
    resultat_ex13 = gauche - droite
elif operateur == '*':
    resultat_ex13 = gauche * droite
elif operateur == '/':
    resultat_ex13 = gauche / droite