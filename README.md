Netflix ETL Pipeline (Python + PostgreSQL)
This project is a simple end-to-end ETL (Extract, Transform, Load) pipeline built for learning and interview preparation as a junior data engineer. It takes a raw Netflix titles dataset (CSV), cleans it using Python and pandas, and loads it into a PostgreSQL database for SQL analysis.

1. Project goals
Build a realistic batch ETL pipeline on a local machine.

Practice working with CSV data, cleaning it, and loading it into a relational database.

Run SQL queries to answer basic questions about the data (e.g., shows by country and rating).

This project is designed to mirror real-world beginner data engineering tasks.

2. Tech stack
Programming: Python 3.14

Libraries: pandas, SQLAlchemy, psycopg2-binary

Database: PostgreSQL (local)

Tools: VS Code, Git, pgAdmin (optional)

3. Dataset
Source: Netflix titles dataset from Kaggle (movies and TV shows metadata).

Format: CSV file (e.g., netflix_titles.csv).

Location: Saved locally in the project under data/raw/.

Note: The original dataset is not included in this repository due to licensing; it can be downloaded directly from Kaggle by searching for “Netflix titles dataset”.

4. Project structure
Example folder layout:

data/

raw/ → original CSV file from Kaggle (e.g., netflix_titles.csv)

processed/ → optional cleaned CSV exports

src/

etl.py → main ETL script (Python)

sql/

analysis.sql → SQL queries used for analysis

README.md → project documentation

5. ETL pipeline steps
The ETL pipeline in src/etl.py does the following:

Extract

Reads the raw CSV file (Netflix titles) from data/raw/ using pandas.

Transform

Drops duplicate rows.

Fills missing values with the string “Unknown” for consistency.

Standardizes column names to snake_case (lowercase, underscores instead of spaces).

Converts the date_added column to a proper datetime type.

Load

Connects to a local PostgreSQL database named netflix_db.

Writes the cleaned DataFrame into a table called netflix_shows using SQLAlchemy and pandas to_sql().

When the script finishes, it prints:
ETL complete!

6. How to run the project
Prerequisites:

Python 3 installed and available as py -3.

PostgreSQL installed and running locally.

A database created named netflix_db.

Required Python packages installed.

Install Python dependencies

Run in the project root:

py -3 -m pip install --upgrade pip

py -3 -m pip install pandas numpy sqlalchemy psycopg2-binary openpyxl

Create the PostgreSQL database

Start PostgreSQL.

Create a database named netflix_db (via pgAdmin or psql):

CREATE DATABASE netflix_db;

Place the dataset

Download the Netflix titles CSV from Kaggle.

Save it as data/raw/netflix_titles.csv inside this project.

Run the ETL script

From the project root directory:

py -3 src\etl.py

If everything is configured correctly, you should see:

ETL complete!

This means the cleaned data has been loaded into the netflix_shows table inside the netflix_db database.

7. SQL analysis
After loading the data, use the queries in sql/analysis.sql to explore the dataset.