class BaseTest:
    def run(self):
        print("Running from Basetest class")

class LoginTest:
    def run(self):
        print("Running from LoginTest class")

t = LoginTest()
t.run()
t=BaseTest()
t.run()