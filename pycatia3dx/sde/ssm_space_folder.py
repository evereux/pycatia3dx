"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sde.ssm_spaces import SsmSpaces


class SsmSpaceFolder(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmSpaceFolder
                | 
                | Role: This interface is specific to Space Folder
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def spaces(self) -> SsmSpaces:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Spaces() As SsmSpaces (Read Only)
                |     Get Space References
                | 
                |     Parameters:
                | 
                |         output
                |             list of SpaceRef as a list of CATBaseUnknown 
                | 
                |     Returns:
                |         Error code of function. 

        :return: SsmSpaces
        """

        return SsmSpaces(self.com_object.Spaces)

    def __repr__(self):
        return f'SsmSpaceFolder(name="{ self.name }")'
