"""
    The catia base object is from which most other functionality derives. See examples for more information.

    >>> from pycatia3dx import catia3dx
    >>> application = catia()

"""

from pycatia3dx.base_interfaces.base_application import catia_application as catia3dx
from pycatia3dx.version import version

__author__ = 'Paul Bourne'
__author_email = 'evereux@gmail.com'
__description__ = 'A python module to interface with the CATIA 3DX COM object.'
__name__ = "pycatia3dx"
__version__ = version
__url__ = "https://github.com/evereux/pycatia"

name = __name__
