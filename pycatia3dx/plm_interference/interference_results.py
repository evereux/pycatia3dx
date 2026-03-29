"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.plm_interference.interference_result import InterferenceResult
from pycatia3dx.types.general import CATVariant


class InterferenceResults(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     InterferenceResults
                | 
                | Interface representing InterferenceResult object collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=InterferenceResult)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> InterferenceResult:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As InterferenceResult
                |     Returns a InterferenceResult from its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the InterferenceResult to retrieve from the collection
                |             of InterferenceResults. As a numerics, this index is the rank of the
                |             InterferenceResult in the collection. The index of the first InterferenceResult
                |             in the collection is 1, and the index of the last InterferenceResult is
                |             returned by Collection.get_Count method.

        :param CATVariant i_index:
        :return: InterferenceResult
        """
        return InterferenceResult(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> InterferenceResult:
        if (n + 1) > self.count:
            raise StopIteration

        return InterferenceResult(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[InterferenceResult]:
        for i in range(self.count):
            yield InterferenceResult(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'InterferenceResults(name="{self.name}")'
