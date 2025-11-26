class TestCounter:
    counter = 5

    def __init__(self,name):
        self.name = name
        print(TestCounter.counter,self.name)
        TestCounter.counter = TestCounter.counter + 1
        print(self.counter,self.name)
        print(TestCounter.counter,self.name)
        print("#################")


t = TestCounter("vinod")
t2 = TestCounter("koujalgi")
print(id(t))
print(id(t2))


