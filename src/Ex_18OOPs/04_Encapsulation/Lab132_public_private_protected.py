class TestExample:

    def __init__(self, driver, config, api):
        self.driver = "Chrome"
        self._config = "STAG"
        self.__api__key = "ABC1234"

    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"API Key: {self.__api__key}")

    def __private_method(self, name):
        print(f"Private method: {name}")

    def _protected_method(self, name):
        print(f"Protected method: {name}")

    def gen(self):
        self.__private_method("vinod")
        self._protected_method("koujalgi")


ex1 = TestExample(driver="Firefox", config="New", api="NoAPI")
#ex1.show()
#ex1.gen()
ex1._protected_method("Bye")
