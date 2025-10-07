"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.str_collars import StrCollars
from pycatia3dx.str.str_detail_feature import StrDetailFeature


class StrSlot(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrSlot
                | 
                | Object to manage Structure Functional Slot.
                | Role: Allows accessing and setting of Slot's data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def collars(self) -> StrCollars:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Collars() As StrCollars (Read Only)
                |     Returns StrCollars objects.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Collar objects.
                |              
                | 
                |              Dim ObjStrCollars As StrCollars
                |              Set ObjStrCollars = iObjStrSlot.Collars

        :return: StrCollars
        """

        return StrCollars(self.com_object.Collars)

    @property
    def str_detail_feature(self) -> StrDetailFeature:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrDetailFeature() As StrDetailFeature (Read Only)
                |     Returns the StrDetailFeature object.

        :return: StrDetailFeature
        """

        return StrDetailFeature(self.com_object.StrDetailFeature)

    def get_penetrating_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPenetratingProfile() As AnyObject
                |     Returns the penetrating profile.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the penetrating profile.
                |              
                | 
                |              Set PenetratingProfile = ObjStrSlot.GetPenetratingProfile

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetPenetratingProfile())

    def set_penetrating_profile(self, i_profile: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPenetratingProfile(Reference iProfile)
                |     Sets the penetrating profile.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             Profile. 
                | 
                |     Example:
                | 
                | 
                |              This example sets the penetrating profile.
                |              
                | 
                |              ObjStrSlot As StrSlot
                |              Set ObjStrSlot = ObjStrSlots.Add
                |              Dim penetratingElem As Reference
                |              Set penetratingElem = ObjPart.CreateReferenceFromObject(ObjSfdStiffener)
                |              ObjStrSlot.SetPenetratingProfile penetratingElem

        :param Reference i_profile:
        :return: None
        """
        return self.com_object.SetPenetratingProfile(i_profile.com_object)

    def __repr__(self):
        return f'StrSlot(name="{ self.name }")'
