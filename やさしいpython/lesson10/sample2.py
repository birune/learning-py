f = open("sample1.txt", "r")
lines = f.readlines()
#すべての行を読み出す
for line in lines:
    print(line, end="")
    #1行ずつ表示する
    #改行なしにしないと一行間隔があく

f.close()