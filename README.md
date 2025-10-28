# 🎃 Halloween Face Transformer (Full Python)

Bienvenue dans **Halloween Face Transformer** 👻  
Une application IA qui transforme votre photo en **version Halloween** (zombie, vampire, sorcière, etc.) grâce à **OpenAI** et **Streamlit**.

---

## 🌐 Démo en ligne

🚀 L’application est disponible gratuitement ici :  
👉 **[https://halloween-challenge-2025.streamlit.app/](https://halloween-challenge-2025.streamlit.app/)**  

Pas besoin d’installer quoi que ce soit — charge simplement une photo, choisis un effet (zombie, vampire, etc.), et laisse la magie opérer 🧙‍♀️  

---

## 💻 Utilisation locale (avec ta propre clé OpenAI)

Si tu veux exécuter le projet toi-même, suis les étapes ci-dessous 👇  

---

## ⚙️ Prérequis

### 🧠 Outils nécessaires
- **Python 3.10+**
- **Git**
- **VS Code** ou un autre éditeur
- **Connexion Internet**
- Une **clé OpenAI API** (crée-la ici : [https://platform.openai.com/](https://platform.openai.com/))

---

## 📂 Structure du projet

```
ouidsChallenge/
├─ app/
│  ├─ ui.py                # ✅ Interface Streamlit
│  └─ services/
│     └─ openai_client.py  # ✅ Transformation via OpenAI API
├─ assets/
│  └─ logo.png
├─ requirements.txt         # Dépendances Python
├─ .env.example             # Modèle de configuration
└─ README.md                # Ce guide complet
```

---

## 🚀 Installation locale

### 🪜 Étape 1 — Cloner le projet
```bash
git clone https://github.com/Rwouaf/ouidsChallenge.git
cd ouidsChallenge
```

---

### 🪜 Étape 2 — Créer un environnement virtuel

#### 💻 Sous Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\activate
```

> ⚠️ Si PowerShell affiche une erreur "execution of scripts is disabled" :
> 1. Ouvre PowerShell en administrateur  
> 2. Exécute : `Set-ExecutionPolicy RemoteSigned`  
> 3. Choisis `[A] Oui pour tous`, puis relance ton terminal.

---

### 🪜 Étape 3 — Installer les dépendances
```bash
pip install -r requirements.txt
```

💡 Pour sauvegarder de nouvelles dépendances plus tard :
```bash
pip freeze > requirements.txt
```

---

### 🪜 Étape 4 — Configurer ton fichier `.env`

Copie le modèle :
```bash
cp .env.example .env
```

Puis ouvre `.env` et ajoute **ta clé OpenAI personnelle** :
```
API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

---

### 🪜 Étape 5 — Lancer l’application
```bash
streamlit run app/ui.py
```

Une page s’ouvrira automatiquement sur :  
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧑‍💻 Fonctionnalités principales

✅ Interface **Streamlit** complète :  
- Capture caméra / Upload d’image  
- Choix d’un effet (zombie, vampire, sorcière, etc.)  
- Transformation IA via OpenAI  
- Téléchargement du résultat  

✅ Sécurité :
- La clé API reste **locale** et **n’est jamais exposée**  
- L’hébergement public (sur Streamlit Cloud) utilise **des secrets serveur sécurisés**

---

## 🌐 Hébergement

L’app est hébergée gratuitement sur **Streamlit Cloud**.  
👉 [https://halloween-challenge-2025.streamlit.app/](https://halloween-challenge-2025.streamlit.app/)

Les utilisateurs peuvent :
- Utiliser le site en ligne (aucune configuration requise)  
- Ou cloner le dépôt et **utiliser leur propre clé OpenAI** localement.

---

## 🎉 Auteur

Projet créé par **Raphaël Direz**, **Alexandre Rousselle** et **Orion Prieto**"" — 2025  
🧡 Basé sur **Python + Streamlit + OpenAI**
