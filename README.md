# US_conflict_forecasting
Setting up a repo for the United States conflict forecasting model 

### Project Setup:  
To run the scripts, please follow this setup:
- create a .env file in the 'US_conflict_forecasting' folder and define your local project root:
```ini
PROJECT_ROOT='your/local/file/path/US_conflict_forecasting'
```
- Ensure that the .env file is included in the .gitignore
- the configuration module project_setup.py defines your project root as the working directory of the project
- The following code chunk needs to be included in all scripts in order to work with relative paths. It defines the correct search path and imports the working directory to each script:
  
```ini
import sys
import os

current_dir = os.getcwd()
while 'US_conflict_forecasting' not in os.path.basename(current_dir):
    current_dir = os.path.dirname(current_dir)

if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from project_setup import setup_project
project_root_dir = setup_project()
```
