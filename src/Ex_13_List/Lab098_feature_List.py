#append()
a = [1,2,3]
a.append("Vinod")
print(a)

#extend()
a.extend([1,2,3])
print(a)

#extend list using set
a.extend({1,2,4,5})
print(a)

#insert
a.insert(1,"#")
print(a)

#modifying value at index 1
a[1]= "Amit"
print(a)

#remove()
a.remove("Amit")
print(a)

new_list = list(a)
print(new_list)

#pop
new_list.pop()
print(new_list)

#finding index
#print(new_list.index("Amit"))
#print(new_list.index("vinod"))
print(new_list.index("Vinod"))

print(new_list.count(1))

