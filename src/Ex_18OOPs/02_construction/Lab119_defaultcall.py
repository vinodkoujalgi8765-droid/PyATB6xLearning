class Dog:

    name =None
    age =None


    def __init__(self):
        print("Default calling")

    def talk(self):
        print("Dog talking")

    def walk(self):
        print("Dog walking")

d1 = Dog()
d2=Dog()

print(d1.name)
print(d2.age)