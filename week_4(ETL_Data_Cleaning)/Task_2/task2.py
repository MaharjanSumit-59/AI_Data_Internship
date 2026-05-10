"""
# Task 02 — API → Clean → Save [Hard]
Goal:Build a complete ETL pipeline from an API, clean the data with Pandas, and load to both CSV and SQLite.
1. EXTRACT
Fetch all 100 posts from:
https://jsonplaceholder.typicode.com/posts
2. Load into Pandas
Load the API response into a Pandas DataFrame using:
pd.DataFrame(data)
3. TRANSFORM
Keep only these columns:
userId, id, title, body
4. Add a word_count column
Count the number of words in the title column using: .str.split().str.len()
5. Filter
Keep only posts where:
word_count >= 4
6. Standardise data
- Convert title to title case
- Strip whitespace from body
7. LOAD
Save the cleaned data:
- To CSV as clean_posts.csv (without index)
- To SQLite database posts.db using df.to_sql()
8. Print
Print:
- Total posts fetched
- Total posts after filtering
- Top 3 users by post count
Deliverables:
- clean_posts.csv
- posts.db
- 3 printed statistics
Bonus:
- Add error handling for the API call
- Validate that all userId values are integers
"""

import json, os
from urllib import request, error
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. EXTRACT -Fetch API Data
url = os.getenv("POSTS_API_URL")

try:
    with request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    print("API data fetched successfully.")

except error.URLError as e:
    print(f"Error fetching data: {e}")
    exit()
    
# 2. LOAD INTO PANDAS
df = pd.DataFrame(data)

# 3. TRANSFORM (Keep required columns only)
df = df[['userId', 'id', 'title', 'body']]

# 4. ADD word_count COLUMN
df["word_count"] = df["title"].str.split().str.len()

# 5. FILTER POSTS (Keep titles with >= 4 words)
df = df[df['word_count'] >= 4]

# 6. STANDARDISE DATA
df['title'] = df['title'].str.title() # converts title to Title case
df['body'] = df['body'].str.strip() # strips whitespace from body

# BONUS VALIDATION (Validate userId values)
if not pd.api.types.is_integer_dtype(df["userId"]):
    print("Validation failed: userId contains non-integer values.")
    exit()

print("Validation passed: all userId values are integers.")

# 7. SAVE TO CSV
df.to_csv("clean_posts.csv", index=False)
print("CSV file saved as clean_posts.csv")

# 8. LOAD INTO MYSQL
try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    cursor = conn.cursor()
    

    # create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS posts_db")
    print("\nDatabase created successfully!")

    cursor.execute("USE posts_db")

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            userId INT,
            id INT PRIMARY KEY,
            title TEXT,
            body TEXT,
            word_count INT
        )
    """)
    # Insert rows
    data_tuples = list(df.itertuples(index=False, name=None))

    cursor.executemany("""
        INSERT INTO posts (userId, id, title, body, word_count)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            title = VALUES(title),
            body = VALUES(body),
            word_count = VALUES(word_count)
    """, data_tuples)
    conn.commit()

    print("Data loaded into MySQL successfully.")

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()

    if 'conn' in locals() and conn.is_connected():
        conn.close()

# 9. PRINT REQUIRED STATS


print("\n--- STATS ---")

print(f"Total posts fetched: {len(data)}")

print(f"Posts after filtering: {len(df)}")

top_users = df["userId"].value_counts().head(3)

print("\nTop 3 users by post count:")

for user, count in top_users.items():
    print(f"User {user}: {count} posts")