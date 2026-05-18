"""Rebuild whenever a file under src/ changes. It polls; paper is cheap."""
import time
from pathlib import Path

from .build import build


def snapshot(src):
    return {p: p.stat().st_mtime for p in Path(src).rglob("*") if p.is_file()}


def watch(src="src", out="out", every=0.5):
    seen = None
    while True:
        now = snapshot(src)
        if now != seen:
            print(f"built {build(src, out)} pages")
            seen = now
        time.sleep(every)
