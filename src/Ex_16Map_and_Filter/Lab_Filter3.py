names = ["QA", "", "Automation", "", "Tester"]

def non_empty(name):
    return name != ""

result = filter(non_empty, names)
print(list(result))

result1 = map(non_empty, names)
print(list(result1))
