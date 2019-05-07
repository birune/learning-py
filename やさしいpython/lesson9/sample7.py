import re

ptr = ["TXT", "^TXT", "TXT$", "^TXT$"]
#^は行頭にあった時
#$は行末にあった時
str = ["TXT", "TXTT", "TTXT"]

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