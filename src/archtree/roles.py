###############################################################################
# Role management and permissions
# Copyright (c) 2026 Vladimir Lekic
###############################################################################
from enum import Enum

class Role(Enum):
    PUBLIC_INTERFACE = 1
    IMPLEMENTATION = 2
    DOCUMENTATION = 3
    BUILD = 4
    TEST = 5
    OTHER = 6
    DIRECTORY = 7