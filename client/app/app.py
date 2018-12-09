from app.client import Client


class App:
    def __init__(self, client=None):
        self.client = client or Client()

    def run(self, **kwargs):
        self.client.communicate()
