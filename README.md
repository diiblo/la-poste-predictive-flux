# 📦 Prédiction des flux colis La Poste – Machine Learning, Airflow & Streamlit

🚀 Projet Data Engineering complet de bout en bout simulant un cas métier réel de **prédiction opérationnelle de flux logistique**, avec :

* Modélisation prédictive avec LightGBM
* Orchestration automatique via Airflow
* Stockage dans PostgreSQL
* Visualisation interactive via Streamlit

---

## 🎯 Objectif pédagogique

Développer un pipeline **de prédiction automatisée** et visualisable, dans un contexte logistique.

Ce projet permet de mettre en pratique :

* 🔄 l’automatisation d’un modèle ML en production
* 📊 la création d’un dashboard dynamique
* 🧱 l’architecture complète d’un projet Data Engineering réaliste

🎓 Réalisé dans le cadre de ma formation en Mastère 2 **Data Engineering** à l’**ECE Paris**, dans une logique orientée **projet professionnel**.

---

## ⚙️ Stack Technique

| Outil / Librairie           | Rôle                                  |
| --------------------------- | ------------------------------------- |
| **Python**                  | Traitement, Machine Learning          |
| **Pandas / Numpy**          | Préparation de données                |
| **Scikit-learn / LightGBM** | Modélisation prédictive               |
| **Airflow**                 | Orchestration automatique quotidienne |
| **PostgreSQL**              | Stockage structuré des prédictions    |
| **Streamlit**               | Dashboard dynamique interactif        |
| **Docker**                  | Environnement reproductible           |

---

## 🧱 Architecture du Projet

```
la-poste-predictive-flux/
├── airflow/              # Déploiement Airflow (DAG + Docker)
├── app/                  # Dashboard Streamlit
├── data/                 # Données brutes, synthétiques, fusionnées
├── diagrams/             # Architecture, flux de données
├── models/               # Modèles ML entraînés (.pkl)
├── notebooks/            # Analyse exploratoire et entraînement
├── src/                  # Scripts modulaires Python
├── README.md             # Document de présentation du projet
```

---

## 🚀 Pipeline Étape par Étape

1. **📥 Collecte & génération de données**

   * Données colis synthétiques
   * Données météo via API
   * Jours fériés officiels (France 2005–2030)

2. **🧹 Prétraitement**

   * Fusion des datasets
   * Création de variables temporelles & météo
   * Insertion dans PostgreSQL (`merged_data`)

3. **🧠 Modélisation**

   * Entraînement avec LightGBM + optimisation
   * Évaluation : RMSE ≈ 49, R² ≈ 0.94
   * Sauvegarde du modèle + scaler (`.pkl`)

4. **☁️ Déploiement via Airflow**

   * DAG journalier `predict_colis_daily`
   * Prédictions pour les 5 centres de tri
   * Insertion des résultats dans la base PostgreSQL

5. **📊 Dashboard Streamlit**

   * Interface dynamique : date + centre
   * Graphiques + tableau de valeurs
   * Lecture en live depuis PostgreSQL

---

## ✅ État d’avancement du projet (TODO)

### 📁 Préparation des données

* [x] Génération des données colis #data
* [x] Collecte météo + jours fériés #data
* [x] Fusion et enrichissement #data
* [x] Stockage `merged_data` dans PostgreSQL #data

### 🤖 Modélisation

* [x] Exploration et EDA #model
* [x] Entraînement LightGBM #model
* [x] Optimisation hyperparamètres #model

### 📊 Dashboarding

* [x] Création Streamlit connecté à PostgreSQL #dashboard

### ☁️ Déploiement

* [x] DAG Airflow journalier #deployment
* [x] Sauvegarde automatique en base #deployment

### 📚 Documentation

* [x] Ajout de README #docs
* [x] Ajout schéma draw\.io architecture technique #docs

---

## 📸 Capture du Dashboard

![png](/assets/image.png)

---

## 📊 Exemple de prédictions

| date       | centre\_id | prediction |
| ---------- | ---------- | ---------- |
| 2025-06-05 | 1          | 868        |
| 2025-06-05 | 2          | 921        |
| 2025-06-05 | 3          | 910        |

---

## 👨‍💻 Auteur

**Moctarr Basiru King Rahman**
🎓 Mastère 2 Data Engineering – [ECE Paris](https://www.ece.fr)
🔗 [LinkedIn](https://www.linkedin.com/in/moctarr)
📧 [moctarrbasiru.kingrahman@edu.ece.fr](mailto:moctarrbasiru.kingrahman@edu.ece.fr)

---

## 📄 Licence

MIT – Libre pour usage éducatif, académique ou démonstratif.
