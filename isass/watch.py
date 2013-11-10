# -*- coding: utf-8 -*-
'''
Created on:    Nov 10, 2013
@author:        vahid
'''
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from isass.helpers import get_source_dirs,get_source_files,distinct,split_paths
from isass import SassCompiler
import os.path


class IsassEventHandler(FileSystemEventHandler):
    extension = '.sass'
    def __init__(self,outfile,dirs,lib_dirs = None):
        self.outfile = outfile
        self.dirs = dirs
        self.lib_dirs = lib_dirs
        super(FileSystemEventHandler, self).__init__()
        
    def write_out(self):
        lib_dirs = get_source_dirs(self.dirs)
        if self.lib_dirs:
            lib_dirs += self.lib_dirs
        lib_dirs = distinct(lib_dirs)
        
        compiler = SassCompiler(lib_dirs=lib_dirs)
        for sf in get_source_files(self.dirs,extension=self.extension):
            print "Reading %s" % os.path.abspath(sf)
            compiler.read_file(sf)
            
            
        print "Writing %s" % os.path.abspath(self.outfile)
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
