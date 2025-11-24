class BaseTest:
    def setup(self):
        print("Setup from BaseTest")

class LoginTest(BaseTest):
    def run(self):
        print("running LoginTest")

class Singup(BaseTest):
    def run(self):
        self.setup()
        print("running Singup")

t = Singup()
t.run()
tt = LoginTest()
tt.run()

