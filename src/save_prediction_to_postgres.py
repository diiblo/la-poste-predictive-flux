"""
save_predictions.py

Création de la table 'predictions' si absente
Insertion de lignes dans PostgreSQL

Usage :
    Ce script est appelé depuis un DAG Airflow avec un DataFrame

Auteur : Projet La Poste
"""

import pandas as pd
from sqlalchemy import create_engine, text

# Connexion à ta base locale
DB_URI = "postgresql+psycopg2://postgres:root@host.docker.internal:5432/laposte_flux"
engine = create_engine(DB_URI)

# Création de la table si elle n'existe pas
def create_table_if_not_exists():
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                date DATE NOT NULL,
                centre_id INTEGER NOT NULL,
                prediction INTEGER NOT NULL,
                volume_moyen FLOAT,
                temperature_max FLOAT,
                temperature_min FLOAT,
                precipitation FLOAT,
                windspeed_max FLOAT,
                is_holiday BOOLEAN,
                day_of_week INTEGER,
                month INTEGER,
                day_of_month INTEGER,
                is_weekend BOOLEAN
            );
        """))

# Insertion de données
def insert_predictions(df: pd.DataFrame):
    df.to_sql("predictions", engine, if_exists="append", index=False)
    print(f"✅ {len(df)} lignes insérées dans 'predictions'.")

# Test local
if __name__ == "__main__":
    create_table_if_not_exists()
    
    # Exemple de prédiction (à remplacer par une vraie DataFrame)
    df = pd.DataFrame([{
        "date": "2025-06-05",
        "centre_id": 1,
        "prediction": 823,
        "volume_moyen": 2.0,
        "temperature_max": 22,
        "temperature_min": 12,
        "precipitation": 0,
        "windspeed_max": 18,
        "is_holiday": False,
        "day_of_week": 3,
        "month": 6,
        "day_of_month": 5,
        "is_weekend": False
    }])
    
    insert_predictions(df)
