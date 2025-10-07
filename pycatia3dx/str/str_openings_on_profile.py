"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.str.str_opening_on_profile import StrOpeningOnProfile
from pycatia3dx.types.general import CATVariant


class StrOpeningsOnProfile(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrOpeningsOnProfile
                | 
                | Object for StrOpeningsOnProfile.
                | Role: To access an opening from a collection of openings on
                | profile.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self) -> StrOpeningOnProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As StrOpeningOnProfile
                |     Adds a opening to the profile. (@see
                |     CATIAStrOpeningOnProfile)
                | 
                |     Parameters:
                | 
                |         oOpeningOnProfile
                |             New opening added to profile. 
                | 
                |     Example:
                | 
                |          
                | 
                |              This example creates a opening on the profile.
                |              
                | 
                |               Dim ObjStrOpeningsOnProfile As
                |               StrOpeningsOnProfile
                |               Set ObjStrOpeningsOnProfile = iObjSfdStiffener.OpeningsOnProfile(0)
                |               Set oObjSfdOpeningOnProfile = ObjStrOpeningsOnProfile.Add

        :return: StrOpeningOnProfile
        """
        return StrOpeningOnProfile(self.com_object.Add())

    def item(self, i_index: CATVariant) -> StrOpeningOnProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As StrOpeningOnProfile
                |     Returns a opening from a list of openings on profile. (@see
                |     CATIAStrOpeningOnProfile)
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of StrOpening. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first opening from the list of
                |              openings on profile.
                |              
                | 
                |               Set oObjSfdOpeningOnProfile = ObjStrOpeningsOnProfile.Item(1)

        :param CATVariant i_index:
        :return: StrOpeningOnProfile
        """
        return StrOpeningOnProfile(self.com_object.Item(i_index))

    def remove(self, i_opening_on_profile: StrOpeningOnProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(StrOpeningOnProfile iOpeningOnProfile)
                |     Removes the Opening on profile.
                | 
                |     Parameters:
                | 
                |         iOpeningOnProfile
                |             The opening object to be removed. 
                | 
                |     Example:
                | 
                | 
                |              This example removes the opening 
                | 
                |              ObjStrOpeningOnProfile 
                |
                |               ObjStrOpeningsOnProfile.Remove
                |               ObjStrOpeningOnProfile

        :param StrOpeningOnProfile i_opening_on_profile:
        :return: None
        """
        return self.com_object.Remove(i_opening_on_profile.com_object)

    def __repr__(self):
        return f'StrOpeningsOnProfile(name="{ self.name }")'
