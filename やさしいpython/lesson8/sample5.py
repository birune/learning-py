class Person:

    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Customer(Person):
#派生クラスの定義
    def __init__(self, nm, ag, tl):
        super().__init__(nm, ag)
        #基底クラスのデータ属性を初期化するために基底クラスのコンストラクタを呼び出す
        self.tel = tl
    
    def getName(self):
    #メソッドのオーバーライド
        self.name = "顧客:" + self.name
        return self.name
    
    def getTel(self):
        return self.tel

pr = Customer("aaa", 10, "090-0000-0000")

print(pr.getName())
print(pr.getTel())