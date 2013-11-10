# -*- coding: utf-8 -*-    
'''
Created on:    Nov 10, 2013
@author:        vahid
'''

import unittest
import os.path
from isass.helpers import purifylines
from subprocess import Popen, PIPE    

class TestCLI(unittest.TestCase):
    
    def setUp(self):
        self.input_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "colors.sass"))
        self.cmd = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../scripts/isass"))
        
    def test_std_in(self):
        """
        isass < file.sass
        """
        
        # feed standard input
        with open(self.input_file) as input_file:
            p = Popen([self.cmd], stdin=input_file, stdout=PIPE)
            ret_code = p.wait()
            self.assertEqual(ret_code,0)
            if ret_code == 0:
                o = p.stdout.read()
                
        expected_result='''
body {
  background-color: #EEE; } '''
        self.assertEqual(purifylines(expected_result), purifylines(o))
        
if __name__ == "__main__":
    unittest.main()