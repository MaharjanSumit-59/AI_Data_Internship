"""
Task 06 · Automated Data Pipeline with Transformation [Hard — Capstone+]

Goal
Build a complete automated data pipeline that fetches, cleans, stores, analyses, and exports data with no manual steps.

Flow:
Fetch API → Validate & Clean → Store (MySQL) → Analyse → Export → Log

Core Idea:
Use any public API (weather, crypto, news, country stats, etc.) that returns slightly messy or nested data.

Must:

- Fetch data from a public API
- Implement strong error handling:
  - Network errors
  - Non-200 responses
  - Empty or malformed data

- Clean and transform the data before storing:
  - Handle missing values
  - Convert data types (e.g., string → float, timestamp → datetime)
  - Flatten nested JSON

- Store ALL processed data in a properly structured MySQL database:
  - Use appropriate data types
  - Include a primary key
  - Prevent duplicate entries

- Run at least 4 meaningful SQL queries:
  - Aggregations (AVG, MAX, MIN)
  - Grouping
  - Trend or time-based analysis
  - Top N results

- Print query results clearly with labels

- Export results:
  - At least one CSV file
  - One readable .txt summary report

- Handle errors at every step:
  - API
  - Data cleaning
  - Database connection
  - SQL execution
  - File writing

Should:

- Use reusable functions:
  - fetch_data()
  - clean_data()
  - store_data()
  - run_analysis()
  - export_results()

- Use environment variables for database credentials

Bonus (optional):

- Add logging system:
  - Save logs to a file (e.g., pipeline.log)
  - Log success and error messages

- Implement incremental updates:
  - Avoid inserting duplicate data

- Add CLI support:
  - Example: python pipeline.py --mode=report

- Generate a simple visualization:
  - Create a chart using matplotlib
  - Save it as an image file 
"""

