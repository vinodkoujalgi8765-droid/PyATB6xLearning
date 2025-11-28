names = ["QA", "", "Automation", "", "Tester"]

def non_empty(name):
    return name != ""

result = filter(non_empty, names)
print(result)  #<filter object at 0x0000021AE8730700>
print(list(result)) #['QA', 'Automation', 'Tester']


# result1 = map(non_empty, names)
# print(list(result1))
