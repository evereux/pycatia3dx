"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.del_resource_builder.rsc_applicative_profile import RscApplicativeProfile
from pycatia3dx.types.general import CATVariant


class RscApplicativeProfilesGroup(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     RscApplicativeProfilesGroup
                | 
                | Interface to manage Applicative Profile Groups.
                | Role: This interface provides methods to get/set information related to an
                | Applicative Profile Group.
                | 
                | Example:
                | 
                |      This example code shows how to retrieve an applicative profile
                |      group.
                | 
                |      The examples here are written in Visual Studio Tools for Applications
                |      (VSTA) VB.NET
                |      
                | 
                |      ' First select an applicative profile
                |      Dim selector As INFITF.Selection = CATIA.ActiveEditor.Selection
                |      Dim type(0) As Object
                |      type(0) = "RscApplicativeProfile"
                |      selector.SelectElement2(type, "Select AP", False)
                |      Dim applicativeProfile As DELResourceBuilderIDLTypeLib.RscApplicativeProfile = selector.Item(1).Value
                | 
                |      ' Retrieve the parent of the applicative object (the
                |      group)
                |      Dim applicativeProfileGroup As DELResourceBuilderIDLTypeLib.RscApplicativeProfilesGroup = applicativeProfile.Parent
                | 
                |      ' Get the name of the profile group and display it
                |      Dim name As String = "Name of Applicative Profile Group is " & applicativeProfileGroup.Name
                |      MsgBox(name)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=RscApplicativeProfile)
        self.com_object = com_object

    @property
    def current_profile(self) -> RscApplicativeProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentProfile() As RscApplicativeProfile
                |     Gets/sets the current profile.
                |     The current profile may not be set, in which case the returned values is
                |     NULL (or Nothing in VB).
                | 
                |     Example:
                | 
                |      ' Retrieve the current profile and display its name
                |      Dim currentProfile As DELResourceBuilderIDLTypeLib.RscApplicativeProfile = applicativeProfileGroup.CurrentProfile
                | 
                |      If currentProfile IsNot Nothing Then
                |         MsgBox(" The current profile is named " &
                |         currentProfile.Name
                |      Else
                |         MsgBox "There is no current profile"
                |      End If
                | 
                |      ' Set the current profile
                |      applicativeProfileGroup.CurrentProfile = newCurrentProfile

        :return: RscApplicativeProfile
        """

        return RscApplicativeProfile(self.com_object.CurrentProfile)

    @current_profile.setter
    def current_profile(self, value: RscApplicativeProfile):
        """
        :param RscApplicativeProfile value:
        """

        self.com_object.CurrentProfile = value

    @property
    def profile_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProfileType() As CATBSTR (Read Only)
                |     Retrieves the profile type for this applicative profile
                |     group.
                |     A group has both a name and a type. The Name is what is displayed in the
                |     user interface. The type is what is used to create, remove, or retrieve the
                |     group from the manager.
                | 
                |     Example:
                | 
                |      ' Retrieve the profile group type and display it.
                |      Dim profileType As String = applicativeProfileGroup.ProfileType
                | 
                |      MsgBox(" Profile Type is " & profileType)

        :return: str
        """

        return self.com_object.ProfileType

    def build_profile_instance(self, i_name: str) -> RscApplicativeProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func BuildProfileInstance(CATBSTR iName) As
                | RscApplicativeProfile
                |     Creates a new profile instance in this applicative profile
                |     group.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the new profile instance. The name must be
                |             unique.
                | 
                |             Example:
                | 
                |              ' Create a new applicative profile in this applicative profile
                |              group.
                |              Dim newProfileInstance As DELResourceBuilderIDLTypeLib.RscApplicativeProfile = applicativeProfileGroup.BuildProfileInstance("MyNewProfile")
                | 
                |              If newProfileInstance IsNot Nothing Then
                |                  Dim temp As String = newProfileInstance.Name
                |                  MsgBox(" BuildProfileInstance OK and the name is " &
                |                  temp)
                |              End If

        :param str i_name:
        :return: RscApplicativeProfile
        """
        return RscApplicativeProfile(self.com_object.BuildProfileInstance(i_name))

    def get_template_profile(self) -> RscApplicativeProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTemplateProfile() As RscApplicativeProfile
                |     Retrieves the template profile for this applicative profile
                |     group.
                |     The template profile contains user parameters and their default values. The
                |     user parameters on the template profile will be added to all new profile
                |     instances.
                | 
                |     Example:
                | 
                |      ' Retrieve the template profile for this applicative profile
                |      group.
                |      Dim templateProfile As DELResourceBuilderIDLTypeLib.RscApplicativeProfile = applicativeProfileGroup.GetTemplateProfile
                | 
                |      If templateProfile IsNot Nothing Then
                |          MsgBox(" Found the template profile" )
                |      End If

        :return: RscApplicativeProfile
        """
        return RscApplicativeProfile(self.com_object.GetTemplateProfile())

    def item(self, i_index: CATVariant) -> RscApplicativeProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As RscApplicativeProfile
                |     Retrieves a profile using its index or its name.
                |     Can also use CATIACollection::GetItem to get the profile by
                |     name.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the profile to retrieve from the
                |             collection of profiles. As a number, this index is the index of the profile in
                |             the collection. The index of the first parameter in the collection is 1, and
                |             the index of the last parameter is Count. As a string, it is the name you
                |             assigned to the profile using the RscApplicativeProfile.Name property or with
                |             RscApplicativeProfile.BuildProfileInstance when creating the profile.
                |             
                | 
                |     Returns:
                |         profile retrieved
                | 
                |         Examples:
                | 
                |          ' Retrieve an applicative profile using an index
                |          Dim foundProfile As DELResourceBuilderIDLTypeLib.RscApplicativeProfile = applicativeProfileGroup.Item(1)
                | 
                |          If foundProfile IsNot Nothing Then
                |              Dim profileName As String = foundProfile.Name
                |              MsgBox(" Got the profile using index 1, and the name is " &
                |              profileName)
                |          End If
                | 
                |          ' Retrieve an applicative profile using a name
                |          Dim foundProfile As DELResourceBuilderIDLTypeLib.RscApplicativeProfile = applicativeProfileGroup.Item("ApplicativeProfile.1")
                | 
                |          If foundProfile IsNot Nothing Then
                |              Dim profileName As String = foundProfile.Name
                |              MsgBox(" Got the profile using its name.  For a sanity check, the
                |              name is " & profileName)
                |          End If

        :param CATVariant i_index:
        :return: RscApplicativeProfile
        """
        return RscApplicativeProfile(self.com_object.Item(i_index))

    def remove_profile(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveProfile(CATBSTR iName)
                |     Removes (and deletes) an existing profile from applicative profile
                |     group.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the profile instance to delete.
                | 
                |             Example:
                | 
                |              ' Remove/delete an existing applicative profile from this
                |              applicative profile group.
                |             applicativeProfileGroup.Remove("AnExistingApplicativeProfile")

        :param str i_name:
        :return: None
        """
        return self.com_object.RemoveProfile(i_name)

    def __repr__(self):
        return f'RscApplicativeProfilesGroup(name="{self.name}")'
