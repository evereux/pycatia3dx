"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.sim_rep.sim_sequence import SimSequence
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimSequences(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimSequences
                | 
                | Interface representing Simulation Sequences collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimSequence)
        self.com_object = com_object

    def add(self, i_type: str) -> SimSequence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As SimSequence
                |     Creates a new Simulation Sequence and adds it to the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iType:
                |             The type of Simulation Sequence to create. 
                | 
                |     Returns:
                |         The created Simulation Sequence.

        :param str i_type:
        :return: SimSequence
        """
        return SimSequence(self.com_object.Add(i_type))

    def item(self, i_index: CATVariant) -> SimSequence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimSequence
                |     Returns a Simulation Sequence using its index from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Simulation Sequence to retrieve from the
                |             collection.
                |             This index is the rank of the Simulation Sequence in the
                |             collection. The index of the first Simulation Sequence in the collection is 1,
                |             and the index of the last Simulation Sequence is Count.
                |             
                | 
                |     Returns:
                |         The retrieved Simulation Sequence.

        :param CATVariant i_index:
        :return: SimSequence
        """
        return SimSequence(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Simulation Sequence using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the Simulation Sequence to retrieve from
                |             the collection.
                |             As a numeric, this index is the rank of the Simulation Sequence in
                |             the collection. The index of the first Simulation Sequence in the collection is
                |             1, and the index of the last Simulation Sequence is
                |             Count.
                |             As a string, it is the name you assigned to the Simulation Sequence
                |             using the Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __getitem__(self, n: int) -> SimSequence:
        if (n + 1) > self.count:
            raise StopIteration

        return SimSequence(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SimSequence]:
        for i in range(self.count):
            yield SimSequence(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SimSequences(name="{self.name}")'
