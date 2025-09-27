#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.i_dispatch import IDispatch


class CatBaseUnknown(IDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         CATBaseUnknown
                | 
                | Base class for creating interfaces and for implementing
                | interfaces.
                | Role: CATBaseUnknown supplies the infrastructure and the basic mechanisms to
                | create interface abstract classes and to manage interface pointers. It is also
                | the base class for classes which implements interfaces and for their extension
                | classes because it supplies the code for the interface methods QueryInterface,
                | AddRef and Release.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'CatBaseUnknown(name="{self.name}")'
