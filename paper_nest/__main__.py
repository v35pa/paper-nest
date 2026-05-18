"""paper-nest: paper-thin static sites.

    python -m paper_nest build [src] [out]
    python -m paper_nest watch [src] [out]
"""
import os
import sys

from . import __version__


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    cmd, args = argv[0], argv[1:]
    if cmd == "--version":
        print(__version__)
    elif cmd == "build":
        from .build import build
        print(f"built {build(*args[:2])} pages")
    elif cmd == "watch":
        from .watch import watch
        watch(*args[:2])
    else:
        print(f"unknown command: {cmd}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
