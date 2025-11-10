#set
squares_set = {x**2 for x in range(5)}
print(squares_set)

#List
squares_list = [x**2 for x in range(5)]
print(squares_list)

#tuple
squares_tuple = (x**2 for x in range(5))
print(squares_tuple)  #<generator object <genexpr> at 0x000001FCABA4A9B0>
print(tuple(squares_tuple))

