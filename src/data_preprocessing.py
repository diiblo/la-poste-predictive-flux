"""
data_preprocessing.py

- Fusionner les datasets (colis, météo, jours fériés)

- Créer des features temporelles (jour de la semaine, mois, etc.)

- Gérer les jours fériés

- Nettoyer et préparer les données pour la modélisation

Usage:
    python src/data_preprocessing.py
"""

import pandas as pd

# ---------------------------
# Chargement des données brutes
# ---------------------------
print("🔍 Chargement des datasets…")
colis_df = pd.read_csv("data/synthetic/colis_synthetiques.csv")
meteo_df = pd.read_csv("data/raw/meteo.csv")
feries_df = pd.read_csv("data/raw/jours_feries_metropole.csv")

# Conversion des dates
colis_df["date"] = pd.to_datetime(colis_df["date"])
meteo_df["date"] = pd.to_datetime(meteo_df["date"])
feries_df["date"] = pd.to_datetime(feries_df["date"])

# ---------------------------
# Fusion colis + météo
# ---------------------------
print("🔗 Fusion des données colis et météo…")
merged_df = colis_df.merge(meteo_df, on="date", how="left")

# ---------------------------
# Ajout de la feature 'is_holiday'
# ---------------------------
print("🏖️ Détection des jours fériés…")
ferie_dates = feries_df["date"].unique()
merged_df["is_holiday"] = merged_df["date"].isin(ferie_dates).astype(int)

# ---------------------------
# Features temporelles
# ---------------------------
print("⏳ Création des features temporelles…")
merged_df["day_of_week"] = merged_df["date"].dt.dayofweek  # 0=lundi, 6=dimanche
merged_df["month"] = merged_df["date"].dt.month
merged_df["day_of_month"] = merged_df["date"].dt.day

# Exemple : week-end ou pas
merged_df["is_weekend"] = merged_df["day_of_week"].isin([5, 6]).astype(int)

# ---------------------------
# Vérification finale
# ---------------------------
print("✅ Vérification du dataset final :")
print(merged_df.head())
print(merged_df.info())

# ---------------------------
# Sauvegarde du dataset prêt
# ---------------------------
output_file = "data/processed/merged_data.csv"
merged_df.to_csv(output_file, index=False)
print(f"✅ Dataset prêt sauvegardé dans : {output_file}")