"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.del_resource_builder.rsc_applicative_profiles_group import RscApplicativeProfilesGroup
from pycatia3dx.types.general import CATVariant


class RscUserProfilesMgr(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     RscUserProfilesMgr
                | 
                | Interface to manage a collection of all User Profile Groups.
                | Role: This interface provides methods to manage all of the User Profile
                | Groups.
                | 
                | Example:
                | 
                |      This example code shows how to retrieve a User Profile
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
                |      Dim userProfileGroup As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesGroup = applicativeProfile.Parent
                | 
                |       ' Get the manager from the group
                |      Dim userProfileManager As DELResourceBuilderIDLTypeLib.RscUserProfilesManager = userProfileGroup.Parent
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def build_user_group(self, i_name: str) -> RscApplicativeProfilesGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func BuildUserGroup(CATBSTR iName) As
                | RscApplicativeProfilesGroup
                |     Creates a new user profile group.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the new user group.
                | 
                |             Example:
                | 
                |              ' Create a new user profile group.
                |              Dim newGroup As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesGroup = userProfileManager.BuildUserGroup("MyUserProfileGroup")
                |              If newGroup IsNot Nothing Then
                |                  Dim temp As String = newGroup.Name
                |                  MsgBox(" BuildProfileInstance OK and the name is " &
                |                  temp)
                |              End If

        :param str i_name:
        :return: RscApplicativeProfilesGroup
        """
        return RscApplicativeProfilesGroup(self.com_object.BuildUserGroup(i_name))

    def item(self, i_index: CATVariant) -> RscApplicativeProfilesGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As RscApplicativeProfilesGroup
                |     Retrieves a profile group using its index or its name.
                |     Can also use CATIACollection::GetItem to get the profile group by
                |     name.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the profile group to retrieve from the
                |             collection of groups. As a number, this is the index of the group in the
                |             collection. The index of the first group in the collection is 1 and the index
                |             of the last group is Count. As a string, it is the type of the group to
                |             retrieve. 
                | 
                |     Returns:
                |         profile retrieved
                | 
                |         Example:
                | 
                |          ' Retrieve a user profile group by index
                |          Dim profileGroup As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesGroup = userProfileManager.Item(1)
                |          If profileGroup IsNot Nothing Then
                |              Dim name As String = profileGroup.Name
                |              MsgBox(" Retrieved the first user profile group by index , and the
                |              name is: " & name)
                |          End If
                | 
                |          ' Retrieve a user profile group by name
                |          Dim profileGroup As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesGroup = userProfileManager.Item("MyUserProfileGroup")
                |          If profileGroup IsNot Nothing Then
                |              Dim name As String = profileGroup.Name
                |              MsgBox(" Retrieved a user profile group by its name, and the name
                |              is: " & name)
                |          End If

        :param CATVariant i_index:
        :return: RscApplicativeProfilesGroup
        """
        return RscApplicativeProfilesGroup(self.com_object.Item(i_index))

    def remove_user_group(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveUserGroup(CATBSTR iName)
                |     Removes (and deletes) a user profile group.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the user group to delete.
                | 
                |             Example:
                | 
                |              ' Remove/delete a profile group.
                |             userProfileManager.RemoveUserGroup("MyProfileGroup")

        :param str i_name:
        :return: None
        """
        return self.com_object.RemoveUserGroup(i_name)

    def __repr__(self):
        return f'RscUserProfilesMgr(name="{ self.name }")'
