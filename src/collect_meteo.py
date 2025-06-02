"""
collect_meteo.py

Récupère les données météos de la ville de Paris de 2023 à 2024

Usage:
    python src/collect_meteo.py
"""

import requests
import pandas as pd
from datetime import datetime, timedelta

# --------------------------
# Paramètres de la requête
# --------------------------
latitude = 48.8566   # Latitude de Paris
longitude = 2.3522   # Longitude de Paris
start_date = "2023-01-01"
end_date = "2024-12-31"
timezone = "Europe/Paris"

# Variables météo à récupérer
weather_variables = [
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum",
    "windspeed_10m_max"
]

# --------------------------
# Requête API Open-Meteo
# --------------------------
url = (
    f"https://archive-api.open-meteo.com/v1/archive"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&start_date={start_date}"
    f"&end_date={end_date}"
    f"&daily={','.join(weather_variables)}"
    f"&timezone={timezone}"
)

print("🔍 Requête API envoyée…")
response = requests.get(url)
data = response.json()

# --------------------------
# Création du DataFrame
# --------------------------
df = pd.DataFrame({
    "date": data["daily"]["time"],
    "temperature_max": data["daily"]["temperature_2m_max"],
    "temperature_min": data["daily"]["temperature_2m_min"],
    "precipitation": data["daily"]["precipitation_sum"],
    "windspeed_max": data["daily"]["windspeed_10m_max"]
})

# --------------------------
# Sauvegarde en CSV
# --------------------------
df.to_csv("data/raw/meteo.csv", index=False)
print("✅ Données météo sauvegardées dans data/raw/meteo.csv")
