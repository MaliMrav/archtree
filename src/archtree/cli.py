"""
Command line interface.
"""

import argparse
from pathlib import Path

from .tree import build_tree
from .renderer import render


def main():

    parser = argparse.ArgumentParser(
        prog="archtree",
        description="Display source trees in architectural order.",
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Directory to display",
    )

    args = parser.parse_args()

    root = Path(args.path)

    if not root.exists():
        print(f"archtree: '{args.path}' does not exist.")
        raise SystemExit(1)

    if not root.is_dir():
        print(f"archtree: '{args.path}' is not a directory.")
        raise SystemExit(1)

    tree = build_tree(root)

    for line in render(tree, label=args.path):
        print(line)


if __name__ == "__main__":
    main()