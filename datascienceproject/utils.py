import os
import sys
import pandas as pd
import mysql.connector
from datascienceproject.exception import CustomException
from datascienceproject.logger import logging
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
username = os.getenv("root")
password = os.getenv("password")
database = os.getenv("database")


def read_sql_data():
    logging.info("Reading from MySQL Database Started !")
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        logging.info("Connection Established to MySQL database !",mydb)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM bank_customers_churn")
        myresult = mycursor.fetchall()
        
        df = pd.DataFrame(myresult, columns=[i[0] for i in mycursor.description])
        logging.info("Reading from MySQL Database Completed !")
        print(df.head(5))
        return df
    except Exception as ex:
        raise CustomException(ex,sys)