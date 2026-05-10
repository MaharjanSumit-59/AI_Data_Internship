"""
Task 01 · Clean a Messy CSV [Medium]
Independent — practice every cleaning technique on a prepared dataset
Goal Create a messy CSV yourself, then write a cleaning script that fixes every problem.
1 Create messy_students.csv manually — add at least 15 rows with these problems deliberately:
  Some rows with missing score or name Duplicate rows Names in inconsistent casing
  Score stored as string e.g. '85' Extra spaces in names Some scores below 0 (invalid)
2 Load it with Pandas and print df.info() + df.isnull().sum() — show the problems first
3 Fix all 6 problems: nulls, duplicates, casing, type, whitespace, invalid values
4 Add a grade column: A ( 90), B ( 75), C ( 50), F (<50) — use df['score'].apply()
5 Save the cleaned result to clean_students.csv and print a before/after row count
"""

import pandas as pd
import numpy as np


# 1. CREATE A MESSY CSV MANUALLY (USING DICTIONARY)

messy_data = {
    "name": [
        " alice ",     # extra spaces
        "BOB",         # uppercase
        "charlie",
        "DAVID",
        "Emma",
        None,          # missing name
        "frank",
        " Grace ",     # extra spaces
        "alice",       # duplicate-like row
        "BOB",         # exact duplicate
        "Henry",
        " isabella ",
        "JACK",
        "kate",
        "Leo",
        "mia",
        "NORA "
    ],

    "score": [
        "85",          # string score
        "92",
        "48",
        "-5",          # invalid score
        None,          # missing score
        "77",
        "65",
        "88",
        "85",
        "92",
        "105",         # invalid (>100)
        "73",
        "44",
        "-10",         # invalid
        "91",
        "58",
        "81"
    ]
}

# Create DataFrame
messy_df = pd.DataFrame(messy_data)

# Save messy CSV
messy_df.to_csv("messy_students.csv", index=False)

print("messy_students.csv created successfully!\n")


# 2. LOAD CSV + SHOW PROBLEMS

df = pd.read_csv("messy_students.csv")

print("ORIGINAL DATA")
print(df)

print("\nDATAFRAME INFO")
print(df.info())

print("\nNULL VALUES")
print(df.isnull().sum())

before_rows = len(df)

# 3. FIX ALL 6 PROBLEMS

# CLEANING REPORT COUNTERS
null_count_before = df.isnull().sum().sum()
duplicate_count_before = df.duplicated().sum()


# FIX WHITESPACE
df["name"] = df["name"].astype(str).str.strip()


# FIX INCONSISTENT CASING
df["name"] = df["name"].str.title()


# CONVERT SCORE TO NUMERIC
df["score"] = pd.to_numeric(df["score"], errors="coerce")


# HANDLE MISSING VALUES
df = df.dropna(subset=["name", "score"])

# Remove rows where name became "None"
df = df[df["name"] != "None"]


# REMOVE INVALID SCORES
# Keep only scores between 0 and 100
invalid_scores_before = len(df[(df["score"] < 0) | (df["score"] > 100)])

df = df[(df["score"] >= 0) & (df["score"] <= 100)]


# REMOVE DUPLICATES
df = df.drop_duplicates()

duplicate_count_after = df.duplicated().sum()


# 4. ADD GRADE COLUMN

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

df["grade"] = df["score"].apply(assign_grade)



# 5. SAVE CLEANED CSV

after_rows = len(df)

df.to_csv("clean_students.csv", index=False)

print("\nCLEANED DATA")
print(df)

print("\nROW COUNT")
print(f"Before Cleaning : {before_rows}")
print(f"After Cleaning  : {after_rows}")

print("\nclean_students.csv saved successfully!")


# BONUS: CLEANING REPORT

print("\n========== CLEANING REPORT ==========")

print(f"Null values fixed      : {null_count_before}")
print(f"Duplicate rows removed : {duplicate_count_before}")
print(f"Invalid scores removed : {invalid_scores_before}")

print("=====================================")