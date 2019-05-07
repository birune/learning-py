#"for 変数 in 繰り返しの仕組み:"

#"range(開始値, 停止値, 間隔)"
#rangeのなかは開始値は0が初期値、間隔は1が初期値なので省略できる
for i in range(1,13,1):
    print(i, "月")

for i in range(12):
    print(i+1, "月")

for i in range(1,13):
    print(i, "月")