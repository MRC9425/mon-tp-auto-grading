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
number = donnees["range1_stop"]
b = []
i = 0
for c in range(number): 
    b.append(i)
    i += 1
#print(b)


# EXERCICE 2 : range(start, stop)
# Construire la liste des valeurs de range(3, 8)
# Résultat attendu : [3, 4, 5, 6, 7]
b = []
i = 0
for c in range(donnees["range2_start"],donnees["range2_stop"],1): 
    b.append(c)
    i += 1
#print(b)


# EXERCICE 3 : range(start, stop, step)
# Construire la liste des valeurs de range(2, 10, 3)
# Résultat attendu : [2, 5, 8]
b = []
i = 0
for c in range(donnees["range3_start"],donnees["range3_stop"],donnees["range3_step"]): 
    b.append(c)
    i += 1
#print(b)
#resultat_ex3 = b


# EXERCICE 4 : range() négatif
# Construire la liste des valeurs de range(5, 0, -1)
# Résultat attendu : [5, 4, 3, 2, 1]
b = []
i = 0
for c in range(donnees["range4_start"],donnees["range4_stop"],donnees["range4_step"]): 
    b.append(c)
    i += 1
#print(b)

#resultat_ex4 = b


# EXERCICE 5 : Compter des occurrences
# Compter le nombre de fois que "s" apparaît dans "mississippi"
# Résultat attendu : 4
# Interdit : count()
word = donnees["chaine1"]
res=0
for l in word:
    if l =="s":
        res+=1
#print (res) 
#resultat_ex5 = res


# EXERCICE 6 : Accumulateur
# Calculer la somme de tous les entiers pairs de 2 à 20 inclus
# Résultat attendu : 110
# Interdit : sum()
number =donnees["somme_fin"]
res=0
for c in range(number+1):
    if c %2==0 :
        res+=c
#print (res)     
#resultat_ex6 = res


# EXERCICE 7 : Multiples
# Construire la liste de tous les multiples de 3 entre 1 et 30 inclus
# Résultat attendu : [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
res=[]
mult=0
j = donnees[ "multiple"]
for i in range(1, 11):
 mult=i*j
 res.append(mult)
#print(res)
#resultat_ex7 = res


# EXERCICE 8 : Position des caractères
# Créer un dictionnaire {position: caractère} pour "algorithmique"
# Résultat attendu : {0: 'a', 1: 'l', 2: 'g', ...}
# Obligatoire : utiliser range() et un index i
word = donnees["chaine2"]
res = [] 
for i in range(len(word)):
    res.append(f"{i}:{word[i]}")
#print(res)
#resultat_ex8 = res


# EXERCICE 9 : Trouver une position
# Trouver la 1ère position de "g" dans "algorithmique"
# Résultat attendu : 2
# Interdit : find(), index()
# Conseil : utilisez un booléen pour ne retenir que la 1ère occurrence
chaine =donnees["chaine3"]
cible = donnees["lettre2"]
position =-1
for i in range(len(chaine)) :
   if chaine[i] == cible and position ==-1 :
      position = i
#print (position)
#resultat_ex9 = position


# EXERCICE 10 : Parcours à l'envers
# Reconstruire "Python" à l'envers en utilisant range(len(mot)-1, -1, -1)
# Résultat attendu : "nohtyP"
# Interdit : [::-1]
chaine = donnees["mot1"]
res=""
for i in range(len(chaine)-1, -1, -1):
  res+=(chaine[i])
#print (res)
# resultat_ex10 = None


# EXERCICE 11 : Majuscules via ASCII
# Transformer "bonjour" en "BONJOUR" caractère par caractère
# Obligatoire : ord() et chr()
# Interdit : upper()
# Rappel : minuscule → majuscule = soustraire 32 au code ASCII
chaine=donnees["chaine4"]
resultat = ""
for c in chaine:
  if "a" <= c <= "z":
    resultat = resultat + chr(ord(c) - 32)
  else: 
    resultat = resultat + c
#print(resultat)
#resultat_ex11 = None


# EXERCICE 12 : Filtrer les voyelles
# Construire une chaîne avec uniquement les voyelles de "algorithmique"
# Résultat attendu : "aoiiue"   (voyelles : a, e, i, o, u, y)
resultat_ex12 = None


# EXERCICE 13 : Table de multiplication
# Construire la table de 7 sous forme de liste de 10 chaînes
# Résultat attendu : ["7 x 1 = 7", "7 x 2 = 14", ..., "7 x 10 = 70"]
j=donnees["table_n"]
res=[]
for i in range(1, 11) :
    res.append(f"{j}x{i}={i*j}")
#print(res)
#resultat_ex13 = None


# EXERCICE 14 : Boucles imbriquées — carré d'étoiles
# Construire un carré de n=4 lignes sous forme de liste de chaînes
# Résultat attendu : ["****", "****", "****", "****"]
# Obligatoire : deux boucles for imbriquées (une pour les lignes, une pour les colonnes)
res = []
for i in range(1, 5):
    temp_str = ""
    for j in range(1, donnees["carre_n"]):
        temp_str += "*"
    res.append(temp_str)  
#for string in res:
    #print(string) 



# EXERCICE 15 : Comparer deux mots caractère par caractère
# Comparer "algo" et "alco" sans utiliser == entre les deux chaînes entières
# Résultat attendu : {"identiques": False, "position": 2}
# Si les longueurs sont différentes : {"identiques": False, "position": -1}
# Si identiques : {"identiques": True, "position": -1}

mot2 = donnees["mot2"]
mot3 = donnees["mot3"]
identiques = True
position = -1
for i in range(len(mot2)):
    if mot2[i] != mot3[i] and identiques:
        identiques = False
        position = i

        resultat = {"identiques": identiques, "position": position}
    else :
       resultat = {"identiques": identiques, "position": position} 
#print(resultat)
#resultat_ex15 = None
