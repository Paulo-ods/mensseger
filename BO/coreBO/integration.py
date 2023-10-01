import requests


class IntegrationBO:

    def __init__(self, url=None, body=None, headers=None, request=None):
        self.url = url
        self.body = body
        self.headers = headers
        self.request = request
        self.response = None

    def get(self):
        self.response = requests.get(self.url, data=self.body, headers=self.headers)

    def post(self):
        self.response = requests.post(self.url, data=self.body, headers=self.headers)


