import re
print("ファイルのリストは以下です")
str = ["sample.csv", "sample.exe", "sample1.py", "sample2.py", "sample.txt", "index.html"]
for i in str:
    print(i)

ptr = input("拡張子を入力してください:")
print("該当するファイルは以下です")

pattern = re.compile(ptr)
for valuestr in str:
    res = pattern.search(valuestr)
    if res is not None:
        print(valuestr)
