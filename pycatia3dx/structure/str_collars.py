"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.str_collar import StrCollar
from pycatia3dx.types.general import CATVariant


class StrCollars(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrCollars

    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrCollar)
        self.com_object = com_object

    def add(self) -> StrCollar:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As StrCollar
                |     Adds a collar to the slot. (@see CATIAStrCollar)
                | 
                |     Parameters:
                | 
                |         oCollar
                |             New Collar added to the slot. 
                | 
                |     Example:
                | 
                |          
                | 
                |              This example creates a collar on the slot.
                |              
                | 
                |               Dim ObjStrCollars As StrCollars
                |               Set ObjStrCollars = iObjStrSlot.Collars
                |               Set oObjStrCollar = ObjStrCollars.Add

        :return: StrCollar
        """
        return StrCollar(self.com_object.Add())

    def item(self, i_index: CATVariant) -> StrCollar:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As StrCollar
                |     Returns a collar from a list of collars. (@see
                |     CATIAStrCollar)
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of StrCollar 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first collar from the list of
                |              collars.
                |              
                | 
                |               Set oObjStrCollar = ObjStrCollars.Item(1)

        :param CATVariant i_index:
        :return: StrCollar
        """
        return StrCollar(self.com_object.Item(i_index))

    def remove(self, i_collar: StrCollar) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(StrCollar iCollar)
                |     Removes the Collar.
                | 
                |     Parameters:
                | 
                |         iCollar
                |             The Collar object to be removed. 
                | 
                |     Example:
                | 
                | 
                |              This example removes the collar 
                | 
                |              ObjStrCollar 
                | 
                |             .
                |              
                | 
                |               ObjStrCollars.Remove ObjStrCollar

        :param StrCollar i_collar:
        :return: None
        """
        return self.com_object.Remove(i_collar.com_object)

    def __getitem__(self, n: int) -> StrCollar:
        if (n + 1) > self.count:
            raise StopIteration

        return StrCollar(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[StrCollar]:
        for i in range(self.count):
            yield StrCollar(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'StrCollars(name="{self.name}")'
