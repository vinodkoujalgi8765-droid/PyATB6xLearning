class APIBase:
    def api_auth(self):
        print("Authentication API")

class DBBase:
    def dbconnection(self):
        print("DB connection")

class testhybdrid(APIBase,DBBase):
    def run(self):
        self.api_auth()
        self.dbconnection()
        print("Running Test case")

t = testhybdrid()
t.run()