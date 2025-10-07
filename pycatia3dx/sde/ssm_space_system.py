"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sde.ssm_space_manager import SsmSpaceManager


class SsmSpaceSystem(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmSpaceSystem
                | 
                | Role: This interface is specific to Space System
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def space_manager(self) -> SsmSpaceManager:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpaceManager() As SsmSpaceManager (Read Only)
                |     Get Child SpaceManager
                | 
                |     Parameters:
                | 
                |         oSpaceManager
                |             output SpaceManager 
                | 
                |     Returns:
                |         Error code of function. 

        :return: SsmSpaceManager
        """

        return SsmSpaceManager(self.com_object.SpaceManager)

    def __repr__(self):
        return f'SsmSpaceSystem(name="{ self.name }")'
