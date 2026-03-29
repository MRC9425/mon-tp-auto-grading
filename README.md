# 🚀 Système d'Auto-Grading TP Python

Bienvenue dans le système d'auto-grading pour les TP Python ! Ce système permet une correction automatique et un suivi pédagogique en temps réel.

## 📋 Table des matières

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Pour les élèves](#pour-les-élèves)
5. [Pour les formateurs](#pour-les-formateurs)
6. [Résolution de problèmes](#résolution-de-problèmes)

---

## 🎯 Vue d'ensemble

Ce système permet :

✅ **Tests automatiques** : Chaque commit déclenche des tests  
✅ **Suivi en temps réel** : Résultats enregistrés dans PostgreSQL  
✅ **Historique complet** : Voir la progression de chaque élève  
✅ **Comparaisons** : Comparer les élèves entre eux  
✅ **Feedback immédiat** : Les élèves voient les résultats en live  

---

## 🏗️ Architecture

```
mon-tp-auto-grading/
│
├── 📁 eleves/                    # Code de chaque élève
│   ├── alice/
│   │   ├── tp3.py               # Travail de Alice sur TP3
│   │   ├── tp4.py
│   │   └── ...
│   ├── bob/
│   │   ├── tp3.py
│   │   └── ...
│   └── ...
│
├── 📁 tests/                     # Suite de tests
│   ├── test_tp3.py
│   ├── test_tp4.py
│   └── ...
│
├── 📁 scripts/                   # Scripts utilitaires
│   ├── setup_db.py              # Initialise PostgreSQL
│   ├── save_results.py          # Enregistre résultats en BD
│   └── run_all_tests.py         # Lance les tests
│
├── 📁 .github/workflows/         # GitHub Actions
│   └── test.yml                 # Workflow automatique
│
├── 📄 README.md                 # Ce fichier
├── 📄 requirements.txt          # Dépendances Python
└── 📄 .env.example              # Config PostgreSQL
```

---

## 💾 Installation

### Prérequis

- Python 3.10+
- PostgreSQL 12+
- Git
- GitHub (pour les actions automatiques)

### Étape 1 : Cloner le repo

```bash
git clone https://github.com/ton-username/mon-tp-auto-grading.git
cd mon-tp-auto-grading
```

### Étape 2 : Configurer PostgreSQL

#### Localement (développement)

1. **Créer une base de données** :
```bash
sudo -u postgres psql
CREATE USER tp_user WITH PASSWORD 'tp_password';
CREATE DATABASE tp_grading OWNER tp_user;
\q
```

2. **Copier .env.example → .env** et éditer :
```bash
cp .env.example .env
# Éditer avec tes paramètres PostgreSQL
```

3. **Initialiser les tables** :
```bash
python scripts/setup_db.py
```

#### Sur GitHub Actions (automatique)

GitHub Actions configure PostgreSQL automatiquement dans le workflow.

### Étape 3 : Installer les dépendances

```bash
pip install -r requirements.txt
```

### Étape 4 : Créer la structure des élèves

```bash
# Pour chaque élève
mkdir -p eleves/alice
mkdir -p eleves/bob
mkdir -p eleves/charlie
# ...
```

---

## 👨‍🎓 Pour les élèves

### Workflow quotidien

#### 1️⃣ Cloner le repo

```bash
git clone https://github.com/ton-username/mon-tp-auto-grading.git
cd mon-tp-auto-grading
```

#### 2️⃣ Télécharger le template TP

Par exemple, pour le TP4 :
```bash
# Cherche sur Google Drive ou par email le fichier
# tp4_template_VIDE.py
```

#### 3️⃣ Placer le fichier

```bash
# Crée ton dossier personnel (première fois seulement)
mkdir -p eleves/ton-nom
cp tp4_template_VIDE.py eleves/ton-nom/tp4.py
```

#### 4️⃣ Remplir les exercices

Édite `eleves/ton-nom/tp4.py` et remplis les sections `[ÉCRIVEZ VOTRE CODE ICI]`.

#### 5️⃣ Tester localement (optionnel)

```bash
# Avant de push, vérifie tes résultats
cd eleves/ton-nom
pytest ../../tests/test_tp4.py -v
cd ../..
```

#### 6️⃣ Commiter et pousser

```bash
git add eleves/ton-nom/tp4.py
git commit -m "TP4: Exercices 1-15"
git push
```

#### 7️⃣ Voir les résultats

- GitHub Actions lance **automatiquement** les tests
- Résultats visibles dans l'onglet "Actions" du repo
- Les résultats sont enregistrés dans PostgreSQL

### Conseils

✅ **Teste souvent** : Chaque push = feedback immédiat  
✅ **Commite régulièrement** : Crée un historique  
✅ **Lis les erreurs** : Les messages d'erreur te disent ce qui ne va pas  
✅ **Demande de l'aide** : Crée une issue ou contacte le formateur  

---

## 👨‍🏫 Pour les formateurs

### Voir les résultats

#### Via ligne de commande

```bash
# Lancer les tests en local
python scripts/run_all_tests.py

# Voir les résultats JSON
cat test_results.json
```

#### Via PostgreSQL

```bash
# Voir tous les résultats
psql -U tp_user -d tp_grading -c "SELECT * FROM resultats;"

# Résultats pour un élève
psql -U tp_user -d tp_grading -c \
  "SELECT * FROM resultats WHERE eleve_id = (SELECT id FROM eleves WHERE nom='alice');"

# Progression d'un élève par TP
psql -U tp_user -d tp_grading -c \
  "SELECT tp_name, COUNT(*) as tests_passes, 
   (SELECT COUNT(*) FROM resultats WHERE statut='PASSED') as total
   FROM resultats WHERE eleve_id = 1 GROUP BY tp_name;"
```

#### Via Python

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="tp_user",
    password="tp_password",
    database="tp_grading"
)

cursor = conn.cursor()

# Voir la progression d'Alice
cursor.execute("""
    SELECT tp_name, COUNT(*) as exercices_passes
    FROM resultats
    WHERE eleve_id = (SELECT id FROM eleves WHERE nom='alice')
    AND statut = 'PASSED'
    GROUP BY tp_name
    ORDER BY tp_name
""")

for row in cursor.fetchall():
    print(f"TP {row[0]}: {row[1]} exercices")

conn.close()
```

### Créer un nouveau TP

1. **Créer le template vide** : `tp5_template_VIDE.py`
2. **Créer les tests** : `tests/test_tp5.py`
3. **Créer le doc** : `TP5_MODIFIE.docx`
4. **Distribuer aux élèves**

### Ajouter un élève

```bash
mkdir -p eleves/nouveau-nom-eleve
# L'élève clonera le repo et mettra ses fichiers là
```

### Analyser la progression

**Dashboard (à venir)** : Script Streamlit pour visualiser tout graphiquement.

Pour l'instant, tu peux :
- Consulter les résultats via PostgreSQL
- Générer des graphiques avec Excel/Python
- Créer des rapports personnalisés

---

## 🔧 Configuration PostgreSQL

### .env (exemple)

```ini
# PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_USER=tp_user
DB_PASSWORD=tp_password
DB_NAME=tp_grading

# GitHub (automatique en Actions)
GITHUB_TOKEN=ton_token
```

### Variables d'environnement

Sur **GitHub Actions**, les variables sont définies dans le workflow `.github/workflows/test.yml`.

En **local**, crée un fichier `.env` ou définis les variables :

```bash
export DB_HOST=localhost
export DB_PORT=5432
export DB_USER=tp_user
export DB_PASSWORD=tp_password
export DB_NAME=tp_grading
```

---

## 🆘 Résolution de problèmes

### ❌ "ModuleNotFoundError: No module named 'psycopg2'"

```bash
pip install psycopg2-binary
```

### ❌ "Connection refused" (PostgreSQL)

```bash
# Vérifie que PostgreSQL est démarré
sudo service postgresql status
sudo service postgresql start

# Ou sur macOS
brew services start postgresql@15
```

### ❌ "Authentication failed for user 'tp_user'"

Vérifie les variables d'environnement :
```bash
echo $DB_USER
echo $DB_PASSWORD
```

### ❌ "Test failed: FileNotFoundError: tp.py"

Les tests cherchent `tp.py` dans le dossier de l'élève. Assure-toi que le fichier est bien placé :
```
eleves/alice/tp4.py  ✓
```

### ❌ "GitHub Actions ne lance pas"

Vérifie que le fichier `.github/workflows/test.yml` existe et est bien formaté :
```bash
ls -la .github/workflows/test.yml
```

### ❌ Les tests passent localement mais échouent sur GitHub

Les versions de Python peuvent différer. Vérifie `test.yml` :
```yaml
python-version: '3.10'  # ou '3.11', etc.
```

---

## 📚 Documentation supplémentaire

- [Pytest docs](https://docs.pytest.org/)
- [PostgreSQL docs](https://www.postgresql.org/docs/)
- [GitHub Actions docs](https://docs.github.com/en/actions)

---

## 📞 Support

❓ Questions ? Crée une **issue** sur GitHub ou contacte le formateur.

---

## 📝 Licence

Ce projet est sous licence MIT.

---

**Bon travail ! 🚀**
