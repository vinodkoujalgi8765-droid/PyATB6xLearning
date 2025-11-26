#Normal class with self Method, created obj and calling method
class Utility:

    def greet_name(self,name):
        print("Hi", name)

t = Utility()
t.greet_name("John")

##Normal class with self Method, without creating obj and calling method
class Utility2:

    def greet_name(self,name):
        print("Hi", name)

#Utility2.greet_name("Vinod")  #Error: TypeError: Utility2.greet_name() missing 1 required positional argument: 'name'
                                        # bcz of self

#Normal class without self Method, without creating obj and calling method
class Utility3:

    def greet_name(name):
        print("Hi", name)

Utility3.greet_name("Vinod")

#static Method

class Utility4:

    @staticmethod
    def greet_name(name):
        print("Hi", name)

Utility4.greet_name("Static Method")

