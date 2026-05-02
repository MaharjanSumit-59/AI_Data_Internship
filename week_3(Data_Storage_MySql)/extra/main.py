"""
Task 06 · Automated Data Pipeline with Transformation [Hard — Capstone+]

Goal
Build a complete automated data pipeline that fetches, cleans, stores, analyses, and exports data with no manual steps.

Flow:
Fetch API → Validate & Clean → Store (MySQL) → Analyse → Export → Log

Core Idea:
Use any public API (weather, crypto, news, country stats, etc.) that returns slightly messy or nested data.

Must:

- Fetch data from a public API
- Implement strong error handling:
  - Network errors
  - Non-200 responses
  - Empty or malformed data

- Clean and transform the data before storing:
  - Handle missing values
  - Convert data types (e.g., string → float, timestamp → datetime)
  - Flatten nested JSON

- Store ALL processed data in a properly structured MySQL database:
  - Use appropriate data types
  - Include a primary key
  - Prevent duplicate entries

- Run at least 4 meaningful SQL queries:
  - Aggregations (AVG, MAX, MIN)
  - Grouping
  - Trend or time-based analysis
  - Top N results

- Print query results clearly with labels

- Export results:
  - At least one CSV file
  - One readable .txt summary report

- Handle errors at every step:
  - API
  - Data cleaning
  - Database connection
  - SQL execution
  - File writing

Should:

- Use reusable functions:
  - fetch_data()
  - clean_data()
  - store_data()
  - run_analysis()
  - export_results()

- Use environment variables for database credentials

Bonus (optional):

- Add logging system:
  - Save logs to a file (e.g., pipeline.log)
  - Log success and error messages

- Implement incremental updates:
  - Avoid inserting duplicate data

- Add CLI support:
  - Example: python pipeline.py --mode=report

- Generate a simple visualization:
  - Create a chart using matplotlib
  - Save it as an image file 
"""

import os
import requests
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

api_url = os.getenv("API_URL")

# Function to fetch data from the API

def fetch_data():
  try: 
    response = requests.get(api_url, timeout=10)
    
    if response.status_code != 200:
      raise Exception(f"API returned non-200 status code: {response.status_code}")
    
    data = response.json()
    
    if not data:
      raise Exception("API returned empty data")
    
    return data
  
  except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
    return None
  except Exception as e:
    print(f"Error fetching data: {e}")
    return None
  
  
def clean_data(raw_data):
  clean_data = []
  
  try:
    for item in raw_data:
      cleaned_item = {
        "user_id": int(item.get("id", 0)),
        "name": item.get("name", "").strip(),
        "username": item.get("username", "").strip(),
        "email": item.get("email", "").strip(),

        # flatten nested fields
        "city": item.get("address", {}).get("city", "").strip(),
        "company": item.get("company", {}).get("name", "").strip()
   }
      
      # validate cleaned item
      if cleaned_item["user_id"] == 0 or not cleaned_item["email"]:
        print(f"Skipping invalid record: {cleaned_item}")
        continue
      
      clean_data.append(cleaned_item)

  except Exception as e:
    print(f"Error cleaning data: {e}")

  return clean_data

if __name__ == "__main__":
  data = fetch_data()
  if data:
    print(f"Fetched {len(data)} records")
    # print(data[0])  # preview one record
    cleaned_data = clean_data(data)
    print(f"Cleaned {len(cleaned_data)} users")
    print(cleaned_data[0])