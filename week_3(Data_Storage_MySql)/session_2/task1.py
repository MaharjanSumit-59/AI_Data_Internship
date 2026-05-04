"""
Task A · Multi-Table Relational System [Hard]
Using mysql-connector-python, create a database called store_db with three tables — customers, products, and orders 
— where orders links to the other two via foreign keys. 
Insert at least 10 customers, 8 products, and 20 orders using %s parameterized queries. 
Then run these 4 queries and print the results with clear labels: 
total money spent per customer (JOIN + price x quantity, sorted highest first), 
most ordered product by total quantity, 
customers who placed more than 2 orders (HAVING COUNT), 
and average order value per city. Finally, export the revenue-per-customer result into a revenue_report.csv using Python's csv module.
Deliverable: MySQL store_db + Python script + revenue_report.csv
"""

import mysql.connector
import csv, os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection parameters from environment variables
def get_connection(db=None): #db=None means we can connect to MySQL without specifying a database, useful for creating the database
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database="store_db"
    )
# Create database and tables
def create_database_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS store_db")
        print("[DB] Database ensured: store_db")
    except Exception as e:
        print(f"[DB ERROR] Database creation failed: {e}")
    
    # Create tables
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            city VARCHAR(100)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            price DECIMAL(10, 2)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT PRIMARY KEY AUTO_INCREMENT,
            customer_id INT,
            product_id INT,
            quantity INT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
        """)
        print("[DB] Tables ensured: customers, products, orders")
    except Exception as e:
        print(f"[DB ERROR] Table creation failed: {e}")
    finally:
        cursor.close()
        conn.close()
        
# 