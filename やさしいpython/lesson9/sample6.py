import re
#正規表現を扱うときにインポートするモジュール

ptr = ["ラグナ", "ザ", "ブラッドエッジ"]
#検索する文字列
str = ["ラグニャ", "ニャ", "ブラッドエッジ"]
#検索される文字列

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