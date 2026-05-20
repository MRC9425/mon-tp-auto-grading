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
resultat_ex2 = sum(1 for c in mot if c == lettre)


# EXERCICE 3 : Compter les voyelles
mot = donnees["ex3_mot"]
# Comptez les voyelles (a, e, i, o, u, y)
voyelles = "aeiouy"
resultat_ex3 = sum(1 for c in mot if c in voyelles)


# EXERCICE 4 : Inverser une chaîne
mot = donnees["ex4_mot"]
# Affichez le mot à l'envers : "hello" → "olleh"
resultat_ex4 = mot[::-1]


# EXERCICE 5 : Vérifier un palindrome
mot = donnees["ex5_mot"]
# Vérifiez si le mot se lit pareil dans les deux sens
# "radar" → True
resultat_ex5 = mot == mot[::-1]


# EXERCICE 6 : Compter les mots
phrase = donnees["ex6_phrase"]
# Comptez combien de mots la phrase contient (sans utiliser split)
nb_mots = 1
for c in phrase:
    if c == " ":
        nb_mots += 1
resultat_ex6 = nb_mots


# EXERCICE 7 : Supprimer les espaces en début et fin
phrase = donnees["ex7_phrase"]
# Retournez la phrase sans espaces au début et fin
debut = 0
fin = len(phrase) - 1
while phrase[debut] == " ":
    debut += 1
while phrase[fin] == " ":
    fin -= 1
resultat_ex7 = phrase[debut:fin+1]


# EXERCICE 8 : Trouver le mot le plus long
phrase = donnees["ex8_phrase"]
# Retournez le mot le plus long de la phrase (sans utiliser split)mot_long = ""
mot_actuel = ""
for c in phrase:
    if c != " ":
        mot_actuel += c
    else:
        if len(mot_actuel) > len(mot_long):
            mot_long = mot_actuel
        mot_actuel = ""
if len(mot_actuel) > len(mot_long):
    mot_long = mot_actuel
resultat_ex8 = mot_long


# EXERCICE 9 : Supprimer les espaces multiples
phrase = donnees["ex9_phrase"]
# Transformez "Bonjour  tout   le    monde" en "Bonjour tout le monde"
espace_precedent = False
for c in phrase:
    if c == " ":
        if not espace_precedent:
            resultat_ex9 += c
        espace_precedent = True
    else:
        resultat_ex9 += c
        espace_precedent = False
resultat_ex9 = ""


# EXERCICE 10 : Inverser les mots d'une phrase
phrase = donnees["ex10_phrase"]
# "Python est genial" → "genial est Python"
mots = []
mot_actuel = ""
for c in phrase + " ":
    if c != " ":
        mot_actuel += c
    else:
        if mot_actuel:
            mots.append(mot_actuel)
        mot_actuel = ""
resultat_ex10 = " ".join(mots[::-1])


# EXERCICE 11 : Supprimer les caractères consécutifs identiques
chaine = donnees["ex11_chaine"]
# "booonnjooour" → "bonjour"
resultat_ex11 = ""
for c in chaine:
    if not resultat_ex11 or c != resultat_ex11[-1]:
        resultat_ex11 += c


# EXERCICE 12 : Compression simple d'une chaîne
chaine = donnees["ex12_chaine"]
# "aaabbc" → "a3b2c1"
resultat_ex12 = ""
count = 1
for i in range(1, len(chaine)):
    if chaine[i] == chaine[i-1]:
        count += 1
    else:
        resultat_ex12 += chaine[i-1] + str(count)
        count = 1
resultat_ex12 += chaine[-1] + str(count)


# EXERCICE 13 : Vérifier des parenthèses équilibrées
expression = donnees["ex13_expression"]
# Vérifiez si les parenthèses sont correctement équilibrées
# "(a + b) * (c - d)" → True
compteur = 0
resultat_ex13 = True
for c in expression:
    if c == "(":
        compteur += 1
    elif c == ")":
        compteur -= 1
    if compteur < 0:
        resultat_ex13 = False
        break
if compteur != 0:
    resultat_ex13 = False


# EXERCICE 14 : Vérifier deux anagrammes
mot1 = donnees["ex14_mot1"]
mot2 = donnees["ex14_mot2"]
# Vérifiez si les deux mots sont des anagrammes
# "listen" et "silent" → True
resultat_ex14 = sorted(mot1) == sorted(mot2)


# EXERCICE 15 : Mini analyseur de phrase
phrase = donnees["ex15_phrase"]
# Retournez un dictionnaire avec :
# - "nombre_mots": nombre de mots
# - "mot_le_plus_long": le mot le plus long
# - "nombre_caracteres": nombre total de caractères (sans espaces)
mots = []
mot_actuel = ""
for c in phrase + " ":
    if c != " ":
        mot_actuel += c
    else:
        if mot_actuel:
            mots.append(mot_actuel)
        mot_actuel = ""

mot_long = max(mots, key=len)
nb_chars = sum(len(m) for m in mots)

resultat_ex15 = {
    "nombre_mots": len(mots),
    "mot_le_plus_long": mot_long,
    "nombre_caracteres": nb_chars
}