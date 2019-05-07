hira = ["あ", "い", "う", "え", "お"]
num = [1, 2, 3, 4, 5]

#zip(リスト1, リスト2)で二つのリストの要素を組み合わせる
for d in zip(hira, num):
    print(d)

print("hira:", hira)
print("num:", num)

#enumerate(リスト)で要素とインデックスを組み合わせる
for d in enumerate(hira):
    print(d)