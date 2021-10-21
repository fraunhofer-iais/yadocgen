import os
from abc import ABC, abstractmethod
from jinja2 import Environment, PackageLoader, select_autoescape


def dots_to_underscores(s):
    return "_".join(s.split("."))


jinja = Environment(loader=PackageLoader("yadocgen", "templates"))
jinja.globals["dots_to_underscores"] = dots_to_underscores


class Page(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def page_name(self):
        pass

    @abstractmethod
    def output_filename(self):
        pass

    @abstractmethod
    def render(self):
        pass


class DocPage(Page):
    def __init__(self, fpath, fname):
        super().__init__()
        self.fpath = fpath
        self.fname = fname

    def page_name(self):
        name = "_".join(self.fname.split(".")[:-1])
        return f"doc_{name}"

    def output_filename(self):
        return self.page_name() + ".md"

    def render(self):
        template = jinja.get_template("docpage.md.jinja")
        return template.render(
            file=os.path.join("..", "..", self.fpath, self.fname),
            doc_dir=self.fpath,
            img_doc=os.path.join(self.fpath, "img"),
        )


class SourcePage(Page):
    def __init__(self, node):
        super().__init__()
        self.node = node

    def page_name(self):
        name = "_".join(self.node.module.name.split("."))
        return f"src_{name}"

    def output_filename(self):
        return self.page_name() + ".rst"

    def render(self):
        if self.node.module.ispkg:
            template = jinja.get_template("package.rst.jinja")
        else:
            template = jinja.get_template("module.rst.jinja")
        underline = "".join(["=" for _ in range(len(self.node.module.name))])
        return template.render(node=self.node, title_underline=underline)


class WelcomePage(Page):
    def __init__(self, welcome_page, pages, api_index):
        super().__init__()
        self.welcome_page = welcome_page
        self.pages = pages
        self.api_index = api_index

    def page_name(self):
        return "index"

    def output_filename(self):
        return "index.md"

    def render(self):
        template = jinja.get_template("welcome.md.jinja")
        return template.render(
            file=os.path.join("..", "..", self.welcome_page),
            pages=self.pages,
            api=self.api_index,
        )


class APIPage(Page):
    def __init__(self, pages):
        super().__init__()
        self.pages = pages

    def page_name(self):
        return "api_index"

    def output_filename(self):
        return "api_index.rst"

    def render(self):
        template = jinja.get_template("api_index.rst.jinja")
        return template.render(pages=self.pages)
