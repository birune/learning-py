import re

ptr = ["T*", "T+", "T?", "T{3}", "T{2,3}"]
#0回以上、1回以上、0か1回、3回以上、2回以上3回以下

#最長部分にマッチングする
#*か+の後に?をつけると最短部分にマッチングする
str = ["X", "T", "TT", "TTT", "TTTT"]

for valueptr in ptr:
    print("-----")
    pattern = re.compile(valueptr)
    #valueptrをパターンとしてコンパイルして代入してる
    for valuestr in str:
        res = pattern.search(valuestr)
        if res is not None:
        #resに値があった時
            m = "〇"
        else:
            m = "×"
        msg = "(パターン)" + valueptr + "(文字列)" + valuestr + "(マッチ)" + m

        print(msg)