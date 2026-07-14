"""
Architectural roles.
"""

from enum import Enum, auto


class Role(Enum):
    PUBLIC_INTERFACE = auto()
    IMPLEMENTATION = auto()
    DIRECTORY = auto()
    OTHER = auto()