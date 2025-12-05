
#print(10/0) #ZeroDivisionError: division by zero

try:
    print(10/0)
except ZeroDivisionError:
    print("Number can not be divisible by Zero")
