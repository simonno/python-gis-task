# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install argparse geopandas matplotlib shapely numpy

# Copy the current directory contents into the container at /app
COPY . /app

# Default command to run the script with arguments
CMD ["python", "main.py"]
