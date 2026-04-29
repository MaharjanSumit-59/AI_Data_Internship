"""
Task 01 · Create, Insert & Query [Medium]
Independent task — build your first MySQL database from scratch
Goal:
Create a MySQL database, populate it with data, and run queries to answer questions about it.
1. Create a database called library.db with a table books
   (id, title, author, year, genre, rating REAL)
2. Insert at least 8 books — use a mix of genres, years, and ratings
3. Query 1:
   SELECT all books published after 2000, ordered by rating (highest first)
4. Query 2:
   SELECT all books in the 'Fiction' genre with rating above 4.0
5. Query 3:
   Find the average rating across all books
6. Query 4:
   Count how many books exist per genre — use GROUP BY genre
7. Print all query results neatly with labels — not just raw tuples
"""
import os
from dotenv import load_dotenv
import mysql.connector

# load environment variables
load_dotenv()

# Connect to MySQL server
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="library_db"
    )
cursor = conn.cursor()

queries = {
    "Books after 2000 (highest rated first)": """
        SELECT title, year, rating FROM books
        WHERE year > 2000
        ORDER BY rating DESC
    """,
    
    "Fiction books with rating > 4.0": """
        SELECT title, rating FROM books
        WHERE genre='Fiction' AND rating > 4.0
    """,

    "Average rating of all books": """
        SELECT AVG(rating) FROM books
    """,

    "Book count per genre": """
        SELECT genre, COUNT(*) FROM books GROUP BY genre
    """
}

for label, query in queries.items():
    print(f"\n--- {label} ---")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

cursor.close()
conn.close()