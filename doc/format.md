# Format Options

Sphinx with Myst-Parser brings several extensions that are not available in vanilla markdown.

## Code Blocks

Code block e.g. for examples are easily create by using the \`\`\` delimiter followed by the name of the language (latex, shell etc. are also supported):

```python
import os
import sys

print(f"This is a Python3 f-string: {os.name}")

```

Or you can use the more powerful `{code-block}` directive to add additional parameters to the rendering of the code block, for example line numbers and highlighting lines

```
:::{code-block} python
---
lineno-start: 1
caption: Code block example
emphasize-lines: 4
---
import os
import sys

print(f"This is a Python3 f-string: {os.name}")
:::

```
___Result:___

:::{code-block} python
---
lineno-start: 1
caption: Code block example
emphasize-lines: 4
---
import os
import sys

print(f"This is a Python3 f-string: {os.name}")

:::


## Definition Blocks/Lists

As an alternative to bullet lists you can use definition list or single definition blocks. These are also used in the API documentation.


```
Term 1
: Definition of the first term.

Term 2
: Definition of the second term.
```

___Result:___


Term 1
: Definition of the first term.

Term 2
: Definition of the second term.

## Admonitions

There are also different types of admonitions (`tip`, `note`, `warning`) are available

```markdown

:::{tip} 
This is a **tip**.
:::
```
___Result:___

:::{tip} 
This is a **tip**.
:::


:::{note} 
This is a **note**.
:::


:::{warning} 
This is a **warning**.
:::

## Literature References

In other good news: Just use your BibTeX file for referencing literature!

```markdown
Just use your BibTeX file for referencing literature  {cite}`wulff2013lecturesight`!

:::{bibliography} refs.bib
:labelprefix: 
:keyprefix:
:::

```
___Result:___

Just use your BibTeX file for referencing literature  {cite}`wulff2013lecturesight`!

:::{bibliography} refs.bib
:labelprefix: 
:keyprefix:
:::

## Footnotes

And finally, footnotes are also available

```markdown
This is an auto-numbered footnote reference.[^myref]

[^myref]: This is an auto-numbered footnote definition.

```
___Result:___

This is an auto-numbered footnote reference.[^myref]

[^myref]: It uses the definition block macro.