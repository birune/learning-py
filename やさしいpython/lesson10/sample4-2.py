import json

f = open("sample4-2.json", "w")
json.dump({"Tokyo":30, "Osaka":20}, f)
f.close