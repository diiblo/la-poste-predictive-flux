import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Connexion à PostgreSQL
DB_URI = "postgresql+psycopg2://postgres:root@localhost:5432/laposte_flux"
engine = create_engine(DB_URI)

# Chargement des données
@st.cache_data
def load_predictions():
    query = text("""
        SELECT date, centre_id, prediction
        FROM predictions
        ORDER BY date DESC
        LIMIT 500
    """)
    with engine.connect() as connection:
        result = connection.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df

# Charger les données
df = load_predictions()

# ─────────────────────────────
# 🎛️ SIDEBAR - Filtres
# ─────────────────────────────
st.sidebar.header("📌 Filtres")

# 1. Sélection de la date
dates = sorted(df["date"].unique(), reverse=True)
selected_date = st.sidebar.selectbox("📅 Date :", dates)

# 2. Sélection du centre (filtré selon la date)
filtered_by_date = df[df["date"] == selected_date]
centres = ["Tous"] + sorted(filtered_by_date["centre_id"].unique())
selected_centre = st.sidebar.selectbox("🏢 Centre de tri :", centres)

# ─────────────────────────────
# 📊 CONTENU PRINCIPAL
# ─────────────────────────────
st.title("📦 Dashboard des prédictions de flux colis")
st.markdown(f"### 🔎 Résultats pour le **{selected_date}**")

# Filtrage selon le centre
if selected_centre == "Tous":
    filtered = filtered_by_date
else:
    filtered = filtered_by_date[filtered_by_date["centre_id"] == selected_centre]

# 📈 Graphique
st.subheader("📊 Graphique des prédictions")
st.bar_chart(
    filtered.set_index("centre_id")["prediction"],
    use_container_width=True
)

# 🧮 Valeurs numériques
st.subheader("🔢 Détail des prédictions")
st.dataframe(filtered, use_container_width=True)