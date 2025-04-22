from datascienceproject.logger import logging
from datascienceproject.exception import CustomException
# from datascienceproject.components.data_ingestion import DataIngestion, DataIngestionConfig
from datascienceproject.components.data_transformation import DataTransformation, DataTransformationConfig
from datascienceproject.components.model_trainer import ModelTrainer, ModelTrainerConfig
import sys

if __name__=="__main__":
    logging.info("Starting the application")
    try:
        # data_ingetion_config = DataIngestionConfig()
        # data_ingestion = DataIngestion()
        # train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_path=train_data_path, test_path=test_data_path)
        train_array, test_array,_ = data_transformation.initiate_data_transformation(train_path="artifacts/train.csv", test_path="artifacts/test.csv")

        # Model training
        model_tainer_config = ModelTrainerConfig()
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_array=train_array,test_array=test_array))

    except Exception as ex:
        logging.info("Custom exception")
        raise CustomException(ex,sys)