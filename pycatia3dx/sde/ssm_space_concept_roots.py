"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.sde.ssm_space_concept_root import SsmSpaceConceptRoot
from pycatia3dx.types.general import CATVariant


class SsmSpaceConceptRoots(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SsmSpaceConceptRoots
                | 
                | Role: This interface is collection of Space Concept root
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SsmSpaceConceptRoot)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SsmSpaceConceptRoot:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SsmSpaceConceptRoot
                |     Retrieves a Space Concept root
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of Space Concept root 

        :param CATVariant i_index:
        :return: SsmSpaceConceptRoot
        """
        return SsmSpaceConceptRoot(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> SsmSpaceConceptRoot:
        if (n + 1) > self.count:
            raise StopIteration

        return SsmSpaceConceptRoot(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SsmSpaceConceptRoot]:
        for i in range(self.count):
            yield SsmSpaceConceptRoot(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SsmSpaceConceptRoots(name="{self.name}")'
