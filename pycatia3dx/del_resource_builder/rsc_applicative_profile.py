"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameters import Parameters
from pycatia3dx.system.any_object import AnyObject


class RscApplicativeProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscApplicativeProfile
                | 
                | Interface to manage Applicative Profiles.
                | Role: This interface provides methods to retrieve information related to
                | Applicative Profiles.
                | 
                | Example:
                | 
                |      This example code shows how to retrieve an applicative profile
                |      interface.
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
                |      ' Display the name of the profile
                |      MsgBox(" Name of selected Applicative Profile is " &
                |      applicativeProfile.Name)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def attributes(self) -> Parameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Attributes() As Parameters (Read Only)
                |     Retrieves the attributes for this profile.
                |     Attributes are the parameters which always exist for a particular profile
                |     type. Profiles in a user profile group do not have any attributes. Attributes
                |     cannot be added or removed. Only the value can be changed. If there are no
                |     attributes, this function succeeds and returns an empty list of
                |     parameters.
                | 
                |     Example:
                | 
                |      ' Get the profile attributes for this profile
                |      Dim profileAttributes As KnowledgewareTypeLib.Parameters = applicativeProfile.Attributes
                | 
                |      ' Display the profile attributes
                |      If profileAttributes IsNot Nothing Then
                |          For Each Param As KnowledgewareTypeLib.Parameter In
                |          profileAttributes
                |              Dim paramName As String = Param.Name
                |              MsgBox(Param.Name & " = " & Param.ValueAsString)
                |          Next
                |      End If

        :return: Parameters
        """

        return Parameters(self.com_object.Attributes)

    @property
    def is_current(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsCurrent() As short (Read Only)
                |     Retrieves whether this profile is the current profile or
                |     not.
                |     See RscApplicativeProfilesGroup.CurrentProfile
                | 
                |     Example:
                | 
                |      ' Determine if the profile is the current profile
                |      Dim isCurrent As Short = applicativeProfile.IsCurrent
                | 
                |      If isCurrent = 0 Then
                |         MsgBox "The profile is not the current profile"
                |      Else
                |         MsgBox "The profile is the current profile"
                |      End If

        :return: int
        """

        return self.com_object.IsCurrent

    @property
    def is_user_defined(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsUserDefined() As short (Read Only)
                |     Retrieves whether this profile is user defined or not.
                |     User defined profiles do not have Attributes and groups of user defined
                |     profiles are managed by RscUserProfilesMgr. Profiles and profile groups which
                |     are not user defined are managed by
                |     RscApplicativeProfilesMgr.
                | 
                |     Example:
                | 
                |      ' Determine if the profile is user defined
                |      Dim isCurrent As Short = applicativeProfile.IsUserDefined
                | 
                |      If isCurrent = 0 Then
                |         MsgBox "The profile is not user defined"
                |      Else
                |         MsgBox "The profile is user defined"
                |      End If

        :return: int
        """

        return self.com_object.IsUserDefined

    @property
    def user_params(self) -> Parameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserParams() As Parameters (Read Only)
                |     Retrieves the user defined parameters for this profile.
                |     If there are no user parameters, this function succeeds and returns an
                |     empty list of parameters.
                | 
                |     Example:
                | 
                |      ' Get user defined params on this profile
                |      Dim userParams As KnowledgewareTypeLib.Parameters = applicativeProfile.UserParams
                | 
                |      ' Display the user parameters
                |      If userParams IsNot Nothing Then
                |          For Each Param As KnowledgewareTypeLib.Parameter In
                |          userParams
                |              Dim paramName As String = Param.Name
                |              MsgBox(Param.Name & " = " & Param.ValueAsString)
                |          Next
                |      End If

        :return: Parameters
        """

        return Parameters(self.com_object.UserParams)

    def __repr__(self):
        return f'RscApplicativeProfile(name="{ self.name }")'
