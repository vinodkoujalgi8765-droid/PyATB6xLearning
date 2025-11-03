def fun1():
    a = 10

    def fun2():
        b = 20
        print(a)

    def fun3():
        c = 30
        print(a)

    fun2()
    fun3()

fun1()
