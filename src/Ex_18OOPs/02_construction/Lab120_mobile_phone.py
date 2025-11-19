class MobilePhone:
    Model = None

    def talk(self,Model = "i5"):
        print("talk",Model)
        print("talk2",self.Model)

    def __init__(self):
        print("I am constructor and by defalut call when obj is created")


iphone = MobilePhone()
iphone.talk()

sam = MobilePhone()
sam.talk(Model = "S22")
