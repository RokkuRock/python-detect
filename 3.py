import pickle, base64
data = input()
obj = pickle.loads(base64.b64decode(data))
