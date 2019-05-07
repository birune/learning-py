import re

ptr = ["[012]", "[0-3]", "[^012]"]
#[]をつけると文字列クラスになる(文字列がandならこっちはor)
#文字列クラスに^をつけると否定をとる
str = ["0", "1", "2", "3"]

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