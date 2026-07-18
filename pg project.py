import pandas as pd
import mysql.connector

conn=mysql.connector.connect(host="localhost",
                             user="root",
                             password="T@mil#2005",
                             database="retail_ai")
df=pd.read_sql("SELECT * FROM retail_sales_data",conn)
print(df.head)
print(df.info)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.shape)
print(df.columns)
