# Single Inheritance
# A Subclass/Child/Son inherits from one Parent/Base/Father.

class BaseTest:
    driver = "Chrome"
    __driver = "FireFox"

    def setup(self):
        print("Basesetup with browser and env", self.__driver)
        print(self.__driver)


class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Running login test",self.driver)
        print(self.__driver)

t = LoginTest()
t.run()
print(t.driver)
#print(t.__driver)

