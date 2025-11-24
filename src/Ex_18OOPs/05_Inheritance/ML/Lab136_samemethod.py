class GrandFather:
    brand = "Maruti"
    def car_g(self):
        print("It is my GF car",self.brand)

class Father(GrandFather):
    brand = "Honda"
    def car_f(self):
        print("It is my Father car",self.brand)

class Son(Father):
    #brand = "MG"
    def drive(self):
        print("It is my Son car",self.brand)

s1 = Son()
s1.drive()   # Always consider local varible -->It is my Father car MG