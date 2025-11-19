class Calc:
    num2  = float(input("Enter the second number: "))

    a = None
    b = None

    def __init__(self):
        print("This is non PC")

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    num1 = float(input("Enter the first number: "))

c1 = Calc()
print(c1.add(Calc.num1,Calc.num2))


