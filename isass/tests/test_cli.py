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
        self.thisdir = os.path.join(os.path.dirname(__file__))
        self.input_file = os.path.abspath(os.path.join(self.thisdir, "colors.sass"))
        self.output_file = os.path.abspath(os.path.join(self.thisdir, "styles.css"))
        self.cmd = os.path.abspath(os.path.join(self.thisdir, "../../scripts/isass"))
        self.index_sass_file = os.path.abspath(os.path.join(self.thisdir, "index.sass"))
        
    def test_std_in_out(self):
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
        
    def test_input_output_files(self):
        """
        isass -o out.css file1
        """
        Popen([self.cmd,'-o',self.output_file, self.input_file]).wait()
        with open(self.output_file) as of:
            o = of.read()
            
        expected_result='''
body {
  background-color: #EEE; } '''
        self.assertEqual(purifylines(expected_result), purifylines(o))
        

    def test_scss(self):
        """
        isass --scss file1
        """
        p = Popen([self.cmd,'--scss', self.input_file],stdout=PIPE)
        ret_code = p.wait()
        self.assertEqual(ret_code,0)
        if ret_code == 0:
            o = p.stdout.read()
            
        expected_result='''
/* http://colorschemedesigner.com/#3.61Eqarrxnho */
$link-color : #333333;
$back-color: #333333;
$primary-color: #22598e;
body {
  background-color: #EEE; }'''
        self.assertEqual(purifylines(expected_result), purifylines(o))

    def test_lib_dirs(self):
        """
        isass -l . file1
        """
        p = Popen([self.cmd, '--lib-dir', self.thisdir, self.index_sass_file],stdout=PIPE)
        ret_code = p.wait()
        self.assertEqual(ret_code,0)
        if ret_code == 0:
            o = p.stdout.read()
            
        expected_result='''body {
  background-color: #EEE; }

  #divroot {
    color: #22598e; }'''
        self.assertEqual(purifylines(expected_result), purifylines(o))
        
        
if __name__ == "__main__":
    unittest.main()