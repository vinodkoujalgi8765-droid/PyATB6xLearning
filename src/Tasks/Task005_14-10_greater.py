num=float(input("Enter the number: "))
#Method1
if num >= 100:
    print("Yes it is greater than 100")
else:
    print("Yes it is less than 100")

#Method2
print("Yes it is greater than 100" if num >= 100 else "Yes it is less than 100")