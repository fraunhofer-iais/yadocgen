import click
import os
import sys
import pkgutil
import yaml
from bunch import Bunch, bunchify, unbunchify
from traceback import print_tb
from anytree import Node, RenderTree, Resolver, PreOrderIter


@click.group()
def cli():
    """ Yet Another Documentation Generator """
    pass


@cli.command
@click.option("--work-dir", envvar="YDG_WORK_DIR", default=".", help="yadocgen working directory (default: current directory)")
@click.option("--src-dir", envvar="YDG_SOURCE_DIR", default="src", help="directory that holds the source code of the project")
@click.option("--doc-dir", envvar="YDG_DOC_DIR", default="doc", help="directory that holds arbitrary documentation pages")
@click.option("--output", envvar="YDG_OUTPUT_DIR", default="sphinxdoc", help="directory for generated documentation files")
@click.option("--project", envvar="YDG_PROJECT_NAME", prompt="Project name", help="project name used in the documentation")
@click.option("--author", envvar="YDG_AUTHOR", prompt="Author", help="Name(s) of the documentation's author")
@click.option("--version", envvar="YDG_VERSION", prompt="Version", help="version (taken automatically from VERSION file)")
def initialize(work_dir, src_dir, doc_dir, output):
    """ Sets up the Sphinx documentation for a project. """

    # write yadoc config file
    CONFIG = Bunch(
        source_dir = src_dir,
        docs_dir = doc_dir,
        output_dir = output,
        sphinx_config = Bunch(
            project_name = "",
            copyright = "",
            author = "",
            version = "",
            add_paths = [src_dir]
            )
    )
    with open(os.path.join(project_dir, '.yadocgen'), "w") as f:
        yaml.dump(unbunchify(CONFIG), f)

    # create Sphinx config and directory structure
    


@cli.command()
@click.option("--overwrite", default=False, help="If set to True a pre-existing documentation directory will be overwritten (default: False)")
def generate(overwrite):
    """ Generates the documentation for a project. """
    with open(os.path.join(work_dir, '.yadocgen'), "r") as f:
        CONFIG = bunchify(yaml.full_load(f))

    # if overwrite option is set remove an existing output dir, quit otherwise
    if os.path.isdir(CONFIG.output_dir):
        if overwrite:
            # delte output dir
        else:
            print(f"WARNING: Output directory {CONFIG.output_dir} already exists and overwrite option is not set, exiting.")
            sys.exit(-1)

    generate_documentation(CONFIG)


