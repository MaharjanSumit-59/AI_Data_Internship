"""
Task 03 · Multi-Source ETL [Hard]
Merge data from two sources, clean and combine, load as one unified dataset
Goal: Combine users and their posts from two API endpoints into one clean merged DataFrame.
1. EXTRACT: Fetch users from /users and posts from /posts — two separate API calls
2. Create two DataFrames: df_users and df_posts
3. From df_users keep: id, name, email, city (from address.city — requires pd.json_normalize!)
4. From df_posts keep: userId, title — rename userId to id to match users
5. TRANSFORM: Merge the two DataFrames on id using
   pd.merge(df_users, df_posts, on='id')
6. Count posts per user — add a post_count column to df_users using
   df_posts.groupby('id').size()
7. Clean: lowercase email, strip whitespace from name and city, drop nulls
8. LOAD: Save to merged_data.csv and merged.db — print the top 3 most active users
Deliverable: merged_data.csv + merged.db + top 3 users printed
Bonus: also merge todos and add completion_rate column
"""

import json, os
from urllib import request, error
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. EXTRACT -Fetch API Data
user_url = os.getenv("API_URL")
post_url = os.getenv("POSTS_API_URL")

# Fetch Users
try:
    with request.urlopen(user_url) as response:
        users_data = json.loads(response.read().decode())

    print("USER data fetched successfully.")

except error.URLError as e:
    print(f"Error fetching data: {e}")
    exit()
    
# Fetch Posts
try:
    with request.urlopen(post_url) as response:
        posts_data = json.loads(response.read().decode())

    print("POST data fetched successfully.")

except error.URLError as e:
    print(f"Error fetching data: {e}")
    exit()


# 2. CREATE DATAFRAMES
# Normalize nested JSON (address.city)
df_users = pd.json_normalize(users_data)

# Keep required columns
df_users = df_users[["id", "name", "email", "address.city"]]

# Rename column
df_users.rename(columns={"address.city": "city"}, inplace=True)

# Create posts dataframe
df_posts = pd.DataFrame(posts_data)

# Keep required columns
df_posts = df_posts[["userId", "title"]]

# Rename userId -> id
df_posts.rename(columns={"userId": "id"}, inplace=True)

# 3. TRANSFORM
# Merge users and posts
merged_df = pd.merge(df_users, df_posts, on="id")

# Count posts per user
post_counts = merged_df.groupby("id").size().reset_index(name="post_count")

# Merge post count into user dataframe
df_users = pd.merge(df_users, post_counts, on="id")


# 4. CLEANING
# Lowercase email
df_users["email"] = df_users["email"].str.lower()
# Strip whitespace
df_users["name"] = df_users["name"].str.strip()
df_users["city"] = df_users["city"].str.strip()
# Drop null values
df_users.dropna(inplace=True)

# 5. LOAD TO CSV
df_users.to_csv("merged_data.csv", index=False)
print("CSV file saved as merged_data.csv")

# 6. LOAD TO MYSQL
# 8. LOAD INTO MYSQL

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    cursor = conn.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS users_db")
    print("\nDatabase created successfully!")

    # Use database
    cursor.execute("USE users_db")

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users_posts (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            city VARCHAR(255),
            post_count INT
        )
    """)

    # Convert dataframe rows to tuples
    data_tuples = list(df_users.itertuples(index=False, name=None))

    # Insert rows
    cursor.executemany("""
        INSERT INTO users_posts (id, name, email, city, post_count)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            email = VALUES(email),
            city = VALUES(city),
            post_count = VALUES(post_count)
    """, data_tuples)

    # Commit changes
    conn.commit()

    print("Data loaded into MySQL successfully.")


except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()

    if 'conn' in locals() and conn.is_connected():
        conn.close()
        
        
        
# TOP 3 MOST ACTIVE USERS    
top_users = df_users.sort_values(
        by="post_count",
        ascending=False
    ).head(3)   

print("\nTop 3 Most Active Users:\n")
print(top_users.to_string(index=False))