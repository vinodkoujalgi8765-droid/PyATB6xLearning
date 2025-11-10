my_list = [1,2,3,4,5,6,7]

def eva(x):
    return x%2==0

result = map(eva, my_list)
print(list(result))

result1 = map(lambda x:x%2==0, my_list)
print(list(result1))


result2 = filter(lambda x:x%2==0, my_list)
print(list(result2))

