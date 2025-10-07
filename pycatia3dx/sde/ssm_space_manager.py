"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sde.ssm_cutting_set import SsmCuttingSet
from pycatia3dx.sde.ssm_space_input import SsmSpaceInput
from pycatia3dx.sde.ssm_tool_set import SsmToolSet


class SsmSpaceManager(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmSpaceManager
                | 
                | Role: This interface is specific to Space Manager
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def bounding_box(self) -> SsmSpaceInput:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BoundingBox() As SsmSpaceInput (Read Only)
                |     Get Bounding Box
                | 
                |     Parameters:
                | 
                |         oBoundingBox
                |             [out] BoundingBox 
                | 
                |     Returns:
                |         Error code of function.

        :return: SsmSpaceInput
        """

        return SsmSpaceInput(self.com_object.BoundingBox)

    @property
    def cutting_set(self) -> SsmCuttingSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CuttingSet() As SsmCuttingSet (Read Only)
                |     Get CuttingSet
                | 
                |     Parameters:
                | 
                |         oCuttingSet
                |             [out] CuttingSet 
                | 
                |     Returns:
                |         Error code of function.

        :return: SsmCuttingSet
        """

        return SsmCuttingSet(self.com_object.CuttingSet)

    @property
    def external_volume(self) -> SsmSpaceInput:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExternalVolume() As SsmSpaceInput (Read Only)
                |     Get external volume
                | 
                |     Parameters:
                | 
                |         oExternalVolume
                |             [out] External Volume 
                | 
                |     Returns:
                |         Error code of function.

        :return: SsmSpaceInput
        """

        return SsmSpaceInput(self.com_object.ExternalVolume)

    @property
    def internal_space_set(self) -> SsmToolSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InternalSpaceSet() As SsmToolSet (Read Only)
                |     Get InternalSpaceSet
                | 
                |     Parameters:
                | 
                |         oInternalSpaceSet
                |             [out] InternalSpaceSet 
                | 
                |     Returns:
                |         Error code of function.

        :return: SsmToolSet
        """

        return SsmToolSet(self.com_object.InternalSpaceSet)

    @property
    def space_cell_set(self) -> SsmToolSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpaceCellSet() As SsmToolSet (Read Only)
                |     Get SpaceCellSet
                | 
                |     Parameters:
                | 
                |         oSpaceCellSet
                |             [out] SpaceCellSet 
                | 
                |     Returns:
                |         Error code of function. 

        :return: SsmToolSet
        """

        return SsmToolSet(self.com_object.SpaceCellSet)

    def __repr__(self):
        return f'SsmSpaceManager(name="{ self.name }")'
