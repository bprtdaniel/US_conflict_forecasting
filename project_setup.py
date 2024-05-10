import os
from dotenv import load_dotenv
import sys

def setup_project():
    load_dotenv()
    project_root_dir = os.getenv('PROJECT_ROOT', default=os.getcwd())
    os.chdir(project_root_dir)
    sys.path.append(project_root_dir)  
    return project_root_dir

project_root_dir = setup_project()
print(f"Current Project Root Directory set to: {project_root_dir}")
print(f"Current Search Path set to: {sys.path}")

#Adding project root to Python path for direct import
sys.path.append(project_root_dir)
