# 📰 News Data Pipeline & Analysis

This project consists of two Python scripts:

* **`data_pipeline.py`** → Collects and stores news data from an API
* **`data_analysis.py`** → Cleans, processes, and analyzes the collected data

Together, they form a simple end-to-end data workflow for fetching, storing, and extracting insights from news headlines across multiple countries.

---

# 📦 Features

## 🔄 Data Pipeline

* Fetches news headlines from multiple countries:

  * Nepal 🇳🇵
  * India 🇮🇳
  * USA 🇺🇸
  * UK 🇬🇧
  * Australia 🇦🇺
* Cleans and structures API response data
* Stores data in a CSV file (`news_data.csv`)
* Removes duplicate headlines based on:

  * Title
  * Source

---

## 📊 Data Analysis

* Computes:

  * Country with most headlines today
  * Average headline length per country
  * Duplicate headlines across countries
  * Most frequent news source
  * % of recent (<6 hours) vs older headlines
* Filters long headlines (>6 words) into a separate CSV
* Identifies:

  * Country with longest average headlines
  * Country with shortest average headlines

---

# 🛠️ Tech Stack

* Python
* Pandas
* Requests
* dotenv

---


# 🚀 Usage

## Step 1: Run Data Pipeline

```bash
python data_pipeline.py
```

This will:

* Fetch latest headlines
* Save them to `news_data.csv`
* Avoid duplicates

---

## Step 2: Run Data Analysis

```bash
python data_analysis.py
```

This will:

* Analyze the stored data
* Print insights in the console
* Generate:

  * `Filtered_Headlines.csv`

---


# 📌 Key Functions

## data_pipeline.py

* `fetch_news(country_code)` → Calls API and retrieves articles
* `clean_articles(article, country)` → Formats raw data
* `load_existing_data()` → Loads existing CSV
* `save_data(data)` → Saves cleaned data and removes duplicates
* `run_pipeline()` → Orchestrates the workflow

---

## data_analysis.py

* `load_data()` → Loads dataset
* `preprocess_data(df)` → Cleans and prepares data
* `analyze_data(df)` → Runs all analysis tasks

---

# ⚠️ Notes

* API rate limits may apply (currently handled using `time.sleep(2)`)
* Missing or malformed dates are safely handled using `errors="coerce"`
* Duplicate detection is based on title + source combination

---

