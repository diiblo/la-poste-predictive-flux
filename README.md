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

- [x] Collecter les données La Poste (générées), météo, jours fériés #data ✅ 2025-06-02
    
- [x] Nettoyer et standardiser les données #data ✅ 2025-06-02
    
- [x] Créer des features pertinentes (météo, jours fériés, tendances) #data ✅ 2025-06-02
    
- [x] Sauvegarder les datasets nettoyés dans PostgreSQL #data ✅ 2025-06-02
    

### 🤖 Modélisation

- [x] Exploration des données (EDA) #model ✅ 2025-06-02
    
- [x] Choisir un modèle (Random Forest, XGBoost, etc.) #model ✅ 2025-06-04
    
- [x] Entraîner les modèles #model ✅ 2025-06-04
    
- [x] Évaluer la performance (cross-validation, métriques) #model ✅ 2025-06-04
    
- [x] Ajuster les hyperparamètres #model ✅ 2025-06-04
    

### 📊 Dashboarding

- [ ] Concevoir un Streamlit app pour visualiser les prédictions #dashboard
    
- [ ] Ou un Power BI interactif #dashboard
    

### ☁️ Déploiement

- [ ] Créer les DAGs Airflow pour automatiser l’ETL et la prédiction #deployment
    
- [ ] Déployer le modèle (API REST ou batch) #deployment
    

### 📚 Documentation

- [ ] Documenter chaque étape (README, diagrammes draw.io) #docs
    
- [ ] Mettre à jour le TODO et la doc sur GitHub #docs
