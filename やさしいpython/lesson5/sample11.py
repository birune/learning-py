data = [1, 2, 3, 4, 5]
print("現在のデータは", data, "です")

#逆順で表示する
print("data[::-1]:", data[::-1])
#[5, 4, 3, 2, 1]
for d in data[::-1]:
    print(d, end='/')
    #5/4/3/2/1/
print()
#元のリストに変更はない
print("data:", data)
#[1, 2, 3, 4, 5]

#逆順で表示する
print("reversed(data)", reversed(data))
#<list_reverseiterator object at ~~~>
for d in reversed(data):
    print(d, end='/')
    #1/2/3/4/5/
print()
#元のリストに変更はない
print("data:", data)
#[1, 2, 3, 4, 5]

#リストを逆順に入れ替える
data.reverse()
print("data.reversed():", data)
