"""
save_to_postgres.py

Sauvegarder les datasets nettoyés dans PostgreSQL

Usage:
    python src/save_to_postgres.py
"""

import pandas as pd
from sqlalchemy import create_engine

# ------------------------
# Chargement du dataset final
# ------------------------
df = pd.read_csv("data/processed/merged_data.csv")
print("✅ Dataset chargé :")
print(df.head())

# ------------------------
# Paramètres de connexion PostgreSQL
# ------------------------
db_user = "postgres"
db_password = "root"   # 🔴 À changer par ton vrai mot de passe
db_host = "localhost"
db_port = "5432"
db_name = "laposte_flux"

# ------------------------
# Connexion à la base PostgreSQL
# ------------------------
engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# ------------------------
# Sauvegarde dans la table 'flux_colis'
# ------------------------
table_name = "flux_colis"

print("🚀 Sauvegarde en cours…")
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"✅ Données sauvegardées dans la table '{table_name}' de la base '{db_name}'")