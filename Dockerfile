FROM python:3.9.21

# Set the working directory inside the container
WORKDIR /app
COPY models/student_performance_model.pkl /app/models/


# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set the command to run your app
CMD ["python", "app.py"]
