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
            name VARCHAR(100) UNIQUE,
            city VARCHAR(100)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) UNIQUE,
            price DECIMAL(10, 2)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT PRIMARY KEY AUTO_INCREMENT,
            customer_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity INT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
                ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
                ON DELETE CASCADE
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
    
    try:
        cursor.executemany("""
        INSERT INTO customers (name, city)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE
        city = VALUES(city)
        """, customers)
        
        cursor.executemany("""
        INSERT INTO products (name, price)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE
        price = VALUES(price)
        """, products)  # executemany allows us to insert multiple rows in one query
        
        conn.commit()
        
        # SAFE ID MAPPING (IMPORTANT FIX)
        cursor.execute("SELECT customer_id, name FROM customers")
        customer_map = {name: cid for cid, name in cursor.fetchall()}

        cursor.execute("SELECT product_id, name FROM products")
        product_map = {name: pid for pid, name in cursor.fetchall()}
        
        # Orders using names (SAFE)
        raw_orders = [
            ("Alice", "Laptop", 1),
            ("Alice", "Smartphone", 2),
            ("Bob", "Headphones", 1),
            ("Bob", "Monitor", 1),
            ("Charlie", "Keyboard", 3),
            ("Charlie", "Mouse", 2),
            ("David", "Printer", 1),
            ("David", "Webcam", 4),
            ("Eve", "Laptop", 2),
            ("Eve", "Smartphone", 7),
            ("Eve", "Headphones", 6),
            ("Frank", "Monitor", 2),
            ("Grace", "Keyboard", 1),
            ("Grace", "Mouse", 5),
            ("Grace", "Printer", 2),
            ("Ivan", "Webcam", 1),
            ("Ivan", "Laptop", 2),
            ("Ivan", "Smartphone", 3),
            ("Judy", "Headphones", 2),
            ("Judy", "Monitor", 9)
        ]
        
        cleaned_orders = [
            (customer_map[c], product_map[p], q)
            for c, p, q in raw_orders
        ]
        
        cursor.executemany("""
        INSERT INTO orders (customer_id, product_id, quantity)
        VALUES (%s, %s, %s)
        """, cleaned_orders)
        
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
            
        # 3. Customers with more than 2 orders
        cursor.execute("""
            SELECT 
                c.name AS customer_name,
                COUNT(o.order_id) AS total_orders
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            GROUP BY c.customer_id, c.name
            HAVING COUNT(o.order_id) > 2
        """)

        results["frequent_customers"] = cursor.fetchall()

        print("\n=== Customers with More Than 2 Orders ===")
        for row in results["frequent_customers"]:
            print(f"{row['customer_name']} -> {row['total_orders']} orders")
        
        # 4. Average order value per city
        cursor.execute("""
            SELECT 
                c.city,
                AVG(o.quantity * p.price) AS avg_order_value
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN products p ON o.product_id = p.product_id
            GROUP BY c.city
            ORDER BY avg_order_value DESC
        """)

        results["avg_order_value_per_city"] = cursor.fetchall()

        print("\n=== Average Order Value Per City ===")
        for row in results["avg_order_value_per_city"]:
            print(f"{row['city']} -> {row['avg_order_value']:.2f}")
            
        # csv export
        with open("revenue_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Customer", "Total Spent"])

            for r in results["total_spent_per_customer"]:
                writer.writerow([r["customer_name"], r["total_spent"]])

        print("\n[CSV] revenue_report.csv created")
        
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