# isass

**isass** (Indented SASS) compiles [SASS-indented-syntax](http://sass-lang.com/documentation/file.INDENTED_SYNTAX.html) into CSS or SCSS. 

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

#### Line extensions

Lines ending with `,` will be continued to the next line:

    #container, #article_container, #sidebar_container,
    #footer_container, #useless_container
      background-color: #DDD

That first line is treated is one whole line:

    #container, #article_container, #sidebar_container #footer_container, #useless_container {
      background-color: #DDD; }

#### Comments

Comments are prefaced with `/*` and is implemented on a per-line basis:

    /* This is a comment
    /* This is another comment
    body
      /* Yep, a short width
      width: 50px 

Will give:

    /* This is a comment */
    /* This is another comment */
    body {
      /* Yep, a short width */
      width: 50px; }

#### Imports

A handy little command is `@import` that - surprise surprise - imports an external `.sass` file into the current `.sass` file.

So let's say you have a `night.sass`:

    body
      background-color: black
      color: white

Then in your file `style.sass`:

    @import night.sass

    #sunny-message
       background-color: white
       color: yellow

Which produces:

    body {
      background-color: #000000;
      color: #ffffff;
    }
    #sunny-message {
      background-color: #ffffff;
      color: #ffff00;
    }

`isass` looks for the filenames relative to the current working directory. Please don't abuse the imports, it doesn't check for circular imports - that would be your bad.


But of course you want to take advantage of the programmatic syntax extensions introduced by SASS. This will require that you pre-install the `PySCSS` module, and the compilation is then:

    import sassin

    s = '''
    @mixin box($width)
      width: $width px
    body
      @include box(500)
    '''

    print sassin.compile_with_scss(s)

#### Variable substitution

You can use variables, prefaced by a `$`:

    $highlight-color: #999
    #big-box
      border: 1px solid $highlight-color
    #message
      color: $highlight-color 

Which makes it much easier to pass colors around, as in the resultant CSS: 

    #big-box {
      border: 1px solid #999999;
    }
    #message {
      color: #999999;
    }

#### Expressions

Cobble together simple expressions:

    $big-width: 500
    #container
      width: $big-width px
    $panel-left
      float: left
      width: $big-width/2 px

And we get, in the CSS:

    #container {
      width: 500 px;
    }
    $panel-left {
      float: left;
      width: 250 px;
    }

Just beware that `/` will be intrepreted as a division expression, so if `/` appears in `url()` parameters, wrap it with quotation marks `""`.

#### Mix-ins with arguments

Mix-ins that group common elements, and can take arguments, which are prefaced by `@`:

    @mixin left($dist)
      float: left
      margin-left: -$dist
      width: $dist - 20
      padding-right: 20

    #sidebar
      @include left(200px) 

Gives:

    #sidebar {
      float: left;
      margin-left: -200px;
      width: 180px;
      padding-right: 20;
    }

#### Nesting

Handy nesting, and self reference `&` to save even more typing:

    #article
      a
        font:
          family: Garamond
        &:link
          text-decoration: none
        &:hover
          text-decoration: underline

Flattens out into:

    #article a {
      font-family: Garamond;
    }
    #article a:link {
      text-decoration: none;
    }
    #article a:hover {
      text-decoration: underline;
    }

#### Class Extensions

Extend a class with a new twist:

    #message
      border: 1px solid red

    #bad-message
      @extend #message
      background-color: red

Creates a similar class quite easily:

    #bad-message, #message {
      border: 1px solid #ff0000;
    }
    #bad-message {
      background-color: #ff0000;
    }



The canonical syntax reference is [sass-lang.com](http://sass-lang.com/guide)

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
    
 Watches for changes in source files, and automatically update output on any changes.
 
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
    
    

