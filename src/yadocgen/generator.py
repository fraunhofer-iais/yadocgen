def onerror(name):
    """Error callback for pkgutil.walk_packages."""
    extype, value, traceback = sys.exc_info()
    print(f"{extype} importing module {name}")
    print_tb(traceback)
    sys.exit(-1)


def find_modules(where="."):
    """Returns a tree representing the source tree in a given directory"""
    rsv = Resolver("name")
    root = Node("src", module=None)

    for pkginfo in pkgutil.walk_packages([where], onerror=onerror):
        path = pkginfo.name.split(".")
        if len(path) == 1:
            parent = root
        else:
            # !! this assumes that walk_packages does a pre-order walk ... it seems to do
            parent = rsv.get(root, "/".join([path[i] for i in range(len(path) - 1)]))
        node = Node(pkginfo.name.split(".")[-1], parent=parent, module=pkginfo)

    return root


def generate_documentation(source_dir, output_dir):
    """Generates the documentation files given a source tree."""
    # add path to sys.path so that pkgtools can load package definitions
    src_dir = os.path.abspath(os.path.join(source_dir, "src"))
    sys.path.insert(0, src_dir)

    # find packages in source path
    print("Source tree\n")
    pages = find_modules(where=src_dir)
    print(RenderTree(pages).by_attr("name") + "\n")

    # create output directory if not existing
    if not os.path.isdir(output_dir):
        print(f"Directory {output_dir} does not exist, creating it...")
        os.makedirs(output_dir)

    # generate Sphinx files
    print("Generating files:")
    for node in PreOrderIter(pages):
        if node is pages:               # pages is the root elemnt
            filename = "index.rst"
            src_file = os.path.join(source_dir, "README.md")
            content = pypandoc.convert_file(src_file, "rst")
        else:
            filename = rst_filename(node)
            if node.module.ispkg:
                content = render_package(node)
            else:
                content = render_module(node)
        filename = os.path.join(output_dir, filename)
        print(f"  {filename}")
        with open(filename, "w") as f:
            f.write(content)
