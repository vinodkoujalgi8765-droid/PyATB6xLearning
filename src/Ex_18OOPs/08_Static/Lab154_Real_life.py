class ExcelReader:

    @staticmethod
    def readExcelfile():
        print("reading from Excel file")

class MYSQLDBconnect:

    @staticmethod
    def readMYSQLdb():
        print("reading from MySQLdb")

class TC1:
    def runTC(self):
        ExcelReader.readExcelfile()
        MYSQLDBconnect.readMYSQLdb()
        print("tc1 Done")

class TC2:

    def runTC(self):
        ExcelReader.readExcelfile()
        MYSQLDBconnect.readMYSQLdb()
        print("tc2 Done")

tc1 = TC1()
tc1.runTC()

tc2 = TC2()
tc2.runTC()


