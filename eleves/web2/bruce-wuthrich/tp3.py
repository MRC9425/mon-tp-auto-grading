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
mot = "algorithmique"
resultat_ex1 = list(mot)


# EXERCICE 2 : Compter une lettre
mot = "programmation"
lettre = "a"
# Comptez combien de fois la lettre "a" apparaît
nb = 0
i = 0
while i < len(mot):
    if mot[i] == lettre:
        nb += 1
    i += 1
resultat_ex2 = nb


# EXERCICE 3 : Compter les voyelles
mot = "bonjour"
# Comptez les voyelles (a, e, i, o, u, y)
voyelles = "aeiouy"
nb = 0
i = 0
while i < len(mot):
    if mot[i] in voyelles:
        nb += 1
    i += 1
resultat_ex3 = nb


# EXERCICE 4 : Inverser une chaîne
mot = "hello"
# Affichez le mot à l'envers : "hello" → "olleh"
inverse = ""
i = len(mot) - 1
while i >= 0:
    inverse += mot[i]
    i -= 1
resultat_ex4 = inverse


# EXERCICE 5 : Vérifier un palindrome
mot = "radar"
# Vérifiez si le mot se lit pareil dans les deux sens
# "radar" → True
inverse = ""
i = len(mot) - 1
while i >= 0:
    inverse += mot[i]
    i -= 1
resultat_ex5 = (mot == inverse)


# EXERCICE 6 : Compter les mots
phrase = "Bonjour tout le monde"
# Comptez combien de mots la phrase contient (sans utiliser split)
nb_mots = 0
en_mot = False
i = 0
while i < len(phrase):
    if phrase[i] != ' ' and not en_mot:
        en_mot = True
        nb_mots += 1
    elif phrase[i] == ' ':
        en_mot = False
    i += 1
resultat_ex6 = nb_mots


# EXERCICE 7 : Supprimer les espaces en début et fin
phrase = "  Bonjour le monde  "
# Retournez la phrase sans espaces au début et fin
debut = 0
while debut < len(phrase) and phrase[debut] == ' ':
    debut += 1
fin = len(phrase) - 1
while fin >= 0 and phrase[fin] == ' ':
    fin -= 1
resultat_ex7 = phrase[debut:fin+1]


# EXERCICE 8 : Trouver le mot le plus long
phrase = "Bonjour tout le monde"
# Retournez le mot le plus long de la phrase (sans utiliser split)
mot_courant = ""
mot_long = ""
i = 0
while i < len(phrase):
    if phrase[i] != ' ':
        mot_courant += phrase[i]
    else:
        if len(mot_courant) > len(mot_long):
            mot_long = mot_courant
        mot_courant = ""
    i += 1
if len(mot_courant) > len(mot_long):
    mot_long = mot_courant
resultat_ex8 = mot_long


# EXERCICE 9 : Supprimer les espaces multiples
phrase = "Bonjour  tout   le    monde"
# Transformez "Bonjour  tout   le    monde" en "Bonjour tout le monde"
resultat_ex9 = ""
i = 0
while i < len(phrase):
    if phrase[i] != ' ':
        resultat_ex9 += phrase[i]
    elif i == 0 or phrase[i-1] != ' ':
        resultat_ex9 += phrase[i]
    i += 1


# EXERCICE 10 : Inverser les mots d'une phrase
phrase = "Python est genial"
# "Python est genial" → "genial est Python"
mots = phrase.split()
resultat_ex10 = ""
i = len(mots) - 1
while i >= 0:
    if resultat_ex10 == "":
        resultat_ex10 = mots[i]
    else:
        resultat_ex10 = resultat_ex10 + " " + mots[i]
    i -= 1


# EXERCICE 11 : Supprimer les caractères consécutifs identiques
chaine = "booonnjooour"
# "booonnjooour" → "bonjour"
resultat_ex11 = ""
i = 0
while i < len(chaine):
    if i == 0 or chaine[i] != chaine[i-1]:
        resultat_ex11 += chaine[i]
    i += 1


# EXERCICE 12 : Compression simple d'une chaîne
chaine = "aaabbc"
# "aaabbc" → "a3b2c1"
resultat_ex12 = ""
i = 0
while i < len(chaine):
    char_actuel = chaine[i]
    count = 0
    while i < len(chaine) and chaine[i] == char_actuel:
        count += 1
        i += 1
    resultat_ex12 += char_actuel + str(count)


# EXERCICE 13 : Vérifier des parenthèses équilibrées
expression = "(a + b) * (c - d)"
# Vérifiez si les parenthèses sont correctement équilibrées
# "(a + b) * (c - d)" → True
count = 0
valide = True
i = 0
while i < len(expression):
    if expression[i] == '(':
        count += 1
    elif expression[i] == ')':
        count -= 1
        if count < 0:
            valide = False
    i += 1
resultat_ex13 = valide and count == 0


# EXERCICE 14 : Vérifier deux anagrammes
mot1 = "listen"
mot2 = "silent"
# Vérifiez si les deux mots sont des anagrammes
# "listen" et "silent" → True
resultat_ex14 = sorted(mot1) == sorted(mot2)


# EXERCICE 15 : Mini analyseur de phrase
phrase = "Bonjour tout le monde avec tous"
# Retournez un dictionnaire avec :
# - "nombre_mots": nombre de mots
# - "mot_le_plus_long": le mot le plus long
# - "nombre_caracteres": nombre total de caractères (sans espaces)
mots = phrase.split()
nombre_mots = len(mots)
mot_le_plus_long = ""
i = 0
while i < len(mots):
    if len(mots[i]) > len(mot_le_plus_long):
        mot_le_plus_long = mots[i]
    i += 1
nb_chars = 0
i = 0
while i < len(phrase):
    if phrase[i] != ' ':
        nb_chars += 1
    i += 1
resultat_ex15 = {
    "nombre_mots": nombre_mots,
    "mot_le_plus_long": mot_le_plus_long,
    "nombre_caracteres": nb_chars
}
