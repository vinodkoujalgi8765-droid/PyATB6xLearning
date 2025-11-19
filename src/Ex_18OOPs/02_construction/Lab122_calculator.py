class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

c1 = Calculator(5,4)
print(c1.add())
print(c1.sub())
print(c1.mul())
