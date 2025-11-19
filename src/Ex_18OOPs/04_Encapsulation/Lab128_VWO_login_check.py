class VMWLoginPage:

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def login_status(self):
        if self.email == "vinod@gamil.com" and self.password == "12345":
            print("Login Successful")
        else:
            print("Login Failed")
email_user = input("Enter your email: ")
password_user = input("Enter your password: ")

login = VMWLoginPage(email_user,password_user)
login.login_status()
print(login.email)
print(login.password)