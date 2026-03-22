"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.str_slot import StrSlot
from pycatia3dx.types.general import CATVariant


class StrSlots(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrSlots
                | 
                | Object for StrSlots
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=StrSlot)
        self.com_object = com_object

    def add(self) -> StrSlot:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As StrSlot
                |     Adds a slot under this Panel / Profile.
                | 
                |     Example:
                | 
                | 
                |              This example creates a slot under the
                |              Panel/Profile.
                |              
                | 
                |              Dim ObjStrSlots As StrSlots
                |              Set ObjStrSlots = iObjSfdPanel.StrSlots
                |              Set ObjStrSlot = ObjStrSlots.Add

        :return: StrSlot
        """
        return StrSlot(self.com_object.Add())

    def item(self, i_index: CATVariant) -> StrSlot:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As StrSlot
                |     Returns a slot from a list of slots
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of StrSlot 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first slot from the list of
                |              slots.
                |              
                | 
                |               Set SlotReference = ListOfSlots.Item(1)

        :param CATVariant i_index:
        :return: StrSlot
        """
        return StrSlot(self.com_object.Item(i_index))

    def remove(self, i_slot: StrSlot) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(StrSlot iSlot)
                |     Removes the Slot.
                | 
                |     Parameters:
                | 
                |         iSlot
                |             Slot 
                | 
                |     Example:
                | 
                | 
                |              This example removes the slot.
                |              
                | 
                |               ObjStrSlots.Remove ObjStrSlot

        :param StrSlot i_slot:
        :return: None
        """
        return self.com_object.Remove(i_slot.com_object)

    def __repr__(self):
        return f'StrSlots(name="{self.name}")'
