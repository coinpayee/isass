

__version__ = '0.1.1'

from .compiler import SassCompiler
from .watch import SassObserver

def get_css(sass, lib_dirs=None):
    c = SassCompiler(lib_dirs=lib_dirs)
    c.read_string(sass)
    return c.get_css()
    
def get_scss(sass, lib_dirs=None):
    c = SassCompiler(lib_dirs=lib_dirs)
    c.read_string(sass)
    return c.get_scss()



# live(outputs,lib_dirs=None)

# TODO: scripts watchdog


__all__ = ['__version__',
           'get_css',
           'get_scss',
           'SassCompiler',
           'SassObserver']
 

    