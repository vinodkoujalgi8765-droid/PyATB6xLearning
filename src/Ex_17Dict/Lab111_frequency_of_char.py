string = "automation"

def frequenct_of_char(string):
    my_dict = {}
    for char in string:
        my_dict[char]= my_dict.get(char, 0)+1

    return my_dict

print(frequenct_of_char(string))


'''
string = "automation"

def frequency_of_char(data):
    my_dict = {}
    for i in data:
        if i in my_dict:
            my_dict[i]= my_dict[i]+1
        else:
            my_dict[i] = 1
    return my_dict

print(frequency_of_char(string))

'''