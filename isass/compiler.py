# -*- coding: utf-8 -*-
'''
Created on:    Nov 1, 2013
@author:        vahid
'''

import sassin

def compile(sass_string):
    return sassin.compile(sass_string)

def compile_file(output_file, *input_files):
    inp = ''
    for input in input_files:
        inp += input.read()
    res = compile(inp)
    output_file.write(res)
