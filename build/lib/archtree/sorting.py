"""
Architectural sorting.
"""

from .models import Node
from .roles import Role


ORDER = {
    Role.PUBLIC_INTERFACE: 0,
    Role.IMPLEMENTATION: 1,
    Role.OTHER: 2,
    Role.DIRECTORY: 3,
}


def sort_nodes(nodes: list[Node]) -> list[Node]:

    return sorted(
        nodes,
        key=lambda node: (
            ORDER[node.role],
            node.path.name.lower(),
        ),
    )