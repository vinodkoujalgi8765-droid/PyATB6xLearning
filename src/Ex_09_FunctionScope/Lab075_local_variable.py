var_global = 72

def local_var():
    a = 10
    print(a)
    print(var_global)

x = local_var()
print(var_global)


