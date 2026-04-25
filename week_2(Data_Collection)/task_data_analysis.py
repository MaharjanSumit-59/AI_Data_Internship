"""
Which country out of Nepal, India, USA, UK and Australia published the most headlines today?
What is the average number of words in a headline title — per country?
Are there any headlines that appeared in more than one country? If yes, which ones?
Which news source published the most headlines across all 5 countries combined?
What percentage of all headlines were published in the last 6 hours vs older than 6 hours?
# If you run your script twice, does your database end up with duplicate rows? How did you prevent that?
Save only headlines with a title longer than 6 words to a CSV. How many passed that filter?
Which country had the longest headline on average — and which had the shortest?
"""

import pandas as pd
from datetime import datetime, timedelta
import os
from dateutil import parser

def load_data():
    try:
        df = pd.read_csv("news_data.csv")
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_') # Clean column names: no spaces, all lowercase
        return df
    except FileNotFoundError:
        print("CSV file not found. Please run the data pipeline script first.")
        return None
    
def preprocess_data(df):
    # word count in headline titles
    df["word_count"] = df["title"].str.split().str.len() # Add a new column for word count in headline titles
    # Datetime parsing
    df["published_at"] = df["published_at"].apply(lambda x: parser.parse(x) if x != "N/A" else pd.NaT)
    return df


def analyze_data(df):
    # 1. Which country published the most headlines today?
    today = datetime.now().date()
    df_today = df[df["published_at"].dt.date == today] # Filter headlines published today
    most_headlines_country = df_today["country"].value_counts().idxmax()
    print(f"Country with most headlines today: {most_headlines_country}")
    
    # 2. Average number of words in a headline title — per country
    avg_words_per_country = df.groupby("country")["word_count"].mean()
    print("\nAverage number of words in a headline title per country:")
    for country, avg_words in avg_words_per_country.items():
        print(f"  {country}: {avg_words:.2f}")


if __name__ == "__main__":
    df = load_data()
    if df is not None:
        df = preprocess_data(df)
        analyze_data(df)
    else:
        print("No data to analyze.")