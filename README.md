# 🎃 Halloween Face Transformer — Base de Projet (Full Python)

Bienvenue dans le projet **Halloween Face Transformer** 👻  
Cette application permet de **transformer une photo en version Halloween** (zombie, vampire, sorcière, etc.) à l’aide d’une IA.

Ce dépôt contient :
- ✅ une **interface Streamlit** (front-end complet)
- ⚙️ des **fichiers backend vides** à implémenter ensuite (OpenAI API, stockage, email)
- 📦 une structure prête à l’emploi pour travailler en équipe

---

## 🧩 Objectif

Créer une application où :
1. L’utilisateur **prend une photo** ou **upload** une image  
2. Il **choisit un effet Halloween** (zombie, vampire, etc.)  
3. L’app génère une **version transformée** via une API d’IA  
4. Il peut **télécharger** ou **envoyer** le résultat par email  

---

## 📂 Structure du projet

```
ouidsChallenge/
├─ app/
│ ├─ ui.py # ✅ Interface Streamlit (front)
│ └─ services/
│   ├─ openai_client.py # ⚙️ Appel à l’API d’image
│   ├─ storage.py # ⚙️ Sauvegarde des images (à coder)
│   └─ mailer.py # ⚙️ Envoi d’emails (à coder)
├─ requirements.txt # Dépendances Python
├─ .env.example # Modèle de configuration
└─ README.md # Ce guide complet
```

---

## ⚙️ Prérequis

### 🧠 Outils nécessaires
- **Python 3.10+**
- **Git** installé
- **VS Code** ou un autre éditeur de code
- **Connexion Internet**
- (Optionnel) un compte [OpenAI](https://platform.openai.com/) pour la future intégration API

---

## 🚀 Installation pas à pas

### 🪜 Étape 1 — Cloner le projet

```bash
git clone https://github.com/Rwouaf/ouidsChallenge.git
cd ouidsChallenge
```


### 🪜 Étape 2 — Créer un environnement virtuel

#### 🪟 Sous Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 🪜 Étape 2 — Créer un environnement virtuel

#### 🪟 Sous Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\activate

# ⚠️ Si PowerShell affiche une erreur "execution of scripts is disabled" :
# 1. Ouvre PowerShell en administrateur
# 2. Tape :  Set-ExecutionPolicy RemoteSigned
# 3. Choisis [A] Oui pour tous, ferme la fenêtre et relance ton terminal. mais parfois y'a pas besoin de le faire !
```
### 🪜 Étape 3 — Installer les dépendances
```powershell
pip install -r requirements.txt
.venv\Scripts\activate
```
💡 Pour sauvegarder les futures dépendances ajoutées :

```powershell
pip freeze > requirements.txt
```

### 🪜 Étape 4 — Lancer l’application
```powershell
streamlit run app/ui.py
```

# Une page s’ouvrira automatiquement sur : http://localhost:8501

## Tu devrais voir :

Le titre "🎃 Halloween Face Transformer"

La caméra ou le bouton d’upload

Une liste d’effets (zombie, vampire, etc.)

Un bouton "Transformer maintenant"

Un bouton "Télécharger le résultat"


# 🧑‍💻 Ce qui fonctionne déjà

✅ Interface Streamlit :

Capture caméra

Upload d’image

Choix d’un effet

Bouton de transformation

Téléchargement d’image

Transformation d'image via call API


# 🧰 Ce qu’il reste à implémenter
## 💾 app/services/storage.py
    def save_image_bytes(img_bytes: bytes, effect: str) -> str:
        """
        TODO:
        - Sauvegarder l'image dans un dossier local (outputs/)
        - Créer le dossier s’il n’existe pas
        - Retourner le chemin du fichier ou une URL
        """
        pass

# 🔐 Fichier .env (optionnel)

Le .env sert à stocker les variables de configuration (clé API, dossier de sortie, etc.).

```bash
OPENAI_API_KEY=
OPENAI_IMAGE_MODEL=gpt-image-1
OUTPUT_DIR=outputs
MAX_UPLOAD_MB=10
ALLOW_PERSIST_OUTPUTS=true
```
## 📋 Pour l’utiliser :

Copier le fichier :

cp .env.example .env


Coller ta clé OpenAI :

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx


✅ .env est déjà dans .gitignore, donc il ne sera pas envoyé sur GitHub.

# 👥 Workflow équipe
🔀 1. Créer une branche
git checkout -b feat/openai-integration

🧠 2. Coder et tester localement
streamlit run app/ui.py

💾 3. Sauvegarder ton travail
git add .
git commit -m "feat: ajout de la méthode transform_face()"
git push origin feat/openai-integration

🧩 4. Ouvrir une Pull Request

Fais une PR sur GitHub pour review avant de fusionner.