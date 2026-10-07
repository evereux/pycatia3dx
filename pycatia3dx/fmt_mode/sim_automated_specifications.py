"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.sim_rep.sim_generative_specification import SimGenerativeSpecification
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimAutomatedSpecifications(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimAutomatedSpecifications
                | 
                | Represents the collection of Simulation automated
                | specifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimGenerativeSpecification)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SimGenerativeSpecification:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimGenerativeSpecification
                |     Returns a generative specification using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the generative specification to retrieve
                |             from the collection.
                |             As a numeric, this index is the rank of the generative
                |             specification in the collection. The index of the first generative
                |             specification in the collection is 1, and the index of the last generative
                |             specification is Count.
                |             As a string, it is the name you assigned to the generative
                |             specification using the Name object property. 
                | 
                |     Returns:
                |         The retrieved genrative specification.

        :param CATVariant i_index:
        :return: SimGenerativeSpecification
        """
        return SimGenerativeSpecification(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> SimGenerativeSpecification:
        if (n + 1) > self.count:
            raise StopIteration

        return SimGenerativeSpecification(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SimGenerativeSpecification]:
        for i in range(self.count):
            yield SimGenerativeSpecification(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SimAutomatedSpecifications(name="{self.name}")'
