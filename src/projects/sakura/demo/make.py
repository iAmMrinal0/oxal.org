import re
import os
import sys

with open('demo.tmpl') as f:
    tmpl = f.read()

content = os.popen("pandoc --toc -f markdown -t html demo.md").read()

SUBSTR = "{{{content}}}"

content = re.sub(SUBSTR, content, tmpl)

with open('index.html', 'w') as f:
    f.write(content)
