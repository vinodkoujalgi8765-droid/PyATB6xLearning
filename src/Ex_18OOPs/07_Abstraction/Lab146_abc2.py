from abc import ABC,abstractmethod


class Father(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def loan(self):
        print("who can pay loan")


class Amit(Father):

    def loan(self):
        print("Paying loan",self.name)

t =Amit("Vinod")
t.loan()