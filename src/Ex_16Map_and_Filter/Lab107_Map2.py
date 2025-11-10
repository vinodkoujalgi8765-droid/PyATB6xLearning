my_list = [1,2,3,4,5,6,7,8]

def even(num):
    return num%2 == 0

result = map(even, my_list)
print(list(result))