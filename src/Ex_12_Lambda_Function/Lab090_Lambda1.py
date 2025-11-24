def triple_number(num):
    return num * 3

print(triple_number([1,2]))
print(triple_number((1,2)))
#print(triple_number({1,2}))  # set wont keep duplicates

#in case of lambda
result = lambda num:num*3
print(result([1,3]))
print(result("vinod "))
print(result(5))