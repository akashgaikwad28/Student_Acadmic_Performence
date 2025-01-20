import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# Load dataset
df = pd.read_csv('data/dataset.csv')  # Ensure the correct path to your dataset

# Encode categorical variables
le_gender = LabelEncoder()
le_support = LabelEncoder()

df['Gender'] = le_gender.fit_transform(df['Gender'])
df['ParentalSupport'] = le_support.fit_transform(df['ParentalSupport'])

# Select features and target
features = ['AttendanceRate', 'StudyHoursPerWeek', 'PreviousGrade', 
            'ExtracurricularActivities', 'Gender', 'ParentalSupport']
X = df[features]
y = df['FinalGrade']

# Scale numerical features
scaler = StandardScaler()
numeric_features = ['AttendanceRate', 'StudyHoursPerWeek', 'PreviousGrade']
X[numeric_features] = scaler.fit_transform(X[numeric_features])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model and encoders
model_data = {
    'model': model,
    'gender_encoder': le_gender,
    'support_encoder': le_support,
    'scaler': scaler,  # Include the scaler
    'features': features
}

# Save the model data
joblib.dump(model_data, 'models/student_performance_model.pkl')
print("Model and preprocessor successfully saved!")
