from dotenv import load_dotenv
import os

class VWOLoginPage:

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def login_status(self):
        load_dotenv(dotenv_path= r'C:\Users\koujalgi\PycharmProjects\PyATB6xLearning\src\Ex_18OOPs\04_Encapsulation\.env')
        if self.email == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD"):
            print("Login successful")
        else:
            print("Login failed")
login_check = VWOLoginPage("vinod","123")
login_check.login_status()
print(os.name)
