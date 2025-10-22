count = float(input("Enter time in sec to verify page loading check: "))

while count >=0:
    if count <= 5:
        print("success page loaded within 5sec")
        print(count, "seconds completed")
        break
    else:
        print("Timed out, taken more than 5sec")
        print(count, "seconds completed")
        break
    count = count + 1

