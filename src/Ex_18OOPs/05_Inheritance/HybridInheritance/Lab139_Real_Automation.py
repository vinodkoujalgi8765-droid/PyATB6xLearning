class BaseTest:

    def __init__(self,browser):
        self.browser = browser

    def setup(self):
        print("lanching browser",self.browser)

class LoginTest:
    def run_test(self):
        self.setup()
        print("browser is ready to add address")

class Singup(BaseTest):
    def signup(self):
        self.setup()
        print("Enter credentials for singup")

t = Singup("chrome")
t.signup()
print(id(t))
print(t)

t = Singup("FireFox")
t.signup()
print(id(t))
print(t)
