class Bank:

    def __init__(self,account,balance):
        self.balance = balance
        self.__account_number=account



    def deposite(self,amount):
        self.balance = self.balance + amount

    def show_account(self,name):
        if name == "vinod":
            print(name, "your account number is ",self.__account_number)
        else:
            print("wrong person")
        self.__IFSCcode = "BANK001"
        print("IFSC code is ",self.__IFSCcode)

p1 = Bank("123456789",100)
p1.show_account("mina")
p1.deposite(500)
print(p1.balance)