a = [5, 1, 2, 5, 3, 4, 5]
print(a)

#"del リスト名[インデックス]"で指定したインデックスの要素を削除する
del a[1]
print(a)

#"リスト名.remove(値)"で指定した値と等しい最初の要素を削除する
a.remove(5)
print(a)
a.remove(5)
print(a)

#リストにない要素をremoveすることはできない
#ex) a.remove(6)