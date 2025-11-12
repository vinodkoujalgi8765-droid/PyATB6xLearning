dict1 = {
    "a":10,
    "b":20,
    "c":30,
    "d":40
}

# def max_value(my_dict):
#     return max(my_dict.values()), min(my_dict.values())
# print(max_value(dict1))

def max_value(my_dict):
    value = list(my_dict.values())
    max_num = value[0]
    for i in range(len(value)):
        if value[i] > max_num:
            max_num = value[i]
    return max_num

print(max_value(dict1))


max_value(dict1)
