"""
Task 04 · Transform & Enrich [Hard]
Focus purely on the Transform step — advanced column engineering with Pandas
Goal: Take your clean_students.csv from Task 01 and enrich it with multiple new calculated columns.
1. Load clean_students.csv from Task 01 into a DataFrame
2. Add grade column:
   A (≥90), B (≥75), C (≥60), D (≥50), F (<50)
   — use apply() with a function
3. Add passed column:
   True if score >= 50, False otherwise
4. Add score_category column:
   'High' (≥80), 'Medium' (50–79), 'Low' (<50)
5. Add rank column:
   rank all students by score — highest score gets rank 1
   (use .rank(ascending=False))
6. Group by grade:
   print count, mean score, and min/max score per grade using groupby()
7. Sort the final DataFrame by rank and reset the index
8. Save enriched data to enriched_students.csv
   and print the top 5 ranked students
Deliverable:
enriched_students.csv + groupby summary printed in terminal
Bonus:
Use pivot_table() to create a summary table
— grade vs subject vs average score
"""

import pandas as pd


# 1. Load clean_students.csv
df = pd.read_csv("../Task_1/clean_students.csv")

print("Original Data:")
print(df.head())



# 2. Add grade column using apply()
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

df["grade"] = df["score"].apply(assign_grade)


# 3. Add passed column
df["passed"] = df["score"] >= 50


# 4. Add score_category column
def score_category(score):
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"

df["score_category"] = df["score"].apply(score_category)



# 5. Add rank column
df["rank"] = df["score"].rank(ascending=False)

# Convert rank to integer
df["rank"] = df["rank"].astype(int)



# 6. Group by grade
group_summary = df.groupby("grade")["score"].agg(
    count="count",
    mean="mean",
    minimum="min",
    maximum="max"
)

print("\nGroup By Summary:")
print(group_summary)

# adding subject column
subjects = [
    "Math",
    "Science",
    "English",
    "Computer",
    "Physics"
    ]

# Repeat subjects for all rows
df["subject"] = [
        subjects[i % len(subjects)]
        for i in range(len(df))
    ]

# BONUS: Pivot Table
# grade vs subject vs average score
pivot_summary = pd.pivot_table(
    df,
    values="score",
    index="grade",
    columns="subject",
    aggfunc="mean"
)

print("\nPivot Table Summary:")
print(pivot_summary)


# 7. Sort by rank and reset index
df = df.sort_values(by="rank").reset_index(drop=True)


# 8. Save enriched data
df.to_csv("enriched_students.csv", index=False)

print("\nTop 5 Ranked Students:")
print(df.head(5))

print("\nEnriched data saved as 'enriched_students.csv'")