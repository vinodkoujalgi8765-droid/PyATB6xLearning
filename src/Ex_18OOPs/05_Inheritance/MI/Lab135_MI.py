class Father1:
    def money(self):
        print("Money from F1")

class Father2:
    def money(self):
        print("Money from F2")

class Son(Father1, Father2):
    def party(self):
        self.money()

class Daughter(Father2, Father1):
    def party(self):
        self.money()
s1 = Son()
s1.party()
d1 = Daughter()
d1.party()
