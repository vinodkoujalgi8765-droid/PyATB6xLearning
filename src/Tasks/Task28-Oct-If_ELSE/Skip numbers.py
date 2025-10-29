'''
Skip numbers divisible by 3, from (0,100)
'''

for i in range(101):
    if i % 3 == 0:
        continue
    else:
        print(f"This is not divide by 3: {i}")
