class MathOperation:

    def div(self,a,b):
        return a/b

    @staticmethod
    def summ(a,b):
        return a+b


t = MathOperation()
print(t.div(10,2))
print(t.summ(10,2))  #this is not reccomanded
print(MathOperation.summ(10,2))  # this is best practice
