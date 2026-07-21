import json
with open("sample.json", "r" ,encoding="utf-8") as file:
    logs = json.load(file)
print(logs)