class Person:
    count = 0
    #クラス変数(C++でいう静的データメンバ)

    def __init__(self, n, a):
        Person.count += 1
        self.name = n
        self.age = a
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    @classmethod
    #クラスメソッド(c++でいう静的データ関数)の前につけるやつ
    def getCount(cls):#clsにはクラス名が入る
        return cls.count
    
pr1 = Person("aaa", 10)
pr2 = Person("bbb", 20)

print(pr1.getName(), "さんは", pr1.getAge(), "歳")
print(pr2.getName(), "さんは", pr2.getAge(), "歳")
print("合計人数は", Person.count, "人")