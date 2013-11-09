# -*- coding: utf-8 -*-
'''
Created on:    Nov 10, 2013
@author:        vahid
'''
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from isass import SassCompiler
import os.path
import glob

def split_paths(p):
    if isinstance(p,basestring):
        res = p.split(',')
    else:
        res = p
    return [os.path.abspath(i.strip()) for i in res ]

def distinct(l):
    return list(set(l))

class IsassEventHandler(FileSystemEventHandler):
    extension = '.sass'
    def __init__(self,outfile,dirs,lib_dirs = None):
        self.outfile = outfile
        self.dirs = dirs
        self.lib_dirs = lib_dirs
        super(FileSystemEventHandler, self).__init__()
        
    def _get_source_files(self):
        source_files = []
        for d in self.dirs:
            for f in glob.iglob(os.path.join(d,'*%s' % self.extension)):
                source_files.append(os.path.abspath(f))
        return sorted(distinct(source_files))
        
    def write_out(self):
        compiler = SassCompiler(lib_dirs=self.lib_dirs)
        for sf in self._get_source_files():
            compiler.read_file(sf)
        with open(self.outfile,'w') as of:
            of.write(compiler.get_css())
        
        
    def on_any_event(self,event):
        paths = []
        if hasattr(event,'src_path'):
            paths += split_paths(event.src_path)
        if hasattr(event,'dest_path'):
            paths += split_paths(event.dest_path)
        
        paths = [p for p in paths if p.endswith(self.extension)]
        if len(paths):
            # One or more sass file changes, trying to regenerate output
            self.write_out()


class SassObserver(Observer):
    
    def add_output(self,outfile,dirs=None,lib_dirs=None):
        dirs = distinct(split_paths(dirs))
        handler = IsassEventHandler(outfile, dirs,lib_dirs=lib_dirs)
        handler.write_out()
        for d in dirs:
            self.schedule(handler, d, recursive=True)
