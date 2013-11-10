# -*- coding: utf-8 -*-
'''
Created on Nov 1, 2013

@author: vahid
'''
import unittest
import isass
import os.path
from nose.tools import raises
from isass.helpers import purifylines



class TestCompiler(unittest.TestCase):
    
    def setUp(self):
        self.lib_dirs = [os.path.dirname(__file__)]

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

        res = isass.get_css(sass,lib_dirs=self.lib_dirs)
        self.assertTrue(len(purifylines(res)) > 0)
        
    def test_indent(self):
        in_sass = """
a
  font:
      family: Helvetica
    """
        out_css = isass.get_scss(in_sass)
        out_lines = purifylines(out_css)
        test_css = """
a {
  font: {
      family: Helvetica; } }
    """
        test_lines = purifylines(test_css)
        self.assertEqual(out_lines, test_lines)

    def test_comment(self):
        in_sass = """
/* comment
body
  /* comment
  background-color: white
    """
        out_css = isass.get_scss(in_sass)
        out_lines = purifylines(out_css)
        test_css = """
/* comment */
body {
  /* comment */
  background-color: white; }
    """
        test_lines = purifylines(test_css)
        self.assertEqual(out_lines, test_lines)

    def test_line_continuation(self):
        in_sass = """
#container, #article_container, 
#sidebar_container,
#footer_container, #useless_container
  background-color: #DDD
    """
        out_css = isass.get_css(in_sass)
        out_lines = purifylines(out_css)
        self.assertTrue(len(out_lines) > 0 )

    def test_import(self):
        in_sass = """
@import colors.sass
    """
        out_css = isass.get_css(in_sass,lib_dirs=self.lib_dirs)
        out_lines = purifylines(out_css)
        test_css = """
body {
  background-color: #EEE;
}
    """
        test_lines = purifylines(test_css)
        self.assertEqual(out_lines, test_lines)

    @raises(ValueError)
    def test_exception_for_misaligned_identation(self):
        in_sass = """
  a
    font:
        family: Helvetica
      weight: bold
      """
        _out_css = isass.get_css(in_sass)

    @raises(ValueError)
    def test_exception_for_margin_identation(self):
        in_sass = """
    a
      font:
        family: Helvetica
   #new_class
      """
        _out_css = isass.get_css(in_sass)        
            

if __name__ == "__main__":
    unittest.main()