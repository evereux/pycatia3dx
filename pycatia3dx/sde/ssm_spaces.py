"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.sde.ssm_space import SsmSpace
from pycatia3dx.types.general import CATVariant


class SsmSpaces(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SsmSpaces
                | 
                | Role: This interface is collection of Space reference
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SsmSpace)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SsmSpace:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SsmSpace
                |     Retrieves a Space Reference
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of Space reference 

        :param CATVariant i_index:
        :return: SsmSpace
        """
        return SsmSpace(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> SsmSpace:
        if (n + 1) > self.count:
            raise StopIteration

        return SsmSpace(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SsmSpace]:
        for i in range(self.count):
            yield SsmSpace(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SsmSpaces(name="{self.name}")'
