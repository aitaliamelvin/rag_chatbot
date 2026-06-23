# 📚 Chatbot RAG avec FastAPI, Streamlit et OpenAI

## 📌 Description

Ce projet est un chatbot RAG (Retrieval-Augmented Generation) permettant d'interroger des documents PDF en langage naturel.

L'utilisateur peut importer un ou plusieurs fichiers PDF, sélectionner le document à analyser puis poser des questions directement sur son contenu.

Le système utilise une recherche sémantique afin de retrouver les passages les plus pertinents avant de générer une réponse avec un modèle OpenAI.

---

## 🚀 Fonctionnalités

* Upload de fichiers PDF
* Gestion de plusieurs documents
* Sélection du document à interroger
* Suppression de documents
* Historique de conversation
* Réinitialisation de la conversation
* Recherche sémantique avec ChromaDB
* Génération de réponses avec OpenAI
* Affichage des sources utilisées
* Interface utilisateur moderne avec Streamlit
* API REST développée avec FastAPI

---

## 🛠️ Technologies utilisées

### Backend

* Python
* FastAPI
* LangChain
* OpenAI API

### Frontend

* Streamlit

### Base vectorielle

* ChromaDB

### Traitement documentaire

* PyPDF
* RecursiveCharacterTextSplitter

---

## 📂 Structure du projet

```bash
rag_chatbot/
│
├── app/
│   └── main.py
│
├── src/
│   ├── ingest.py
│   ├── rag.py
│   └── vector_store.py
│
├── data/
│   └── documents/
│
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone <url_du_repo>
cd rag_chatbot
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 3. Activer l'environnement virtuel

Sous Windows :

```bash
.venv\Scripts\Activate.ps1
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Créer un fichier `.env` à la racine du projet :

```env
OPENAI_API_KEY=votre_cle_api
```

---

## ▶️ Lancer l'application

### Démarrer l'API FastAPI

```bash
uvicorn app.main:app --reload
```

### Démarrer Streamlit

```bash
streamlit run streamlit_app.py
```

---

## 🧠 Fonctionnement du système RAG

1. Import d'un PDF.
2. Découpage du document en chunks.
3. Création des embeddings OpenAI.
4. Stockage des embeddings dans ChromaDB.
5. Recherche des passages les plus pertinents.
6. Génération d'une réponse contextualisée avec GPT.

---

## 📸 Aperçu

*Ajouter ici des captures d'écran de l'application.*

---

## 🔮 Améliorations futures

* Mémoire conversationnelle avancée
* Déploiement cloud
* Support d'autres formats (Word, TXT)
* Authentification utilisateur
* Gestion de plusieurs conversations

---

## 🌐 Démonstration en ligne

L'application est accessible à l'adresse suivante :

https://rag-chatbot-melvin.streamlit.app/

---

## 👨‍💻 Auteur

Projet réalisé par **Melvin Ait-Alia** dans le cadre d'un apprentissage des systèmes RAG et des technologies d'IA générative.
