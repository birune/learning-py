import re 

ptr = "\.(csv|html|py)$"

str = ["sample.csv", "sample.exe", "test.py", "index.html"]

pattern = re.compile(ptr)
for valuestr in str:
    res = pattern.sub(".txt", valuestr)
    #patternがvaluestrとマッチしたらマッチ部分を.txtに置き換えてresに代入する
    msg = "(変換前)" + valuestr + "(変換後)" + res
    print(msg)