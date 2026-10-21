from typing import Union, Any

from pycatia3dx.mode.reference import Reference
from pycatia3dx.scripts.vba import VBANothing

CATVariant = Union[
    int, str, tuple, Reference, VBANothing
]

Variant = Union[
    int, str, list, dict, tuple, set
]
