class BaseCounter:
    counter = 0

    @staticmethod
    def testrun():
        BaseCounter.counter = BaseCounter.counter + 1
        print(BaseCounter.counter,"TetsExecution")

BaseCounter.testrun()
BaseCounter.testrun()
BaseCounter.testrun()

