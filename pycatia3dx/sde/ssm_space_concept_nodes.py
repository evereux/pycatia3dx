"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.todo_sde.ssm_space_concept_node import SsmSpaceConceptNode
from pycatia3dx.types.general import CATVariant


class SsmSpaceConceptNodes(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SsmSpaceConceptNodes
                | 
                | Role: This interface is collection of Space concept Node
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SsmSpaceConceptNode:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SsmSpaceConceptNode
                |     Retrieves a Space concept Node
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of Space concept Node 

        :param CATVariant i_index:
        :return: SsmSpaceConceptNode
        """
        return SsmSpaceConceptNode(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SsmSpaceConceptNodes(name="{ self.name }")'
