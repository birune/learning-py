str1 = input("文字列を入力してください:")
old = input("置換される文字列を入力してください:")
new = input("置換する文字列を入力してください:")

if old in str1:
    str2 = str1.replace(old, new)
    #置換された文字列がstr2に代入される
    print(str2, "に置換しました")
else:
    print(str1, "のなかに", old, "はありませんでした")