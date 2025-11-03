# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

# Step 1 - I/O and O/P
# I/O -  int
# O/P - int

# Step 2 - Rough Logic
# return n1+n2+n3


# Step 3 - Write Logic

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

def sum_nums(num1=100, num2=200, num3=300):
    return num1 + num2 + num3

result0 = sum_nums(num1, num2, num3)  # taking values from user
result1 = sum_nums()
result2 = sum_nums(10,20,30)
result3 = sum_nums(num1=10)
print(result3)

