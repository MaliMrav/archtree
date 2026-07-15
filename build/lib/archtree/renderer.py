"""
Tree renderer.
"""

from .models import Node


BRANCH = "├── "
LAST_BRANCH = "└── "
PIPE = "│   "
SPACE = "    "


def render(
        node: Node,
        label: str,
) -> list[str]:
    """
    Render a tree using unicode branches.
    """

    lines: list[str] = []

    lines.append(label)

    if node.children:
        lines.extend(
            _render_children(
                node.children,
                prefix="",
            )
        )

    return lines


def _render_children(
    children: list[Node],
    prefix: str,
) -> list[str]:

    lines: list[str] = []

    count = len(children)

    for index, child in enumerate(children):

        last = index == count - 1

        connector = (
            LAST_BRANCH
            if last
            else BRANCH
        )

        lines.append(
            prefix
            + connector
            + child.path.name
        )

        if child.children:

            extension = (
                SPACE
                if last
                else PIPE
            )

            lines.extend(
                _render_children(
                    child.children,
                    prefix + extension,
                )
            )

    return lines