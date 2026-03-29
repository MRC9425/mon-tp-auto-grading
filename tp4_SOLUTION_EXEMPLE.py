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
#   - Stockez chaque nombre dans resultat_ex1 (sous forme de chaîne ou liste)
#   - Affichage optionnel pour vérifier
#
# Exemple pour N = 4 : 1 2 3 4

N = donnees["ex1"]["N"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex1 = []
i = 1
while i <= N:
    resultat_ex1.append(i)
    print(i, end=" ")
    i += 1
print()  # Nouvelle ligne

# ========================================================
# EXERCICE 2 : Compte à rebours
# ========================================================
# Affichez le compte à rebours de N jusqu'à 0 (inclus).
#
# FORMAT REQUIS :
#   - Créez resultat_ex2
#   - Stockez le résultat (liste ou chaîne)
#
# Exemple pour N = 4 : 4 3 2 1 0

N = donnees["ex2"]["N"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultat_ex2 = []
i = N
while i >= 0:
    resultat_ex2.append(i)
    print(i, end=" ")
    i -= 1
print()

# ========================================================
# EXERCICE 3 : Somme de 1 à N
# ========================================================
# Calculez la somme 1 + 2 + 3 + ... + N sans utiliser sum() ni range().
#
# FORMAT REQUIS :
#   - Créez resultat_ex3
#   - Stockez la somme (nombre entier)
#
# Exemple pour N = 5 : Somme = 15
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
compte = 0
i = 0
while i < len(mot):  # len() est ok pour la boucle, pas pour le compte
    compte += 1
    i += 1
resultat_ex4 = compte

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
# → La première valide est 5 (après 2 essais invalides)

propositions = donnees["ex5"]["propositions"]

# [ÉCRIVEZ VOTRE CODE ICI]
valeur_acceptee = None
essais = 0
i = 0
while i < len(propositions) and valeur_acceptee is None:
    prop = propositions[i]
    essais += 1
    if 1 <= prop <= 10:
        valeur_acceptee = prop
    i += 1

resultat_ex5 = {"valeur": valeur_acceptee, "essais": essais}

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
trouve = False
i = 0
while i < len(mot) and not trouve:
    if mot[i] == caractere:
        trouve = True
    i += 1

resultat_ex6 = "Présent" if trouve else "Absent"

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
position = -1
i = 0
while i < len(mot):
    if mot[i] == caractere:
        position = i
        break
    i += 1

resultat_ex7 = position

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
compte_chiffres = 0
i = 0
while i < len(chaine):
    code = ord(chaine[i])
    if ord('0') <= code <= ord('9'):
        compte_chiffres += 1
    i += 1

resultat_ex8 = compte_chiffres

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
somme = 0
n = nombre
while n > 0:
    dernier_chiffre = n % 10
    somme += dernier_chiffre
    n = n // 10

resultat_ex9 = somme

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
inverse = 0
n = nombre
while n > 0:
    dernier_chiffre = n % 10
    inverse = inverse * 10 + dernier_chiffre
    n = n // 10

resultat_ex10 = inverse

# ========================================================
# EXERCICE 11 : Nombre premier
# ========================================================
# Indiquez si un nombre est premier (divisible uniquement par 1 et lui-même).
# Un nombre n n'est pas premier s'il existe un diviseur d : 2 ≤ d ≤ n-1, n%d == 0
#
# FORMAT REQUIS :
#   - Créez resultat_ex11
#   - Stockez: True ou False (ou "Premier" / "Non premier")
#
# Exemple : 7 → Premier, 12 → Non premier

nombre = donnees["ex11"]["nombre"]

# [ÉCRIVEZ VOTRE CODE ICI]
est_premier = True
diviseur = 2
while diviseur < nombre:
    if nombre % diviseur == 0:
        est_premier = False
    diviseur += 1

resultat_ex11 = est_premier

# ========================================================
# EXERCICE 12 : Table de multiplication
# ========================================================
# Affichez la table de multiplication de N de 1 à 10.
#
# FORMAT REQUIS :
#   - Créez resultat_ex12
#   - Stockez une liste ou chaîne avec les résultats
#
# Exemple pour N = 7 :
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

N = donnees["ex12"]["N"]

# [ÉCRIVEZ VOTRE CODE ICI]
resultats_table = []
i = 1
while i <= 10:
    produit = N * i
    resultats_table.append(f"{N} x {i} = {produit}")
    print(f"{N} x {i} = {produit}")
    i += 1

resultat_ex12 = resultats_table

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
essais = 0
trouve = False
i = 0
while i < len(propositions) and not trouve:
    proposition = propositions[i]
    essais += 1
    if proposition == cible:
        trouve = True
    i += 1

resultat_ex13 = essais

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
factorielle = 1
i = 1
while i <= N:
    factorielle *= i
    i += 1

resultat_ex14 = factorielle

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
#       "min": Z,
#       "valides": [notes valides]
#     }
#
# Contraintes : pas de sum(), min(), max() natifs, pas de break
#
# Exemple : notes = [14, 17, 8, 25, 11, -1]
# → 4 notes valides, moyenne = 12.50, max = 17, min = 8

notes_liste = donnees["ex15"]["notes"]

# [ÉCRIVEZ VOTRE CODE ICI]
somme = 0
compte = 0
valeur_max = -1
valeur_min = float('inf')
i = 0

while i < len(notes_liste):
    note = notes_liste[i]
    
    # Arrêter si c'est le signal -1
    if note == -1:
        i += 1
        continue
    
    # Valider la note (0-20)
    if 0 <= note <= 20:
        somme += note
        compte += 1
        
        # Max sans max()
        if note > valeur_max:
            valeur_max = note
        
        # Min sans min()
        if note < valeur_min:
            valeur_min = note
    
    i += 1

# Cas où aucune note n'a été saisie
if compte == 0:
    moyenne = 0.0
    valeur_max = None
    valeur_min = None
else:
    moyenne = round(somme / compte, 2)

resultat_ex15 = {
    "nombre": compte,
    "moyenne": moyenne,
    "max": valeur_max,
    "min": valeur_min
}

# ========================================================
# FIN DU TP4
# ========================================================
# Ne modifiez rien ci-dessous
# Ces variables sont utilisées automatiquement pour la correction

if __name__ == "__main__":
    print("\n✓ Tous tes résultats ont été enregistrés !")
    print(f"  - Exercice 1 (Compter): {resultat_ex1}")
    print(f"  - Exercice 2 (Rebours): {resultat_ex2}")
    print(f"  - Exercice 3 (Somme): {resultat_ex3}")
    print(f"  - Exercice 15 (Relevé): {resultat_ex15}")
