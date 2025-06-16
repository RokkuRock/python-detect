import pickle
import base64

def main():
    data = input("Enter base64-encoded pickled object: ")
    decoded = base64.b64decode(data)
    obj = pickle.loads(decoded)  # ⚠️ 不安全反序列化
    print(f"Deserialized: {obj}")

main()
