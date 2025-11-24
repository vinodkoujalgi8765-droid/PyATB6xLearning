#Hybrid Inheritance
#A mix of multiple and multilevel inheritance.

class Base:
    brand = "Base_Method"
    def base_method(self):
        print("Base Method",self.brand)

class A(Base):
    brand = "A_Method"
    def a_method(self):
        print("A Method",self.brand)

class B(Base):
    brand = "B_Method"
    def b_method(self):

        print("B Method",self.brand)

class C(A,B):
    #brand = "C_Method"
    def c_method(self):
        print("C Method",self.brand)

obj = C()
obj.c_method()


