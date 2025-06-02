"""
generate_synthetic_data.py

Génère un dataset synthétique de flux de colis pour les centres de tri de La Poste.

Usage:
    python src/generate_synthetic_data.py
"""

import pandas as pd
import numpy as np

# -----------------------------
# Paramètres de génération
# -----------------------------
start_date = "2023-01-01"
end_date = "2024-12-31"
n_centres = 5  # Nombre de centres de tri

# -----------------------------
# Génération des dates
# -----------------------------
dates = pd.date_range(start=start_date, end=end_date, freq="D")

# -----------------------------
# Création des données synthétiques
# -----------------------------
data = []
for centre_id in range(1, n_centres + 1):
    # Tendance de base : 1000 colis/jour +/- 200
    base_volume = np.random.randint(800, 1200)
    
    for date in dates:
        # Saisonnalité hebdomadaire
        day_of_week = date.dayofweek
        if day_of_week >= 5:  # Week-end
            volume_factor = 0.7
        else:
            volume_factor = 1.0
        
        # Saisonnalité annuelle
        month = date.month
        if month in [11, 12]:  # Pic de fin d'année (Noël)
            seasonal_factor = 1.3
        elif month in [6, 7, 8]:  # Été : creux
            seasonal_factor = 0.9
        else:
            seasonal_factor = 1.0
        
        # Génération du volume total avec un bruit aléatoire
        nb_colis_entree = int(base_volume * volume_factor * seasonal_factor * (1 + np.random.normal(0, 0.05)))
        nb_colis_sortie = int(nb_colis_entree * (0.9 + np.random.normal(0, 0.02)))  # Sorties légèrement inférieures
        
        # Volume moyen par colis (kg)
        volume_moyen = round(np.random.normal(2, 0.5), 2)
        
        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "centre_id": centre_id,
            "nb_colis_entree": nb_colis_entree,
            "nb_colis_sortie": nb_colis_sortie,
            "volume_moyen": volume_moyen
        })

# -----------------------------
# Sauvegarde dans un CSV
# -----------------------------
df = pd.DataFrame(data)
df.to_csv("data/raw/colis_synthetiques.csv", index=False)

print("✅ Données synthétiques générées et sauvegardées dans data/raw/colis_synthetiques.csv")
