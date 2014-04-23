"""Longboard DOM elements."""


class Element(object):

    def __init__(self, element):
        self._element = element

    @property
    def text(self):
        return self._element.text
