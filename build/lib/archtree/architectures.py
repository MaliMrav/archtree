"""
Language architecture definitions.
"""

from pathlib import Path

from .roles import Role


def determine_role(path: Path) -> Role:

    if path.is_dir():
        return Role.DIRECTORY

    if path.suffix in {".h", ".hpp"}:
        return Role.PUBLIC_INTERFACE

    if path.suffix in {".cpp", ".cc", ".c"}:
        return Role.IMPLEMENTATION

    return Role.OTHER