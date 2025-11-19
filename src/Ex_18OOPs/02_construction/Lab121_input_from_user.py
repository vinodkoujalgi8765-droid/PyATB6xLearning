class Person:

    def __init__(self):
        self.name = input("What is your name?\n") #value entered interactively
        self.age = input("How old are you?\n") # Needs user input When program runs, at runtime
        self.phone = input("What is your favorite phone number?\n")

    def display_details(self):
        print(f"\nName: {self.name} \nAge:{self.age} \nPhone number:{self.phone}")

p1 = Person()
p1.display_details()

class Person2: #fixed value, no user input
    def __init__(self):
        self.surname = "Kouyjalgi"

    def lastname(self):
        print("lastname is ", self.surname)

p2=Person2()
p2.lastname()

class Person3:
    def __init__(self,midname): #value passed as argument, Needs user input When calling class
        self.midname = midname

    def mname(self):
        print("My Mid name is ", self.midname)

p3 = Person3("P")
p3.mname()

