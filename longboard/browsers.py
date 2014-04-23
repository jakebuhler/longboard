"""Longboard browsers."""


from selenium import webdriver

from longboard.elements import Element


class Browser(object):

    def __init__(self):
        self._driver = self.driver_class()

    def visit(self, url):
        self._driver.get(url)

    def close(self):
        self._driver.close()

    def find(self, tag):
        element = self._driver.find_element_by_tag_name(tag)
        return Element(element)


class Chrome(Browser):

    driver_class = webdriver.Chrome
