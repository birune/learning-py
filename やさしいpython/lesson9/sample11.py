import re

ptr = ["(TXT)+", "TXT|XTX"]
#TXTの一回以上の繰り返し、TXTまたはXTX

str = ["TX", "TXT", "XTX", "TXTXT"]

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