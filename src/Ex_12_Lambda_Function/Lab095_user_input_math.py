import math

def power_num(num):
    return math.pow(num,3)

print(power_num(2))

num = int(input("Enter a number: "))

result = lambda num: math.pow(num,3)
print(result(num))
