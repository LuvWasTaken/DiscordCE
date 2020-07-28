import json
import http.client

class API:

    def __init__(self):
        self.jsonData = str()
        self.rates = str()

    def request(self, base):
        conn = http.client.HTTPSConnection("api.exchangeratesapi.io")
        conn.request("GET", "/latest?base=%s" % (base))
        response = conn.getresponse()

        self.jsonData  = json.loads(response.read().decode())
        self.rates = self.jsonData['rates']

        return self.rates
