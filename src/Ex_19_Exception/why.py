'''
#this gives any error and stop at same step
print(10/0)  #ZeroDivisionError: division by zero
print("vinod")

#using Exceptions
'''
try:
    print(10/0)
except ZeroDivisionError:
    print("not divisible by zero")

print("Vinod")