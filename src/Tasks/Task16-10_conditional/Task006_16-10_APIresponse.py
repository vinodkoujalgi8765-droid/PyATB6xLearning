code = int(input("Enter the code: "))

if code == 200:
    print("O/P ✅ Passed API Request")
elif code == 404:
    print("O/P ❌ Failed API Request")
else:
    print("Enter correct code")

