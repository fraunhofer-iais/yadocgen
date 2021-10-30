___NOTE:___ Because the pip guys broke pip, it gives some error [about version in filename and metadata being inconsisten](https://github.com/pypa/pip/issues/9203) (it's closed but it still doesn't work!) and I'm not willing to dive into this because I regard my time to valuable for it:  __download the source repository and install locally!__

![yaDocGen Logo](doc/img/ydg_logo.png)

![Publish action badge](https://github.com/fraunhofer-iais/yadocgen/actions/workflows/main.yml/badge.svg)

This is a documentation generator that makes effortlessly accessible what I like and use often from Sphinx. 

Highlights

- write your documentation pages in markdown
- use [numpy style](https://numpydoc.readthedocs.io/en/latest/format.html) docstrings
- use your README.md as the welcome page
- use all the goodness that [Sphinx](https://www.sphinx-doc.org/) and [myst_parser](https://myst-parser.readthedocs.io/en/latest/index.html) provide
    - `$` and `$$` math environments
    - (literature) references
    - figures and tables
    - definition block
    - footnotes
    - admonitions

## Installation

The tool is available as a package on PyPI. You can install it using pip

```shell
pip install yadocgen

```

## Usage

Initialize the project using the `init` subcommand in the root directory of your repo and answer the questions
```shell
$ cd project-dir
$ yadocgen init

Project name: Test project
Author: Ben
Version: 1.0
Sphinx template [karma_sphinx_theme]: 
Welcome page [README.md]: 
Source code directory [src]: 
Documentation directory [doc]: 
Output directory [sphinx]: 
```

Once initialized you can (re-)generate your documentation using the `generate` subcommand and then use the Sphinx Makefile to compile it
```shell
$ yadocgen generate
$ cd sphinx
$ make html

```

..then you will find your documentation in `sphinx/build`.
