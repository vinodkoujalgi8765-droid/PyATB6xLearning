class Dog:
    name = None
    breed = None

    def __init__(self,namegiven,breedgiven):
        self.name = namegiven
        self.breed = breedgiven
        print("constructor has parameter, when obj create will I call default?")

    def talk(self):
        #self.name = "Common Name"
        print(self.name, "talking and belongs to ", self.breed)


d1 = Dog("chow","BB")
d1.talk()

d2 =Dog("tom","WB")
d2.talk()