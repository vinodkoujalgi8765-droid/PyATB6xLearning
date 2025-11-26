from abc import ABC, abstractmethod

class GearBox(ABC):
    @abstractmethod
    def setGear(self):
        a = "gear1"
        print("only one gear here",a)

class Engine:
    @abstractmethod
    def start(self):
        print("starting Engine")

    @abstractmethod
    def stop(self):
        print("stopping Engine")

class Car(Engine,GearBox):
    pass
    # def start(self):
    #     print("car started")

    def stop(self):
        print("car stopped")

    def setGear(self):
        b= "gear2"
        print("Gear box is ready")

    def drive(self):
        self.start()  ##If class has not inherit ABC then method can be accessible from anywhere
        self.stop()
        self.setGear()
        #self.drive()  #error - repeated calling same method

t = Car()
t.drive()