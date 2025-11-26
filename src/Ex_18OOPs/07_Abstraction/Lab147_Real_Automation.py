from abc import ABC, abstractmethod

class BrowseManager(ABC):
    name = "Vinod"
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Browse manager is stopped")

class ChromeBrowser(BrowseManager):
    def start(self):
        print("chrome browser is started")

t = ChromeBrowser()
t.start()
t.stop()
print(t.name)
tt = BrowseManager()
print(tt.name)




