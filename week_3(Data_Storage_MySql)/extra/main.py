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

import os, csv, json
from urllib import request,error
from dotenv import load_dotenv
import mysql.connector

# load environment variables from .env file
load_dotenv()

api_url = os.getenv("API_URL")

# Database setup
def get_connection(db=None):
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database="pipeline_db"
    )
def create_database_table():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS pipeline_db")
        print("[DB] Database ensured: pipeline_db")

    except Exception as e:
        print(f"[DB ERROR] Database creation failed: {e}")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            name VARCHAR(100),
            username VARCHAR(100),
            email VARCHAR(100),
            city VARCHAR(100),
            company VARCHAR(100)
        )
        """)

        print("[DB] Table ensured: users")

    except Exception as e:
        print(f"[DB ERROR] Table creation failed: {e}")

    finally:
        cursor.close()
        conn.close()



# Function to fetch data from the API
def fetch_data():
  try: 
    with request.urlopen(api_url, timeout=10) as response:
      if response.status != 200:
        raise Exception(f"API returned non-200 status code: {response.status_code}")
      data = json.loads(response.read())

      if not data:
        raise Exception("API returned empty data")
    
    return data
  
  except error.HTTPError as e:
        print(f"[API HTTP ERROR] {e.code} - {e.reason}")

  except error.URLError as e:
        print(f"[API URL ERROR] {e.reason}")
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

# Function to store cleaned data in MySQL database
def store_data(cleaned_data):
    conn = get_connection()

    if not conn:
        print("[ERROR] No DB connection")
        return

    try:
        cursor = conn.cursor()

        query = """
        INSERT INTO users (user_id, name, username, email, city, company)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name=VALUES(name),
            username=VALUES(username),
            email=VALUES(email),
            city=VALUES(city),
            company=VALUES(company)
        """

        for user in cleaned_data:
            values = (
                user["user_id"],
                user["name"],
                user["username"],
                user["email"],
                user["city"],
                user["company"]
            )

            cursor.execute(query, values)

        conn.commit()
        print(f"[DB] Stored {len(cleaned_data)} records successfully")

    except Exception as e:
        print(f"[DB ERROR] Store failed: {e}")

    finally:
        cursor.close()
        conn.close()

def run_analysis():
    conn = get_connection()
    results = {}

    try:
        cursor = conn.cursor(dictionary=True) # return results as dicts instead of tuples

        # 1. Total users
        cursor.execute("SELECT COUNT(*) AS total_users FROM users")
        results["total_users"] = cursor.fetchone()

        # 2. Users per city (GROUP BY)
        cursor.execute("""
            SELECT city, COUNT(*) AS user_count
            FROM users
            GROUP BY city
        """)
        results["users_per_city"] = cursor.fetchall()

        # 3. Top 3 cities
        cursor.execute("""
            SELECT city, COUNT(*) AS user_count
            FROM users
            GROUP BY city
            ORDER BY user_count DESC
            LIMIT 3
        """)
        results["top_cities"] = cursor.fetchall()

        # 4. Email domain analysis
        cursor.execute("""
            SELECT SUBSTRING_INDEX(email, '@', -1) AS domain, COUNT(*) AS count 
            FROM users
            GROUP BY domain
        """)
        results["email_domains"] = cursor.fetchall()

        print("\n📊 ANALYSIS RESULTS")

        print("\nTotal Users:")
        print(results["total_users"])

        print("\nUsers per City:")
        for row in results["users_per_city"]:
            print(row)

        print("\nTop 3 Cities:")
        for row in results["top_cities"]:
            print(row)

        print("\nEmail Domains:")
        for row in results["email_domains"]:
            print(row)

    except Exception as e:
        print(f"[DB ERROR] Analysis failed: {e}")

    finally:
        cursor.close()
        conn.close()

    return results


def export_to_csv(cleaned_data):
    try:
        with open("users.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["user_id", "name", "username", "email", "city", "company"])
            writer.writeheader()
            writer.writerows(cleaned_data)

        print("[EXPORT] CSV file created: users.csv")

    except Exception as e:
        print(f"[EXPORT ERROR] CSV failed: {e}")
        
def export_to_txt(results):
    try:
        with open("report.txt", "w") as file:
            file.write("DATA PIPELINE REPORT\n")
            file.write("=" * 40 + "\n\n")

            file.write(f"Total Users: {results['total_users']['total_users']}\n\n")

            file.write("Top Cities:\n")
            for row in results["top_cities"]:
                file.write(f"{row['city']}: {row['user_count']}\n")

            file.write("\nEmail Domains:\n")
            for row in results["email_domains"]:
                file.write(f"{row['domain']}: {row['count']}\n")

        print("[EXPORT] TXT report created: report.txt")

    except Exception as e:
        print(f"[EXPORT ERROR] TXT failed: {e}")

if __name__ == "__main__":
  # Step 1: Fetch data from API
  data = fetch_data()
  if data:
    print(f"Fetched {len(data)} records")
    # print(data[0])  # preview one record
    
    # Step 2: Clean and transform data
    cleaned_data = clean_data(data)
    print(f"Cleaned {len(cleaned_data)} users")
    print(cleaned_data[0])

    # Database setup
    create_database_table()

    
    # Step 3: Store data in database
    store_data(cleaned_data)
    
    # Step 4: Run analysis queries
    analysis_results = run_analysis()
    
    # Step 5: Export results to CSV
    export_to_csv(cleaned_data)
    
    # Step 6: Export summary report to TXT
    export_to_txt(analysis_results)