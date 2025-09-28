#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.cat_base_unknown import CATBaseUnknown


class CATBaseDispatch(CATBaseUnknown):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             CATBaseDispatch
                | 
                | Base class for Automation interfaces.
                | Role: All Automation interfaces must inherit from the CATBaseDispatch
                | interface. They usually do not inherit directly from CATBaseDispatch, but
                | rather from one of its subclasses: AnyObject for individual objects or
                | Collection for collection objects. Some methods may however have arguments of
                | type CATBaseDispatch when they accept both individual objects or collection
                | objects. The interface provides no functionalities per se.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'CatBaseDispatch(name="{self.name}")'
