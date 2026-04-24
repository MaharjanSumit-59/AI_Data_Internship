"""
TASK 2  ·  MEDIUM
Fetch & Save to CSV
Fetch posts from the API. Save them to a CSV with columns: id, title, body. Then read the CSV back and print only posts where title contains more than 5 words.
Steps:
Endpoint: /posts
Save: id, title, body  to  posts.csv
Read back with DictReader
Filter: Posts having title more than 5 words and write in a new CSV
Deliverable: posts.csv + filter script + new csv
"""

import requests
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Fetch posts from the API
url = os.getenv("POSTS_API_URL")
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    
    # Save posts to CSV
    with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        for post in posts:
            writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
    print(f"Saved {len(posts)} posts to posts.csv")
    
    # Read back the CSV and filter posts
    with open('posts.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        filtered_posts = [row for row in reader if len(row['title'].split()) > 5]
    
    # Save filtered posts to a new CSV
    with open('filtered_posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        for post in filtered_posts:
            writer.writerow(post)
    print(f"Filtered {len(filtered_posts)} posts into filtered_posts.csv")
else:
    print(f"Failed to fetch posts. Status code: {response.status_code}")


