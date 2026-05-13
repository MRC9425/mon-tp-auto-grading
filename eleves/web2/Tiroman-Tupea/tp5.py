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
ma_list=[]
for a in range(0,5):
    ma_list.append(a)
resultat_ex1 = ma_list


# EXERCICE 2 : range(start, stop)
# Construire la liste des valeurs de range(3, 8)
# Résultat attendu : [3, 4, 5, 6, 7]
for b in range(3, 8):
   ma_list.append(b)
resultat_ex2 = ma_list


# EXERCICE 3 : range(start, stop, step)
# Construire la liste des valeurs de range(2, 10, 3)
# Résultat attendu : [2, 5, 8]
for c in range(2,10,3):
    ma_list.append(c)
resultat_ex3 = ma_list


# EXERCICE 4 : range() négatif
# Construire la liste des valeurs de range(5, 0, -1)
# Résultat attendu : [5, 4, 3, 2, 1]
for d in range(5,0,-1):
    ma_list.append(d)
resultat_ex4 = ma_list


# EXERCICE 5 : Compter des occurrences
# Compter le nombre de fois que "s" apparaît dans "mississippi"
# Résultat attendu : 4
# Interdit : count()
mot = "mississipi"
i = 0
for e in mot:
    if e == "s":
        i += 1
        print(i)
resultat_ex5 = 


# EXERCICE 6 : Accumulateur
# Calculer la somme de tous les entiers pairs de 2 à 20 inclus
# Résultat attendu : 110
# Interdit : sum()
i = 0
for f in range(2, 21):
    if f%2 == 0:
        i += f
        print(i)
resultat_ex6 = 


# EXERCICE 7 : Multiples
# Construire la liste de tous les multiples de 3 entre 1 et 30 inclus
# Résultat attendu : [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for g in range(1, 31):
    if g%3 == 0:
        print(g)
resultat_ex7 = None


# EXERCICE 8 : Position des caractères
# Créer un dictionnaire {position: caractère} pour "algorithmique"
# Résultat attendu : {0: 'a', 1: 'l', 2: 'g', ...}
# Obligatoire : utiliser range() et un index i
mot = "algorithmique"
i = 0
for h in mot:
    i = i + 1
    print(i,': ', h)
resultat_ex8 = None


# EXERCICE 9 : Trouver une position
# Trouver la 1ère position de "g" dans "algorithmique"
# Résultat attendu : 2
# Interdit : find(), index()
# Conseil : utilisez un booléen pour ne retenir que la 1ère occurrence
mot = "algorithmique"
a = 0
for i in mot:
    a = a + 1
    if i == 'g':
        print(a)
resultat_ex9 = None


# EXERCICE 10 : Parcours à l'envers
# Reconstruire "Python" à l'envers en utilisant range(len(mot)-1, -1, -1)
# Résultat attendu : "nohtyP"
# Interdit : [::-1]
mot = "Python"
for j in range(len(mot)-1,-1,-1):
    print(mot[j])
resultat_ex10 = None


# EXERCICE 11 : Majuscules via ASCII
# Transformer "bonjour" en "BONJOUR" caractère par caractère
# Obligatoire : ord() et chr()
# Interdit : upper()
# Rappel : minuscule → majuscule = soustraire 32 au code ASCII
mot = "bonjour"
result = ""
for k in mot:
    if "a" <= k <= "z":
        result = result + chr(ord(k) - 32)
    else : 
        result = result + k

    print(result)
resultat_ex11 = None


# EXERCICE 12 : Filtrer les voyelles
# Construire une chaîne avec uniquement les voyelles de "algorithmique"
# Résultat attendu : "aoiiue"   (voyelles : a, e, i, o, u, y)
mot = "algorithmique"
voy = ["a","e","i","o","u","y"]
for l in mot:
    for m in voy:
        if l == m:
            print(l)
resultat_ex12 = None


# EXERCICE 13 : Table de multiplication
# Construire la table de 7 sous forme de liste de 10 chaînes
# Résultat attendu : ["7 x 1 = 7", "7 x 2 = 14", ..., "7 x 10 = 70"]
ma_list = []
mult = 7
result = 0
txt = ""
for n in range(1,11):
    result = mult * n
    txt = ''n,'' ' x ', mult, ' = ', result
    ma_list.append(txt)
    print(txt)
resultat_ex13 = None


# EXERCICE 14 : Boucles imbriquées — carré d'étoiles
# Construire un carré de n=4 lignes sous forme de liste de chaînes
# Résultat attendu : ["****", "****", "****", "****"]
# Obligatoire : deux boucles for imbriquées (une pour les lignes, une pour les colonnes)
resultat_ex14 = None


# EXERCICE 15 : Comparer deux mots caractère par caractère
# Comparer "algo" et "alco" sans utiliser == entre les deux chaînes entières
# Résultat attendu : {"identiques": False, "position": 2}
# Si les longueurs sont différentes : {"identiques": False, "position": -1}
# Si identiques : {"identiques": True, "position": -1}
resultat_ex15 = None
