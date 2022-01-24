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
    description="Flexgrid Pricing API",
    author_email="",
    url="",
    keywords=["Swagger", "Flexgrid Pricing API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Interface for performing evaluations of pricing algorithms  The credentials for the API are from the central DB can be obtained by the ICCS team of the [FlexGrid project](https://flexgrid-project.eu)  Use the central DB api defined at [https://db.flexgrid-project.eu/swagger/](https://db.flexgrid-project.eu/swagger/) for obtaining the objects for the requests (dr_prosumers, flex_request)
    """
)
