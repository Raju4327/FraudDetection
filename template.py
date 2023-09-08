import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

project_name='FraudDetection'

list_of_files=[
    ".github/workflows/.gitkeep",
    ".ebextensions/python.config",
    f"catboost_info/learn/catboost_training.json",
    f"catboost_info/learn/leran_error.tsv",
    f"catboost_info/learn/time_left.tsv",
    f"notebook/catboost_info/learn/events.out.tfevents",
    f"notebook/catboost_info/catboost_training.json",
    f"notebook/catboost_info/leran_error.tsv",
    f"notebook/catboost_info/time_left.tsv",
    f"notebook/data",    
    f"src/__init__.py",
    f"src/components/_init_.py",
    f"src/utils/_init_.py", 
    f"src/pipeline/_init_.py",
    f"src/exception.py",
    f"src/logger.py" ,
    f"src/utils.py",
    f"templates/home.html",
    f"templates/index.html",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory;{filedir} for the file:{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating the empty file :{filepath}")
    else:
        logging.info(f"{filename} is already exists")