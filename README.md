🎬 Netflix ETL Pipeline | Python + PostgreSQL
A clean, beginner-friendly end-to-end data engineering project showcasing ETL skills with real-world dataset.

🎯 What This Project Does
Extracts raw Netflix titles data (CSV) → Transforms with Python & pandas → Loads into PostgreSQL → Runs SQL analytics.

Built to demonstrate:
✅ ETL pipeline design
✅ Data cleaning & transformation
✅ Database integration
✅ SQL querying skills

🛠️ Tech Stack
Component	Technology
Language	Python 3.14
Libraries	pandas, SQLAlchemy, psycopg2-binary
Database	PostgreSQL
Tools	VS Code, Git, pgAdmin

📂 Project Structure
text
├── data/
│   ├── raw/          # Netflix CSV from Kaggle
│   └── processed/    # Optional cleaned exports
├── src/
│   └── etl.py        # Main ETL pipeline script
├── sql/
│   └── analysis.sql  # SQL queries for insights
└── README.md

🚀 Pipeline Flow
1️⃣ Extract
Reads netflix_titles.csv using pandas

2️⃣ Transform
Removes duplicates

Fills missing values with "Unknown"

Standardizes column names to snake_case

Converts date_added to datetime

3️⃣ Load
Connects to PostgreSQL (netflix_db)

Writes cleaned data to netflix_shows table via SQLAlchemy

Result: ETL complete! 🎉

💡 Key SQL Insights
✔️ Shows by Country – Identified top content-producing regions
✔️ Shows by Rating – Analyzed content maturity distribution (TV-MA, PG, etc.)

📊 Full queries available in sql/analysis.sql

📌 Notes
Dataset not included (Kaggle licensing) – download from Kaggle: "Netflix titles dataset"

.gitignore configured to exclude raw data files

🔗 Live Repo: github.com/Visa-Data/netflix-etl-pipeline
