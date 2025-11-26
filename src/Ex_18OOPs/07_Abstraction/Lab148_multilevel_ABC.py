from abc import ABC, abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def readfromexcel(self):
        print("readfromexcel from ABC")

class Browser(ExcelReader):
    a = "vinod"
    @abstractmethod
    def startbrowser(self):
        print("startbrowser from ABC")

    @abstractmethod
    def stopbrowser(self):
        print("stopbrowser from ABC")

class TC1(Browser):
    def startbrowser(self):
        print('start')

    def stopbrowser(self):
        print('stop')

    def readfromexcel(self):
        print('readfromexcel is ready')

    def runTC(self):
        self.startbrowser()
        self.stopbrowser()
        self.readfromexcel()

t = Browser()
print(t.a)
#t.stopbrowser()

# e = ExcelReader()
# e.readfromexcel()

