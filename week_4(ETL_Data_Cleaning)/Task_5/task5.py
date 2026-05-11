"""
Task 05 · Full ETL System [Hard — Month 1 Capstone]
Bring together everything from Week 1 → 2 → 3 → 4 in one complete automated pipeline

Goal: Build a fully automated, reusable ETL pipeline that you could run every day to get fresh data.
Week 1: File handling
Week 2: API + requests
Week 3: MySql
Week 4:Pandas + ETL

Must:
1. EXTRACT from at least 1 real public API with full error handling
2. Load into Pandas — clean nulls, duplicates, types, and string issues
3. TRANSFORM — add at least 2 calculated/enriched columns
4. LOAD to SQLite using df.to_sql() AND export to clean CSV
5. Write reusable functions:
   extract(), transform(), load()
   — not one big block
Should:
6. Add logging — print what each step is doing and how many rows
Bonus:
7. Run full pipeline twice
   — 2nd run should not create duplicate rows
"""

from urllib import request, error
import json, os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
from datetime import datetime



# LOAD ENV VARIABLES
load_dotenv()

API_URL = os.getenv("PRODUCT_URL")

CSV_FILE = "clean_products.csv"

# MYSQL CONNECTION
def get_connection(db=None):
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=db
    )



# CREATE DATABASE + TABLE
def create_database_table():

    conn = get_connection()
    cursor = conn.cursor()

    # CREATE DATABASE
    try:

        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS products_db"
        )

        print("[DB] Database ensured: products_db")

        cursor.close()
        conn.close()

        # reconnect using database
        conn = get_connection("products_db")
        cursor = conn.cursor()

    except Exception as e:

        print(f"[DB ERROR] Database creation failed: {e}")

    
    # CREATE TABLE
    try:

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (

            id INT PRIMARY KEY,
            title VARCHAR(255),
            category VARCHAR(100),
            price FLOAT,
            discount_percentage FLOAT,
            rating FLOAT,
            stock INT,
            brand VARCHAR(100),
            final_price FLOAT,
            stock_status VARCHAR(50),
            rating_category VARCHAR(50),
            etl_loaded_at DATETIME
        )
        """)

        print("[DB] Table ensured: products")

    except Exception as e:

        print(f"[DB ERROR] Table creation failed: {e}")

    finally:

        cursor.close()
        conn.close()



# EXTRACT
def extract(api_url):
    print("\n========== EXTRACT ==========")
    try:

        print("[INFO] Fetching API data...")

        req = request.Request(
            api_url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )
        
        response = request.urlopen(req)
        data = json.loads(response.read().decode())

        products = data.get("products", [])

        print(f"[SUCCESS] Extracted {len(products)} rows")

        return products

    except error.HTTPError as e:

        print(f"[HTTP ERROR] {e.code}")

    except error.URLError as e:

        print(f"[URL ERROR] {e.reason}")

    except Exception as e:

        print(f"[ERROR] {e}")

    return []


# TRANSFORM
def transform(data):

    print("\n========== TRANSFORM ==========")

    df = pd.DataFrame(data)

    print(f"[INFO] Initial rows: {len(df)}")

    # SELECT REQUIRED COLUMNS    
    columns = [
        "id",
        "title",
        "category",
        "price",
        "discountPercentage",
        "rating",
        "stock",
        "brand"
    ]
    df = df[columns]

    
    # HANDLE NULLS
    df.dropna(inplace=True)
    # REMOVE DUPLICATES
    df.drop_duplicates(subset=["id"], inplace=True)
    # CLEAN STRINGS
    string_cols = ["title", "category", "brand"]
    for col in string_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

    # FIX DATA TYPES    
    df["id"] = df["id"].astype(int)
    df["price"] = df["price"].astype(float)
    df["rating"] = df["rating"].astype(float)
    df["stock"] = df["stock"].astype(int)

    
    # TRANSFORMATIONS
    # 1. Final Price After Discount
    df["final_price"] = (
        df["price"]
        - (df["price"] * df["discountPercentage"] / 100)
    ).round(2)

    # 2. Stock Status
    df["stock_status"] = df["stock"].apply(
        lambda x: "Low Stock" if x < 20 else "In Stock"
    )

    # 3. Rating Category
    df["rating_category"] = df["rating"].apply(
        lambda x:
        "Excellent" if x >= 4.5 else
        "Good" if x >= 4 else
        "Average"
    )

    # 4. ETL Timestamp
    df["etl_loaded_at"] = datetime.now()

    print(f"[SUCCESS] Clean rows: {len(df)}")

    return df

# LOAD
def load(df):

    print("\n========== LOAD ==========")

    try:
        # CONNECT TO DATABASE
       
        conn = get_connection("products_db")
        cursor = conn.cursor()

        print("[DB] Connected to products_db")

        # GET EXISTING IDS
        cursor.execute(
            "SELECT id FROM products"
        )

        existing_ids = set(
            row[0]
            for row in cursor.fetchall()
        )

       
        # REMOVE DUPLICATE ROWS
        new_df = df[
            ~df["id"].isin(existing_ids)
        ]

        if len(new_df) == 0:

            print(
                "[INFO] No new rows to insert"
            )

        else:

           
            # INSERT QUERY
            insert_query = """
            INSERT INTO products (

                id,
                title,
                category,
                price,
                discount_percentage,
                rating,
                stock,
                brand,
                final_price,
                stock_status,
                rating_category,
                etl_loaded_at

            )

            VALUES (%s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s)
            """

           
            # DATAFRAME -> LIST OF TUPLES
            values = [

                (
                    int(row["id"]),
                    row["title"],
                    row["category"],
                    float(row["price"]),
                    float(row["discountPercentage"]),
                    float(row["rating"]),
                    int(row["stock"]),
                    row["brand"],
                    float(row["final_price"]),
                    row["stock_status"],
                    row["rating_category"],
                    row["etl_loaded_at"]
                )

                for _, row in new_df.iterrows()
            ]

           
            # INSERT DATA
            cursor.executemany(
                insert_query,
                values
            )

            conn.commit()

            print(
                f"[SUCCESS] Inserted {len(new_df)} rows"
            )

       
        # EXPORT CSV
        full_df = pd.read_sql(
            "SELECT * FROM products",
            conn
        )

        full_df.to_csv(
            CSV_FILE,
            index=False
        )

        print(
            f"[SUCCESS] CSV Exported -> {CSV_FILE}"
        )

    except mysql.connector.Error as e:

        print(f"[MYSQL ERROR] {e}")

    except Exception as e:

        print(f"[ERROR] {e}")

    finally:
        cursor.close()
        conn.close()
        print("[DB] Connection Closed")


# MAIN PIPELINE
def run_pipeline():

    print("\n" + "=" * 50)
    print("RUNNING FULL ETL PIPELINE")
    print("=" * 50)

    # CREATE DATABASE + TABLE
    create_database_table()

    # EXTRACT
    raw_data = extract(API_URL)

    if not raw_data:
        print("[PIPELINE] Extraction failed")
        return

    # TRANSFORM
    clean_df = transform(raw_data)

    # LOAD
    load(clean_df)

    print(
        "\n[PIPELINE] ETL COMPLETED SUCCESSFULLY"
    )


# RUN PIPELINE TWICE
if __name__ == "__main__":

    print("\nFIRST RUN")
    run_pipeline()
