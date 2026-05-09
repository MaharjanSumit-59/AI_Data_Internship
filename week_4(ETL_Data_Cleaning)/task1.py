"""
# Task 01 · Clean a Messy CSV [Medium]
Independent — practice every cleaning technique on a prepared dataset
Goal: Create a messy CSV yourself, then write a cleaning script that fixes every problem.
1. Create messy_students.csv manually — add at least 15 rows with these problems deliberately:
   - Some rows with missing score or name
   - Duplicate rows
   - Names in inconsistent casing
   - Score stored as string e.g. '85'
   - Extra spaces in names
   - Some scores below 0 (invalid)
2. Load it with Pandas and print:
   df.info()
   df.isnull().sum()
   — show the problems first
3. Fix all 6 problems:
   - nulls
   - duplicates
   - casing
   - type
   - whitespace
   - invalid values
4. Add a grade column:
   - A (>=90)
   - B (>=75)
   - C (>=50)
   - F (<50)
   Use:
   df['score'].apply()
5. Save the cleaned result to clean_students.csv and print a before/after row count.
Deliverable:
- messy_students.csv
- clean_students.csv
- cleaning script
Bonus:
Print a full cleaning report — how many nulls, dupes, and bad values were fixed.
"""

import pandas as pd
import numpy as np

# STEP 1: CREATE MESSY DATA

data = {
    "name": [
        "Alice",
        "bob",
        "CHARLIE",
        " david ",
        None,
        "Emma",
        "Frank", 
        "bob",
        "Grace ",
        " Henry",
        "isabella",
        "JACK",
        "kate",
        "Leo",
        "Mia",
        "Nina"
    ],

    "score": [
        95,
        "85",
        78,
        -5,
        88,
        None,
        "90",
        "85",
        45,
        -10,
        "72",
        100,
        "55",
        "40",
        None,
        "invalid"
    ]
}

df = pd.DataFrame(data)

# Save messy CSV
df.to_csv("messy_students.csv", index=False)
print("Messy CSV created!\n")


# STEP 2: LOAD & INSPECT DATA
df = pd.read_csv("messy_students.csv")

print("===== DATA INFO =====")
print(df.info())

print("\n===== NULL VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== ACTUAL DUPLICATE ROWS =====")
print(df[df.duplicated()])

print("\n===== ORIGINAL DATA =====")
print(df)

# Keep original row count
before_rows = len(df)

# STEP 3: CLEAN THE DATA

print("\n===== CLEANING PROCESS =====")

# Count issues before fixing
null_count_before = df.isnull().sum().sum()
duplicate_count_before = df.duplicated().sum()

# 1. Remove extra spaces
df["name"] = df["name"].astype(str).str.strip()

# 2. Fix casing
df["name"] = df["name"].str.title()

# 3. Convert score to numeric
df["score"] = pd.to_numeric(df["score"], errors="coerce")

# 4. Remove invalid scores (<0)
invalid_scores = (df["score"] < 0).sum()
df = df[df["score"].isna() | (df["score"] >= 0)]

# 5. Fill missing names
missing_names = df["name"].isnull().sum()
df["name"] = df["name"].replace("None", np.nan)
df["name"] = df["name"].fillna("Unknown")

# 6. Fill missing scores with average
missing_scores = df["score"].isnull().sum()
average_score = round(df["score"].mean(),2)
df["score"] = df["score"].fillna(average_score)

# 7. Remove duplicates
df = df.drop_duplicates()

# STEP 4: ADD GRADE COLUMN

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

df["grade"] = df["score"].apply(get_grade)

# STEP 5: SAVE CLEANED FILE

df.to_csv("clean_students.csv", index=False)

after_rows = len(df)

# BONUS: CLEANING REPORT


print("\n===== CLEANING REPORT =====")

print(f"Null values fixed: {null_count_before}")
print(f"Duplicate rows removed: {duplicate_count_before}")
print(f"Invalid negative scores removed: {invalid_scores}")
print(f"Missing names fixed: {missing_names}")
print(f"Missing scores fixed: {missing_scores}")

print("\nRows before cleaning:", before_rows)
print("Rows after cleaning:", after_rows)

print("\n===== CLEANED DATA =====")
print(df)

print("\nCleaned CSV saved as clean_students.csv")