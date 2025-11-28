a = input("Enter a number: ")
b = input("Enter another number: ")

try:
    c = a/b
    print(c)
except TypeError:
    print("a and b both must be integers")
except ZeroDivisionError:
    print("b is Zero and zero can not be divisible")
