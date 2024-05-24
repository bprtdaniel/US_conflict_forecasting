# US_conflict_forecasting
Setting up a repo for the United States conflict forecasting model 

### Context:
The primary goal of the project was to offer predictions of potential conflict hotspots at the most granular temporal and geographical levels for which data was available. Ideally, such a model would have been used to forecast future conflict and thereby provide early warnings to local governments or relevant authorities for threat assessment. The scope of this project, however, was training a supervised machine learning model to make predictions on previously unseen, yet observed data.

Features used in the model:

- Conflict Features: Historical data on conflicts.
- Sociodemographic Features: Demographic and economic data.
- Election-Specific Features: Political dynamics and election cycles.
- Current Issues: Contemporary issues influencing protests.
- Time-Specific Features: Temporal aspects relevant to the time series.

### Modeling Approach:

Models Tested:

- Random Forest (dataset with time-lag features included)
- Random Forest (dataset with time-lag features excluded)
- XGBoost (dataset with time-lag features included)
- XGBoost (dataset with time-lag features excluded)
- An additional linear model for both sets of data

Training and Test Splits:

Data was split temporally
- Training Set: January to September
- Test Set: October to December

Cross-Validation:
A 4-fold time-series cross-validation ensured that training data always preceded test data, fitting the time series nature of the dataset.

Hyperparameter Tuning:
Grid search was used to optimize parameters for Random Forest and XGBoost models, focusing on tree depth, learning rates, and sample/feature fractions.

### Model Evaluation and Validation

Models were evaluated using Mean Squared Error (MSE) and Root Mean Squared Error (RMSE). Comparisons between models with and without time-lag features identified the most predictive features.

### Results 





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
