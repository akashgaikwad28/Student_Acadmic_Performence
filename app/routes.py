import os
import pandas as pd
from flask import Blueprint, render_template, request, send_file
from werkzeug.utils import secure_filename
import joblib
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

main = Blueprint('main', __name__)

# Configurations
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
PREDICTIONS_FOLDER = os.path.join(os.getcwd(), 'predictions')

ALLOWED_EXTENSIONS = {'csv'}

# Create necessary directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PREDICTIONS_FOLDER, exist_ok=True)

# Load the trained model
try:
    model_data = joblib.load(os.path.join(os.getcwd(), 'models', 'student_performance_model.pkl'))
    model = model_data['model']
    gender_encoder = model_data['gender_encoder']
    support_encoder = model_data['support_encoder']
    scaler = model_data['scaler']
    features = model_data['features']
except Exception as e:
    logging.error(f"Error loading model: {e}")
    raise

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Process the uploaded file and get predictions
        try:
            predictions = process_uploaded_file(file_path)
            output_filename = f"predictions_{filename}"
            output_path = os.path.join(PREDICTIONS_FOLDER, output_filename)
            predictions.to_csv(output_path, index=False)

            # Pass the filename to the template for the download link
            return render_template('result.html', predictions=predictions, download_filename=output_filename)
        except Exception as e:
            logging.error(f"Error processing file: {e}")
            return f"Error processing the file: {str(e)}", 500

    return "Invalid file format", 400

@main.route('/download/<filename>')
def download_file(filename):
    sanitized_filename = secure_filename(filename)  # Secure the filename
    file_path = os.path.join(PREDICTIONS_FOLDER, sanitized_filename)

    # Debug: Print the file path
    logging.info(f"Looking for file: {file_path}")

    # Check if the file exists
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)

    # File not found
    logging.error(f"File not found: {file_path}")
    return "File not found", 404

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_uploaded_file(file_path):
    """
    Processes the uploaded file and predicts scores using the pre-trained model.
    """
    # Read the uploaded CSV file
    input_data = pd.read_csv(file_path)

    # Validate that required features are present
    missing_features = [feature for feature in features if feature not in input_data.columns]
    if missing_features:
        raise ValueError(f"The uploaded file is missing required features: {missing_features}")

    # Encode categorical variables
    try:
        input_data['Gender'] = gender_encoder.transform(input_data['Gender'])
        input_data['ParentalSupport'] = support_encoder.transform(input_data['ParentalSupport'])
    except Exception as e:
        logging.error(f"Error encoding categorical features: {e}")
        raise

    # Scale numerical features
    numeric_features = ['AttendanceRate', 'StudyHoursPerWeek', 'PreviousGrade']
    try:
        input_data[numeric_features] = scaler.transform(input_data[numeric_features])
    except Exception as e:
        logging.error(f"Error scaling numerical features: {e}")
        raise

    # Select features for prediction
    X = input_data[features]

    # Predict final grades
    try:
        input_data['PredictedFinalGrade'] = model.predict(X)
    except Exception as e:
        logging.error(f"Error predicting final grades: {e}")
        raise

    return input_data[['AttendanceRate', 'StudyHoursPerWeek', 'PreviousGrade', 
                        'ExtracurricularActivities', 'Gender', 'ParentalSupport', 
                        'PredictedFinalGrade']]
