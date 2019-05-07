import json
f = open("sample4-1.json", "r")
data = json.load(f)
#ディクショナリとして読み込まれる
print(data)
f.close
