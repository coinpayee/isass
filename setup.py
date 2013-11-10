# -*- coding: utf-8 -*-
'''
Created on:    Nov 1, 2013
@author:        vahid
'''

from setuptools import setup
import os.path
import re

# reading isass version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'isass', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

description = \
"""`isass` is a Python compiler for indented-SASS-syntax
files into CSS stylesheets. The full syntax requires `PySCSS`, but a limited syntax
compiles straight to CSS. 

Docs at http://github.com/pylover/isass.
"""


setup(
    name='isass',
    version=package_version,
    author='Vahid Mardani',
    author_email='vahid.mardani@gmail.com',
    url='http://github.com/pylover/isass',
    description='compiles indented-SASS-syntax to CSS stylesheets',
    long_description=description,
    license='MIT',
    install_requires=['pyscss>=1.2.0',
                      'watchdog>=0.6.0'],
    packages=['isass'],
    scripts=['scripts/isass'],
)