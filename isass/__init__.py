

__version__ = '0.1a'
from .compiler import css_from_sass,scss_from_sass

get_css = css_from_sass
get_scss = scss_from_sass


# live(outputs,lib_dirs=None)


__all__ = ['__version__',
           'get_css',
           'css_from_sass',
           'get_scss',
           'scss_from_sass']
 

    