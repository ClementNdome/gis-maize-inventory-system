# Crop Inventory & Maize Yield Prediction System

## Overview
This project leverages remote sensing data, local agricultural records, and machine learning techniques to predict maize yield with high accuracy. It integrates spatial data analysis with predictive modeling to support farmers and policymakers in making data-driven agricultural decisions.

## Features
- Uses remote sensing data and vegetation indices.
- Implements machine learning models for yield prediction.
- Visualizes crop inventory and yield predictions on an interactive WebGIS.
- Provides insights on soil health and climatic factors influencing yield.

## Technologies Used
- Python (Flask, Pandas, NumPy, Scikit-learn, TensorFlow)
- Google Earth Engine (for remote sensing data)
- Flask (for WebGIS visualization)
- PostgreSQL/PostGIS (for spatial database management)
- Leaflet.js (for interactive maps)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ClementNdome/gis-maize-inventory-system.git
   cd gis-maize-inventory-system
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```
5. Open a web browser and go to `http://localhost:5000`.

## Usage
- Upload satellite imagery or input agricultural data.
- Run machine learning models to generate yield predictions.
- View results on an interactive map.
- Export reports for further analysis.

## Deployment
This project can be deployed using:
- Docker for containerized deployment.
- AWS/GCP for cloud-based processing.
- Render, Heroku, or DigitalOcean for web hosting.

## License
This project is licensed under the MIT License.

## Author
[Clement Ndome](https://github.com/ClementNdome)

