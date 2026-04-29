"""
TP3 : Algorithmique sur les chaînes de caractères
Template à remplir par les élèves
"""

donnees = {
    "ex1_mot": "algorithmique",
    "ex2_mot": "programmation",
    "ex2_lettre": "a",
    "ex3_mot": "bonjour",
    "ex4_mot": "hello",
    "ex5_mot": "radar",
    "ex6_phrase": "Bonjour tout le monde",
    "ex7_phrase": "  Bonjour le monde  ",
    "ex8_phrase": "Bonjour tout le monde",
    "ex9_phrase": "Bonjour  tout   le    monde",
    "ex10_phrase": "Python est genial",
    "ex11_chaine": "booonnjooour",
    "ex12_chaine": "aaabbc",
    "ex13_expression": "(a + b) * (c - d)",
    "ex14_mot1": "listen",
    "ex14_mot2": "silent",
    "ex15_phrase": "Bonjour tout le monde avec tous",
}

# ==================== EXERCICES ====================

# EXERCICE 1 : Parcourir une chaîne
# Créez une liste avec chaque caractère du mot "algorithmique"
mot = donnees["ex1_mot"]
resultat_ex1 = list(mot)


# EXERCICE 2 : Compter une lettre
mot = donnees["ex2_mot"]
lettre = donnees["ex2_lettre"]
# Comptez combien de fois la lettre "a" apparaît
resultat_ex2 = mot.count(lettre)


# EXERCICE 3 : Compter les voyelles
mot = donnees["ex3_mot"]
# Comptez les voyelles (a, e, i, o, u, y)
voyelles = "aeiouy"
resultat_ex3 = 0
i = 0
while i < len(mot):
    if mot[i] in voyelles:
        resultat_ex3 = resultat_ex3 + 1
    i = i + 1


# EXERCICE 4 : Inverser une chaîne
mot = donnees["ex4_mot"]
# Affichez le mot à l'envers : "hello" → "olleh"
resultat_ex4 = mot[::-1]


# EXERCICE 5 : Vérifier un palindrome
mot = donnees["ex5_mot"]
# Vérifiez si le mot se lit pareil dans les deux sens
# "radar" → True
resultat_ex5 = (mot == mot[::-1])


# EXERCICE 6 : Compter les mots
phrase = donnees["ex6_phrase"]
# Comptez combien de mots la phrase contient (sans utiliser split)
resultat_ex6 = 0
i = 0
if len(phrase) > 0:
    resultat_ex6 = 1
while i < len(phrase):
    if phrase[i] == ' ':
        resultat_ex6 = resultat_ex6 + 1
    i = i + 1

# EXERCICE 7 : Supprimer les espaces en début et fin
phrase = donnees["ex7_phrase"]
# Retournez la phrase sans espaces au début et fin
resultat_ex7 = phrase.strip()


# EXERCICE 8 : Trouver le mot le plus long
phrase = donnees["ex8_phrase"]
# Retournez le mot le plus long de la phrase (sans utiliser split)
mot_courant = ""
mot_long = ""
i = 0
while i < len(phrase):
    if phrase[i] != ' ':
        mot_courant = mot_courant + phrase[i]
    else:
        if len(mot_courant) > len(mot_long):
            mot_long = mot_courant
        mot_courant = ""
    i = i + 1
if len(mot_courant) > len(mot_long):
    mot_long = mot_courant
resultat_ex8 = mot_long


# EXERCICE 9 : Supprimer les espaces multiples
phrase = donnees["ex9_phrase"]
# Transformez "Bonjour  tout   le    monde" en "Bonjour tout le monde"
resultat_ex9 = ""
i = 0
while i < len(phrase):
    if phrase[i] == ' ':
        if len(resultat_ex9) > 0 and resultat_ex9[-1] != ' ':
            resultat_ex9 = resultat_ex9 + ' '
    else:
        resultat_ex9 = resultat_ex9 + phrase[i]
    i = i + 1

# EXERCICE 10 : Inverser les mots d'une phrase
phrase = donnees["ex10_phrase"]
# "Python est genial" → "genial est Python"
mots = phrase.split()
resultat_ex10 = ""
i = len(mots) - 1
while i >= 0:
    if i < len(mots) - 1:
        resultat_ex10 = resultat_ex10 + " "
    resultat_ex10 = resultat_ex10 + mots[i]
    i = i - 1


# EXERCICE 11 : Supprimer les caractères consécutifs identiques
chaine = donnees["ex11_chaine"]
# "booonnjooour" → "bonjour"
resultat_ex11 = ""
i = 0
while i < len(chaine):
    if len(resultat_ex11) == 0 or chaine[i] != resultat_ex11[-1]:
        resultat_ex11 = resultat_ex11 + chaine[i]
    i = i + 1


# EXERCICE 12 : Compression simple d'une chaîne
chaine = donnees["ex12_chaine"]
# "aaabbc" → "a3b2c1"
resultat_ex12 = ""
i = 0
while i < len(chaine):
    char = chaine[i]
    compteur = 0
    while i < len(chaine) and chaine[i] == char:
        compteur = compteur + 1
        i = i + 1
    resultat_ex12 = resultat_ex12 + char + str(compteur)


# EXERCICE 13 : Vérifier des parenthèses équilibrées
expression = donnees["ex13_expression"]
# Vérifiez si les parenthèses sont correctement équilibrées
# "(a + b) * (c - d)" → True
compteur = 0
resultat_ex13 = True
i = 0
while i < len(expression):
    if expression[i] == '(':
        compteur = compteur + 1
    elif expression[i] == ')':
        compteur = compteur - 1
    if compteur < 0:
        resultat_ex13 = False
    i = i + 1
if compteur != 0:
    resultat_ex13 = False


# EXERCICE 14 : Vérifier deux anagrammes
mot1 = donnees["ex14_mot1"]
mot2 = donnees["ex14_mot2"]
# Vérifiez si les deux mots sont des anagrammes
# "listen" et "silent" → True
resultat_ex14 = ""
if len(mot1) != len(mot2):
    resultat_ex14 = False
else:
    resultat_ex14 = True
    i = 0
    while i < len(mot1):
        if mot1.count(mot1[i]) != mot2.count(mot1[i]):
            resultat_ex14 = False
        i = i + 1


# EXERCICE 15 : Mini analyseur de phrase
phrase = donnees["ex15_phrase"]
# Retournez un dictionnaire avec :
# - "nombre_mots": nombre de mots
# - "mot_le_plus_long": le mot le plus long
# - "nombre_caracteres": nombre total de caractères (sans espaces)
resultat_ex15 = ""
nombre_mots = 0
i = 0
if len(phrase) > 0:
    nombre_mots = 1
while i < len(phrase):
    if phrase[i] == ' ':
        nombre_mots = nombre_mots + 1
    i = i + 1

# Mot le plus long
mot_courant = ""
mot_long = ""
i = 0
while i < len(phrase):
    if phrase[i] != ' ':
        mot_courant = mot_courant + phrase[i]
    else:
        if len(mot_courant) > len(mot_long):
            mot_long = mot_courant
        mot_courant = ""
    i = i + 1
if len(mot_courant) > len(mot_long):
    mot_long = mot_courant

nombre_chars = 0
i = 0
while i < len(phrase):
    if phrase[i] != ' ':
        nombre_chars = nombre_chars + 1
    i = i + 1

resultat_ex15 = {
    "nombre_mots": nombre_mots,
    "mot_le_plus_long": mot_long,        
    "nombre_caracteres": nombre_chars,   
}

