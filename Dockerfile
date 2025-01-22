# Use a lightweight official Python image with a specific version
FROM python:3.9-slim

# Set environment variables to ensure non-interactive installs and Python behaviors
ENV PYTHONDONTWRITEBYTECODE 1  # Prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED 1        # Force stdout/stderr to be unbuffered

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for Python and app-specific needs
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Run the script to generate the model
RUN python create_model.py

# Expose the application port (adjust if your app listens on a different port)
EXPOSE 5000


# Start Gunicorn with multiple workers
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
