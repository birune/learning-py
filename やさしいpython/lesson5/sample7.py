#リストを代入すると2つの変数で1つのリストを表す
a = [1, 2, 3, 4, 5]
b = a
print(b)
#[1, 2, 3, 4, 5]
b.append(6)
print(b)
#[1, 2, 3, 4, 5, 6]
print(a)
#[1, 2, 3, 4, 5, 6]