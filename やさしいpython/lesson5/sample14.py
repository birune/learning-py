data1 = [1, 2, 3, 4, 5]

#[式 for 変数 in リスト if 条件で
#条件がtrueのとき式の値を新しいリストの要素とする
data2 = [n*2 for n in data1 if n!=3]
print(data2)
#[2, 4, 8, 10]