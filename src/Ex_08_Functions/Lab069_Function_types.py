#user define function

#non-return type
#with return type
#without parameter
#with parameter /arguments



import math

result = max(2,3)
print(result)

# 1. non-return and no parameter / arguments
'''
it is non-return and parameter 
it means we can define any param while declaring fun and calling function
'''

def fun1():
    print("it is non-return and parameter ")
    a = 2
    b = 5
    result = a+b
    print(result)
fun1()


# 2. # No Return Type and with Argument/ Param
'''
this is with parameter , 
it means user can pass values where it defined while declaring fun
 and these values will use inside fun  as below
'''

def fun2(a,b):
    result = a+b
    print("Type2 :",result)

fun2(5,2)

# 3. No Return Type and with Default Argument ( # positional argument)
'''
no need to pass values at time of calling funtion. Its optional
'''

def fun3(a=5,b=2):
    result = a+b
    print("Type3 :",result)
fun3()
fun3("vinod",'8')
fun3(b=100)


# 4. Argument + return Type

def fun4(a,b):
    result = a+b
    return "Type4 :",result

print(fun4(a=2,b=5))


