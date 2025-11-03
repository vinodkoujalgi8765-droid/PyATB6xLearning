'''
parameter does not matter what type of data user provided,
User can any type of data and interpreter automaticaaly identify it.
'''
def fun_param(name):
    #print("I am function ", name)
    print(type(name))
    for i in name:
        print(i)
        print(type(i))

#fun_param(5)
#fun_param("vinod")
fun_param(["it", "is ","from","list", 12345])
