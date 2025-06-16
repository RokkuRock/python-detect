import sqlite3

def main():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (username TEXT, password TEXT)")
    user_input = input("Enter username: ")
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    print(f"Executing query: {query}")
    conn.execute(query)  # ⚠️ 拼接輸入，易受 SQL 注入攻擊

main()
