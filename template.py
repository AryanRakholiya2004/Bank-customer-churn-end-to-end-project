import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "datascienceproject"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/piplines/__init__.py",
    f"{project_name}/piplines/training_pipeline.py",
    f"{project_name}/piplines/prediction_pipeline.py",
    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    f"{project_name}/utils.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "README.md"
]

for file in list_of_files:
    file_path = Path(file)
    file_dir = file_path.parent
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
        logging.info(f"Creating directory: {file_dir}")
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")