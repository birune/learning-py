#デコレータを使うと関数を変更することなく処理を追加できる
#デコレータの定義
def deco(func):#デコる関数を受け取る
    def wrapper(*args, **kwargs):#デコる関数の引数を受け取る
        print("---")
        result = func(*args, **kwargs)
        print("---")
        return result#デコる関数の戻り値を返す
    return wrapper#最終的に返す関数

@deco#使うデコ内容を決める
def printmsg(x):#今回デコる関数
    print(x, "を入力しました")

s = input("メッセージを入力してください")

printmsg(s)
        
