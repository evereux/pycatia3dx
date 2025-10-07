"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sde.ssm_space import SsmSpace
from pycatia3dx.todo_sde.ssm_space_concept_nodes import SsmSpaceConceptNodes


class SsmSpaceConceptNode(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmSpaceConceptNode
                | 
                | Role: This interface is specific to Space concept Node
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def space(self) -> SsmSpace:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Space() As SsmSpace (Read Only)
                |     Get Child SpaceReference
                | 
                |     Parameters:
                | 
                |         oSpace
                |             output Space 
                | 
                |     Returns:
                |         Error code of function.

        :return: SsmSpace
        """

        return SsmSpace(self.com_object.Space)

    @property
    def space_concept_nodes(self) -> SsmSpaceConceptNodes:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpaceConceptNodes() As SsmSpaceConceptNodes (Read
                | Only)
                |     Get SpaceConcepts
                | 
                |     Parameters:
                | 
                |         output
                |             list of SpaceConceptNode as a list of CATBaseUnknown
                |             
                | 
                |     Returns:
                |         Error code of function. 

        :return: SsmSpaceConceptNodes
        """

        return SsmSpaceConceptNodes(self.com_object.SpaceConceptNodes)

    def __repr__(self):
        return f'SsmSpaceConceptNode(name="{ self.name }")'
