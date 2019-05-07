import os
import os.path

curdir = os.listdir(".")

for name in curdir:
    print(os.path.abspath(name), end=",")
    #abspathで絶対パス名(階層を省略せずに書いたもの)を返す
    if(os.path.isfile(name)):
    #ファイルかどうかの真偽を返す
        print("ファイルです")
    else:
        print("ディレクトリです")
print()