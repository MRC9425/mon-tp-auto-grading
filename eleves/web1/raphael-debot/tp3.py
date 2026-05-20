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
res = []

for i in mot:
    res = res + [i]

resultat_ex1 = res


# EXERCICE 2 : Compter une lettre
mot = donnees["ex2_mot"]
lettre = donnees["ex2_lettre"]
# Comptez combien de fois la lettre "a" apparaît
res = 0

for i in mot:
    if i == lettre:
        res = res + 1

resultat_ex2 = res


# EXERCICE 3 : Compter les voyelles
mot = donnees["ex3_mot"]
# Comptez les voyelles (a, e, i, o, u, y)
res = 0

for i in mot:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y":
        res = res + 1

resultat_ex3 = res


# EXERCICE 4 : Inverser une chaîne
mot = donnees["ex4_mot"]
# Affichez le mot à l'envers : "hello" → "olleh"
res = ""

for i in mot:
    res = i + res

resultat_ex4 = res


# EXERCICE 5 : Vérifier un palindrome
mot = donnees["ex5_mot"]
# Vérifiez si le mot se lit pareil dans les deux sens
# "radar" → True
inverse = ""

for i in mot:
    inverse = i + inverse

if mot == inverse:
    resultat_ex5 = True
else:
    resultat_ex5 = False


# EXERCICE 6 : Compter les mots
phrase = donnees["ex6_phrase"]
# Comptez combien de mots la phrase contient (sans utiliser split)
res = 0
dans_mot = False

for i in phrase:
    if i != " " and dans_mot == False:
        res = res + 1
        dans_mot = True

    if i == " ":
        dans_mot = False

resultat_ex6 = res


# EXERCICE 7 : Supprimer les espaces en début et fin
phrase = donnees["ex7_phrase"]
# Retournez la phrase sans espaces au début et fin
debut = 0
fin = len(phrase) - 1

while debut < len(phrase) and phrase[debut] == " ":
    debut = debut + 1

while fin >= 0 and phrase[fin] == " ":
    fin = fin - 1

res = ""

while debut <= fin:
    res = res + phrase[debut]
    debut = debut + 1

resultat_ex7 = res


# EXERCICE 8 : Trouver le mot le plus long
phrase = donnees["ex8_phrase"]
# Retournez le mot le plus long de la phrase (sans utiliser split)
mot_actuel = ""
mot_plus_long = ""

for i in phrase:
    if i != " ":
        mot_actuel = mot_actuel + i
    else:
        if len(mot_actuel) > len(mot_plus_long):
            mot_plus_long = mot_actuel

        mot_actuel = ""

# vérifier aussi le dernier mot
if len(mot_actuel) > len(mot_plus_long):
    mot_plus_long = mot_actuel

resultat_ex8 = mot_plus_long


# EXERCICE 9 : Supprimer les espaces multiples
phrase = donnees["ex9_phrase"]
# Transformez "Bonjour  tout   le    monde" en "Bonjour tout le monde"
res = ""
espace_avant = False

for i in phrase:
    if i != " ":
        res = res + i
        espace_avant = False
    else:
        if espace_avant == False:
            res = res + " "
            espace_avant = True

resultat_ex9 = res


# EXERCICE 10 : Inverser les mots d'une phrase
phrase = donnees["ex10_phrase"]
# "Python est genial" → "genial est Python"
resultat_ex10 = None


# EXERCICE 11 : Supprimer les caractères consécutifs identiques
chaine = donnees["ex11_chaine"]
# "booonnjooour" → "bonjour"
resultat_ex11 = None


# EXERCICE 12 : Compression simple d'une chaîne
chaine = donnees["ex12_chaine"]
# "aaabbc" → "a3b2c1"
resultat_ex12 = None


# EXERCICE 13 : Vérifier des parenthèses équilibrées
expression = donnees["ex13_expression"]
# Vérifiez si les parenthèses sont correctement équilibrées
# "(a + b) * (c - d)" → True
resultat_ex13 = None


# EXERCICE 14 : Vérifier deux anagrammes
mot1 = donnees["ex14_mot1"]
mot2 = donnees["ex14_mot2"]
# Vérifiez si les deux mots sont des anagrammes
# "listen" et "silent" → True
resultat_ex14 = None


# EXERCICE 15 : Mini analyseur de phrase
phrase = donnees["ex15_phrase"]
# Retournez un dictionnaire avec :
# - "nombre_mots": nombre de mots
# - "mot_le_plus_long": le mot le plus long
# - "nombre_caracteres": nombre total de caractères (sans espaces)
resultat_ex15 = None
