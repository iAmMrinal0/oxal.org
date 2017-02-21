"""
Defines functions which take in text in one format,
and returns metadata and text in another format.
"""
import re
import mistune
import yaml
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

class MetaParseException(Exception):
    pass


class HighlightRenderer(mistune.Renderer):
    """
    Using pygments on code blocks.
    """
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


markdown = mistune.Markdown(renderer=HighlightRenderer())

def md2html(text):
    """
    Takes input as markdown text, returns
    yaml metadata and html contents
    """
    first_line = True
    metadata = []
    content = []
    metadata_parsed = False

    for line in text.split('\n'):
        if first_line:
            first_line = False
            if line.strip() != '---':
                raise MetaParseException('Invalid metadata')
        elif line.strip() == '' and not metadata_parsed:
            pass
        elif line.strip() == '---' and not metadata_parsed:
            # reached the last line
            metadata_parsed = True
        elif not metadata_parsed:
            metadata.append(line)
        else:
            content.append(line)

    try:
        content = '\n'.join(content)
        metadata = yaml.load('\n'.join(metadata))
        metadata = metadata or {}
    except:
        raise

    return content, metadata


if __name__ == '__main__':
    t = """
---
date: 2015-06-14
title: Experiments [alpha]
category: life
---

I like experiments. 
They are fun. 
They give you data. 

---

This is a generic list of the experiments I wish to conduct.
"""
    a, b = Marker().extract_meta(t)
    print(b)
