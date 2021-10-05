.. toctree::

{% for child in node.children %}
   {{child.module.name}}
{% endfor %}

Package {{node.module.name}}
===

.. automodule:: {{node.module.name}}
   :members:
   :undoc-members:
   :show-inheritance:
