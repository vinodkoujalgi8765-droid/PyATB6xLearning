'''
Q - Create a function which will take a positive number from the user and
perform square of the number?
'''

number = int(input("Enter a positive number: "))

def square_of_number(number):
    if number > 0:
        return number * number
    else:
        return "it is negative"
result = square_of_number(number)
print(result)
