"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_endcut_mngt import StrEndcutMngt
from pycatia3dx.structure.str_openings import StrOpenings
from pycatia3dx.structure.str_openings_mgr import StrOpeningsMgr
from pycatia3dx.structure.str_openings_on_profile import StrOpeningsOnProfile
from pycatia3dx.structure.str_profile_limit_mngt import StrProfileLimitMngt
from pycatia3dx.structure.str_profile_sub_element_mngt import StrProfileSubElementMngt
from pycatia3dx.structure.str_section_mngt import StrSectionMngt
from pycatia3dx.structure.str_slots import StrSlots


class StructureProfile(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StructureProfile
                | 
                | Object to manage Structure Functional Modeler Profile.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def profile_sub_elements(self) -> StrProfileSubElementMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProfileSubElements() As StrProfileSubElementMngt (Read
                | Only)
                |     Returns the StrProfileSubElementMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfileSubElementMngt object of this
                |              Profile.
                |              
                | 
                |              Set oObjSddProfileSubElementMngt = iObjSddStiffener.ProfileSubElements

        :return: StrProfileSubElementMngt
        """

        return StrProfileSubElementMngt(self.com_object.ProfileSubElements)

    @property
    def profile_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProfileType() As CATStrProfileMode
                |     Returns or sets the Profile's type.
                |     Legal values :
                |     - catStrProfileModePtLength : profile defined by a point and a length.
                |     - catStrProfileModePtLimit : profile defined by a point and a limit.
                |     - catStrProfileModePts : straight profile between two points.
                |     - catStrProfileModeCrv : profile on a curve and optionally a reference surface. a spec point type or a point on curve.
                |     - catStrProfileModeSurf2Crvs : profile by the intersection of a surface and two curves.
                |     - catStrProfileModeSurfSurf : profile define by the intersection of two surfaces. (default)
                |     - catStrProfileModeOnOpening : profile on the edges of a Panel Opening.
                |     - catStrProfileModeOnLimits : profile on the edges of Panel limits.
                | 
                |     Example:
                | 
                | 
                |              This example sets the profile's type 
                |              ObjSfdStiffener.ProfileType = catStrProfileModePtLength

        :return: CATStrProfileMode
        """

        return self.com_object.ProfileType

    @profile_type.setter
    def profile_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ProfileType = value

    @property
    def str_endcut_mngt(self) -> StrEndcutMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrEndcutMngt() As StrEndcutMngt (Read Only)
                |     Returns the StrEndcutMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrEndcutMngt object of the
                |              StrProfile.
                |              
                | 
                |              Set ObjStrEndcutMngt = ObjStrProfile.StrEndcutMngt

        :return: StrEndcutMngt
        """

        return StrEndcutMngt(self.com_object.StrEndcutMngt)

    @property
    def str_openings_mgr(self) -> StrOpeningsMgr:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrOpeningsMgr() As StrOpeningsMgr (Read Only)
                |     Returns the StrOpeningsMgr object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrOpeningsMgr the StrOpeningsMgr
                |              object
                |              of the SfdStiffener.
                |              
                | 
                |             Dim ObjStrOpeningsMgr As StrOpeningsMgr
                |              Set ObjStrOpeningsMgr = iObjSfdStiffener.StrOpeningsMgr

        :return: StrOpeningsMgr
        """

        return StrOpeningsMgr(self.com_object.StrOpeningsMgr)

    @property
    def str_profile_limit_mngt(self) -> StrProfileLimitMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrProfileLimitMngt() As StrProfileLimitMngt (Read
                | Only)
                |     Returns the StrProfileLimitMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrProfileLimitMngt object of the
                |              StrProfile.
                |              
                | 
                |              Set ObjStrProfileLimitMngt = ObjSfdStiffener.StrProfileLimitMngt

        :return: StrProfileLimitMngt
        """

        return StrProfileLimitMngt(self.com_object.StrProfileLimitMngt)

    @property
    def str_section_mngt(self) -> StrSectionMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrSectionMngt() As StrSectionMngt (Read Only)
                |     Returns the StrSectionMngt object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves StrSectionMngt object of the
                |              StrProfile.
                |              
                | 
                |              Set ObjStrSectionMngt = ObjSfdStiffener.StrSectionMngt

        :return: StrSectionMngt
        """

        return StrSectionMngt(self.com_object.StrSectionMngt)

    @property
    def str_slots(self) -> StrSlots:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrSlots() As StrSlots (Read Only)
                |     Returns the Slots that are inside this object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the StrSlots object.
                |              
                | 
                |               Dim ListOfSlots As StrSlots
                |               Set ListOfSlots = ObjSfdStiffener.StrSlots

        :return: StrSlots
        """

        return StrSlots(self.com_object.StrSlots)

    def get_canonic_support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCanonicSupport() As Reference
                |     Returns the canonic Trace of this Profile.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves canonic support of this
                |              profile.
                |              
                | 
                |               Set RefCanonicSupp = ObjStrProfile.GetCanonicSupport

        :return: Reference
        """
        return Reference(self.com_object.GetCanonicSupport())

    def get_delimited_support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDelimitedSupport() As Reference
                |     Returns the delimited Trace of this Profile.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves delimited support of this
                |              profile.
                |              
                | 
                |               Set RefDelimitedSupp = ObjStrProfile.GetDelimitedSupport

        :return: Reference
        """
        return Reference(self.com_object.GetDelimitedSupport())

    def get_openings(self, i_type: int) -> StrOpenings:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOpenings(long iType) As StrOpenings
                |     Returns the list of Openings that are inside this object.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of Opening you want to retrieve:
                |             - 0: All
                |             - 1: Openings piercing the Plates inside the
                |             OpeningPlateSet
                |             - 2: Openings piercing the Plates and interrupting the Profiles
                |             inside the OpeningPlateProfileSet
                |             - 3: Openings piercing the Profile inside the OpeningProfileSet
                |             
                | 
                |     Example:
                | 
                |          
                | 
                |              This example retrieves all type of Openings
                |              
                | 
                |              Dim ObjStrOpenings As StrOpenings
                |              Set ObjStrOpenings = ObjSfdStiffener.GetOpenings(0)

        :param int i_type:
        :return: StrOpenings
        """
        return StrOpenings(self.com_object.GetOpenings(i_type))

    def get_openings_on_profile(self, i_type: int) -> StrOpeningsOnProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOpeningsOnProfile(long iType) As StrOpeningsOnProfile
                |     Returns openings on this Profile.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of Opening you want to retreive:
                |             - 0: All
                |             - 1: Openings piercing the Plates inside the
                |             OpeningPlateSet
                |             - 2: Openings piercing the Plates and interrupting the Profiles
                |             inside the OpeningPlateProfileSet
                |             - 3: Openings piercing the Profile inside the OpeningProfileSet
                |             
                | 
                |     Example:
                | 
                | 
                |              This example retrieves openings on this profile.
                |              
                | 
                |               Set ObjStrOpeningsOnProfile = iObjSfdStiffener.GetOpeningsOnProfile

        :param int i_type:
        :return: StrOpeningsOnProfile
        """
        return StrOpeningsOnProfile(self.com_object.GetOpeningsOnProfile(i_type))

    def __repr__(self):
        return f'StructureProfile(name="{self.name}")'
