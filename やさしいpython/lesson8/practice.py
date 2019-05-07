class Car:
    def __init__(self, n=0, g=0):
        self._num = n
        self._gas = g
    
    def getNum(self):
        return self._num
    
    def getGas(self):
        return self._gas
    
c = Car(1234, 20.5)
print(c.getGas(), "/", c.getNum())

c0 = Car()
print(c0.getGas(), "/", c0.getNum())