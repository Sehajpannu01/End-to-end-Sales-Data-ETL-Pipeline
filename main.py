from src.extract import extract_data
from src.tansform import clean_data
from src.load import load_to_sql

def main():
    print("🔄 Extracting raw data...")
    df = extract_data("Data/raw/Online Retail.csv")
    print(df.head())
    

    print("🧹 Cleaning data...")
    cleaned_df = clean_data(df)
    print(cleaned_df.head())

    print("🔄 Loading data to SQL...")
    load_to_sql(cleaned_df)

if __name__ == "__main__":
    main()