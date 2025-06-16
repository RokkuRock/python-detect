def main():
    user_input = input("Enter message: ")
    print(f"<div>{user_input}</div>")  # ⚠️ 沒有轉義，模擬 XSS 輸出

main()
