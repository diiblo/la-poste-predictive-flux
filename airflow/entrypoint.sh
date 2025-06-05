#!/bin/bash

# Initialisation de la base Airflow
airflow db migrate

# Lancement de Airflow standalone (webserver + scheduler)
exec airflow standalone