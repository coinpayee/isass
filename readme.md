# isass

**isass** (Indented SASS) compiles [SASS-indented-syntax](http://sass-lang.com/documentation/file.INDENTED_SYNTAX.html) 
into CSS or SCSS. 

    import isass
    
    sass = '''
    body
      width: 500px
    '''
    
    print isass.get_css(sass)
    print isass.get_scss(sass)


**isass** uses [pyScss](https://github.com/Kronuz/pyScss) as its internal compiler, to compile *scss* to *css*. So **isass** is a *sass* to *scss* convertor, including: 

* [All](#syntax-reference) pyScss [features](https://github.com/Kronuz/pyScss#features) are supported
* A [**Command Line Interface**](#command-line-interface)
* A [**Watchdog**](#watchdog) to automatically reproduce output.css when one or more source files are changed.



### Installation

Latest stable version:

    $ pip install isass
    # or
    $ easy_install isass

Development version:

    pip install git+git@github.com:pylover/isass.git

From source:

    $ cd source_dir
    $ python setup.py install
    
    
### Syntax Reference

The canonical syntax reference is part of the [Ruby Sass documentation](http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html)

### Command Line Interface

    $ isass --help

    usage: isass [-h] [-o OUTPUT] [-c] [-l [LIB_DIRS]] [-e [EXTENSION]] [-w]
                 [sources [sources ...]]
    
    isass compiles SASS-indented-syntax into CSS or SCSS.
    
    positional arguments:
      sources               Source files or directories to process. default:
                            standard input. example: `./*.sass` or `.`
    
    optional arguments:
      -h, --help                                show this help message and exit
      -o OUTPUT, --output OUTPUT                Output file. default: standard output
      -c, --scss                                Skip scss compilation, just return scss contents.
      -l [LIB_DIRS], --lib-dir [LIB_DIRS]       Library dir to search for @imports.
      -e [EXTENSION], --extension [EXTENSION]   Search for this file extension.
      -w, --watch                               Watch for source modifications, and update output.


### Watchdog


