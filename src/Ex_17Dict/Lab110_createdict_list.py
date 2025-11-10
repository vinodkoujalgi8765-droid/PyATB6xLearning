list1 = ['a','b','c']
list2 = [1,2,3]

my_dict = dict(zip(list1,list2))
print(my_dict)

d1 = {
    "name":"vinod",
    "age":22
}

d2 = {
    "place" : "Pune",
    "Pin" : 12345
}

result = d1|d2
print(result)