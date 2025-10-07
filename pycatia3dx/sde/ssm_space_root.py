"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sde.ssm_space_concept_roots import SsmSpaceConceptRoots
from pycatia3dx.todo_sde.ssm_space_folder import SsmSpaceFolder
from pycatia3dx.todo_sde.ssm_space_systems import SsmSpaceSystems


class SsmSpaceRoot(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmSpaceRoot
                | 
                | Role: This interface is specific to Space root
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def space_concept_roots(self) -> SsmSpaceConceptRoots:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpaceConceptRoots() As SsmSpaceConceptRoots (Read
                | Only)
                |     Gets space concept Roots present in it
                | 
                |     Parameters:
                | 
                |         olSpaceConceptRoots
                |             List of Space concept Roots.

        :return: SsmSpaceConceptRoots
        """

        return SsmSpaceConceptRoots(self.com_object.SpaceConceptRoots)

    @property
    def space_folder(self) -> SsmSpaceFolder:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpaceFolder() As SsmSpaceFolder (Read Only)
                |     Get Child SpaceFolder
                | 
                |     Parameters:
                | 
                |         oSpaceFolder
                |             output SpaceFolder 
                | 
                |     Returns:
                |         Error code of function.

        :return: SsmSpaceFolder
        """

        return SsmSpaceFolder(self.com_object.SpaceFolder)

    @property
    def space_systems(self) -> SsmSpaceSystems:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpaceSystems() As SsmSpaceSystems (Read Only)
                |     Gets space systems present in it
                | 
                |     Parameters:
                | 
                |         olSpaceSystems
                |             List of Space systems. 

        :return: SsmSpaceSystems
        """

        return SsmSpaceSystems(self.com_object.SpaceSystems)

    def __repr__(self):
        return f'SsmSpaceRoot(name="{ self.name }")'
