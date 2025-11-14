
class Person:
    name = None
    age = None
    height = None
    wieght = None
    occupation = None


    def __init__(self,namex,agex,heightx,wieghtx,occupationx):
        self.name = namex
        self.age = agex
        self.height = heightx
        self.wieght = wieghtx
        self.occupation = occupationx

    def intro(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def tall(self):
        print(f"I am {self.height} height")

    def fat(self):
        print(f"I am {self.wieght} wieght")

    def work(self):
        print(f"I am {self.occupation}")

    def hobby(self):
        print(f"I am {self.height} height and {self.wieght} weight, hence I love sport ")

    def disply_attribute(self):
        print(f"{p_info.name} \n{p_info.age} \n{p_info.height} \n{p_info.wieght} \n{p_info.occupation}")


p_info = Person("Vinod",20,7.0,88.26,"QA")
p_info.intro()
p_info.tall()
p_info.work()
p_info.hobby()
p_info.fat()
print("These are Instance varible")
p_info.disply_attribute()

