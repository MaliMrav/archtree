"""
Tree data models.
"""

from dataclasses import dataclass
from pathlib import Path

from .roles import Role


@dataclass
class Node:
    path: Path
    role: Role
    children: list["Node"] | None = None