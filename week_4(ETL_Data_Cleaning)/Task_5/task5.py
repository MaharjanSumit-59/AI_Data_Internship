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
import logging


# LOGGING CONFIGURATION

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="etl_pipeline.log",   # save logs in file
    filemode="a"                   # append mode
)

# Optional: also show logs in terminal
console = logging.StreamHandler()
console.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console.setFormatter(formatter)

logging.getLogger().addHandler(console)


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

    logging.info("========== DATABASE SETUP ==========")
    conn = get_connection()
    cursor = conn.cursor()

    # CREATE DATABASE
    try:

        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS products_db"
        )

        logging.info("Database ensured: products_db")

        cursor.close()
        conn.close()

        # reconnect using database
        conn = get_connection("products_db")
        cursor = conn.cursor()

    except Exception as e:

        logging.error(f"Database creation failed: {e}")

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

        logging.info("Table ensured: products")

    except Exception as e:

        logging.error(f"Table creation failed: {e}")


    finally:

        cursor.close()
        conn.close()



# EXTRACT
def extract(api_url):
    logging.info("========== EXTRACT PHASE ==========")
    try:

        logging.info("Fetching API data...")

        req = request.Request(
            api_url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )
        
        response = request.urlopen(req)
        data = json.loads(response.read().decode())

        products = data.get("products", [])

        logging.info(f"Successfully extracted {len(products)} rows")
        return products

    except error.HTTPError as e:

        logging.error(
            f"HTTP ERROR: {e.code}"
        )

    except error.URLError as e:

        logging.error(
            f"URL ERROR: {e.reason}"
        )

    except Exception as e:

        logging.error(
            f"Unexpected ERROR: {e}"
        )

    return []


# TRANSFORM
def transform(data):

    logging.info(
        "========== TRANSFORM PHASE =========="
    )

    df = pd.DataFrame(data)

    logging.info(
        f"Initial rows: {len(df)}"
    )

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
    before_null = len(df)
    df.dropna(inplace=True)
    logging.info(
        f"Removed {before_null - len(df)} rows with null values"
    )
    # REMOVE DUPLICATES
    before_dup = len(df)
    df.drop_duplicates(subset=["id"], inplace=True)
    logging.info(
        f"Removed {before_dup - len(df)} duplicate rows"
    )
    # CLEAN STRINGS
    string_cols = ["title", "category", "brand"]
    for col in string_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )
    logging.info(
        "String cleaning completed"
    )

    # FIX DATA TYPES    
    df["id"] = df["id"].astype(int)
    df["price"] = df["price"].astype(float)
    df["rating"] = df["rating"].astype(float)
    df["stock"] = df["stock"].astype(int)
    logging.info(
        "Data type conversion completed"
    )
    
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

    logging.info(
        "Calculated columns added successfully"
    )

    logging.info(
        f"Final clean rows: {len(df)}"
    )

    return df

# LOAD
def load(df):

    logging.info(
        "========== LOAD PHASE =========="
    )

    try:
        # CONNECT TO DATABASE
       
        conn = get_connection("products_db")
        cursor = conn.cursor()

        logging.info(
            "Connected to products_db"
        )

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

            logging.warning(
                "No new rows to insert"
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

            logging.info(
                f"Inserted {len(new_df)} rows into database"
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

        logging.info(
            f"CSV Exported -> {CSV_FILE}"
        )


    except mysql.connector.Error as e:

        logging.error(
            f"MySQL ERROR: {e}"
        )
    except Exception as e:

        logging.error(
            f"Unexpected ERROR: {e}"
        )
    finally:
        cursor.close()
        conn.close()
        logging.info(
            "Database connection closed"
        )

# MAIN PIPELINE
def run_pipeline():

    logging.info("=" * 50)
    logging.info(
        "RUNNING FULL ETL PIPELINE"
    )
    logging.info("=" * 50)
    # CREATE DATABASE + TABLE
    create_database_table()

    # EXTRACT
    raw_data = extract(API_URL)

    if not raw_data:
        logging.error(
            "Pipeline stopped: Extraction failed"
        )
        return

    # TRANSFORM
    clean_df = transform(raw_data)

    # LOAD
    load(clean_df)

    logging.info(
        "ETL COMPLETED SUCCESSFULLY"
    )


# RUN PIPELINE TWICE
if __name__ == "__main__":

    logging.info("FIRST RUN")
    run_pipeline()
