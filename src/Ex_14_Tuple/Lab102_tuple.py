cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(len(cities))
print("London" in cities)
print("a" in cities)


t = (12, 34, 56)
#t.append(5)
#print(t)  #AttributeError: 'tuple' object has no attribute 'append'

ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLS)

numbers = "Pramod" * 3
print(numbers)

numbers = ("Pramod",) * 3
print(numbers)

numbers = (1, 2) * 3
print(numbers)