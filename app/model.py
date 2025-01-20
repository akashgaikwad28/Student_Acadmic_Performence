import joblib
import pandas as pd

# Load the trained model
MODEL_PATH = 'models/student_performance_model.pkl'
model = joblib.load(MODEL_PATH)

def predict_scores(data):
    features = data.drop(columns=['Final_Grade'], errors='ignore')  # Adjust column name if needed
    predictions = model.predict(features)
    data['Predicted_Grade'] = predictions
    return data
