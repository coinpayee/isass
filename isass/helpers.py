# -*- coding: utf-8 -*-
'''
Created on:    Nov 2, 2013
@author:        vahid
'''
import os
import glob

def get_source_files(sources):
    source_files = []
    for s in sources:
        p = os.path.abspath(s)
        if os.path.isfile(p):
            source_files.append(p)
        elif os.path.isdir(p):
            for _f in glob.iglob(os.path.join(p,'*.sass')):
                source_files.append(os.path.abspath(_f))
    return list(set(source_files))

def get_source_dirs(sources):
    source_dirs = []
    for s in sources:
        p = os.path.abspath(os.path.dirname(s))
        if os.path.isdir(p):
            source_dirs.append(p)
            
    return list(set(source_dirs))

# def _get_file(f,mode='r'):
#     if isinstance(f, basestring):
#         return open(f,mode)
#     else:
#         return f
#         
# 
# def compile_file(output_file,lib_dirs=None,*input_files):
#     inp = ''
#     for input in input_files:
#         with _get_file(input) as f: 
#             inp += f.read()
#     res = compile(inp,lib_dirs=lib_dirs)
#     with _get_file(output_file,mode='w') as fw:
#         fw.write(res)