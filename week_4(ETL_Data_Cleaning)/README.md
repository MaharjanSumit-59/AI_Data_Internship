# 🧹 Python ETL & Data Cleaning Projects

A collection of beginner-to-intermediate **ETL (Extract, Transform, Load)** and **Data Cleaning** projects built using **Python, Pandas, APIs, and MySQL**.  
These projects were completed as hands-on practice for mastering real-world data engineering and preprocessing workflows.

---

# 📌 Project Overview

This repository contains 5 practical tasks covering:

- CSV Cleaning
- API Data Extraction
- Data Transformation with Pandas
- Multi-source ETL Pipelines
- Database Loading (MySQL)
- Automation & Reusable ETL Systems

---

# 🛠️ Technologies Used

- Python
- Pandas
- MySQL
- REST APIs
- JSON
- dotenv
- Logging
- Jupyter Notebook / VS Code

---


# 🚀 Tasks Completed

---

# ✅ Task 01 — Clean a Messy CSV

## Goal
Create and clean a deliberately messy student dataset using Pandas.

## Features
- Hand-created messy CSV dataset
- Missing values handling
- Duplicate removal
- String cleaning & whitespace removal
- Invalid score filtering
- Data type conversion
- Grade generation using `.apply()`

## Output
- `clean_students.csv`

## Concepts Practiced
- Data Cleaning
- Pandas preprocessing
- Null handling
- Feature engineering

---

# ✅ Task 02 — API → Clean → Save ETL Pipeline

## Goal
Build a complete ETL pipeline using a public REST API.

## Workflow
1. Extract data from API
2. Load into Pandas
3. Transform & clean data
4. Filter records
5. Save to CSV and SQLite

## Features
- API extraction using `requests`
- Error handling
- Word count feature engineering
- Title formatting
- SQLite integration

## Outputs
- `clean_posts.csv`
- `posts.db`

## Concepts Practiced
- REST API handling
- ETL pipelines
- SQLite databases
- Data transformation

---

# ✅ Task 03 — Multi-Source ETL

## Goal
Combine data from multiple API endpoints into one unified dataset.

## Features
- Multiple API calls
- DataFrame merging
- `pd.json_normalize()`
- GroupBy aggregations
- User activity analysis
- Data cleaning and normalization

## Outputs
- `merged_data.csv`
- `merged.db`

## Concepts Practiced
- Multi-source ETL
- Data merging
- Aggregation
- Advanced Pandas operations

---

# ✅ Task 04 — Transform & Enrich

## Goal
Perform advanced transformation and feature engineering on cleaned student data.

## Features
- Grade generation
- Pass/fail logic
- Score categorization
- Ranking system
- GroupBy statistics
- Pivot tables

## Output
- `enriched_students.csv`

## Concepts Practiced
- Feature engineering
- Ranking
- Aggregations
- Pivot tables
- Analytical transformations

---

# ✅ Task 05 — Full Automated ETL System (Capstone)

## Goal
Develop a reusable production-style ETL pipeline.

## Features
- Modular ETL architecture
- Reusable functions:
  - `extract()`
  - `transform()`
  - `load()`
- Logging system
- CSV + SQLite/MySQL loading
- Duplicate prevention
- Automated workflow structure

## Concepts Practiced
- Production ETL design
- Modular programming
- Database integration
- Automation
- Error handling

---

# 📊 Key Skills Demonstrated

- Data Cleaning & Preprocessing
- ETL Pipeline Development
- REST API Integration
- MySQL Operations
- Pandas Data Analysis
- Data Transformation
- Logging & Automation
- Error Handling
- Feature Engineering

---

# 📦 Example Requirements

```txt
pandas
requests
python-dotenv
mysql-connector-python
```

---

# 🎯 Learning Outcomes

Through these projects, I learned:

- How real ETL systems work
- Data extraction from APIs
- Cleaning messy real-world datasets
- Building reusable pipelines
- Working with SQL databases
- Automating data workflows
- Writing scalable Python scripts

---

# 📈 Future Improvements

- Add scheduling using Cron/Airflow
- Dockerize pipelines
- Add unit testing
- Build dashboard visualizations
- Integrate cloud databases
- Add CI/CD pipeline

---

