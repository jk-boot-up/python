import requests
from requests import Response

class UrlCaller:

    def request(self, url):
        x = requests.get(url)
        print(type(x))
        return x.status_code
