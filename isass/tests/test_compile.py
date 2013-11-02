# -*- coding: utf-8 -*-
'''
Created on Nov 1, 2013

@author: vahid
'''
import unittest
import isass
import glob
import os
from StringIO import StringIO
import hashlib

class Test(unittest.TestCase):

    def testCompileString(self):

        sass = """
.page-footer .copy-right,
.page-footer .bottom
  display: block
  width:100%
  float: left
"""

        expected_res = """.page-footer .bottom, .page-footer .copy-right {
  display: block;
  width: 100%;
  float: left;
}"""          
        res = isass.compile(sass)
        self.assertEqual(res.strip(),expected_res.strip())
        
    def _get_file_md5(self,f):
        m = hashlib.md5()
        m.update(f.read())
        return m.hexdigest()
        
        
    def testCompileFile(self):
        test_files_dir =os.path.join(os.path.dirname(__file__),'test_files') 
        test_files = os.path.join(test_files_dir,'*.sass')
        expected_output_file = open( os.path.join(test_files_dir,'out.css'))
         
        
        input_files = [open(f) for f in glob.glob(test_files)]
        out =  StringIO()
        try:
            isass.compile_file(out, *input_files)
            out.seek(0)
#             expected_output_file.write(out.read())
#             return
            res_md5 = self._get_file_md5(out)
            expected_md5 = self._get_file_md5(expected_output_file)             
            self.assertEqual(res_md5, expected_md5)
            
            
        finally:
            for f in input_files:
                f.close()
            expected_output_file.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCompileString']
    unittest.main()