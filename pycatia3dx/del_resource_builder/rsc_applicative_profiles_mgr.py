"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.del_resource_builder.rsc_applicative_profiles_group import RscApplicativeProfilesGroup
from pycatia3dx.types.general import CATVariant


class RscApplicativeProfilesMgr(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     RscApplicativeProfilesMgr
                | 
                | Interface to manage a collection of all Applicative Profile
                | Groups.
                | Role: This interface provides methods to manage all of the Applicative Profile
                | Groups.
                | 
                | Example:
                | 
                |      This example code shows how to retrieve an Applicative Profile
                |      Manager.
                | 
                |      The examples here are written in Visual Studio Tools for Applications
                |      (VSTA) VB.NET
                |      
                | 
                |      ' Select an applicative profile
                |      Dim selector As INFITF.Selection = CATIA.ActiveEditor.Selection
                |      Dim type(0) As Object
                |      type(0) = "RscApplicativeProfile"
                |      selector.SelectElement2(type, "Select AP", False)
                |      Dim applicativeProfile As DELResourceBuilderIDLTypeLib.RscApplicativeProfile = selector.Item(1).Value
                | 
                |      ' Get the profile's group
                |      Dim applicativeProfileGroup As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesGroup = applicativeProfile.Parent
                | 
                |      ' Get the manager from the group
                |      Dim applicativeProfileManager As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesManager = applicativeProfileGroup.Parent
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=RscApplicativeProfilesGroup)
        self.com_object = com_object

    @property
    def available_groups(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AvailableGroups() As CATSafeArrayVariant (Read Only)
                |     Get a list of all profile group types including groups which have not yet
                |     been created.
                |     To create a new group use
                |     RscApplicativeProfilesGroup.Item.
                | 
                |     Example:
                | 
                |      ' Get all the available types
                |      Dim Types() As Object = applicativeProfileManager.AvailableGroups
                |      ' Create a new group for the first type
                |      If Types.Count > 0 Then 
                |        Dim FirstType As String = Types(0)
                |        Dim Group As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesGroup = applicativeProfileManager.Item(FirstType)
                |      End If

        :return: tuple
        """

        return self.com_object.AvailableGroups

    def item(self, i_index: CATVariant) -> RscApplicativeProfilesGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As RscApplicativeProfilesGroup
                |     Retrieves a profile group using its index or its name.
                |     Can also use CATIACollection::GetItem to get the profile group by name. If
                |     the input is a string, a profile group will also be created if it doesn't
                |     exist.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the profile group to retrieve from the
                |             collection of groups. As a number, this is the index of the group in the
                |             collection. The index of the first group in the collection is 1 and the index
                |             of the last group is Count. As a string, it is the type of the group to
                |             retrieve. See RscApplicativeProfilesGroup.ProfileType.
                |             
                | 
                |     Returns:
                |         profile retrieved
                | 
                |         Examples:
                | 
                |          ' Retrieve a profile group using an index.
                |          Dim profileGroup As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesGroup = applicativeProfileManager.Item(1)
                |          If profileGroup IsNot Nothing Then
                |              Dim name As String = profileGroup.Name
                |              MsgBox(" Retrieved the first applicative profile group by index ,
                |              and the name is: " & name)
                |          End If
                | 
                |          ' Retrieve a profile group by name.
                |          Dim profileGroup As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesGroup = applicativeProfileManager.Item("GroupType")
                |          If profileGroup IsNot Nothing Then
                |              Dim name As String = profileGroup.Name
                |              MsgBox(" Retrieved an applicative profile group by its name, and
                |              the name is: " & name)
                |          End If

        :param CATVariant i_index:
        :return: RscApplicativeProfilesGroup
        """
        return RscApplicativeProfilesGroup(self.com_object.Item(i_index))

    def remove_profile_group(self, i_type: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveProfileGroup(CATBSTR iType)
                |     Removes (and deletes) an existing profile group.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the group to delete. See
                |             RscApplicativeProfilesGroup.ProfileType.
                | 
                |             Example:
                | 
                |              ' Removes/Deletes an existing applicative profile
                |              group.
                |             applicativeProfileManager.RemoveProfileGroup("AnExistingApplicativeProfileGroupType")

        :param str i_type:
        :return: None
        """
        return self.com_object.RemoveProfileGroup(i_type)

    def __getitem__(self, n: int) -> RscApplicativeProfilesGroup:
        if (n + 1) > self.count:
            raise StopIteration

        return RscApplicativeProfilesGroup(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[RscApplicativeProfilesGroup]:
        for i in range(self.count):
            yield RscApplicativeProfilesGroup(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'RscApplicativeProfilesMgr(name="{self.name}")'
