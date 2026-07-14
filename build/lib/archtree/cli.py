"""
Command line interface.
"""

from pathlib import Path

from .tree import build_tree
from .renderer import render


def main():

    root = Path(".")

    tree = build_tree(root)

    for line in render(tree):
        print(line)


if __name__ == "__main__":
    main()