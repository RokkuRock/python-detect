import os

def main():
    user_input = input("Enter command: ")
    os.system(user_input)  # ⚠️ 無驗證直接執行外部輸入

main()
