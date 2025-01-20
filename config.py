import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    UPLOAD_FOLDER = 'uploads'
