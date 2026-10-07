"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_arc_welding_use.arc_weld_profile import ArcWeldProfile
from pycatia3dx.types.general import CATVariant


class ArcWeldProfileFactory(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArcWeldProfileFactory
                | 
                | Represents a factory whose primary purpose is to create and delete an arc weld
                | profile Role: A Section interface allows access to weld parameters that are
                | specific for a particular section of weld trajectory.
                | There are three such sections - Start Weld, Weld and End Weld section. Each
                | section contains a reference to a particular set of weld
                | parameters.
                | 
                | See also:
                |     ArcWeldProfile, ArcWeldCSPProfiles
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ArcWeldProfile)
        self.com_object = com_object

    def create_profile(self, i_name: str) -> ArcWeldProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateProfile(CATBSTR iName) As ArcWeldProfile
                |     Creates an arc weld profile
                | 
                |     Parameters:
                | 
                |         DELMIARscApplicativeProfile
                |             Name to be assigned to the profile 
                |         DELMIAArcWeldProfile
                |             Arc Weld profile that gets created by the arc weld factory. Profile
                |             is created on the MCA (robot controller).
                | 
                |             Example:
                |                 The following example creates an arc weld profile by using an
                |                 arc welding factory
                | 
                |                   ArcWeldProfileProfile.CreateProfile
                |                   MyArcWeldProfile

        :param str i_name:
        :return: ArcWeldProfile
        """
        return ArcWeldProfile(self.com_object.CreateProfile(i_name))

    def item(self, i_index: CATVariant) -> ArcWeldProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As ArcWeldProfile
                |     Returns a reference to a particular ARW profile based on its index or its
                |     name
                | 
                |     Parameters:
                | 
                |         CATVariant
                |             Index (1-based) or controller-specific profile name
                |             
                |         DELMIARscApplicativeProfile
                |             CSP profile
                | 
                |             Example:
                |                 The following example returns a reference to a particular CSP
                |                 profile:
                | 
                |                   DELMIAArcWeldProfile MyProfile = ArcWeldProfileFactory.Item(1)

        :param CATVariant i_index:
        :return: ArcWeldProfile
        """
        return ArcWeldProfile(self.com_object.Item(i_index))

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAll()
                |     Removes all arc weld profiles
                | 
                |     Example:
                |         The following example deletes all arc weld profiles by using an arc
                |         welding factory
                | 
                |           ArcWeldProfileProfile.RemoveAll()

        :return: None
        """
        return self.com_object.RemoveAll()

    def remove_profile(self, o_profile: ArcWeldProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveProfile(ArcWeldProfile oProfile)
                |     Removes an arc weld profile
                | 
                |     Parameters:
                | 
                |         DELMIAArcWeldProfile
                |             Arc Weld profile that gets deleted by the arc weld factory. Profile
                |             is stored on MCA (robot controller) and is deleted off
                |             it.
                | 
                |             Example:
                |                 The following example deletes an arc weld profile by using an
                |                 arc welding factory
                | 
                |                   ArcWeldProfileProfile.RemoveProfile
                |                   MyArcWeldProfile

        :param ArcWeldProfile o_profile:
        :return: None
        """
        return self.com_object.RemoveProfile(o_profile.com_object)

    def __getitem__(self, n: int) -> ArcWeldProfile:
        if (n + 1) > self.count:
            raise StopIteration

        return ArcWeldProfile(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[ArcWeldProfile]:
        for i in range(self.count):
            yield ArcWeldProfile(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'ArcWeldProfileFactory(name="{self.name}")'
