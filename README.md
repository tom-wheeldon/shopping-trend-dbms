# Shopping Trends DBMS

DBMS designed to analyze and visualize shopping trends using a MySQL database and Python.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Configuration Setup](#configuration-setup)
3. [Database Setup](#database-setup)
4. [Python Dependencies](#python-dependencies)
5. [Running Visualizations](#running-visualizations)

## Project Overview

This project is designed to manage, analyze, and visualize shopping trends data stored in a MySQL database. It includes:
- A MySQL database schema to store customer, product, and transaction data.
- Python scripts for generating visualizations such as customer demographics, seasonal sales trends, and top products by sales.
- Documentation to guide users in setting up and using the project.

## Configuration Setup

To run this project, you'll need to set up a configuration file with your database credentials. There is a template file stored in src/

1. Copy `config_template.py` to `config.py`:

   ```bash
   cp config_template.py config.py
   
2. Open config.py in a text editor and fill in your database details:
   ```python
    DB_CONFIG = {
        'host': 'your_host',       # e.g., 'localhost'
        'user': 'your_user',       # e.g., 'root'
        'password': 'your_password', # e.g., 'yourpassword'
        'database': 'your_database'  # e.g., 'ShoppingTrendsDB'
    }

## Database Setup
1. Clone the Repo
   ```bash
   git clone https://github.com/yourusername/shopping-trend-dbms.git
   cd shopping-trend-dbms
2. Import the SQL File:
Use MySQL Workbench or the command line to import the ShoppingTrendsDB.sql file into your MySQL server.
Command line example:
    ```bash
    mysql -u your_username -p < ShoppingTrendsDB.sql
    ```

## Python Dependencies
To install the required Python packages, follow these steps:

Make sure you're in the project directory.
Install the dependencies using pip:
  ```bash
    pip install -r requirements.txt
  ```
This will install all necessary packages including mysql-connector-python, pandas, and matplotlib.

## Running Visualisations
The project includes several Python scripts to generate visualisations based on the data in the database. You can run these individually or all at once.

To run all visualisations:
  ```bash
  python src/main.py
  ```
To run individual visualisations:
  Customer Demographics:
  ```bash
  python src/visualise_demographics.py
  ```
  Seasonal Sales Trends:
  ```bash
  python src/visualise_seasonal_sales.py
  ```
  Top 10 Products by Sale
  ```bash
  python src/visualise_top_products.py
  ```
  Each Script will connect to the database, (provided you setup the config.py), and generate the corresponding visualisations.
    


