try:
    num = int(input("Enter a number: "))
    print("your result ",10/num)
except ValueError:
    print("Enter only number not character")
except ZeroDivisionError:
    print("Number can not divisible by Zero")

a = 5
b = 6
print("next line code executed,",a+b)
