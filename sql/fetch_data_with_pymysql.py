import pymysql
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook
import configparser
import warnings
import os
from dotenv import load_dotenv
import time

start_time = time.time()
warnings.filterwarnings('ignore')
load_dotenv()

# Database connection details
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')

# Connect to the database
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object
curobj = connection.cursor()

print("Connected to the database")

print("Fetching data from the database")

# Fetch data from the database
# curobj.execute("SELECT * FROM cleaned_sales")
curobj.execute("SELECT * FROM customers")

# Fetch all the data
data = curobj.fetchall()
# print(data)


# df = pd.DataFrame(data,columns = ["InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"])
df = pd.DataFrame(data,columns = ["Costomer ID","Country",'id'])
print(df.head())