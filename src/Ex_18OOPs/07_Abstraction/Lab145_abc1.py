from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        print(self.name,"Making sound from ABC class")

class Dog(Animal):
    def info(self):
        pass#self.sound()

    def sound(self):
        print(self.name,"Making sound from Dog class")


# t = Dog("Dog")
# t.sound()

t = Animal("Cat")
t.sound()