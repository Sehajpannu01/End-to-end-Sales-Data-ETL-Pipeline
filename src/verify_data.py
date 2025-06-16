import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd

load_dotenv()

def verify_data_loading():
    """Verify if data was successfully loaded to the SQL database"""
    try:
        # Get database connection details
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_NAME")
        
        # Create connection
        engine = create_engine(
            f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
        )
        
        # Check if table exists and get basic info
        with engine.connect() as connection:
            # Check if table exists
            result = connection.execute(text("SHOW TABLES LIKE 'cleaned_sales'"))
            table_exists = result.fetchone()
            
            if table_exists:
                print("Table 'cleaned_sales' exists!")
                
                # Get row count
                count_result = connection.execute(text("SELECT COUNT(*) FROM cleaned_sales"))
                row_count = count_result.fetchone()[0]
                print(f"Total rows in table: {row_count:,}")
                
                # Get column info
                columns_result = connection.execute(text("DESCRIBE cleaned_sales"))
                columns = columns_result.fetchall()
                print(f"Table columns:")
                for col in columns:
                    print(f"   - {col[0]} ({col[1]})")
                
                # Get sample data
                sample_result = connection.execute(text("SELECT * FROM cleaned_sales LIMIT 5"))
                sample_data = sample_result.fetchall()
                print(f"\nSample data (first 5 rows):")
                for i, row in enumerate(sample_data, 1):
                    print(f"   Row {i}: {row[:3]}...")  # Show first 3 columns
                    
            else:
                print("Table 'cleaned_sales' does NOT exist!")
                print("Available tables:")
                tables_result = connection.execute(text("SHOW TABLES"))
                tables = tables_result.fetchall()
                for table in tables:
                    print(f"   - {table[0]}")
        
        print(f"\n🗄️ Database: {database}")
        print(f"🌐 Host: {host}:{port}")
        
    except Exception as e:
        print(f"Error connecting to database: {e}")
        print("\nPossible issues:")
        print("   - Check your .env file exists with DB credentials")
        print("   - Verify MySQL server is running")
        print("   - Check network connection to database")

if __name__ == "__main__":
    verify_data_loading() 