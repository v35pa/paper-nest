"""Turn a small subset of Markdown into HTML: headings, paragraphs, code, links."""
import html
import re
import textwrap

LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
CODE = re.compile(r"`([^`]+)`")


def inline(text):
    text = html.escape(text, quote=False)
    text = CODE.sub(r"<code>\1</code>", text)
    return LINK.sub(r'<a href="\2">\1</a>', text)


def render(md):
    out = []
    for block in re.split(r"\n\s*\n", md.strip()):
        if block.startswith("#"):
            level = min(len(block) - len(block.lstrip("#")), 6)
            out.append(f"<h{level}>{inline(block[level:].strip())}</h{level}>")
        elif block.startswith("    "):
            out.append(f"<pre>{html.escape(textwrap.dedent(block))}</pre>")
        else:
            out.append(f"<p>{inline(' '.join(block.split()))}</p>")
    return "\n".join(out)
