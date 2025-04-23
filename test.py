# # import pandas as pd
# # import mysql.connector
# # from mysql.connector import errorcode

# # # --- MySQL connection config ---
# # config = {
# #     'user': 'root',             # your MySQL username
# #     'password': '',             # your MySQL password
# #     'host': 'localhost',
# #     'database': 'Bank'       # replace with your database
# # }

# # # --- CSV File Path ---
# # csv_file = 'Bank_Churn.csv'  # replace with your CSV filename

# # # --- Table Name ---
# # table_name = 'Bank_Customer_Churn'

# # try:
# #     # Connect to MySQL
# #     conn = mysql.connector.connect(**config)
# #     cursor = conn.cursor()

# #     # Load CSV into pandas DataFrame
# #     df = pd.read_csv(csv_file)

# #     # Create table dynamically based on CSV headers
# #     columns = ", ".join(f"`{col}` TEXT" for col in df.columns)
# #     create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})"
# #     cursor.execute(create_table_query)

# #     # Insert data
# #     for _, row in df.iterrows():
# #         placeholders = ", ".join(["%s"] * len(row))
# #         insert_query = f"INSERT INTO `{table_name}` VALUES ({placeholders})"
# #         cursor.execute(insert_query, tuple(row))

# #     # Commit and close
# #     conn.commit()
# #     print(f"✅ Data from '{csv_file}' imported successfully into '{table_name}'!")

# # except mysql.connector.Error as err:
# #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
# #         print("❌ Access denied: Check username/password")
# #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
# #         print("❌ Database does not exist")
# #     else:
# #         print(f"❌ Error: {err}")
# # finally:
# #     if 'conn' in locals() and conn.is_connected():
# #         cursor.close()
# #         conn.close()


# import pandas as pd
# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Aryan9099425680",
#     database="Bank"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM bank_customers_churn")
# myresult = mycursor.fetchall()
# df = pd.DataFrame(myresult, columns=[i[0] for i in mycursor.description])
# print(df.head(5))
# print(df.isnull().sum())


# df2 = pd.read_csv('Bank_Churn.csv')
# print(df2.head(5))
# print(df2.isnull().sum())


import struct
print(struct.calcsize("P") * 8,'bits')