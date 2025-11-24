class Car:

    def __init__(self):
        self.brand = "Honda"
        self.__engine = "super6"

    def car_info(self):
        print("Brand is ", self.brand)
        print("Engine is ", self.__engine)
        self.__engineversion = "v1.0.0"
        print("Engine version is ", self.__engineversion)

p1 = Car()
print(p1.brand)
#print(p1.__engine)
p1.car_info()
print(p1.car_info.__engineversion)