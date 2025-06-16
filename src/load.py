# contains `load_to_sql()` function

# You’ll load cleaned data into SQL here (once ready).

# How to load data to SQL:


import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def load_to_sql(df):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    try:
        engine = create_engine(
            f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
        )

        df.to_sql("cleaned_sales", con=engine, if_exists="replace", index=False) 
        print("Data loaded successfully to SQL!")

    except Exception as e:
        print(f"Error loading data: {e}")
