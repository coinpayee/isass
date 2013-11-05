
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileMovedEvent,\
    FileCreatedEvent #, FileDeletedEvent, FileModifiedEvent
import helpers
import compiler
import os
import time
import traceback

def write_out(outfile,source_dirs,lib_dirs):
    try:
        source_files = helpers.get_source_files(source_dirs)
        compiler.compile_file(outfile, lib_dirs=lib_dirs,*source_files)
    except:
        traceback.print_exc()

class IsassEventHandler(FileSystemEventHandler):
    def __init__(self,outfile,source_dirs,lib_dirs):
        self.outfile = outfile
        self.source_dirs = source_dirs
        self.lib_dirs = lib_dirs
        super(FileSystemEventHandler, self).__init__()
        
    def on_any_event(self,event):
        paths = []
        if hasattr(event,'src_path'):
            paths.append(os.path.abspath(event.src_path))
        if hasattr(event,'dest_path'):
            paths.append(os.path.abspath(event.dest_path))
        
        for p in paths:
            if isinstance(event,FileCreatedEvent) or \
                p in self.source_files or \
                os.path.dirname(p) in self.lib_dirs:
                
                source_files = helpers.get_source_files(self.source_dirs)
                compiler.compile_file(self.outfile, lib_dirs=self.lib_dirs,*source_files)
                break



def live(outputs,lib_dirs=None):
    for outfile, source_dirs in outputs:
        write_out(outfile, source_dirs, lib_dirs)
        
    
    
        






def live(outputs,lib_dirs=None):
    
    if lib_dirs:
        search_dirs = [sd[:-1] if sd.endswith('/') else sd for sd in lib_dirs]
        
    for outfile, source_dirs in outputs:
        source_files = helpers.get_source_files(source_dirs)
        compiler.compile_file(outfile, lib_dirs=search_dirs,*source_files)
        
        
    
            


    source_files = helpers.get_source_files(sources)
    watch_dirs = [os.path.dirname(f) for f in source_files] + search_dirs
    watch_dirs = list(set(watch_dirs))
    recursive = True

    event_handler = IsassEventHandler(source_files, search_dirs)
    observer = Observer()
    for d in watch_dirs:
        observer.schedule(event_handler, path=d, recursive=recursive)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()    
