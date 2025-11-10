a = {1, 2, 3}
print(id(a))
b = {3, 4, 5}
print(a|b) #union {1, 2, 3, 4, 5}
'''
a.add(('a','b','c'))
print(a)
print(id(a))
#print(a[0]) #TypeError: 'set' object is not subscriptable , can not access bcz unordered

a.remove(('a','b','c'))
print(a)

'''
print(a.union(b)) # {1, 2, 3, 4, 5}

print(a & b) #intersection, common {3}
print(a.intersection(b)) # {3}

print(a - b) # {1, 2} , only unique element form a
print(b - a)  #{4, 5}

print(a ^ b) #not includes common element {1, 2, 4, 5}

set1 = {1, 2, 3}
set2 = {4, 5, 6}

union_set1 = set1 | set2
union_set2 = set1.union(set2)
print(union_set1)
print(union_set2)

intersection_set1 = set1 & set2
intersection_set2 = set1.intersection(a)
print(intersection_set1) #set()
print(intersection_set2) #{1, 2, 3}

deferance_set1 = set1 - set2
deferance_set2 = set1.difference(set2)
print(deferance_set1) #{1, 2, 3}
print(deferance_set2) #{1, 2, 3}

deferance_set3 = set2 -set1
print(deferance_set3)
deferance_set4 = set2.difference(set1)
print(deferance_set4)

exclude_common_set = set1 ^ set2
print(exclude_common_set)

