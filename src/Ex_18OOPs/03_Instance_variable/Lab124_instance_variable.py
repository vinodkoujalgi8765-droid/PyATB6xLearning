a = 10  #variable  # can be used every where

class Person:
    b = 20  #Instance variable , can be access within class by self.

    def info(self):
        c = 30  #Local variable for info fun only
        print(a)
        print(self.b)
        print(c)

p = Person()
print(p.b) ##Instance variable , can be access within class by self.

p.info()
print(a)
# print(b) #not valid call
# print(c) #not valid call