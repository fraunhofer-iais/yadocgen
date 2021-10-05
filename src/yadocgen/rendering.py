from jinja2 import Environment, PackageLoader, select_autoescape
import pypandoc


jinja = Environment(
        loader=PackageLoader('yadocgen', 'templates'),
        autoescape=select_autoescape(['rst'])
    )


def rst_filename(node):
    """Returns an rst filename for a given source tree node."""
    return node.module.name.replace(".", "_") + ".rst"


def render_package(node):
    """Returns the content of a documentation file for a given package node."""
    template = jinja.get_template('package.rst')
    return template.render(node=node)


def render_module(node):
    """Returns the content of a documentation file for a given module node."""
    template = jinja.get_template('module.rst')
    return template.render(node=node)


def render_readme(node):
    """Returns the content of a documentation file for a given readme node."""
    template = jinja.get_template('readme.rst')
    return template.render(node=node)


def render_docpage(node):
    """Returns the content of a documentation file for a given documentation page node."""
    template = jinja.get_template('docpage.rst')
    return template.render(node=node)