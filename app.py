from datascienceproject.logger import logging
from datascienceproject.exception import CustomException
from datascienceproject.components.data_ingestion import DataIngestion, DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("Starting the application")
    try:
        data_ingetion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as ex:
        logging.info("Custom exception")
        raise CustomException(ex,sys)