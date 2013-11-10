# -*- coding: utf-8 -*-
'''
Created on:    Nov 10, 2013
@author:        vahid
'''

import unittest
import os.path
import sys
import isass    

class TestCLI(unittest.TestCase):
    
    def setUp(self):
        self.cmd = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../scripts/isass"))
        
    def test_std_in(self):
        """
        isass < file.sass
        """
        
        
    