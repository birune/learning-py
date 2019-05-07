data = [1, 2, 3, 4, 5]

#lambdaを使うと感嘆の式の形で記述できる関数を定義できる
#map(関数(の処理), 繰り返しの仕方)
for d in map(lambda x: x*2, data):
    print(d)