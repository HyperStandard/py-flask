__author__ = 'nonex_000'

class Link:
    """A simple link implementation"""

    def __init__(self, name, url):
        self._name = name
        self._url = url


    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

