hira = ["あ", "い", "う", "え", "お"]
num = [1, 2, 3, 4, 5]

for i, j in zip(hira, num):
    print("平仮名:", i, end='/')
    print("数字:", j)

#n1にはnum[0]が・・・n5にはnum[4]が代入される
n1, n2, n3, n4, n5 = num
print(n1, n2, n3, n4, n5)