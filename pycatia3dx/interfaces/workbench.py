"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class Workbench(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Workbench
                | 
                | Represents a workbench on a document.
                | Role:A workbench is a set of commands that can be used to create, modify and
                | edit the objects making up the document.
                | 
                | See also:
                |     CATIADocument
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Workbench(name="{self.name}")'
