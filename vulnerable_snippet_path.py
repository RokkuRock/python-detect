import os

def main():
    filename = input("Enter filename: ")
    with open(f"./files/{filename}", "r") as f:
        print(f.read())  # ⚠️ 可被路徑遍歷利用讀取任意檔案

main()
