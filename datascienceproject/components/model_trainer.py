import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from datascienceproject.exception import CustomException
from datascienceproject.logger import logging
from datascienceproject.components.model_evaluation import ModelEvaluation
from datascienceproject.utils import save_object
from urllib.parse import urlparse
import mlflow # MLflow setup
import dagshub # DagsHub setup



dagshub.init(repo_owner='AryanRakholiya2004', repo_name='Bank-customer-churn-end-to-end-project', mlflow=True)
mlflow.set_registry_uri("https://dagshub.com/AryanRakholiya2004/Bank-customer-churn-end-to-end-project.mlflow")
tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

@dataclass
class ModelTrainerConfig:
    train_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def eval_matrics(self, y_test, y_pred):
        cr = classification_report(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        acc = accuracy_score(y_test, y_pred)
        return cr, cm, acc

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('Model Training Stated !')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                'Logistic Regression': LogisticRegression(),
                'Random Forest': RandomForestClassifier(),
                'Gradient Boosting': GradientBoostingClassifier(),
                'Decision Tree': DecisionTreeClassifier(),
                'XGBoost': XGBClassifier(),
                'CatBoost': CatBoostClassifier(verbose=0),
                'LightGBM': LGBMClassifier()
            }

            params = {
                'Random Forest': {
                    'n_estimators': [100, 200, 300]
                    },
                'Gradient Boosting': {
                    'n_estimators': [5, 10, 20, 50],
                    'learning_rate' : [0.05, 0.1, 0.2, 0.3, 0.4]
                    },
                'Decision Tree': {
                    'max_depth': range(4, 12, 2)
                    },
                'XGBoost': {
                    'n_estimators': [10, 20, 50 ],
                    'learning_rate' : [0.05, 0.1, 0.2]
                    },
                'CatBoost': {
                    'depth': [2, 4, 6,],
                    'n_estimators': [50, 100, 200],
                    },
                'Logistic Regression': {},
                'LightGBM': {}
            }

            # Model Evaluation
            model_eval = ModelEvaluation()

            score_report, params_report, models_report = model_eval.evaluate_models(X_train, y_train, X_test, y_test, models, params)
            logging.info(f'Model Evaluation Completed !{score_report}')
            print(f'\n=====================================\n MODELS REPORT -{score_report}\n=====================================\n')
            print(f'\n=====================================\nPARAMETERS REPORT -{params_report}\n=====================================\n')

            # Saving the best model
            best_model_score = max(sorted(score_report.values()))
            logging.info('Found best scores of models')

            # Finding best model name and parameters
            best_model_name = max(score_report, key=score_report.get)
            print(f'\n=====================================\nBEST MODEL NAME -{best_model_name}\n=====================================\n')
            best_model_params = params_report[best_model_name]
            print(f'\n=====================================\nBEST MODEL PARAMETERS -{best_model_params}\n=====================================\n')

            best_model = models_report[best_model_name]
            predicted = best_model.predict(X_test)
            logging.info('Found best scored model') 

            if best_model_score<0.6:
                logging.info('No best model found !')
                raise CustomException('No best model found !', sys)
    
            # Mlflow integraring
            with mlflow.start_run():
                (_, _, acc) = self.eval_matrics(y_test, predicted)
                mlflow.log_param("model_name", best_model_name)
                mlflow.log_param("Best_parameters",best_model_params)
                mlflow.log_metric("accuracy", acc)

                if tracking_url_type_store != 'file':
                    mlflow.sklearn.log_model(best_model, "model", registered_model_name="Bank-Customer-Churn-Model")
                else:
                    mlflow.sklearn.log_model(best_model, "model")

            save_object(
                file_path=self.model_trainer_config.train_model_file_path,
                obj=best_model
            )

            accuracy = accuracy_score(y_test, predicted)
            logging.info(f'Model evaluation completed, Model - {best_model_name} found with accuracy of {accuracy} !')
            return accuracy
            
        except Exception as ex:
            raise CustomException(ex, sys)
        
        