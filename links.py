__author__ = 'nonex_000'

class Link:
    """A simple link implementation"""

    def __init__(self, name, url, image=None):
        self._name = name
        self._url = url
        if image is None:
            self._image = ""
        else:
            self._image = image


    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def image(self):
        return self._image