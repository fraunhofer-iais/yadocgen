import click
import os
from os import path
import sys
import pkgutil
import yaml
import datetime
from jinja2 import Environment, PackageLoader
from bunch import Bunch, bunchify, unbunchify
from traceback import print_tb
from anytree import Node, RenderTree, Resolver, PreOrderIter

from yadocgen.generator import generate_documentation

# include for example purposes
from yadocgen.example import foo


@click.group()
def cli():
    """Yet Another Documentation Generator"""
    print("yaDocGen v0.1.5")


@cli.command()
@click.option(
    "--work-dir",
    envvar="YDG_WORK_DIR",
    default=".",
    help="yadocgen working directory (default: current directory)",
)
@click.option(
    "--name",
    envvar="YDG_PROJECT_NAME",
    prompt="Project name",
    help="project name used in the documentation",
)
@click.option(
    "--author",
    envvar="YDG_AUTHOR",
    prompt="Author",
    help="Name(s) of the documentation's author",
)
@click.option(
    "--version",
    envvar="YDG_VERSION",
    prompt="Version",
    help="version (taken automatically from VERSION file if it exists)",
)
@click.option(
    "--theme",
    default="karma_sphinx_theme",
    envvar="YDG_THEME",
    prompt="Sphinx template",
    help="Sphinx theme to use (default: karma)",
)
@click.option(
    "--welcome",
    default="README.md",
    envvar="YDG_WELCOME_PAGE",
    prompt="Welcome page",
    help="File to use a welcome page of the documentation (default: ./README.md)",
)
@click.option(
    "--src-dir",
    envvar="YDG_SOURCE_DIR",
    default="src",
    prompt="Source code directory",
    help="directory that holds the source code of the project",
)
@click.option(
    "--doc-dir",
    envvar="YDG_DOC_DIR",
    default="doc",
    prompt="Documentation directory",
    help="directory that holds arbitrary documentation pages",
)
@click.option(
    "--output",
    envvar="YDG_OUTPUT_DIR",
    default="sphinx",
    prompt="Output directory",
    help="directory for generated documentation files",
)
def init(work_dir, src_dir, doc_dir, output, name, author, version, theme, welcome):
    r"""Initialize yadocgen for a project.

    This function takes the parameters, either from command line, prompt or
    environment variables and creates the necessary directories and the
    configuration file.

    Parameters:
    -----------
    work_dir
    src_dir
    doc_dir
    output
    name
    author
    version
    theme
    welcome

    """

    # build copyright string
    date = datetime.date.today()
    year = date.strftime("%Y")
    copyright = f"{author} {year}"

    if doc_dir == "" or doc_dir.lower() == "none":
        doc_dir = None

    if src_dir == "" or src_dir.lower() == "none":
        src_dir = None

    # write yadocgen config file
    CONFIG = Bunch(
        src_dir=src_dir,
        doc_dir=doc_dir,
        output_dir=output,
        auto_version=True,
        sphinx_config=Bunch(
            project_name=name,
            copyright=copyright,
            author=author,
            version=version,
            add_paths=[os.path.join("..", "..", src_dir)],
            theme=theme,
            welcome=welcome,
        ),
    )

    # write config file
    with open(os.path.join(work_dir, ".yadocgen"), "w") as f:
        yaml.dump(CONFIG, f)

    # create Sphinx directory structure
    work_dir = path.abspath(work_dir)
    os.makedirs(path.join(work_dir, CONFIG.output_dir, "source", "_static"))
    os.makedirs(path.join(work_dir, CONFIG.output_dir, "source", "_templates"))
    os.makedirs(path.join(work_dir, CONFIG.output_dir, "build"))

    env = Environment(loader=PackageLoader("yadocgen", "templates"))

    # create Makefile
    with open(path.join(work_dir, CONFIG.output_dir, "Makefile"), "w") as f:
        template = env.get_template("Makefile.jinja")
        f.write(template.render(config=CONFIG.sphinx_config))

    # create Sphinx config file
    with open(path.join(work_dir, CONFIG.output_dir, "source", "conf.py"), "w") as f:
        template = env.get_template("conf.py.jinja")
        f.write(template.render(config=CONFIG.sphinx_config))


@cli.command()
@click.option(
    "--work-dir",
    envvar="YDG_WORK_DIR",
    default=".",
    help="yadocgen working directory (default: current directory)",
)
@click.option(
    "--purge",
    default=True,
    help="Clean Sphinx source (default: True)",
)
def generate(work_dir, purge):
    """Generates the documentation for a project."""
    work_dir = path.abspath(work_dir)

    # load project config
    config_file_path = os.path.join(work_dir, ".yadocgen")
    if not os.path.isfile(config_file_path):
        print(f"Config file not found in working directory ({config_file_path}).")
    with open(config_file_path, "r") as f:
        CONFIG = yaml.full_load(f)

    generate_documentation(work_dir, purge, CONFIG)


def configure_bibfiles():
    ## TODO check if it is always valid to perform this on current work dir!
    return [
        f for f in os.listdir(".") if os.path.isfile(f) and f.lower().endswith(".bib")
    ]
