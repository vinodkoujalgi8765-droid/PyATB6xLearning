n = int(input("Enter the number: "))
r = 1
for i in range (1,n+1):
    if n!=0:
        r = r * i
    else:
        print(r)
print("The factorial of",n,"is",r)
