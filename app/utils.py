import pandas as pd

def process_uploaded_file(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)
    predictions = predict_scores(data)
    return data, predictions
