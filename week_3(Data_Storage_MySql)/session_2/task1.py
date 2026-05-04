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
        database=db
    )
# Create database and tables
def create_database_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS store_db")
        print("[DB] Database ensured: store_db")
        
        cursor.close()
        conn.close()

        conn = get_connection("store_db")
        cursor = conn.cursor()
        
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
        
# Function to insert sample data into the tables
def insert_sample_data():
    conn = get_connection("store_db")
    cursor = conn.cursor()
    
    # Sample customers
    customers = [
        ("Alice", "New York"),
        ("Bob", "Los Angeles"),
        ("Charlie", "Chicago"),
        ("David", "Houston"),
        ("Eve", "New York"),
        ("Frank", "Los Angeles"),
        ("Grace", "San Antonio"),
        ("Heidi", "San Antonio"),
        ("Ivan", "New York"),
        ("Judy", "San Antonio")
    ]
    
    # Sample products
    products = [
        ("Laptop", 999.99),
        ("Smartphone", 499.99),
        ("Headphones", 199.99),
        ("Monitor", 299.99),
        ("Keyboard", 89.99),
        ("Mouse", 49.99),
        ("Printer", 149.99),
        ("Webcam", 79.99)
    ]
    
    # Sample orders (customer_id, product_id, quantity)
    orders = [
        (1, 1, 1), (1, 2, 2), (2, 3, 1), (2, 4, 1), (3, 5, 3),
        (3, 6, 2), (4, 7, 1), (4, 8, 4), (5, 1, 2), (5, 2, 7),
        (6, 3, 6), (6, 4, 2), (7, 5, 1), (7, 6, 5), (8, 7, 2),
        (8, 8, 1), (9, 1, 2), (9, 2, 3), (10, 3, 2), (10, 4, 9)
    ]
    
    try:
        cursor.executemany("INSERT INTO customers (name, city) VALUES (%s, %s)", customers) 
        cursor.executemany("INSERT INTO products (name, price) VALUES (%s, %s)", products)  # executemany allows us to insert multiple rows in one query
        cursor.executemany("INSERT INTO orders (customer_id, product_id, quantity) VALUES (%s, %s, %s)", orders)
        
        conn.commit()
        print("[DB] Sample data inserted successfully")
    except Exception as e:
        print(f"[DB ERROR] Data insertion failed: {e}")
    finally:
        cursor.close()
        conn.close()
        
# Function to run the required queries 
def run_analysis():
    conn = get_connection("store_db")
    cursor = conn.cursor(dictionary=True) # return results as dicts instead of tuples
    results = {}
    
    try:
        # 1. Total money spent per customer (join + price x quantity, sorted highest first)
        cursor.execute("""
            SELECT c.name AS customer_name, SUM(p.price * o.quantity) AS total_spent
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN products p ON o.product_id = p.product_id
            GROUP BY c.name, c.customer_id
            ORDER BY total_spent DESC
        """)
        results["total_spent_per_customer"] = cursor.fetchall() # fetchall() gets all results of the query, we store it in a dict for later use
        
        print("\n=== Total Money Spent Per Customer ===")
        for row in results["total_spent_per_customer"]:
            print(f"{row['customer_name']} -> {row['total_spent']}")
        
        # 2. Most Ordered Product by quantity
        cursor.execute("""
            SELECT p.name AS product_name, SUM(o.quantity) AS total_quantity
            FROM products p
            JOIN orders o ON p.product_id = o.product_id
            GROUP BY p.product_id
            ORDER BY total_quantity DESC
        """)
        results["most_ordered_product"] = cursor.fetchall()        
        
        print("\n=== Most Ordered Products ===")
        for row in results["most_ordered_product"]:
            print(f"{row['product_name']} -> {row['total_quantity']}")
        
    except Exception as e:
        print(f"[ANALYSIS ERROR] {e}")
    finally:
        cursor.close()
        conn.close()
        

# Main execution
if __name__ == "__main__":
    create_database_table()
    insert_sample_data()
    run_analysis()