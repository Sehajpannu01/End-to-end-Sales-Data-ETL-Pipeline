# contains `clean_data()` function

import pandas as pd

def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.fillna(0.0, inplace=True)
    df.to_csv("Data/cleaned/cleaned_sales.csv", index=False)
    return df
