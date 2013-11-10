# isass

**isass** (Indented SASS) compiles [SASS-indented-syntax](http://sass-lang.com/documentation/file.INDENTED_SYNTAX.html) 
into CSS or SCSS. 


**isass** uses [pyScss](https://github.com/Kronuz/pyScss) as its internal compiler, to compile *scss* to *css*. So **isass** is a *sass* to *scss* convertor, including: 

* A **watchdog** to automatically reproduce output.css when one or more source files are changed.
* A **Command Line Interface**


## Installation

Latest stable version:

    $ pip install isass
    # or
    $ easy_install isass

Development version:

    pip install git+git@github.com:pylover/isass.git

From source:

    $ cd source_dir
    $ python setup.py install
    
    
