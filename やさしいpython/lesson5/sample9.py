a = [1, 2, 3]
b = [4, 5 ,6]
ab = a + b
print(ab)
#[1, 2, 3, 4, 5, 6]

#"リスト名1.extend(リスト名2)"でリスト1にリスト2を連結できる(リスト1の拡張)
a.extend(b)
print(a)
#[1, 2, 3, 4, 5, 6]
print(b)
#[4, 5, 6]

for i in range(4,7):
    a.remove(i)
print(a)
#[1, 2, 3]

#extendと同じ
a += b
print(a)
#[1, 2, 3, 4, 5, 6]
print(b)
#[4, 5 ,6]