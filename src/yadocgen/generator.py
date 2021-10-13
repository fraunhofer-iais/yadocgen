import os
import sys
import shutil
import pkgutil
from os import path
from yadocgen.rendering import *
from anytree import Node, Resolver, RenderTree, PreOrderIter


def walk_packages_error(name):
    """Error callback for pkgutil.walk_packages."""
    extype, value, traceback = sys.exc_info()
    print(f"{extype} importing module {name}")
    print_tb(traceback)
    sys.exit(-1)


def find_modules(where="."):
    """Returns a tree representing the source tree in a given directory"""
    rsv = Resolver("name")
    root = Node("src", module=None)

    for pkginfo in pkgutil.walk_packages([where], onerror=walk_packages_error):
        path = pkginfo.name.split(".")
        if len(path) == 1:
            parent = root
        else:
            # !! this assumes that walk_packages does a pre-order walk ... it seems to do
            parent = rsv.get(root, "/".join([path[i] for i in range(len(path) - 1)]))
        node = Node(pkginfo.name.split(".")[-1], parent=parent, module=pkginfo)

    return root


def generate_documentation(work_dir, purge, config):
    """Generates the documentation files given a source tree."""
    sphinx_dir = path.join(work_dir, config.output_dir)
    sphinx_source_dir = path.join(sphinx_dir, "source")

    # purge Sphinx source directory but keep Sphinx config
    if purge:
        print("purging Sphinx source directory")
        for f in os.listdir(sphinx_source_dir):
            if os.path.isfile(f) and not f == "conf.py":
                    os.remove(os.path.join(root, f))
            # for d in dirs:
            #     os.remove(os.path.join(root, d))

    pages = []

    # scan contents from doc directory
    if not config.doc_dir is None:
        doc_dir = path.join(work_dir, config.doc_dir)
        print(f"Documentation pages (from {doc_dir}):\n")
        for f in os.listdir(doc_dir):
            if os.path.isfile(os.path.join(doc_dir, f)) and f.lower().endswith(".md"):
                # add a documentation page
                pages.append(DocPage(config.doc_dir, f))
                print(f" - {f}")

    # find packages in source path
    if config.src_dir is not None:
        src_dir = path.join(work_dir, config.src_dir)
        sys.path.insert(0, src_dir)                    # add path to sys.path so that pkgtools can load package definitions
        src_pages = find_modules(where=src_dir)
        print(f"Source tree (from: {src_dir}):\n")
        print(RenderTree(src_pages).by_attr("name") + "\n")
        for node in PreOrderIter(src_pages):
            if node is not src_pages:  # src_pages is root element so we skip it
                # add a source code documentation page
                pages.append(SourcePage(node))

    # add the API index page
    api_index = APIPage([p for p in pages if type(p) is SourcePage])
    pages.append(api_index)

    # add the wecome page
    pages.append(
        WelcomePage(
            config.sphinx_config.welcome, 
            [p for p in pages if type(p) is DocPage],
            api_index
        )
    )

    # generate Sphinx files
    print("Generating files:")
    for page in pages:
        print(f" - {page.output_filename()}")
        with open(path.join(sphinx_source_dir, page.output_filename()), "w") as f:
            f.write(page.render())

