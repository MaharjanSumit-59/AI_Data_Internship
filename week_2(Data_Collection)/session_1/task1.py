"""
TASK 1  ·  EASY
Fetch & Print
Use the JSONPlaceholder API to fetch a list of users. Print each user's name and email to the terminal.
Steps:
requests.get('https://jsonplaceholder.typicode.com/users')
Check status_code == 200
Loop through the JSON and print name + email + address city
Deliverable: working script + terminal screenshot
"""

import requests
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch users from the API
url = os.getenv("API_URL")

response = requests.get(url)
if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City: {user['address']['city']}")
        print("-" * 30)
else:
    print(f"Failed to fetch users. Status code: {response.status_code}")
    
