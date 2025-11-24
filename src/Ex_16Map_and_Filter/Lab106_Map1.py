numbers = [1,2,3,4,5]

def square(x):
    return x*x

sq_result = map(square, numbers)
print(list(sq_result))
print(sq_result)
print(tuple(sq_result))
