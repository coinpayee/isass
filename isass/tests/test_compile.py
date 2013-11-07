# -*- coding: utf-8 -*-
'''
Created on Nov 1, 2013

@author: vahid
'''
import unittest
import isass


class Test(unittest.TestCase):

    def testCompileString(self):

        sass = """
@import colors.sass

.page-footer .copy-right,
.page-footer .bottom
  display: block
  width:100%
  float: left
  color: $link-color
"""

        expected_res = """.page-footer .bottom, .page-footer .copy-right {
  display: block;
  width: 100%;
  float: left;
  color: #333333;
}"""          
        res = isass.get_css(sass)
        self.assertEqual(res.strip(),expected_res.strip())
        

            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCompileString']
    unittest.main()