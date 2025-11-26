class BaseTest:

    def __init__(self):
        __password = "12345"
        __username = "koujalgi"

    def run(self):
        print("Base test run")

class APITest(BaseTest):
    def run(self):
        print("API test run")

    def info(self):
        print("API test info")

t=BaseTest() #object created by using () with class
BaseTest.run()   #Type Error Expecting one argument as self

