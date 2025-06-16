import sqlite3
conn = sqlite3.connect(":memory:")
username = input()
query = f"SELECT * FROM users WHERE username = '{username}'"
conn.execute(query)
