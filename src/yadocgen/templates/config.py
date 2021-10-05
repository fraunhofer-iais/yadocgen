# yadocgen Sphinx config template

{% if len(config.add_paths) > 0 %}
import os
import sys
{% for add_path in config.add_paths -%}
    sys.path.insert(0, os.path.abspath("{{ add_path }}"))
{%- endfor %}
{% endif %}

# Project Metadata
project = "{{ config.project_name }}"
copyright = "{{ config.copyright }}"
author = "{{ config.author }}"
release = "{{ config.version }}"

# Basic Configuration
source_encoding = "utf-8-sig"
exclude_patterns = []
templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "alabaster"

# Extensions
extensions = [
"numpydoc", 
"myst_parser",
"sphinx.ext.autodoc", 
#"sphinxcontrib.confluencebuilder",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Configuration for the Markdown parser
myst_enable_extensions = [
    "linkify",                  # trun URLs into links automatically
    "dollarmath",               # support for $..$ and $$..$$ math environments
    "substitution",             # enable jina2 style {{ substitutions }}
    "deflist",                  # enable markup for Pandoc style definitions 
    "html_image",               # enable support for HTML image tags
    "html_admonition",          # enable support for HTML info/warning/tip boxes
    "colon_fence",              # enable support for colon fence environment, e.g. for figure-md
]
myst_dmath_double_inline = True   # enable support for inline $$-blocks 
myst_heading_anchors = 4          # enable automatic anchor generation for down to n-th level headings

# Markdown jinja2 style substitutions 
# e.g. {{ institute_long }} or {{ institute_short }}
myst_substitutions = {
  "institute_long" : "Fraunhofer Institute for Intelligent Analysis and Information Systems IAIS",
  "institute_short" : "Fraunhofer IAIS",
}

# Configuration for the Confluence extension
## TODO add configuration option to yadocgen
# confluence_publish = True
# confluence_server_url = "https://jira.iais.fraunhofer.de/wiki"
# confluence_space_name = ""
# confluence_parent_page = ""
# confluence_server_user = ""
# confluence_ask_password = True
# confluence_page_hierarchy = True
