filename = input()
with open(f"./files/{filename}", "r") as f:
    print(f.read())
