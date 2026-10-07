"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.str_flange import StrFlange
from pycatia3dx.types.general import CATVariant


class StrFlanges(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrFlanges

    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrFlange)
        self.com_object = com_object

    def add(self) -> StrFlange:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As StrFlange
                |     Adds a flange under this Plate. (@see CATIAStrFlange)
                | 
                |     Parameters:
                | 
                |         oFlange
                |             Flange 
                | 
                |     Example:
                | 
                | 
                |              This example creates a flange under this plate.
                |              
                | 
                |               Dim ObjStrFlanges As StrFlanges
                |               Set ObjStrFlanges = iObjSfdPlate.Flanges
                |              Set oObjStrFlange = ObjStrFlanges.Add

        :return: StrFlange
        """
        return StrFlange(self.com_object.Add())

    def item(self, i_index: CATVariant) -> StrFlange:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As StrFlange
                |     Returns a flange from a list of flanges. (@see
                |     CATIAStrFlange)
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of StrFlange 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first flange from the list of
                |              flanges.
                |              
                | 
                |               Set FlangeReference = ListOfFlanges.Item(1)

        :param CATVariant i_index:
        :return: StrFlange
        """
        return StrFlange(self.com_object.Item(i_index))

    def remove(self, i_flange: StrFlange) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(StrFlange iFlange)
                |     Removes the Flange.
                | 
                |     Parameters:
                | 
                |         iFlange
                |             Flange 
                | 
                |     Example:
                | 
                | 
                |              This example removes the flange.
                |              
                | 
                |               ObjStrFlanges.Remove ObjStrFlange

        :param StrFlange i_flange:
        :return: None
        """
        return self.com_object.Remove(i_flange.com_object)

    def __getitem__(self, n: int) -> StrFlange:
        if (n + 1) > self.count:
            raise StopIteration

        return StrFlange(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[StrFlange]:
        for i in range(self.count):
            yield StrFlange(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'StrFlanges(name="{self.name}")'
