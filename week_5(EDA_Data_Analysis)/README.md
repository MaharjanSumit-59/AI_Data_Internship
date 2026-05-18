# Week 5 — Exploratory Data Analysis (EDA) Projects

This repository contains all Week 5 tasks completed during the Data Internship program.
The main focus of this week was learning and applying **Exploratory Data Analysis (EDA)** techniques using real-world and synthetic datasets.

---

# 📌 Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Requests
* MySQL
* Jupyter Notebook

---



# ✅ Task 1 — EDA Checklist Challenge

### Objective

Perform a complete EDA on TV show data fetched from the TVMaze API and stored in a MySQL database.

### Key Tasks Performed

* Loaded data from MySQL using Pandas
* Checked dataset shape, info, and data types
* Identified missing values and percentages
* Generated descriptive statistics using `.describe()`
* Used `value_counts()` on categorical columns
* Created:

  * Histograms
  * Boxplots
  * Pairplots
* Wrote summary observations from the analysis

### Key Insights

* Missing values were mainly present in the `ended` column
* Rating distributions were relatively balanced
* Outliers existed in summary word counts and show duration

---

# ✅ Task 2 — Distribution Deep Dive

### Objective

Analyze weather distributions and outliers using real-time weather data from the Open-Meteo API.

### Key Tasks Performed

* Fetched weather data for Nepalese cities
* Stored data in MySQL database
* Performed histogram analysis
* Created KDE plots and boxplots
* Detected outliers using IQR method
* Compared rainfall distributions
* Analyzed temperature trends

### Key Insights

* Temperature distributions varied across cities
* Some cities showed higher temperature fluctuations
* Rainfall patterns were uneven across regions
* Outliers represented unusually hot or cold days

---

# ✅ Task 3 — Correlation Analysis

### Objective

Create a synthetic student dataset and perform correlation analysis between academic factors.

### Key Tasks Performed

* Created and analyzed `students.csv`
* Performed complete EDA checklist
* Generated correlation matrix using `df.corr()`
* Created:

  * Correlation heatmap
  * Scatter plots with regression lines
  * Pairplot visualization
* Identified strongest and weakest correlations

### Key Insights

* Study hours strongly correlated with scores
* Attendance percentage had very high positive correlation with performance
* Sleep hours had weaker impact compared to study consistency
* Passed and failed students formed visible clusters

---

# ✅ Task 4 — Full EDA Report (Capstone)

### Objective

Fetch real-world cryptocurrency market data and create a complete EDA report with visual storytelling.

### Dataset Used

CoinGecko Cryptocurrency API

### Key Tasks Performed

* Fetched real-time crypto market data using API
* Cleaned and transformed data using Pandas
* Performed complete EDA workflow
* Created:

  * Histogram
  * Boxplot
  * Scatter plot
  * Correlation heatmap
  * Bar chart
  * Pairplot
* Wrote a detailed EDA report with observations

### Key Insights

* Cryptocurrency market cap distribution was heavily right-skewed
* A few major cryptocurrencies dominated trading volume
* Strong positive relationship existed between market cap and trading volume
* Top-ranked cryptocurrencies showed significantly higher market stability

---

# 📊 Charts & Visualizations Created

* Histograms
* Boxplots
* KDE Plots
* Scatter Plots
* Correlation Heatmaps
* Pairplots
* Bar Charts
* Trend Analysis Charts

All visualizations were saved inside the `charts/` folder.

---

# 📘 Things Learned From These Projects

Through these tasks, I learned how to:

* Fetch and work with real-world API data
* Store and retrieve data using MySQL
* Perform complete Exploratory Data Analysis (EDA)
* Detect missing values and outliers
* Analyze distributions and correlations
* Create meaningful visualizations using Matplotlib and Seaborn
* Interpret patterns and trends from datasets
* Write professional EDA reports with insights
* Use statistical analysis to support data-driven conclusions
* Organize data projects using Jupyter Notebook and GitHub

---

# 🚀 Overall Outcome

These projects helped strengthen my understanding of:

* Data cleaning and preprocessing
* Statistical analysis
* Visualization techniques
* Correlation analysis
* Real-world dataset exploration
* Reporting and storytelling with data

The week provided hands-on experience in transforming raw datasets into meaningful insights using Python-based data analysis tools.
