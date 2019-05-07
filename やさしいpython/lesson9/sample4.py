str = input("文字列を入力してください")
key = input("検索する文字列を入力してください")

res = str.find(key)
#最初に見つかった部分のインデックスを返す
#見つからなかったら-1を返す

if res != -1:
    print(str, "の", res, "の位置に", key, "が見つかりました")
else:
    print(str, "のなかに", key, "は見つかりませんでした")

if key in str:
#あるかどうかだけ知りたいときはこれでok
    print(str, "のなかに", key, "が見つかりました")
else:
    print(str, "のなかに", key, "は見つかりませんでした")