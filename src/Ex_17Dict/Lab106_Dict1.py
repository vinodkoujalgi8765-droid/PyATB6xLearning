my_dict = {
    "name" : "Vinod",
    "age" : 18,
    "height" : 70,
    "weight" : 80
}

print(my_dict)
print(my_dict["name"])
print(my_dict['age'])
my_dict["age"] = 25
print(my_dict)

for key,value in my_dict.items():
    print(key, value)


