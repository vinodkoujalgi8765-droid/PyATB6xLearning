class MathClass:
    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b+c

t = MathClass()
#print(t.add(5,2))  #TypeError: MathClass.add() missing 1 required positional argument: 'c
print(t.add(1,2,3))
