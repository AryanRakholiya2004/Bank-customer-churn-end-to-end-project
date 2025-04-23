import pandas as pd
import numpy as np
import sys
import os

from dataclasses import dataclass

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from datascienceproject.exception import CustomException
from datascienceproject.logger import logging
from datascienceproject.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        self.prepro_obj = None

    def get_data_tranformation_instance(self):
        '''
        This function is used to create a data transformation pipeline.
        '''
        try:
            logging.info("Data Transformation Started")

            logging.info("Defining numerical and categorical features")
            numerical_features = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'isActiveMember', 'EstimatedSalary']
            logging.info(f"Numerical features: {numerical_features}")

            categorical_features = ['Geography', 'Gender']
            logging.info(f"Categorical features: {categorical_features}")

            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('ohe', OneHotEncoder()),
                ('scaler', StandardScaler(with_mean=False))
            ])

            preprocessor = ColumnTransformer(
                [
                    ('numerical', num_pipeline, numerical_features),
                    ('categorical', cat_pipeline, categorical_features)
                ]
            )

            logging.info("Data Transformation pipeline created successfully")
            return preprocessor

        except Exception as ex:
            raise CustomException(ex, sys)
        
    def initiate_data_transformation(self,train_path, test_path):
        try:
            logging.info("Data Transformation initiated")

            # Read the data
            logging.info("Reading train and test data")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Data read successfully from the Train/Test CSV files")

            preprocessing_obj = self.get_data_tranformation_instance()

            # Separate features and target variable
            logging.info("Separating features and target variable")
            target_column_name = 'Exited'

            # Trainig set
            X_train = train_df.drop(columns=[target_column_name], axis=1)
            y_train = train_df[target_column_name]

            # Testing set
            X_test = test_df.drop(columns=[target_column_name], axis=1)
            y_test = test_df[target_column_name]
            logging.info("Features and target variable separated successfully")

            x_train_arr = preprocessing_obj.fit_transform(X_train)
            x_test_arr = preprocessing_obj.transform(X_test)

            print('='*36)
            print('\nPreprocessor information - before return from function')
            print(preprocessing_obj)
            print(type(preprocessing_obj))
            print('='*36)

            train_arr = np.c_[x_train_arr, np.array(y_train)]
            test_arr = np.c_[x_test_arr, np.array(y_test)]
            logging.info("Data Transformation completed successfully")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as ex:
            raise CustomException(ex, sys)
