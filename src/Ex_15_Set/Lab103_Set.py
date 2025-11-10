'''
Set is collection of unique elements and represented by {}
'''
list_of_unique_items = {1, 2, 3, 4, 4, 5, 5}
print(list_of_unique_items)

list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1)
print(set1)

t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(t)
print(set(t))

set1.add("A")
print(set1)

set1.remove(33)
print(set1)

mixed = {1, "QA", True, False, 3.5}
print(mixed)
