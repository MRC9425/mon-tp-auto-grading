"""
TP5 : La boucle for
Template à remplir par les élèves
"""

# ==================== DONNÉES DE TEST ====================
# NE PAS MODIFIER

donnees = {
    "range1_stop": 5,
    "range2_start": 3,   "range2_stop": 8,
    "range3_start": 2,   "range3_stop": 10,  "range3_step": 3,
    "range4_start": 5,   "range4_stop": 0,   "range4_step": -1,
    "chaine1": "mississippi",   "lettre1": "s",
    "somme_fin": 20,
    "multiple": 3,              "multiple_fin": 30,
    "chaine2": "algorithmique",
    "chaine3": "algorithmique", "lettre2": "g",
    "mot1": "Python",
    "chaine4": "bonjour",
    "table_n": 7,
    "carre_n": 4,
    "mot2": "algo",             "mot3": "alco",
}

# ==================== EXERCICES ====================

# EXERCICE 1 : range() basique
# Construire la liste des valeurs générées par range(5)
# Résultat attendu : [0, 1, 2, 3, 4]
# Interdit : list(range(...))  — utilisez une boucle for
resultat_ex1 = []
for i in range(5):
    resultat_ex1.append(i)


# EXERCICE 2 : range(start, stop)
# Construire la liste des valeurs de range(3, 8)
# Résultat attendu : [3, 4, 5, 6, 7]
resultat_ex2 = []
for i in range(3, 8):
    resultat_ex2.append(i)


# EXERCICE 3 : range(start, stop, step)
# Construire la liste des valeurs de range(2, 10, 3)
# Résultat attendu : [2, 5, 8]
resultat_ex3 = []
for i in range(2, 10, 3):
    resultat_ex3.append(i)
    


# EXERCICE 4 : range() négatif
# Construire la liste des valeurs de range(5, 0, -1)
# Résultat attendu : [5, 4, 3, 2, 1]
resultat_ex4 = []
for i in range(5, 0, -1):
    resultat_ex4.append(i)


# EXERCICE 5 : Compter des occurrences
# Compter le nombre de fois que "s" apparaît dans "mississippi"
# Résultat attendu : 4
# Interdit : count()
resultat_ex5 = 0
for c in "mississippi":
    if c == "s":
        resultat_ex5 = resultat_ex5 + 1


# EXERCICE 6 : Accumulateur
# Calculer la somme de tous les entiers pairs de 2 à 20 inclus
# Résultat attendu : 110
# Interdit : sum()
resultat_ex6 = 0
for i in range(2, 21):
    if i % 2 == 0:
        resultat_ex6 = resultat_ex6 + i


# EXERCICE 7 : Multiples
# Construire la liste de tous les multiples de 3 entre 1 et 30 inclus
# Résultat attendu : [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
resultat_ex7 = []
for i in range(1, 31):
    if i % 3 == 0:
        resultat_ex7.append(i)


# EXERCICE 8 : Position des caractères
# Créer un dictionnaire {position: caractère} pour "algorithmique"
# Résultat attendu : {0: 'a', 1: 'l', 2: 'g', ...}
# Obligatoire : utiliser range() et un index i
resultat_ex8 = {}
for i in range(len("algorithmique")):
    resultat_ex8[i] = "algorithmique"[i]


# EXERCICE 9 : Trouver une position
# Trouver la 1ère position de "g" dans "algorithmique"
# Résultat attendu : 2
# Interdit : find(), index()
# Conseil : utilisez un booléen pour ne retenir que la 1ère occurrence
resultat_ex9 = -1
trouve = False
for i in range(len("algorithmique")):
    if "algorithmique"[i] == "g" and trouve == False:
        resultat_ex9 = i
        trouve = True


# EXERCICE 10 : Parcours à l'envers
# Reconstruire "Python" à l'envers en utilisant range(len(mot)-1, -1, -1)
# Résultat attendu : "nohtyP"
# Interdit : [::-1]
resultat_ex10 = ""
for i in range(len("Python") - 1, -1, -1):
    resultat_ex10 = resultat_ex10 + "Python"[i]


# EXERCICE 11 : Majuscules via ASCII
# Transformer "bonjour" en "BONJOUR" caractère par caractère
# Obligatoire : ord() et chr()
# Interdit : upper()
# Rappel : minuscule → majuscule = soustraire 32 au code ASCII
resultat_ex11 = ""
for c in "bonjour":
    resultat_ex11 = resultat_ex11 + chr(ord(c) - 32)


# EXERCICE 12 : Filtrer les voyelles
# Construire une chaîne avec uniquement les voyelles de "algorithmique"
# Résultat attendu : "aoiiue"   (voyelles : a, e, i, o, u, y)
resultat_ex12 = ""
voyelles = "aeiouy"
for c in "algorithmique":
    if c in voyelles:
        resultat_ex12 = resultat_ex12 + c


# EXERCICE 13 : Table de multiplication
# Construire la table de 7 sous forme de liste de 10 chaînes
# Résultat attendu : ["7 x 1 = 7", "7 x 2 = 14", ..., "7 x 10 = 70"]
resultat_ex13 = []
for i in range(1, 11):
    ligne = "7 x " + str(i) + " = " + str(7 * i)
    resultat_ex13.append(ligne)


# EXERCICE 14 : Boucles imbriquées — carré d'étoiles
# Construire un carré de n=4 lignes sous forme de liste de chaînes
# Résultat attendu : ["****", "****", "****", "****"]
# Obligatoire : deux boucles for imbriquées (une pour les lignes, une pour les colonnes)
resultat_ex14 = []
for i in range(4):
    ligne = ""
    for j in range(4):
        ligne = ligne + "*"
    resultat_ex14.append(ligne)


# EXERCICE 15 : Comparer deux mots caractère par caractère
# Comparer "algo" et "alco" sans utiliser == entre les deux chaînes entières
# Résultat attendu : {"identiques": False, "position": 2}
# Si les longueurs sont différentes : {"identiques": False, "position": -1}
# Si identiques : {"identiques": True, "position": -1}
