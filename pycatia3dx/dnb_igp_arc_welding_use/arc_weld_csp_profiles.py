"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_resource_builder.rsc_applicative_profile import RscApplicativeProfile
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class ArcWeldCSPProfiles(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ArcWeldCSPProfiles
                | 
                | Represents an object that is a collection of Controller-Specific Profiles Role:
                | Each section of Arc Weld profile consists of several parameters one of them
                | being CSP profiles collection.
                | It is possible to add or remove a CSP profile from a list as well as to access
                | an individual CSP profile based on its name of its index.
                | 
                | See also:
                |     DELMIAArcWeldSection, ArcWeldProfile
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_profile: RscApplicativeProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(RscApplicativeProfile iProfile)
                |     Adds an applicative profile to collection
                | 
                |     Parameters:
                | 
                |         DELMIARscApplicativeProfile
                |             CSP profile
                | 
                |             Example:
                |                 The following example returns a collection of
                |                 profiles:
                | 
                |                   ArcWeldProfile.StartWeld.Profiles.Add
                |                   (MyCSPProfile)

        :param RscApplicativeProfile i_profile:
        :return: None
        """
        return self.com_object.Add(i_profile.com_object)

    def item(self, i_index: CATVariant) -> RscApplicativeProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As RscApplicativeProfile
                |     Returns a reference to a particular CSP profile based on its index or its
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
                |                   DELMIARscApplicativeProfile MyCSPProfile = ArcWeldProfile.StartWeld.Profiles.Item (1)

        :param CATVariant i_index:
        :return: RscApplicativeProfile
        """
        return RscApplicativeProfile(self.com_object.Item(i_index))

    def remove(self, i_profile: RscApplicativeProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(RscApplicativeProfile iProfile)
                |     Removes an applicative profile from collection
                | 
                |     Parameters:
                | 
                |         DELMIARscApplicativeProfile
                |             CSP profile
                | 
                |             Example:
                |                 The following example removes a CSP profile from
                |                 collection:
                | 
                |                   ArcWeldProfile.StartWeld.Profiles.Remove/font>
                |                   (MyCSPProfile)

        :param RscApplicativeProfile i_profile:
        :return: None
        """
        return self.com_object.Remove(i_profile.com_object)

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAll()
                |     Removes all CSP profiles from collection
                | 
                |     Parameters:
                | 
                |         DELMIARscApplicativeProfile
                |             CSP profile
                | 
                |             Example:
                |                 The following example removes all CSP profiles from
                |                 collection:
                | 
                |                   ArcWeldProfile.StartWeld.Profiles.RemoveAll 

        :return: None
        """
        return self.com_object.RemoveAll()

    def __repr__(self):
        return f'ArcWeldCspProfiles(name="{ self.name }")'
