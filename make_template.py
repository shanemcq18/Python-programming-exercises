# make_template.py
"""Strip the solution code from solutions.md and write it as README.md."""

import re


SOURCE = "solutions.md"
TARGET = "README.md"

CODEFINDER = re.compile(r"\n```python.*?```\n\n####", re.DOTALL)


with open(SOURCE, 'r') as infile, open(TARGET, 'w') as outfile:
    outfile.write(CODEFINDER.sub('\n####', infile.read())[:-264])
