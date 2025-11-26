class Utility:

    def greet_name(name):
        print("Hi", name)


#created obj with static method and calling it
t = Utility()
t.greet_name() #Hi <__main__.Utility object at 0x000002DE6E096F90>

t.greet_name("vinod")  #TypeError: Utility.greet_name() takes 1 positional argument but 2 were given

#Static Method
#Utility.greet_name("Vinod")