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

The canonical syntax reference is part of the [Ruby Sass documentation](http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html#css_extensions)

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
      
      
#### CLI examples:

 Read SASS from sources.sass , and writes produced CSS into standard output
 
    $ isass < source.sass
    $ isass < source.sass > out.css

 Read SASS from all *.sass files in sources, extra-sources dirs and myfile.sass , then writes produced CSS into standard output
 
    $ isass sources/ extra-sources/ myfile.sass > out.css
    
 You can use -o or --output options to write the generated result into specific file.
 
    $ isass -o out.css sources/

 Generates SCSS instead of CSS, from SASS file
 
    $ isass -c < source.sass
    
 Watch for changes in source files, and automatically update output on any changes.
 
    $ isass -wo out.css source-dir/
    

### Watchdog

You can use watchdog by CLI that mentioned above, Or from code:

	from isass import SassObserver
	
    observer = SassObserver()    
    observer.add_output('style.css', dirs='my-source-dir', lib_dirs='sass-libs')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() 
    
    

