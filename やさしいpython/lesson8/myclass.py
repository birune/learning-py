class Person:

    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Customer(Person):
    
    def __init__(self, nm, ag, tl):
        super().__init__(nm, ag)
        self.tel = tl
    
    def getName(self):
    #メソッドのオーバーライド
        self.name = "顧客:" + self.name
        return self.name
    
    def getTel(self):
        return self.tel