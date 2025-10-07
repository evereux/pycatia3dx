"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class SsmSpaceInput(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmSpaceInput
                | 
                | Role: This interface is specific to External
                | volume/BoundingBox
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def space_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpaceElement() As Reference (Read Only)
                |     Get SpaceElement
                | 
                |     Parameters:
                | 
                |         oSpaceElement
                |             [out] SpaceElement 
                | 
                |     Returns:
                |         Error code of function. 

        :return: Reference
        """

        return Reference(self.com_object.SpaceElement)

    def __repr__(self):
        return f'SsmSpaceInput(name="{ self.name }")'
