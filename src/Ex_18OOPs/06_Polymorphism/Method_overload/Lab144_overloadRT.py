class Browser:
    def make_http_request(self,url):
        print("Making HTTP request without authentication",url)

    def make_http_request(self,url,auth=None):
        print("Making HTTP request without authentication",url,auth)

t = Browser()
t.make_http_request("http://www.python.org")
#output -> Making HTTP request without authentication http://www.python.org None