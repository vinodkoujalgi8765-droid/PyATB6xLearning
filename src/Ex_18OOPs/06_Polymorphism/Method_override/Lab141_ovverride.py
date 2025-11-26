
class TestSuite:
    def info(self):
        print("Test suite information")

class BaseTest(TestSuite):
    def setup(self):
        print("Base setup")

    def run(self):
        print("Base test run")

class LoginTest(BaseTest):
    def run(self):
        print("Login test run")

class APITest(BaseTest):
    def run(self):
        print("API test run")

t = APITest()
t.run()
t.info()
t = BaseTest()
t.run()

