var_global = "It is globalvar"

def fun1():
    var_a = "It is localvar from fun1"

    #changing here global var value, this value only for this fun
    var_global = "It is globalvar from fun1"

    print(var_global)

print(var_global)
fun1()
print(var_global)
