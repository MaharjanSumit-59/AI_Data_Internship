"""
Task B · API Monitor with Change Detection [Hard]
Using mysql-connector-python and https://jsonplaceholder.typicode.com/posts, 
build a monitoring script that detects changes between runs. 
Create a database called monitor_db with two tables — posts (stores fetched data) and change_log (records what changed and when). 
On first run, insert all posts and log each as 'NEW'. 
Then manually update one row in MySQL (UPDATE posts SET title='Changed' WHERE id=1) 
and re-run — your script must detect the mismatch and log it as 'MODIFIED' in change_log. 
Print results for: post count per user, all change log entries from the latest run, and which user triggered the most change events. 
Wrap every API call and DB operation in try/except with printed error messages.
Deliverable: MySQL monitor_db with both tables populated + Python script
"""

import mysql.connector
import os
import json
from urllib import request,error
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Fetch API URL and key from environment variables
url = os.getenv("POSTS_API_URL")

# Database connection parameters from environment variables
def get_connection(db=None): 
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=db
    )
# Create database and tables
def create_database_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS monitor_db")
        print("[DB] Database ensured: monitor_db")
        
        cursor.close()
        conn.close()

        conn = get_connection("monitor_db")
        cursor = conn.cursor()
        
    except Exception as e:
        print(f"[DB ERROR] Database creation failed: {e}")
    
    # Create tables
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INT PRIMARY KEY,
            userId INT,
            title TEXT,
            body TEXT
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS change_log (
            log_id INT AUTO_INCREMENT PRIMARY KEY,
            post_id INT,
            change_type VARCHAR(20),
            changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (post_id) REFERENCES posts(id)
                ON DELETE CASCADE
        )
        """)
  
        conn.commit()
        print("[DB] Setup complete")
    except Exception as e:
        print(f"[DB ERROR] Table creation failed: {e}")
    finally:
        cursor.close()
        conn.close()
        
# Fetch posts from API
def fetch_api():
    try:
        with request.urlopen(url, timeout=10) as response:
            if response.status != 200:
                raise Exception(f"Status code: {response.status}")

            data = json.loads(response.read())
            return data

    except error.HTTPError as e:
        print(f"[API HTTP ERROR] {e.code} - {e.reason}")

    except error.URLError as e:
        print(f"[API URL ERROR] {e.reason}")

    except json.JSONDecodeError:
        print("[API ERROR] Failed to decode JSON response")

    except Exception as e:
        print("[API ERROR]", e)

    return []

# LOAD EXISTING POSTS (OPTIMIZED DICT LOOKUP)
def load_db_posts(cursor):
    cursor.execute("SELECT id, userId, title, body FROM posts")
    return {
        row[0]: {"userId": row[1], "title": row[2], "body": row[3]}
        for row in cursor.fetchall()
    }
    

# SYNC + CHANGE DETECTION
def sync():
    try:
        conn = get_connection("monitor_db")
        cursor = conn.cursor()

        api_data = fetch_api()
        if not api_data:
            return

        db_posts = load_db_posts(cursor)

        new_count = 0
        mod_count = 0

        for post in api_data:
            pid = post["id"]

            # ---------------- NEW POST ----------------
            if pid not in db_posts:
                cursor.execute("""
                    INSERT INTO posts (id, userId, title, body)
                    VALUES (%s, %s, %s, %s)
                """, (pid, post["userId"], post["title"], post["body"]))

                cursor.execute("""
                    INSERT INTO change_log (post_id, change_type)
                    VALUES (%s, 'NEW')
                """, (pid,))

                new_count += 1

            # ---------------- MODIFIED POST ----------------
            else:
                old = db_posts[pid]

                if (
                    old["title"] != post["title"]
                    or old["body"] != post["body"]
                    or old["userId"] != post["userId"]
                ):
                    cursor.execute("""
                        UPDATE posts
                        SET userId=%s, title=%s, body=%s
                        WHERE id=%s
                    """, (post["userId"], post["title"], post["body"], pid))

                    cursor.execute("""
                        INSERT INTO change_log (post_id, change_type)
                        VALUES (%s, 'MODIFIED')
                    """, (pid,))

                    mod_count += 1

        conn.commit()

        print(f"[SYNC] Done | NEW: {new_count} | MODIFIED: {mod_count}")

    except Exception as e:
        print("[SYNC ERROR]", e)

    finally:
        cursor.close()
        conn.close()
        
# Function to run the required queries 
def run_analysis():
    try:
        conn = get_connection("monitor_db")
        cursor = conn.cursor()

        # 1: POSTS PER USER
        cursor.execute("""
            SELECT userId, COUNT(*) 
            FROM posts
            GROUP BY userId
            ORDER BY userId
        """)

        print("\n--- Posts per User ---")
        for userId, count in cursor.fetchall():
            print(f"User {userId}: {count}")

        # 2: CHANGE LOG
        cursor.execute("""
            SELECT post_id, change_type, changed_at
            FROM change_log
            ORDER BY changed_at DESC
        """)

        print("\n--- Change Log ---")
        for row in cursor.fetchall():
            print(row)
            
        # 3: TOP USER BY CHANGES   
        cursor.execute("""
            SELECT p.userId, COUNT(l.log_id) AS changes
            FROM change_log l
            JOIN posts p ON l.post_id = p.id
            GROUP BY p.userId
            ORDER BY changes DESC
            LIMIT 1
        """)

        result = cursor.fetchone()

        print("\n--- Top User by Changes ---")
        print(result)
        
    except Exception as e:
        print("[ERROR]", e)

    finally:
        cursor.close()
        conn.close()
        
# Main execution
if __name__ == "__main__":
    create_database_table()
    sync()
    run_analysis()