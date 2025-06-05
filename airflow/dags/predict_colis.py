"""
predict_colis.py

DAG Airflow qui charge un modèle LightGBM et fait une prédiction journalière
du nombre de colis entrants. Les résultats sont sauvegardés dans PostgreSQL.

Usage:
    DAG programmé à 8h00 tous les jours
"""

import sys
sys.path.append("/opt/airflow/src")

from save_prediction_to_postgres import create_table_if_not_exists, insert_predictions
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import joblib
import os

# Chemins des artefacts
MODEL_PATH = "/opt/airflow/models/lightgbm_model_optimized.pkl"
SCALER_PATH = "/opt/airflow/models/scaler.pkl"

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 6, 1),
    "retries": 1
}

def predict_colis():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    date = datetime.now()
    logs = []

    for centre_id in range(1, 6):  # Centres de tri 1 à 5
        input_dict = {
            "centre_id": centre_id,
            "volume_moyen": 2.0,
            "temperature_max": 20.0,
            "temperature_min": 10.0,
            "precipitation": 5.0,
            "windspeed_max": 20.0,
            "is_holiday": 0,
            "day_of_week": date.weekday(),
            "month": date.month,
            "day_of_month": date.day,
            "is_weekend": int(date.weekday() >= 5)
        }

        input_df = pd.DataFrame([input_dict])
        input_scaled = scaler.transform(input_df)
        input_scaled_df = pd.DataFrame(input_scaled, columns=input_df.columns)

        try:
            prediction = int(model.predict(input_scaled_df)[0])
        except Exception as e:
            print(f"❌ Erreur de prédiction pour centre {centre_id}: {e}")
            continue

        log_row = {
            "date": date.strftime("%Y-%m-%d"),
            "centre_id": centre_id,
            "prediction": prediction,
            "volume_moyen": input_dict["volume_moyen"],
            "temperature_max": input_dict["temperature_max"],
            "temperature_min": input_dict["temperature_min"],
            "precipitation": input_dict["precipitation"],
            "windspeed_max": input_dict["windspeed_max"],
            "is_holiday": bool(input_dict["is_holiday"]),      # ✅ cast bool
            "day_of_week": input_dict["day_of_week"],
            "month": input_dict["month"],
            "day_of_month": input_dict["day_of_month"],
            "is_weekend": bool(input_dict["is_weekend"])       # ✅ cast bool
        }

        logs.append(log_row)

    log_df = pd.DataFrame(logs)

    # Création table si absente + insertion
    create_table_if_not_exists()
    insert_predictions(log_df)

with DAG(
    dag_id="predict_colis_daily",
    schedule="0 8 * * *",   # 🔁 tous les jours à 08:00
    default_args=default_args,
    catchup=False,
    description="Prédiction journalière du flux de colis entrants"
) as dag:
    
    task_predict = PythonOperator(
        task_id="predict_colis_task",
        python_callable=predict_colis
    )

    task_predict
