num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

class CalculatorPC:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        if self.num1 > self.num2:
            return self.num1 - self.num2
        else:
            return self.num2 - self.num1

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num1 ==0 or self.num2 ==0:
            return "Not divisible by zero"
        else:
            return self.num1/self.num2

cal_add = CalculatorPC(num1=4,num2=8)

print(cal_add.addition())
print(cal_add.subtraction())
print(cal_add.multiplication())
print(cal_add.division())

