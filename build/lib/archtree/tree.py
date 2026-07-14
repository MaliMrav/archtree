"""
Filesystem traversal.
"""

from pathlib import Path

from .models import Node
from .roles import Role


def build_tree(path: Path) -> Node:

    if path.is_dir():

        children = [
            build_tree(child)
            for child in sorted(path.iterdir())
        ]

        return Node(
            path=path,
            role=Role.DIRECTORY,
            children=children,
        )

    return Node(
        path=path,
        role=Role.OTHER,
    )