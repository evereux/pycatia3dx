"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.str_opening import StrOpening
from pycatia3dx.types.general import CATVariant


class StrOpenings(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrOpenings
                | 
                | Object for StrOpenings.
                | Role: To access an opening from a collection of openings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrOpening)
        self.com_object = com_object

    def add(self) -> StrOpening:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As StrOpening
                |     Returns the Opening created with all the data structure
                |     Role: Create an Opening with all the data structure.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example creates an Opening
                |              
                | 
                |              Dim ObjStrOpenings As StrOpenings
                |              Set ObjStrOpenings = iObjSfdPanel.GetOpenings(0)
                |              Dim ObjStrOpening As StrOpening
                |              Set ObjStrOpening = ObjStrOpenings.Add

        :return: StrOpening
        """
        return StrOpening(self.com_object.Add())

    def item(self, i_index: CATVariant) -> StrOpening:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As StrOpening
                |     Returns an Opening from a list
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of StrOpening 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in first opening from the list of
                |              openings.
                |              
                | 
                |               'Get all created opening on the object
                |               Dim ObjStrOpenings As StrOpenings
                |               Set ObjStrOpenings = ObjSfdPanel.GetOpenings(0)
                |               'Get first opening from the list of opening
                |               Dim ObjStrOpening As StrOpening
                |               set ObjStrOpening = ObjStrOpenings.Item(1)

        :param CATVariant i_index:
        :return: StrOpening
        """
        return StrOpening(self.com_object.Item(i_index))

    def remove(self, i_opening: StrOpening) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(StrOpening iOpening)
                |     Removes an opening. The opening must belong to this Panel /
                |     Profile.
                | 
                |     Parameters:
                | 
                |         iOpening
                |             Opening. 
                | 
                |     Example:
                | 
                |          
                | 
                |              This example removes an Opening
                |              
                | 
                |              ObjStrOpenings.Remove(ObjStrOpening)

        :param StrOpening i_opening:
        :return: None
        """
        return self.com_object.Remove(i_opening.com_object)

    def __getitem__(self, n: int) -> StrOpening:
        if (n + 1) > self.count:
            raise StopIteration

        return StrOpening(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[StrOpening]:
        for i in range(self.count):
            yield StrOpening(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'StrOpenings(name="{self.name}")'
