# Write a program to calcuclate even and odd

# def even_odd(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
#
# num = int(input("Enter a number: "))
# print(even_odd(num))

user_input = int(input("Enter a number: "))
result = lambda  x: "x is even"  if x%2==0  else"x is odd"
print(result(user_input))