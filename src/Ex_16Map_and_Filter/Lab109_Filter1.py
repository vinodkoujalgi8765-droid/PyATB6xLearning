num = [1,2,3,4,5,6,7,8,9]

def even(num):
    return num%2==0

result = filter(even, num)
print(list(result))



list_student = [50, 51, 100]
def std(num):
    return num > 50

result = filter(std, list_student)
print(list(result))

result2 = map(std, list_student)
print(list(result2))
