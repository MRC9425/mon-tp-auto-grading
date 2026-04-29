# ========================================================
# TP4 : La boucle while
# ========================================================
# NE PAS MODIFIER CETTE SECTION - DONNÉES DE TEST
# ========================================================

donnees = {
    "ex1": {"N": 4},
    "ex2": {"N": 4},
    "ex3": {"N": 5},
    "ex4": {"mot": "algorithmique"},
    "ex5": {"propositions": [25, 0, 5, 7]},
    "ex6": {"mot": "python", "caractere": "y"},
    "ex7": {"mot": "algorithmique", "caractere": "g"},
    "ex8": {"chaine": "Python3 est version 3.11"},
    "ex9": {"nombre": 1234},
    "ex10": {"nombre": 1234},
    "ex11": {"nombre": 7},
    "ex12": {"N": 7},
    "ex13": {"cible": 42, "propositions": [50, 35, 42]},
    "ex14": {"N": 5},
    "ex15": {"notes": [14, 17, 8, 25, 11, -1]},
}

# ========================================================
# EXERCICE 1 : Compter jusqu'à N
# ========================================================
# Comptez tous les entiers de 1 à N (inclus), un par ligne.
# Utilisez une boucle while.
#
# FORMAT REQUIS :
#   - Créez la variable resultat_ex1
#   - Stockez chaque nombre dans resultat_ex1 (sous forme de liste)
#   - Vous pouvez aussi afficher pour vérifier (optionnel)
#
# Exemple pour N = 4 : [1, 2, 3, 4]

N = donnees["ex1"]["N"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex1 = []
i = 1
while i <= N:
    resultat_ex1.append(i)
    i = i + 1


# ========================================================
# EXERCICE 2 : Compte à rebours
# ========================================================
# Affichez le compte à rebours de N jusqu'à 0 (inclus).
#
# FORMAT REQUIS :
#   - Créez resultat_ex2
#   - Stockez le résultat sous forme de liste
#
# Exemple pour N = 4 : [4, 3, 2, 1, 0]

N = donnees["ex2"]["N"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex2 = []
i = N
while i >= 0:
    resultat_ex2.append(i)
    i = i - 1


# ========================================================
# EXERCICE 3 : Somme de 1 à N
# ========================================================
# Calculez la somme 1 + 2 + 3 + ... + N sans utiliser sum() ni range().
#
# FORMAT REQUIS :
#   - Créez resultat_ex3
#   - Stockez la somme (nombre entier)
#
# Exemple pour N = 5 : 15
# Vérification : testez avec N = 100 — vous devriez obtenir 5050.

N = donnees["ex3"]["N"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex3 = 0
i = 1
while i <= N:
    resultat_ex3 = resultat_ex3 + i
    i = i + 1


# ========================================================
# EXERCICE 4 : Longueur d'un mot sans len()
# ========================================================
# Calculez la longueur sans utiliser len().
#
# FORMAT REQUIS :
#   - Créez resultat_ex4
#   - Stockez la longueur (nombre entier)
#
# Exemple : "algorithmique" → 13

mot = donnees["ex4"]["mot"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex4 = 0
i = 0
while i < len(mot):
    resultat_ex4 = resultat_ex4 + 1
    i = i + 1


# ========================================================
# EXERCICE 5 : Validation de saisie (version adaptation)
# ========================================================
# ADAPTATION : Au lieu de demander à l'utilisateur, vous avez une liste 
# de propositions. Parcourez-la et trouvez la première valide (1-10).
# Comptez combien de propositions invalides avant la valide.
#
# FORMAT REQUIS :
#   - Créez resultat_ex5
#   - Stockez: {"valeur": X, "essais": N}
#
# Exemple propositions: [25, 0, 5, 7]
# → La première valide est 5 (essai numéro 3)

propositions = donnees["ex5"]["propositions"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex5 = None
essais = 0
i = 0
while i < len(propositions):
    essais = essais + 1
    if 1 <= propositions[i] <= 10:
        resultat_ex5 = {"valeur": propositions[i], "essais": essais}
        i = len(propositions)  
    i = i + 1

# ========================================================
# EXERCICE 6 : Chercher un caractère sans in
# ========================================================
# Indiquez si un caractère est présent dans un mot, sans utiliser in.
#
# FORMAT REQUIS :
#   - Créez resultat_ex6
#   - Stockez: "Présent" ou "Absent"
#
# Exemple : mot "python", caractère "y" → "Présent"

mot = donnees["ex6"]["mot"]
caractere = donnees["ex6"]["caractere"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex6 = "Absent"
i = 0
while i < len(mot):
    if mot[i] == caractere:
        resultat_ex6 = "Présent"
        i = len(mot)  
    i = i + 1

# ========================================================
# EXERCICE 7 : Position d'un caractère sans find()
# ========================================================
# Affichez la position de la première occurrence, sans utiliser find() ni index().
# Si absent, affichez -1.
#
# FORMAT REQUIS :
#   - Créez resultat_ex7
#   - Stockez la position (entier, -1 si absent)
#
# Exemple : mot "algorithmique", caractère "g" → 4

mot = donnees["ex7"]["mot"]
caractere = donnees["ex7"]["caractere"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex7 = -1
i = 0
while i < len(mot):
    if mot[i] == caractere and resultat_ex7 == -1:
        resultat_ex7 = i
        i = len(mot)  # forcer la sortie sans break
    i = i + 1

# ========================================================
# EXERCICE 8 : Compter les chiffres dans une chaîne
# ========================================================
# Comptez les chiffres (0-9) sans utiliser isdigit().
# Utilisez les codes ASCII : ord('0') à ord('9')
#
# FORMAT REQUIS :
#   - Créez resultat_ex8
#   - Stockez le nombre de chiffres
#
# Exemple : "Python3 est version 3.11" → 4 chiffres

chaine = donnees["ex8"]["chaine"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex8 = 0
i = 0
while i < len(chaine):
    if 48 <= ord(chaine[i]) <= 57:
        resultat_ex8 = resultat_ex8 + 1
    i = i + 1


# ========================================================
# EXERCICE 9 : Somme des chiffres d'un entier
# ========================================================
# Calculez la somme de ses chiffres.
# Rappel : n % 10 = dernier chiffre, n // 10 = supprime le dernier
#
# FORMAT REQUIS :
#   - Créez resultat_ex9
#   - Stockez la somme des chiffres
#
# Exemple : 1234 → 1 + 2 + 3 + 4 = 10

nombre = donnees["ex9"]["nombre"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex9 = 0
n = nombre
while n > 0:
    resultat_ex9 = resultat_ex9 + n % 10
    n = n // 10


# ========================================================
# EXERCICE 10 : Inverser un entier
# ========================================================
# Affichez cet entier avec ses chiffres dans l'ordre inverse.
# Même technique que l'exercice 9.
#
# FORMAT REQUIS :
#   - Créez resultat_ex10
#   - Stockez le nombre inversé (entier)
#
# Exemple : 1234 → 4321
# Exemple : 5600 → 65 (les zéros de tête disparaissent)

nombre = donnees["ex10"]["nombre"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex10 = 0
n = nombre
while n > 0:
    resultat_ex10 = resultat_ex10 * 10 + n % 10
    n = n // 10


# ========================================================
# EXERCICE 11 : Nombre premier
# ========================================================
# Indiquez si un nombre est premier (divisible uniquement par 1 et lui-même).
# Un nombre n n'est pas premier s'il existe un diviseur d : 2 ≤ d ≤ n-1, n%d == 0
#
# FORMAT REQUIS :
#   - Créez resultat_ex11
#   - Stockez: True ou False
#
# Exemple : 7 → True (premier), 12 → False (non premier)

nombre = donnees["ex11"]["nombre"]

# [ÉCRIVEZ VOTRE CODE ICI]

if nombre < 2:
    resultat_ex11 = False
else:
    resultat_ex11 = True
    d = 2
    while d <= nombre - 1:
        if nombre % d == 0:
            resultat_ex11 = False
            d = nombre  
        d = d + 1


# ========================================================
# EXERCICE 12 : Table de multiplication
# ========================================================
# Affichez la table de multiplication de N de 1 à 10.
#
# FORMAT REQUIS :
#   - Créez resultat_ex12
#   - Stockez une liste avec les résultats
#   - Format: ["7 x 1 = 7", "7 x 2 = 14", ...]
#
# Exemple pour N = 7 :
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

N = donnees["ex12"]["N"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex12 = []
i = 1
while i <= 10:
    resultat_ex12.append(f"{N} x {i} = {N * i}")
    i = i + 1


# ========================================================
# EXERCICE 13 : Jeu de devinette (version adaptation)
# ========================================================
# ADAPTATION : Vous avez une cible et une liste de propositions.
# Parcourez les propositions jusqu'à trouver la cible.
# Comptez le nombre d'essais.
#
# FORMAT REQUIS :
#   - Créez resultat_ex13
#   - Stockez le nombre d'essais pour trouver
#
# Exemple : cible=42, propositions=[50, 35, 42]
# → 3 essais pour trouver

cible = donnees["ex13"]["cible"]
propositions = donnees["ex13"]["propositions"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex13 = 0
i = 0
while i < len(propositions):
    resultat_ex13 = resultat_ex13 + 1
    if propositions[i] == cible:
        i = len(propositions)  # forcer la sortie sans break
    i = i + 1


# ========================================================
# EXERCICE 14 : Factorielle
# ========================================================
# Calculez N! sans utiliser math.factorial().
# Rappel : N! = 1 × 2 × 3 × ... × N et 0! = 1
#
# FORMAT REQUIS :
#   - Créez resultat_ex14
#   - Stockez la factorielle (entier)
#
# Exemple : 5! = 1 × 2 × 3 × 4 × 5 = 120
# Vérification : 10! = 3628800

N = donnees["ex14"]["N"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex14 = 1
i = 1
while i <= N:
    resultat_ex14 = resultat_ex14 * i
    i = i + 1


# ========================================================
# EXERCICE 15 : Relevé de notes (intégrateur complet)
# ========================================================
# ADAPTATION : Au lieu de demander notes une par une,
# vous avez une liste de notes qui se termine par -1.
# Parcourez la liste, validez chaque note (0-20),
# et calculez : nombre, moyenne, max, min.
#
# FORMAT REQUIS :
#   - Créez resultat_ex15
#   - Stockez un dictionnaire :
#     {
#       "nombre": N,
#       "moyenne": X.XX,
#       "max": Y,
#       "min": Z
#     }
#
# Contraintes : pas de sum(), min(), max() natifs, pas de break
#
# Exemple : notes = [14, 17, 8, 25, 11, -1]
# → 4 notes valides, moyenne = 12.50, max = 17, min = 8

notes_liste = donnees["ex15"]["notes"]

# [ÉCRIVEZ VOTRE CODE ICI]
nombre_notes = 0
total = 0
note_max = 0
note_min = 20
i = 0
while i < len(notes_liste):
    note = notes_liste[i]
    if note == -1:
        i = len(notes_liste)  
    elif 0 <= note <= 20:
        nombre_notes = nombre_notes + 1
        total = total + note
        if note > note_max:
            note_max = note
        if note < note_min:
            note_min = note
    i = i + 1

if nombre_notes > 0:
    moyenne = total / nombre_notes
else:
    moyenne = 0

resultat_ex15 = {
    "nombre": nombre_notes,   # 4
    "moyenne": moyenne,       # 12.50
    "max": note_max,          # 17
    "min": note_min,          # 8
}


# ========================================================
# FIN DU TP4
# ========================================================
# Ne modifiez rien ci-dessous
# Ces variables sont utilisées automatiquement pour la correction

if __name__ == "__main__":
    print("\n✓ Tous tes résultats ont été enregistrés !")
