# -*- coding: utf-8 -*-
'''
Created on:    Nov 1, 2013
@author:        vahid
'''

from setuptools import setup

description = \
"""`isass` is a Python compiler for indented-SASS-syntax
files into CSS stylesheets. The full syntax requires `PySCSS`, but a limited syntax
compiles straight to CSS. 

Docs at http://github.com/pylover/isass.
"""

setup(
    name='isass',
    version='0.1a',
    author='Vahid Mardani',
    author_email='vahid.mardani@gmail.com',
    url='http://github.com/pylover/isass',
    description='compiles indented-SASS-syntax to CSS stylesheets',
    long_description=description,
    license='MIT',
    install_requires=['pyscss>=1.2.0',
                      'sassin>=0.9',
                      'watchdog>=0.6.0'],
    packages=['isass'],
    scripts=['scripts/isass'],
)