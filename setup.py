"""
Longboard
---------

Longboard is a high-level API for driving browser interactions using
Selenium.
"""


from setuptools import setup


setup(
    name='longboard',
    version='0.0.1',
    packages=['longboard'],

    install_requires=['Selenium'],

    # PyPI metadata
    author='Jacob R. Rothenbuhler',
    author_email='jake@encodify.net',
    description="Selenium as you'd like it to be",
    long_description=__doc__,
    license='MIT',
    keywords='testing',
    url=''
)
