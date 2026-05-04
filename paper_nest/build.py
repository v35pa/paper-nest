"""Fold every .md file under src/ into an .html page under out/."""
from pathlib import Path

from .render import render

TEMPLATE = Path(__file__).with_name("page.html")


def build(src="src", out="out"):
    template = TEMPLATE.read_text(encoding="utf-8")
    src, out = Path(src), Path(out)
    pages = sorted(src.rglob("*.md"))
    for page in pages:
        md = page.read_text(encoding="utf-8")
        title = md.splitlines()[0].lstrip("#").strip() if md.strip() else page.stem
        target = out / page.relative_to(src).with_suffix(".html")
        target.parent.mkdir(parents=True, exist_ok=True)
        html = template.replace("{{title}}", title).replace("{{body}}", render(md))
        target.write_text(html, encoding="utf-8")
    return len(pages)
