# -*- coding: utf-8 -*-
'''
Created on Nov 1, 2013

@author: vahid
'''
import unittest
import os
import time
from isass import SassObserver


class TestWatchdog(unittest.TestCase):
    
    def setUp(self):
        self.watch_dir = os.path.join(os.path.dirname(__file__),'watch_dir')
        if not os.path.exists(self.watch_dir):
            os.mkdir(self.watch_dir)
        self.sass_file =  os.path.join(self.watch_dir,'00-towatch.sass')
        self.out_file  = os.path.join(self.watch_dir,'out.css')
        with open(self.sass_file,'w') as f:
            f.write("""
/* test sass file to watch
            """)

    def test(self):
        
        # removing output file to test
        if os.path.exists(self.out_file):
            os.remove(self.out_file)
            
        observer = SassObserver()
        observer.add_output(self.out_file, self.watch_dir)
        observer.start()
        # wait some moments to initialize observer thread
        time.sleep(.5)
        # append something to source file
        with open(self.sass_file,'a') as f:
            f.write("""
body
  background-color: #FFFFFF
""")

        # wait another moments to write the out file
        time.sleep(.5)
        self.assertTrue(os.path.exists(self.out_file))
        
        observer.stop()
        observer.join()
        
if __name__ == "__main__":
    unittest.main()        