# 🎓 Student Performance Prediction  

A **Flask-based web application** that predicts students' academic performance based on uploaded CSV data. Teachers can upload student data, and the application processes it using a trained machine learning model to predict final grades.  

## 🚀 Features  

- **Upload CSV Files:** Teachers can upload CSV files containing student data like attendance, study habits, and socio-economic factors.  
- **Automatic Predictions:** The app processes the data and uses a trained machine learning model to predict student performance (e.g., final grades).  
- **Download Results:** Teachers can download the predictions as a CSV file.  
- **User-Friendly Interface:** The web application provides an intuitive interface for effortless interaction.  

---  

## 📂 Project Structure  

```plaintext  
student-performance-prediction/  
├── app/  
│   ├── static/              # Static files like CSS, JS, and images  
│   ├── templates/           # HTML templates for the web interface  
│   │   ├── index.html       # Main page for file upload  
│   │   ├── result.html      # Results display page  
│   ├── __init__.py          # Flask app initialization  
│   ├── routes.py            # Routes and view functions  
│   ├── model.py             # Machine learning model logic  
│   ├── utils.py             # Utility functions for data processing  
├── data/  
│   ├── dataset.csv          # Training dataset from Kaggle  
│   ├── processed_data.csv   # Preprocessed dataset (optional)  
├── notebooks/  
│   ├── EDA.ipynb            # Exploratory Data Analysis notebook  
│   ├── model_training.ipynb # Model training and evaluation notebook  
├── models/  
│   ├── student_performance_model.pkl # Trained machine learning model  
├── uploads/                 # Folder for uploaded files  
├── requirements.txt         # Python dependencies  
├── config.py                # Configuration settings  
├── app.py                   # Entry point to run the application  
├── Procfile                 # For deployment on platforms like Heroku  
├── README.md                # Detailed project documentation  
```  

---  

## 📊 Dataset  

The model is trained using the **[Student Performance Predictions](https://www.kaggle.com/datasets/haseebindata/student-performance-predictions)** dataset available on Kaggle.  

### **Features of the Dataset:**  
- **Input Features:**  
  - `Gender`, `StudyHoursPerWeek`, `ExtracurricularActivities`, `AttendanceRate`, `ParentalSupport`, etc.  
- **Target Feature:**  
  - `Final_Grade` (Predicted based on input features).  

Ensure the uploaded CSV file matches the expected structure for accurate predictions.  

---  

## 🛠️ Setup Instructions  

### **1. Clone the Repository**  
```bash  
git clone https://github.com/your-repo/student-performance-prediction.git  
cd student-performance-prediction  
```  

### **2. Create a Virtual Environment**  
```bash  
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```  

### **3. Install Dependencies**  
```bash  
pip install -r requirements.txt  
```  

### **4. Download and Train the Model**  
- Download the dataset from [Kaggle](https://www.kaggle.com/datasets/haseebindata/student-performance-predictions).  
- Train the model using the `notebooks/model_training.ipynb` notebook.  
- Save the trained model as `student_performance_model.pkl` in the `models/` directory.  

### **5. Run the Application**  
```bash  
python app.py  
```  
Access the application at **http://127.0.0.1:5000/**.  

---  

## 📜 Usage  

1. Open the application in your browser.  
2. Upload a CSV file with student data.  
3. Click "Upload and Predict" to process the data.  
4. View predictions on the results page.  
5. Download the predictions as a CSV file.  

---  

## 🧠 Machine Learning Model  

The application uses a trained machine learning model to predict student performance.  

### **Steps to Train the Model:**  
1. Perform **Exploratory Data Analysis (EDA)** using `EDA.ipynb`.  
2. Preprocess the data (handle missing values, feature scaling, encoding).  
3. Train the model using algorithms like Random Forest, Gradient Boosting, etc.  
4. Evaluate the model using metrics like accuracy, RMSE, and F1-score.  
5. Save the trained model using `joblib`.  

---  



## 🛡️ Error Handling  

- The application handles invalid file uploads and shows meaningful error messages.  
- If the CSV format is incorrect, the app notifies the user to upload a valid file.  

---  

## 🤝 Contributions  

Contributions are welcome! Follow these steps:  
1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m "Add feature-name"`).  
4. Push to the branch (`git push origin feature-name`).  
5. Open a Pull Request.  

---  

## 📝 License  

This project is licensed under the **MIT License**.  

---  

## 📬 Contact  

If you have any questions or need support, feel free to reach out:  
- **Email:** acashtech@gmail.com  
- **LinkedIn:** [Your Profile](https://www.linkedin.com/in/akash-santosh-gaikwad)  

---  

Enjoy predicting student performance with this application! 🎉