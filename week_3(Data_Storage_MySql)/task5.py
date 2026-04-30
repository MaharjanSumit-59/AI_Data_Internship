"""
Task 05 · The Full System [Hard — Capstone]

Bring everything together — Weeks 1, 2, and 3 in one script

Goal  
Build a complete automated data system — fetch, store, analyse, and export. No manual steps.

Flow:
Fetch API → Error handle → Store MySQL → Analyse → Export(csv+text)

Must:
- Fetch data from any public API with error handling
- Store ALL fetched data in a properly structured MySQL database
- Run at least 3 meaningful SQL queries and print results with labels
- Export query results to a CSV file (combine Week 1 + Week 3)
- Handle errors at every step — API, database, file

Should:
- Write reusable functions: fetch_data(), store_data(), run_report()

Bonus:
- Schedule it: run the whole thing every time you run the script fresh
"""

import requests
import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API URL and key from environment variables
url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")

# Define the countries to fetch news for
COUNTRIES = {
    "np" : "Nepal",
    "in" : "India",
    "us" : "USA"
}

# Define MySQL connection =
try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    cursor = conn.cursor()
    print("Connected to MySQL database successfully!")
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
    exit(1)