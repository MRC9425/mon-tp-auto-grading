
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
    i += 1


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
    i -= 1

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

somme = 0
i = 1 
while i <= N: 
    somme += i 
    i += 1
resultat_ex3 = somme


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

compteur = 0 
for c in mot: 
    compteur += 1
resultat_ex4 = compteur


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
resultat_ex6 = None


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
resultat_ex7 = None


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

compteur = 0 
i = 0 
while i < len(chaine): 
    if 48 <= ord(chaine[i]) <= 57:
        compteur += 1
    i += 1 
resultat_ex8 = compteur



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
resultat_ex9 = None


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
resultat_ex10 = None


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
resultat_ex11 = None


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
resultat_ex12 = None


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
resultat_ex13 = None


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
resultat_ex14 = None


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
resultat_ex15 = None


# ========================================================
# FIN DU TP4
# ========================================================
# Ne modifiez rien ci-dessous
# Ces variables sont utilisées automatiquement pour la correction

if __name__ == "__main__":
    print("\n✓ Tous tes résultats ont été enregistrés !")
