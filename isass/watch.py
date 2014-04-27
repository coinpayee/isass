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
from isass.manifest import Manifest
import sys


class IsassEventHandler(FileSystemEventHandler):
    extension = '.sass'
    def __init__(self,outfile,dirs,files=None,lib_dirs = None):
        self.outfile = outfile
        self.dirs = dirs
        self.lib_dirs = lib_dirs if lib_dirs else []
        self.source_files = get_source_files(self.dirs,extension=self.extension)
        if files:
            self.source_files += files
        super(FileSystemEventHandler, self).__init__()

    def write_out(self):
        try:
            lib_dirs = get_source_dirs(self.dirs)
            if self.lib_dirs:
                lib_dirs += self.lib_dirs
            lib_dirs = distinct(lib_dirs)

            compiler = SassCompiler(lib_dirs=lib_dirs)
            for sf in self.source_files:
                print "Reading %s" % os.path.abspath(sf)
                compiler.read_file(sf)

            print "Writing %s" % os.path.abspath(self.outfile)
            with open(self.outfile, 'w') as of:
                of.write(compiler.get_css())
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback)

    def on_any_event(self, event):
        paths = []
        if hasattr(event, 'src_path'):
            paths += split_paths(event.src_path)
        if hasattr(event, 'dest_path'):
            paths += split_paths(event.dest_path)

        changed = False
        for p in paths:
            if p in self.source_files:
                changed = True
                break

            if os.path.abspath(os.path.dirname(p)) in self.lib_dirs and p.endswith(self.extension):
                changed = True
                break


        #paths = [p for p in paths if p.endswith(self.extension)]

        if changed:
            # One or more sass file changes, trying to regenerate output
            self.write_out()


class SassObserver(Observer):

    def add_output(self, outfile, dirs=None, files=None, lib_dirs=None):
        dirs = distinct(split_paths(dirs))

        handler = IsassEventHandler(outfile, dirs, files=files, lib_dirs=lib_dirs)
        watch_dirs = list(dirs)

        if lib_dirs:
            watch_dirs += split_paths(lib_dirs)
        if files:
            watch_dirs += split_paths([os.path.dirname(p) for p in files])

        handler.write_out()
        for d in watch_dirs:
            self.schedule(handler, d, recursive=False)

    def add_manifest(self,manifest):
        manifest = Manifest(manifest)
        for taskname in manifest.get_task_names():
            task = manifest[taskname]
            dirs = []
            files = []
            for s in task.sources:
                if os.path.isfile(s):
                    files.append(s)
                else:
                    dirs.append(s)
            self.add_output(outfile=task.output, dirs=dirs, files = files, lib_dirs=task.libdirs)
