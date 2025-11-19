class Car:
    name =None
    make = None
    model =None


    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.model = o_model
        self.make = o_make

    def select_car(self):
        print(f"selected car is {self.name} and model is {self.model} and {self.make} year")

lambo = Car("AUDI","2025",o_model="V2")
lambo.select_car()

mg = Car("MGHector","Electric","2025")
mg.select_car()
print("name from class ", Car.name)
print(" Same name from constructor ", self.name) # just for understanding
print(" Same name from constructor by using obj mg ", mg.name)


