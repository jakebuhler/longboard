"""Development commands for the Longboard project."""


import os
import sys
import unittest


# Append the repository directory to the path
sys.path.append(os.path.dirname(__file__))


def test(scope='all', verbosity=1):
    if scope in ('acceptance', 'all'):
        _run_tests('tests.acceptance', verbosity)
    if scope in ('integration', 'all'):
        _run_tests('tests.integration', verbosity)
    if scope in ('unit', 'all'):
        _run_tests('tests.unit', verbosity)


def _run_tests(test_module, verbosity):
    _print_header('Running ' + test_module)
    suite = unittest.defaultTestLoader.discover(test_module)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

def _print_header(message):
    border = '#' * len(message)
    print('')
    print(border)
    print(message)
    print(border)
