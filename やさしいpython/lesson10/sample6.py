import os
curdir = os.listdir(".")
#現在のディレクトリからファイル、ディレクトリを取得する
#.はこのプログラムのあるディレクトリを示す

for name in curdir:
    print(name)