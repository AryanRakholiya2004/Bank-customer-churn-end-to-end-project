from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import sys
from datascienceproject.logger import logging
from datascienceproject.exception import CustomException

class ModelEvaluation:
    def evaluate_models(self, X_train, y_train, X_test, y_test, models, param):
        try:

            logging.info('Model Evaluation Started, Finding best parameters in model !')
            report = {}
            best_params = {}
            models_dict = {}

            for i in range(len(models)):
                model_name = list(models.keys())[i]
                model = models[model_name]
                parameters = param[model_name]

                gs = GridSearchCV(model, parameters, cv=3)
                gs.fit(X_train, y_train)


                best_model = gs.best_estimator_
                y_train_pred = best_model.predict(X_train)
                y_test_pred = best_model.predict(X_test)

                train_model_score = accuracy_score(y_train, y_train_pred)
                test_model_score = accuracy_score(y_test, y_test_pred)

                report[model_name] = test_model_score
                best_params[model_name] = gs.best_params_
                models_dict[model_name] = best_model

                print('\n=========================================\n')
                print("Evaluating -", model_name)
                print("Best Parameters: ", gs.best_params_)
                print(f"Accuracy - {test_model_score}")
                print('\n=========================================\n')
                logging.info(f"Model - {model_name} with accuracy - {test_model_score}")

            logging.info('Model Evaluation Completed, Best parameters found !')
            return report, best_params, models_dict

        except Exception as ex:
            raise CustomException(ex,sys)