"""Turn a small subset of Markdown into HTML: headings and paragraphs."""
import html
import re


def render(md):
    out = []
    for block in re.split(r"\n\s*\n", md.strip()):
        if block.startswith("#"):
            level = min(len(block) - len(block.lstrip("#")), 6)
            out.append(f"<h{level}>{html.escape(block[level:].strip())}</h{level}>")
        else:
            out.append(f"<p>{html.escape(' '.join(block.split()))}</p>")
    return "\n".join(out)
