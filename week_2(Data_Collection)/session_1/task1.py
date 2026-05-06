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

import json
import os 
from urllib import request, error
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch users from the API
url = os.getenv("API_URL")

try: 
    with request.urlopen(url) as response:
        if response.status == 200:
            data = response.read()
            users = json.loads(data)
            
            for user in users:
                print(f"Name: {user['name']}")    
                print(f"Email: {user['email']}")
                print(f"City: {user['address']['city']}")
                print("-" * 30)
        else:
            print(f"Failed to fetch users. Status code: {response.status}")
except error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except error.URLError as e:
    print(f"URL Error: {e.reason}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
