#import OS
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componenets/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirement.txt",
    
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
     
     
]

for filepath in list_of_files:
    filepath1 = Path(filepath)
    filedir = filepath1.parent
    filename = filepath1.name


    if not filedir.exists():
        path = Path(filedir)
        path.mkdir(parents=True)
        #os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (filepath1.exists()):
        if (filepath1.stat().st_size == 0):
            logging.info(f"{filename} is already exists")
    else:
        with open(filename, "w") as f:
            pass
        logging.info(f"Creating empty file: {filename}")
