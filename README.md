# Industrial Pump Failure Prediction using IoT and Machine Learning

## Objective

This project predicts industrial pump failure using simulated IoT sensor data.

## Technologies

- Python
- Pandas
- Scikit-learn
- Random Forest
- Flask
- Joblib
- HTML/CSS/JavaScript

## Sensors

- Temperature
- Pressure
- Vibration
- RPM

## Workflow

IoT Sensor Data
↓
Data Processing
↓
Machine Learning Model
↓
Flask API
↓
Real-Time Prediction
↓
Web Dashboard

## Model

Random Forest Classifier is used to predict whether the industrial pump is normal or likely to fail.

## Run

```bash
pip install -r requirements.txt
python create_dataset.py
python train_model.py
python app.py