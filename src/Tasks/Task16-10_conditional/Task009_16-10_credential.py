username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

usr_name = "admin"
passwd = "1234"
if username == usr_name and password == passwd:
    print("✅ Login Successful")
elif username == "admin" and password != passwd:
    print("Password is wrong")
elif usr_name != username and passwd == password:
    print("username is wrong")
else:
    print("Invalid username or password")
