"""
Filesystem traversal.
"""

from pathlib import Path

from .sorting import sort_nodes

from .models import Node
from .architectures import determine_role
from .roles import Role


def build_tree(path: Path) -> Node:

    if path.is_dir():

        children = [
            build_tree(child)
            for child in path.iterdir()
        ]
        children = sort_nodes(children)

        return Node(
            path=path,
            role=Role.DIRECTORY,
            children=children,
        )

    return Node(
        path=path,
        role=determine_role(path),
    )