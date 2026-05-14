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

liste1 = [];
for i in range(5) :
    liste1.append(i); 

resultat_ex1 = liste1;

# EXERCICE 2 : range(start, stop)
# Construire la liste des valeurs de range(3, 8)
# Résultat attendu : [3, 4, 5, 6, 7]
liste2 = []; 
for i in range(3,8) :
    liste2.append(i);

resultat_ex2 = liste2;

# EXERCICE 3 : range(start, stop, step)
# Construire la liste des valeurs de range(2, 10, 3)
# Résultat attendu : [2, 5, 8]
#
liste3 = []; 
for i in range (2, 10, 3) :
    liste3.append(i);

resultat_ex3 = liste3;

# EXERCICE 4 : range() négatif
# Construire la liste des valeurs de range(5, 0, -1)
# Résultat attendu : [5, 4, 3, 2, 1]
#resultat_ex4 = 
liste4 = []; 
for i in range (5, 0, -1) :
    liste4.append(i);

resultat_ex4 = liste4;

# EXERCICE 5 : Compter des occurrences
# Compter le nombre de fois que "s" apparaît dans "mississippi"
# Résultat attendu : 4
# Interdit : count()
chaine5 = "mississippi";
cible ="s";
compteur5 = 0;

for c in chaine5 :
    if c == cible : 
        compteur5 += 1;

        resultat_ex5 = compteur5;

# EXERCICE 6 : Accumulateur
# Calculer la somme de tous les entiers pairs de 2 à 20 inclus
# Résultat attendu : 110
# Interdit : sum()
somme6 = 0;
for i in range (2, 21, 2) :
    somme6 += i;
    
resultat_ex6 = somme6;    

# EXERCICE 7 : Multiples
# Construire la liste de tous les multiples de 3 entre 1 et 30 inclus
# Résultat attendu : [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
liste5 = [];
for i in range(1, 11) :
    for j in range (3, 31, 3) :
        res7 = liste5.append(i*j); 

resultat_ex7 = res7;

# EXERCICE 8 : Position des caractères
# Créer un dictionnaire {position: caractère} pour "algorithmique"
# Résultat attendu : {0: 'a', 1: 'l', 2: 'g', ...}
# Obligatoire : utiliser range() et un index i
mot8 = "algorithmique";
compteur8 = 0;

for i in range(len(mot)) :
    

resultat_ex8 = None


# EXERCICE 9 : Trouver une position
# Trouver la 1ère position de "g" dans "algorithmique"
# Résultat attendu : 2
# Interdit : find(), index()
# Conseil : utilisez un booléen pour ne retenir que la 1ère occurrence
mot9 = "algorithmique";
cible = "g";
position9 = 3;

for i in range (len(mot9)) :
    if mot9[i] == cible and position9 == 3 :
        position9 = i;

resultat_ex9 = i;


# EXERCICE 10 : Parcours à l'envers
# Reconstruire "Python" à l'envers en utilisant range(len(mot)-1, -1, -1)
# Résultat attendu : "nohtyP"
# Interdit : [::-1]
mot10 = "Python";

for i in range (len(mot)-1, -1, -1) : 

resultat_ex10 = mot10[i];


# EXERCICE 11 : Majuscules via ASCII
# Transformer "bonjour" en "BONJOUR" caractère par caractère
# Obligatoire : ord() et chr()
# Interdit : upper()
# Rappel : minuscule → majuscule = soustraire 32 au code ASCII
mot11 = "bonjour";
resultat11 =""
for c in mot11 :
    if "a" <= c <= "z" :
        resultat11 = resultat11 + chr(ord(c) - 32)
    else :
        resultat11 = resultat11 + c;    

resultat_ex11 = resultat11;


# EXERCICE 12 : Filtrer les voyelles
# Construire une chaîne avec uniquement les voyelles de "algorithmique"
# Résultat attendu : "aoiiue"   (voyelles : a, e, i, o, u, y)
mot12 = "algorithmique";
voyelles = "aeiouy";
res12 = "";

for i in range(len(mot12)): 
    if mot[i] == voyelles :
        i+= res;
resultat_ex12 = res12;


# EXERCICE 13 : Table de multiplication
# Construire la table de 7 sous forme de liste de 10 chaînes
# Résultat attendu : ["7 x 1 = 7", "7 x 2 = 14", ..., "7 x 10 = 70"]
liste6 = [];

for i in range(1, 11) :
    res13 = (i , "x", 7, "=", i*7);

resultat_ex13 = res13;


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
mot15 = "algo";
mot152 = "alco";
identification = True;
position = -1;

for i in range (len(mot15)) :
    if mot15[i] != mot152[i] :
        identification = False;

resultat_ex15 = "identiques :", identification , "position :", 
