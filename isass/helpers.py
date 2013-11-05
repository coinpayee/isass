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