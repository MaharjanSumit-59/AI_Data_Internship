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
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        return df
    except FileNotFoundError:
        print("CSV file not found. Please run the data pipeline script first.")
        return None
    
def preprocess_data(df):
    # word count in headline titles
    df["word_count"] = df["title"].str.split().str.len()
    # Datetime parsing
    df["published_at"] = df["published_at"].apply(lambda x: parser.parse(x) if x != "N/A" else pd.NaT)
    return df


