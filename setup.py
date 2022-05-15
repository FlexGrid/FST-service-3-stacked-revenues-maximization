# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Flexgrid Stacked Revenues API",
    author_email="",
    url="",
    keywords=["Swagger", "Flexgrid Stacked Revenues API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Interface for obtaining optimal bids in different markets, based on flex assets that are available.   The credentials for the API are from the central DB can be obtained by the ICCS team of the [FlexGrid project](https://flexgrid-project.eu)
    """
)
