import myclass as my
#別ファイル(myclass.py)をインポートする
#asを使いインポートしたファイルの呼び名を決められる(無くてもいい)

#from myclass import Customerで
#Customerクラスはどのファイルからインポートしているか書かなくてもいい

pr = my.Customer("aaa", 10, "090-0000-0000")
#どのファイルからインポートしているかを明確にする

#from~ でインポートしていればmy.は要らない


print(pr.getName())
print(pr.getTel())