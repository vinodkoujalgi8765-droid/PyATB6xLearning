from unittest import TestCase


class TestSuite:
    def info(self):
        print("This is Grand Father")

class BaseTest(TestSuite):
    def setup(self):
        print("Basetest - Father")

class UItest(BaseTest):
    def test_run(self):
        self.info()
        self.setup()

t = UItest()
t.test_run()
