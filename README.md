# 📊 Sales Data Pipeline & Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4+-orange.svg)](https://www.sqlalchemy.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-red.svg)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive **ETL (Extract, Transform, Load) pipeline** for retail sales data with interactive dashboard visualization. This project demonstrates end-to-end data engineering skills from raw data processing to business intelligence insights.

## 🎯 Project Overview

This project processes a large retail sales dataset (536K+ records) through a complete data pipeline:
- **Extract**: Load raw CSV data from online retail transactions
- **Transform**: Clean, validate, and prepare data for analysis
- **Load**: Store processed data in MySQL database
- **Visualize**: Create interactive Power BI dashboard for business insights

## 🚀 Key Features

- **Scalable ETL Pipeline**: Modular design with separate extract, transform, and load components
- **Data Quality Assurance**: Comprehensive data cleaning and validation
- **Database Integration**: MySQL database storage with SQLAlchemy ORM
- **Interactive Dashboard**: Power BI visualization with sales analytics
- **Jupyter Notebook**: Detailed exploratory data analysis (EDA)
- **Environment Management**: Secure configuration with environment variables

## 📁 Project Structure

```
Sales Data Pipeline & Dashboard/
├── 📊 main.py                 # Main ETL pipeline orchestrator
├── 📁 src/                    # Core pipeline modules
│   ├── extract.py            # Data extraction functionality
│   ├── tansform.py           # Data transformation & cleaning
│   ├── load.py               # Database loading operations
│   └── verify_data.py        # Data validation utilities
├── 📁 Data/                  # Data storage
│   ├── raw/                  # Original CSV/Excel files
│   └── cleaned/              # Processed data files
├── 📁 Dashboards/            # Visualization files
│   ├── sales_dash.pbix       # Power BI dashboard
│   └── dashboard_screenshots/ # Dashboard previews
├── 📁 sql/                   # Database utilities
│   └── fetch_data_with_pymysql.py
├── 📁 database/              # Database configuration
├── 📓 eda_notebook.ipynb     # Exploratory data analysis
└── 📖 README.md              # Project documentation
```

## 🛠️ Technology Stack

### Backend & Data Processing
- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation and analysis
- **SQLAlchemy** - Database ORM and connection management
- **PyMySQL** - MySQL database connectivity

### Database
- **MySQL** - Relational database for data storage

### Visualization & BI
- **Power BI** - Interactive dashboard creation
- **Jupyter Notebook** - Data exploration and analysis

### Development Tools
- **Git** - Version control
- **Virtual Environment** - Dependency management
- **Environment Variables** - Secure configuration

## 📊 Dataset Information

The project processes the **Online Retail Dataset** containing:
- **536,641 records** of retail transactions
- **8 columns**: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country
- **Data period**: Historical retail sales data
- **Source**: Online retail transactions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- MySQL database server
- Power BI Desktop (for dashboard viewing)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sales-data-pipeline.git
   cd sales-data-pipeline
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install pandas sqlalchemy pymysql python-dotenv
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```env
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=sales_database
   ```

5. **Run the ETL pipeline**
   ```bash
   python main.py
   ```

## 📈 Pipeline Workflow

### 1. Data Extraction (`src/extract.py`)
- Loads raw CSV data from `Data/raw/Online Retail.csv`
- Handles file reading errors gracefully
- Returns pandas DataFrame for processing

### 2. Data Transformation (`src/tansform.py`)
- Removes duplicate records
- Handles missing values (fills with 0.0)
- Exports cleaned data to `Data/cleaned/cleaned_sales.csv`

### 3. Data Loading (`src/load.py`)
- Connects to MySQL database using SQLAlchemy
- Creates `cleaned_sales` table
- Loads processed data with proper error handling

### 4. Data Analysis (`eda_notebook.ipynb`)
- Comprehensive exploratory data analysis
- Data quality checks and validation
- Statistical insights and visualizations

## 📊 Dashboard Features

The Power BI dashboard (`Dashboards/sales_dash.pbix`) provides:
- **Sales Performance Metrics**: Revenue, quantity, and transaction analysis
- **Geographic Insights**: Country-wise sales distribution
- **Temporal Analysis**: Sales trends over time
- **Product Analytics**: Top-selling items and categories
- **Customer Segmentation**: Customer behavior analysis

## 🔧 Configuration

### Database Setup
1. Create a MySQL database named `sales_database`
2. Update `.env` file with your database credentials
3. Ensure MySQL server is running on the specified host and port

### Data Source
- Place your `Online Retail.csv` file in `Data/raw/` directory
- The pipeline will automatically process and clean the data

## 📝 Usage Examples

### Running the Complete Pipeline
```python
from main import main
main()
```

### Extracting Data Only
```python
from src.extract import extract_data
df = extract_data("Data/raw/Online Retail.csv")
```

### Database Query Example
```python
from sql.fetch_data_with_pymysql import connection
# Query your cleaned sales data
```

## 🧪 Data Quality & Validation

The pipeline includes comprehensive data validation:
- **Duplicate Removal**: Eliminates redundant records
- **Missing Value Handling**: Fills null values appropriately
- **Data Type Validation**: Ensures proper column types
- **Business Logic Checks**: Validates price and quantity constraints

## 📊 Key Insights from Analysis

- **Data Volume**: 536,641 retail transactions processed
- **Geographic Coverage**: Multi-country retail operations
- **Data Quality**: Comprehensive cleaning and validation
- **Performance**: Efficient ETL pipeline with error handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- LinkedIn: [Your LinkedIn Profile]
- GitHub: [@yourusername]
- Email: your.email@example.com

## 🙏 Acknowledgments

- Online Retail Dataset providers
- Power BI community for visualization insights
- Python data science ecosystem contributors

---

⭐ **Star this repository if you find it helpful!**

🔗 **Connect with me for collaboration opportunities in data engineering and analytics projects.**
