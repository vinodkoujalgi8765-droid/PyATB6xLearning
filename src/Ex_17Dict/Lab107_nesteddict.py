my_dict = {
    "name" : "Vinod",
    "age" : 18,
    "age" : 30,
    "height" : 70,
    "weight" : 80,
    "Address" : {
        "Street" : "Madhav Nagar",
        "PIN" : 12345
    }
}
print(my_dict)
print(my_dict["name"])
print(my_dict["Address"])
print(my_dict["Address"]["PIN"])
my_dict["Address"]["Street"] = "Pune"
print(my_dict)