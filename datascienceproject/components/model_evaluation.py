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

            for i in range(len(models)):
                model_name = list(models.keys())[i]
                model = models[model_name]
                parameters = param[model_name]
                print("Evaluating -", model_name)

                gs = GridSearchCV(model, parameters, cv=3)
                gs.fit(X_train, y_train)

                print("Best Parameters: ", gs.best_params_)

                best_model = gs.best_estimator_
                y_train_pred = best_model.predict(X_train)
                y_test_pred = best_model.predict(X_test)

                train_model_score = accuracy_score(y_train, y_train_pred)
                test_model_score = accuracy_score(y_test, y_test_pred)
                print("Train Model Score: ", train_model_score)

                report[model_name] = test_model_score
                logging.info(f"Model - {model_name} with accuracy - {test_model_score}")

            logging.info('Model Evaluation Completed, Best parameters found !')
            print(report)
            return report, best_model, model_name

        except Exception as ex:
            raise CustomException(ex,sys)