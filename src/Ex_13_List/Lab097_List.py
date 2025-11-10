my_list = [1,2,3,4,5,"vinod",True,2.55]
print(my_list)

for elements in my_list:
    print(elements,end=" ")

a = range(1,5)
print(a)
print(list(a))
print(tuple(a))
print(type(a))
print(tuple(my_list))
print(set(my_list))
print(dict(my_list))  #TypeError: cannot convert dictionary update sequence element #0 to a sequence