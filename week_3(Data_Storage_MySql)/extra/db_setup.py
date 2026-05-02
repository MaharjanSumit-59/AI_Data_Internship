import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_connection(db=None):
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS pipeline_db")
        print("[DB] Database ensured: pipeline_db")

    except Exception as e:
        print(f"[DB ERROR] Database creation failed: {e}")

    finally:
        cursor.close()
        conn.close()


def create_table():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database="pipeline_db"
    )

    cursor = conn.cursor()

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


if __name__ == "__main__":
    create_database()
    create_table()