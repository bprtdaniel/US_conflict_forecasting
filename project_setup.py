import os
from dotenv import load_dotenv

def setup_project():
    load_dotenv()
    project_root_dir = os.getenv('PROJECT_ROOT', default=os.getcwd())
    os.chdir(project_root_dir)

    return project_root_dir