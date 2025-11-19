class Person:
    # Attributes
    name = None
    age = None
    id = None
    place = None
    phone = None

#behaviour
    def talk(self): # self - this , self will be first argument in every behaviour.
        print("I can talk")

    def sleep(self,name): #Parameter with no return
        print("I am a Method!!")
        print("I can sleep",name)

    def eat(self,name): #parameter with return
        print("with return")
        return "I can eat",name

    def walk(self):
        print("without parameter", "I am walking",name)

    def walk2(self):
        print("without parameter and with class attribute", "I am walking", self.name)

p1 = Person()
print(p1.eat("kiran"))
p1.walk2()
print(p1.phone)
p1.talk()
