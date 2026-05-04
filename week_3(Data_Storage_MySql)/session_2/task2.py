"""
Task B · API Monitor with Change Detection [Hard]
Using mysql-connector-python and https://jsonplaceholder.typicode.com/posts, 
build a monitoring script that detects changes between runs. 
Create a database called monitor_db with two tables — posts (stores fetched data) and change_log (records what changed and when). 
On first run, insert all posts and log each as 'NEW'. 
Then manually update one row in MySQL (UPDATE posts SET title='Changed' WHERE id=1) 
and re-run — your script must detect the mismatch and log it as 'MODIFIED' in change_log. 
Print results for: post count per user, all change log entries from the latest run, and which user triggered the most change events. 
Wrap every API call and DB operation in try/except with printed error messages.
Deliverable: MySQL monitor_db with both tables populated + Python script
"""