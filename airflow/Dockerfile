# airflow-custom.Dockerfile
# This Dockerfile is used to create a custom Airflow image with additional Python dependencies
# based on the official Apache Airflow image version 3.0.1.
FROM apache/airflow:3.0.1

# Set the user to root to install system dependencies
# This is necessary to install system packages that require root privileges
USER root

# Install system dependencies required for building Python packages
# This is necessary for packages that require compilation, such as those with C extensions
RUN apt-get update && apt-get install -y build-essential

# Copy the requirements.txt file into the container
# This file should contain the Python dependencies you want to install
COPY requirements.txt /requirements.txt

# Copy the entrypoint script into the container
# This script will be executed when the container starts
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the user to airflow to run the subsequent commands
USER airflow
# Install Python dependencies from requirements.txt
# Note: Ensure that the requirements.txt file is in the same directory as this Dockerfile
RUN pip install --no-cache-dir -r /requirements.txt
