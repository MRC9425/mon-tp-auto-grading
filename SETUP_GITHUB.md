# 📖 Guide de setup - GitHub + PostgreSQL

## Étape 1 : Créer le repo sur GitHub

1. **Sur GitHub.com** :
   - Clique sur **"New repository"**
   - Nom : `mon-tp-auto-grading`
   - Description : "Système d'auto-grading pour les TP Python"
   - **Public** (pour que les élèves le voient)
   - ✅ Initialize with README

2. **Récupère le lien** :
   ```
   https://github.com/ton-username/mon-tp-auto-grading.git
   ```

---

## Étape 2 : Initialiser le repo en local

```bash
# Clone le repo
git clone https://github.com/ton-username/mon-tp-auto-grading.git
cd mon-tp-auto-grading

# Ajoute tous les fichiers de ce projet
# (copie les dossiers: .github, eleves, scripts, tests, etc.)

git add .
git commit -m "Initial commit: système auto-grading"
git push origin main
```

---

## Étape 3 : Configurer PostgreSQL sur GitHub Actions

### ✅ Automatique (recommandé)

Le fichier `.github/workflows/test.yml` configure PostgreSQL **automatiquement** dans GitHub Actions.

**Rien à faire** — ça marche out-of-the-box ! 🎉

### ⚠️ Optionnel : Configurer une vraie BD en ligne

Si tu veux persister les résultats en ligne :

**Option A : Railway (gratuit)**
1. Crée un compte sur [railway.app](https://railway.app)
2. Crée une DB PostgreSQL
3. Copie l'URL de connexion
4. Sur GitHub : Settings → Secrets and variables → New repository secret
   - Nom : `DATABASE_URL`
   - Valeur : `postgresql://user:pass@host:port/dbname`

**Option B : Heroku / AWS RDS / DigitalOcean**
- Même procédure : crée une BD, ajoute l'URL en secret GitHub

---

## Étape 4 : Vérifier que tout fonctionne

1. **Va dans l'onglet Actions** sur GitHub
2. Tu dois voir le workflow `Auto-grading TP` qui s'exécute
3. Clique dessus pour voir les logs

---

## Étape 5 : Ajouter les élèves

### Option A : Donner accès en write

```
Settings → Collaborators → Add people
```

Chaque élève peut directement pusher dans le repo.

### Option B : Via forks (plus sécurisé)

1. Les élèves font un **fork** du repo
2. Ils complètent leur travail
3. Ils font un **Pull Request** (PR)
4. Tu vérifies et merges

---

## 🧪 Tester le workflow

### 1️⃣ En local d'abord

```bash
# Ajoute quelques fichiers de test dans eleves/
mkdir -p eleves/test-student
cp tp4_template_VIDE.py eleves/test-student/tp4.py

# Édite et remplis quelques exercices

# Commit et push
git add eleves/test-student/tp4.py
git commit -m "Test: tp4 exercices 1-3"
git push
```

### 2️⃣ Vérifie sur GitHub

- Onglet **Actions**
- Vois les tests s'exécuter
- Clique sur le workflow pour voir les logs
- Les résultats doivent s'enregistrer en BD

---

## 🔐 Secrets GitHub

Si tu utilises une BD en ligne, ajoute les variables :

**Settings → Secrets and variables → Repository secrets**

```
DB_HOST = ta-host
DB_PORT = 5432
DB_USER = tp_user
DB_PASSWORD = ***
DB_NAME = tp_grading
```

---

## ❓ Dépannage

### "PostgreSQL connection refused"

→ C'est normal en Actions ! PostgreSQL est créé **localement** dans le conteneur.
Les résultats ne persistent que si tu configures une BD en ligne.

### "Test failed: module 'tp4' not found"

→ Assure-toi que les fichiers sont bien placés :
```
eleves/alice/tp4.py  ✓
eleves/bob/tp4.py    ✓
```

### Les logs d'Actions sont vides

→ Attends quelques secondes, rafraîchis la page.

---

## 📊 Voir les résultats

### Option 1 : En JSON (GitHub Actions)

```
Après chaque run :
Onglet Actions → Voir les logs
→ test_results.json en artefact
```

### Option 2 : En BD (si tu as PostgreSQL local)

```bash
psql -U tp_user -d tp_grading
SELECT * FROM resultats;
```

### Option 3 : Dashboard (à venir)

Streamlit pour visualiser tout graphiquement.

---

## 🚀 Prochaines étapes

1. ✅ Setup GitHub Actions
2. ✅ Ajouter les élèves
3. ⏳ Créer le dashboard Streamlit
4. ⏳ Intégrer une vraie BD en ligne

---

**C'est prêt ! 🎉**

Tes élèves peuvent maintenant :
1. Cloner le repo
2. Ajouter `eleves/leur-nom/tp4.py`
3. Compléter les exercices
4. Commiter et pusher
5. Les tests s'exécutent automatiquement !
