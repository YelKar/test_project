import json
import pickle


jsn = pickle.loads(bytes.fromhex(open("file.txt").read()))

print(jsn, len(jsn))
jsn = json.dumps(json.loads(jsn), ensure_ascii=False)
print(jsn)
print(len(jsn))
