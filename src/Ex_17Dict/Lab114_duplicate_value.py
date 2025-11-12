dict1 = {"a":1, "b":2, "c":1, "d":3}

def duplicate_value(dict1):
    unique_values = []
    result = {}
    for key,value in dict1.items():
        if value not in unique_values:
            result[key] = value
            unique_values.append(value)

    print(result)

duplicate_value(dict1)
