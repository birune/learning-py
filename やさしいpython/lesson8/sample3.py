class Person:
    def __init__(self, n, a):
    #コンストラクタの定義
        self.name = n
        self.age = a
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
pr = Person("鈴木", 19)

n = pr.getName()
a = pr.getAge()

print(n, "さんは", a, "歳")

pr.age += 1
nexta = pr.getAge()

print(n, "さんは来年", nexta, "歳")