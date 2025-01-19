import os

def create_directory_structure(base_dir):
    # Define the directory structure
    structure = {
        "app": [
            "static",
            "templates",
            "__init__.py",
            "routes.py",
            "model.py",
            "forms.py",
            "utils.py",
        ],
        "data": ["dataset.csv", "processed_data.csv"],
        "notebooks": ["EDA.ipynb", "model_training.ipynb"],
        "": ["requirements.txt", "config.py", "app.py", "Procfile", "README.md"]
    }

    # Create directories and files
    for folder, items in structure.items():
        folder_path = os.path.join(base_dir, folder)
        if folder:  # Skip the base directory
            os.makedirs(folder_path, exist_ok=True)
        
        for item in items:
            item_path = os.path.join(folder_path, item)
            if "." in item:  # It's a file
                with open(item_path, "w") as f:
                    # Write basic content for certain files
                    if item == "requirements.txt":
                        f.write("flask\nflask-wtf\npandas\nscikit-learn\nnumpy\njoblib\ngunicorn\n")
                    elif item == "README.md":
                        f.write("# Student Performance Prediction Model\n\n"
                                "A Flask application to predict student performance based on various factors.")
                    elif item == "Procfile":
                        f.write("web: gunicorn app:app\n")
            else:  # It's a folder
                os.makedirs(item_path, exist_ok=True)

if __name__ == "__main__":
    base_dir = "student-acadmic-performance"
    create_directory_structure(base_dir)
    print(f"Directory structure for '{base_dir}' created successfully!")
