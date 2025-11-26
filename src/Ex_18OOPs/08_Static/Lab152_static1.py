# Static Methods
# A static method is a method that belongs to a
# class rather than an instance of the class.

class B:

    @staticmethod
    def sum(a,b):
        return a+b


t = B()
print(t.sum(1,2))

print(B.sum(1,2))

