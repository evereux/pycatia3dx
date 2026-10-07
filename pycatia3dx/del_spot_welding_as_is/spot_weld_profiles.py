"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.del_spot_welding_as_is.spot_weld_profile import SpotWeldProfile
from pycatia3dx.types.general import CATVariant


class SpotWeldProfiles(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SpotWeldProfiles
                | 
                | Represents an object that is a collection of Spot weld Profiles Role: Each Spot
                | Weld profile consists of several parameters.
                | It is possible to add or remove a Spot weld profile from a list as well as to
                | access an individual Spot weld profile based on its index or its
                | name.
                | 
                | See also:
                |     SpotWeldProfile
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SpotWeldProfile)
        self.com_object = com_object

    def create_profile(self, i_name: str) -> SpotWeldProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateProfile(CATBSTR iName) As SpotWeldProfile
                |     Creates a new Spot profile
                | 
                |     Parameters:
                | 
                |         iName,
                |             Spot Weld Profile name 
                |         oProfile,
                |             Spot Weld Profile 
                | 
                |     Example:
                | 
                |          
                | 
                |           Dim MySWProfileFactory as SpotWeldProfiles
                |           Dim MySWProfile as SpotWeldProfile
                |           Dim MyProfileName as CATBSTR
                |           Set ProfileName = "MySWProfile"
                |           MySWProfile = MySWProfileFactory.CreateProfile(MyProfileName)

        :param str i_name:
        :return: SpotWeldProfile
        """
        return SpotWeldProfile(self.com_object.CreateProfile(i_name))

    def item(self, i_index: CATVariant) -> SpotWeldProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SpotWeldProfile
                |     Returns a reference to a particular spot profile based on its index or its
                |     name
                | 
                |     Parameters:
                | 
                |         iIndex,
                |             index or name os Spot Weld Profile 
                |         oProfile,
                |             Spot Weld profile 
                | 
                |     Example:
                | 
                |          
                | 
                |           Dim MySWProfile as SpotWeldProfile
                |           Dim iIndex as CATVariant
                |           If  MySWProfileFactory IsNot  Nothing  Then 
                |           Set MySWProfile = MySWProfileFactory.Item(iIndex)
                |           End If

        :param CATVariant i_index:
        :return: SpotWeldProfile
        """
        return SpotWeldProfile(self.com_object.Item(i_index))

    def remove(self, i_profile: SpotWeldProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(SpotWeldProfile iProfile)
                |     Removes an applicative profile from collection
                | 
                |     Parameters:
                | 
                |         iProfile,
                |             Spot weld Profile 
                | 
                |     Example:
                | 
                |          
                | 
                |           Dim MySWProfile as SpotWeldProfile
                |           Dim MyProfileName as CATBSTR = "MySWProfile"
                |           MySWProfile = SpotWeldProfiles.CreateProfile(MyProfileName)
                |           If  MySWProfile  IsNot  Nothing  Then 
                |           MySWProfileFactory.Remove(MySWProfile)
                |           End If

        :param SpotWeldProfile i_profile:
        :return: None
        """
        return self.com_object.Remove(i_profile.com_object)

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAll()
                |     Removes all Spot weld profiles from collection
                | 
                |     Example:
                |
                |           If  MySWProfileFactory IsNot  Nothing  Then 
                |           MySWProfileFactory.RemoveAll()
                |           End If

        :return: None
        """
        return self.com_object.RemoveAll()

    def __getitem__(self, n: int) -> SpotWeldProfile:
        if (n + 1) > self.count:
            raise StopIteration

        return SpotWeldProfile(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SpotWeldProfile]:
        for i in range(self.count):
            yield SpotWeldProfile(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SpotWeldProfiles(name="{self.name}")'
