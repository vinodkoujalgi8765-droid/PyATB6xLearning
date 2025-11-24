# Single Inheritance
# A Subclass/Child/Son inherits from one Parent/Base/Father.

class BaseTest:
    driver = "chrome"
    __driver = "FireFox"

    def setup(self):
        #print("Base setup is with browser ",BaseTest.driver)
        print("Base setup is private browser ", BaseTest.__driver) # enacpsulation only allows within class

class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Login test with browser ", BaseTest.driver)
        #print("Trying to access private instace from BaseTest class ", self.__driver)
        print(BaseTest.__driver)  #encapsulation does not allow private attribute access directly from another class
tt = LoginTest()
tt.run()
