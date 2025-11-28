try:
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    c = a/b
    print(c)
except (TypeError,ZeroDivisionError,ValueError,NameError):
    print("Error Due to the Type, Name, Value or Zero Div!")