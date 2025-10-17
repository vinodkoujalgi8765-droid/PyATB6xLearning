n = float(input("Enter a time in seconds: "))
if n <= 0:
    print("Entered time is -ve")
elif 0 <= n <= 3:
    print(f"Page loaded in {n} sec, this is fast")
elif 3 < n <= 10:
    print(f"Page loaded in {n} sec, this is slow")
else:
    print(f"Page loaded in {n} sec, this very very slow")