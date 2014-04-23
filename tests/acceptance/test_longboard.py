"""Acceptance tests for the Longboard API."""


import os
import unittest

import longboard

from tests.utils import TestingServer


TEST_SITE_PATH = os.path.join(os.path.dirname(__file__), 'site')


class LongboardTest(object):

    """Test functionality that should work in all browsers.

    These tests are meant to be mixed-in to classes with the browser_class
    attribute defined.
    """

    @classmethod
    def setUpClass(cls):
        cls.server = TestingServer(TEST_SITE_PATH)
        cls.server.start()
        cls.browser = cls.browser_class()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.server.stop()

    def test_visiting_page_to_inspect_elements(self):
        url = self.server.make_url('/')

        self.browser.visit(url)
        heading = self.browser.find('h1')

        self.assertEqual(heading.text, "It Works!")


class ChromeTest(LongboardTest, unittest.TestCase):

    browser_class = longboard.Chrome
