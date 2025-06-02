# 📦 La Poste - Optimisation Prédictive des Flux Colis

Projet de data science pour prédire les volumes de colis entrants et sortants dans les centres de tri de La Poste.  
Objectif : optimiser les ressources (personnel, véhicules, machines) en anticipant les volumes.

## 🚀 Stack Technique
- Python (pandas, scikit-learn, etc.)
- Airflow pour l'ETL
- PostgreSQL pour stocker les données traitées
- Streamlit/Power BI pour la visualisation
- Données open data La Poste, météo, jours fériés, données synthétiques

## 📁 Arborescence
- `data/` : données brutes et traitées
- `notebooks/` : notebooks exploratoires
- `dags/` : DAGs Airflow
- `src/` : scripts de traitement et prédiction
- `dashboards/` : visualisations
- `tests/` : tests unitaires

## 📌 TODO
### 📁 Préparation des données

- [x] Collecter les données open data La Poste, météo, jours fériés ✅ 2025-06-02
    
- [ ] Nettoyer et standardiser les données
    
- [ ] Créer des features pertinentes (météo, jours fériés, tendances)
    
- [ ] Sauvegarder les datasets nettoyés dans PostgreSQL
    

### 🤖 Modélisation

- [ ] Exploration des données (EDA)
    
- [ ] Choisir un modèle (Random Forest, XGBoost, etc.)
    
- [ ] Entraîner les modèles
    
- [ ] Évaluer la performance (cross-validation, métriques)
    
- [ ] Ajuster les hyperparamètres
    

### 📊 Dashboarding

- [ ] Concevoir un Streamlit app pour visualiser les prédictions
    
- [ ] Ou un Power BI interactif
    

### ☁️ Déploiement

- [ ] Créer les DAGs Airflow pour automatiser l’ETL et la prédiction
    
- [ ] Déployer le modèle (API REST ou batch)
    

### 📚 Documentation

- [ ] Documenter chaque étape (README, diagrammes draw.io)
    
- [ ] Mettre à jour le TODO et la doc sur GitHub
