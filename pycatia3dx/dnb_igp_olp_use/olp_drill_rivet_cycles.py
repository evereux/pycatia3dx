"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_drill_rivet_cycle import OLPDrillRivetCycle
from pycatia3dx.types.general import CATVariant


class OLPDrillRivetCycles(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpDrillRivetCycles
                | 
                | Interface representing a
                | Collection of OlpDrillRivetCycle This interface can only be used by a
                | translator within the Robotics Off-line Programming (OLP) Download or Upload
                | command. Use this interface to modify data related to a the cycles within a the
                | profile.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OLPDrillRivetCycle)
        self.com_object = com_object

    def append(self, i_cycle: OLPDrillRivetCycle) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Append(OlpDrillRivetCycle iCycle)
                |     Append a cycle at the end of the collection.
                | 
                |     Parameters:
                | 
                |         iCycle
                |             The cycle to append at the end of this cycles collection.

        :param OLPDrillRivetCycle i_cycle:
        :return: None
        """
        return self.com_object.Append(i_cycle.com_object)

    def create_cycle(self, i_match: bool) -> OLPDrillRivetCycle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateCycle(boolean iMatch) As OlpDrillRivetCycle
                |     Create a new cycle.
                |     The created cycle is not appended to the current collection. The user must
                |     either append it or insert it in the desired location.
                | 
                |     Parameters:
                | 
                |         iMatch
                |             If true, the cycle will be matched to other cycles when profile
                |             matching occurs 
                | 
                |     Returns:
                |         The cycle created.

        :param bool i_match:
        :return: OLPDrillRivetCycle
        """
        return OLPDrillRivetCycle(self.com_object.CreateCycle(i_match))

    def insert(self, i_index: int, i_cycle: OLPDrillRivetCycle) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Insert(short iIndex,OlpDrillRivetCycle iCycle)
                |     Insert a cycle at a specific index of the collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index at which to insert the cycle. If it is bigger than the
                |             collection count, the cycle will be appended at the end of the collection. If
                |             equal or smaller than zero it will be inserted to the beginning of the
                |             collection. 
                |         iCycle
                |             The cycle to append at the given index.

        :param int i_index:
        :param OLPDrillRivetCycle i_cycle:
        :return: None
        """
        return self.com_object.Insert(i_index, i_cycle.com_object)

    def item(self, i_index: CATVariant) -> OLPDrillRivetCycle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As OlpDrillRivetCycle
                |     Retrieve a cycle by its name or index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             If iIndex is a string, then a cycle with that name is returned. If
                |             the index is a number, it is the index of the cycle in the collection. The
                |             index of the first parameter in the collection is 1, and the index of the last
                |             parameter is Count. 
                | 
                |     Returns:
                |         The cycle retrieved. If the cycle name was not found, Nothing is
                |         returned but the function succeeds. If the index is out of bounds, the function
                |         fails. 

        :param CATVariant i_index:
        :return: OLPDrillRivetCycle
        """
        return OLPDrillRivetCycle(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> OLPDrillRivetCycle:
        if (n + 1) > self.count:
            raise StopIteration

        return OLPDrillRivetCycle(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[OLPDrillRivetCycle]:
        for i in range(self.count):
            yield OLPDrillRivetCycle(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'OLPDrillRivetCycles(name="{self.name}")'
