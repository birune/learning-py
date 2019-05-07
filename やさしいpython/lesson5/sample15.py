data = [2, 1, 4, 5, 3]
print("最大値",max(data))
print("最小値",min(data))
print("合計",sum(data))
print("昇順",sorted(data))
print("降順",sorted(data, reverse=True))

#メソッドを使うとリスト自体を入れ替える
data.sort()
print(data)
data.sort(reverse=True)
print(data)