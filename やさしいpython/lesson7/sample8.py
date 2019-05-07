def f1():
    print("f1が呼び出されました")
def f2():
    print("f2が呼び出されました")
def f3():
    print("f3が呼び出されました")

FuncList = [f1, f2, f3]

res = int(input("呼び出す関数を指定してください:"))

if res >= 0 and res <= len(FuncList):
    FuncList[res]()
