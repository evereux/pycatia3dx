"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.fmt_mode.sim_group import SimGroup
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimGroups(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimGroups
                | 
                | Represents the collection of Simulation Groups.
                | 
                | See also:
                |     SimGroup
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimGroup)
        self.com_object = com_object

    def add(self, i_type: str) -> SimGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As CATBaseDispatch
                |     Creates a new group and adds it to the collection.
                | 
                |     Parameters:
                | 
                |         iType:
                |             The type of group to create. 
                | 
                |     Returns:
                |         The created group

        :param str i_type:
        :return: SimGroup
        """
        return SimGroup(self.com_object.Add(i_type))

    def item(self, i_index: CATVariant) -> SimGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimGroup
                |     Returns a group using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the simulation group to retrieve from the
                |             collection.
                |             As a numeric, this index is the rank of the simulation group in the
                |             collection. The index of the first simulation group in the collection is 1, and
                |             the index of the last simulation group is Count.
                |             As a string, it is the name you assigned to the property using the
                |             Name object property. 
                | 
                |     Returns:
                |         The retrieved group.

        :param CATVariant i_index:
        :return: SimGroup
        """
        return SimGroup(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a group using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the simulation group to retrieve from the
                |             collection of groups.
                |             As a numeric, this index is the rank of the simulation group in the
                |             collection. The index of the first simulation group in the collection is 1, and
                |             the index of the last simulation group is Count.
                |             As a string, it is the name you assigned to the group using the
                |             Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __getitem__(self, n: int) -> SimGroup:
        if (n + 1) > self.count:
            raise StopIteration

        return SimGroup(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SimGroup]:
        for i in range(self.count):
            yield SimGroup(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SimGroups(name="{self.name}")'
