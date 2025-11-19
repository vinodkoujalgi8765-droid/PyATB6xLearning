class Dog:
    #Attributes
    Name = None
    Breed = None
    height = None
    weight = None

    #behaviour/Method/Functinality
    def bark(self):
        print(self.Name,"Barking")

    def talk(self,Breed):
        print("Taking",Breed)

chow = Dog()
chow.bark()
rancho = Dog("rancho")
rancho.talk()

