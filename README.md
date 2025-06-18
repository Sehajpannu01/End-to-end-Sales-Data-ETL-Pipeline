📊 Sales Data Pipeline & Dashboard
Python Pandas SQLAlchemy Power BI License

# Sales Data Pipeline & Dashboard

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline for retail sales data, with a dashboard for visualization.

## Project Overview

- Extract: Loads raw sales data from a CSV file.
- Transform: Cleans and prepares the data for analysis.
- Load: Stores the cleaned data in a MySQL database.
- Visualize: Power BI dashboard for business insights.

## How to Use

1. Clone the repository.
2. Set up a Python virtual environment and install dependencies:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your MySQL credentials:
   ```
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=sales_database
   ```
4. Place the dataset (`Online Retail.csv`) in the `Data/raw/` directory.
5. Run the pipeline:
   ```
   python main.py
   ```

## Project Structure

- `main.py` — Main script to run the ETL pipeline
- `src/` — Source code for extract, transform, and load steps
- `Data/raw/` — Raw data files (not included in repo)
- `Dashboards/` — Power BI dashboard file
- `.gitignore` — Updated to ignore data, checkpoints, and temp files
- `requirements.txt` — Updated to only include actual dependencies

## Dataset

- Source: Downloaded from Kaggle (Online Retail Dataset)
- Link: https://www.kaggle.com/datasets
- Note: This dataset is used for educational and portfolio purposes only. Please check the dataset's license on Kaggle before using it for commercial purposes. Do not claim the data as your own.

## Requirements

See `requirements.txt` for Python dependencies.

## Notes

- Temporary, checkpoint, and data folders are ignored in `.gitignore` for a clean repository.
- The project is for learning and demonstration purposes.
