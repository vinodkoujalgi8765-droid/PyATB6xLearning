dict1 = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6
}

dict2 = {
    "a":1,
    "b":2,
}
key = dict1.keys()
print(key)
print(type(key))
value = dict1.values()
print(value)
print(type(value))
missing_key = dict1.keys() - dict2.keys()
print(missing_key)
a = set(missing_key)
print(type(missing_key))
print(type(a))