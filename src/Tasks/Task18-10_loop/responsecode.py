
count = 1

while count <= 3:
    response_code = int(input("Enter the response code: "))
    if response_code == 200:
        print(f"Attempt {count}:response working and code is {response_code}")
        break
    else:
        print(f"Attempt {count}:response not-working and code is  {response_code}")

        count = count + 1
