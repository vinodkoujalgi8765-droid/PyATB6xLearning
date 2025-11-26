class Person:
    def say_name(self,name):
        print("Hello " + name)

    def say_name(self,name,surname):
        print("Hello " + name + " " + surname)


print(id(Person))
#Person.say_name("John","Smith")
t = Person()
t.say_name("John","Smith")
print(id(Person))