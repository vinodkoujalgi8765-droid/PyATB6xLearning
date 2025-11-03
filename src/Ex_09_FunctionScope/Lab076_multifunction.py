var_global = "It is GLobal"

def fun1():
    var_a = "It is fun1 local variable"
    print(var_a)
    print(var_global)

def fun2():
    var_b = "It is fun2 local variable"
    print(var_b)
    print(var_global)
    #print(var_a)

fun1()
fun2()
