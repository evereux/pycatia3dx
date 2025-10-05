"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscGenericProfilesMgr(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscGenericProfilesMgr
                | 
                | Interface to access the controller generic profiles.
                | Role: This interface provides methods to access the controller generic
                | profile.
                | This API retrieves the default generic profiles on the controller. There are
                | used before any simulation and must be modified before the simulation
                | starts.
                | 
                | Example:
                |     Let assume there is a robot opened as a root entity in a given
                |     editor.
                | 
                |      Dim MainResource As Variant
                |      Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |      Dim MySelectedResource As RscControllerAttributesAccess
                |      Set MySelectedResource = MainResource.GetItem("CAARscControllerAttributesAccess")
                |      
                |      If Not MySelectedResource Is Nothing Then
                |        Dim MyControllerData As RscGenericProfilesMgr
                |        MyControllerData = MySelectedResource.RetrieveControllerAttributesObject
                |      End If
                | 
                | See also:
                |     RscControllerAttributesAccess
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_generic_profile(self, i_profile_type: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateGenericProfile(DELRscControllerGenericProfilesType iProfileType) As
                | AnyObject
                |     Create a generic profile.
                | 
                |     Example:
                | 
                |      Dim MyToolProfile As RscToolProfile
                |      Set RscToolProfile = MyControllerData.CreateGenericProfile(DELRscControllerGenericProfilesType_Tool)

        :param int i_profile_type:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateGenericProfile(i_profile_type))

    def get_current_generic_profile(self, i_profile_type: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCurrentGenericProfile(DELRscControllerGenericProfilesType iProfileType)
                | As CATBSTR
                |     Retrieves the current generic profile.
                | 
                |     Example:
                | 
                |      Dim NewCurrentID As String
                |     
NewCurrentID.GetCurrentGenericProfile9DELRscControllerGenericProfilesType_Tool)

        :param int i_profile_type:
        :return: str
        """
        return self.com_object.GetCurrentGenericProfile(i_profile_type)

    def get_generic_profile_by_name(self, i_profile_type: int, i_profile_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGenericProfileByName(DELRscControllerGenericProfilesType
                | iProfileType,CATBSTR iProfileName) As AnyObject
                |     Retrieves a profile by its name.
                | 
                |     Example:
                | 
                |      Dim MyToolProfileID As String
                |      MyToolProfileID = "TEST"
                |      Dim MyToolProfile As RscToolProfile
                |      Set MyToolProfile = MyControllerData.GetGenericProfileByName DELRscControllerGenericProfilesType_Tool,MyToolProfileID

        :param int i_profile_type:
        :param str i_profile_name:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetGenericProfileByName(i_profile_type, i_profile_name))

    def get_generic_profile_count(self, i_profile_type: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGenericProfileCount(DELRscControllerGenericProfilesType iProfileType)
                | As long
                |     Retrieves the number of generic profiles for a given type.
                | 
                |     Example:
                | 
                |      Dim NumberToolProfiles As Integer
                |      NumberToolProfiles = MyControllerData.GetGenericProfileCount(DELRscControllerGenericProfilesType_Tool)

        :param int i_profile_type:
        :return: int
        """
        return self.com_object.GetGenericProfileCount(i_profile_type)

    def get_generic_profile_list(self, i_profile_type: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGenericProfileList(DELRscControllerGenericProfilesType iProfileType) As
                | CATSafeArrayVariant
                |     Retrieves the list of generic profiles for a given type.
                | 
                |     Example:
                | 
                |      Dim ToolProfilesList 'array for VBScript
                |      ToolProfilesList = MyControllerData.GetGenericProfileList(DELRscControllerGenericProfilesType_Tool)
                |      Dim ListIndex As Double
                |      For II = LBound(ToolProfilesList) To UBound(ToolProfilesList)
                |          Dim MyToolProfile As RscToolProfile
                |          MyToolProfile = ToolProfilesList(II)
                |          'uncomment next line to display value
                |          'MsgBox ("ListIndex:" & CStr(ListIndex))
                |      Next
                | 
                |     Note: previous example is for CATScript. In case of VBA, the syntax is
                |     slightly different for array declaration:
                | 
                |      Dim ToolProfilesList() As Variant 'array for VBA
                |      ToolProfilesList = MyControllerData.GetGenericProfileList(DELRscControllerGenericProfilesType_Tool)

        :param int i_profile_type:
        :return: tuple
        """
        return self.com_object.GetGenericProfileList(i_profile_type)

    def has_generic_profile(self, i_profile_type: int, i_profile_name: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasGenericProfile(DELRscControllerGenericProfilesType iProfileType,CATBSTR
                | iProfileName) As boolean
                |     Check the existence of a given generic profile
                | 
                |     Example:
                | 
                |      Dim bTest As Boolean
                |      Dim NewCurrentID As String
                |      NewCurrentID = "TEST"
                |      bTest = MyControllerData.HasGenericProfile DELRscControllerGenericProfilesType_Tool, NewCurrentID
                | 
                |     Note: previous example is for CATScript. In case of VBA, the syntax is
                |     significantly different:
                | 
                |      Dim NewCurrentID As String
                |      NewCurrentID = "TEST"
                |      MyControllerData.HasGenericProfile
                |      DELRscControllerGenericProfilesType_Tool, NewCurrentID
                | 
                |     Note: previous example is for CATScript. In case of VBA, the syntax is
                |     significantly different:
                | 
                |      Dim MyObj 'need to change typing due to early typing for
                |      VBA
                |      Set MyObj = MyControllerData
                |      bTest = MyObj.HasGenericProfile DELRscControllerGenericProfilesType_Tool, NewCurrentID

        :param int i_profile_type:
        :param str i_profile_name:
        :return: bool
        """
        return self.com_object.HasGenericProfile(i_profile_type, i_profile_name)

    def remove_generic_profile(self, i_profile_type: int, i_profile_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RemoveGenericProfile(DELRscControllerGenericProfilesType
                | iProfileType,CATBSTR iProfileName) As long
                |     Remove a generic profile by name.
                | 
                |     Example:
                | 
                |      Dim NewCurrentID As String
                |      NewCurrentID = "TEST"
                |      MyControllerData.RemoveGenericProfile
                |      DELRscControllerGenericProfilesType_Tool, NewCurrentID
                | 
                |     Note: previous example is for CATScript. In case of VBA, the syntax is
                |     significantly different:
                | 
                |      Dim NewCurrentID As String
                |      NewCurrentID = "TEST"
                |      MyControllerData.RemoveGenericProfile
                |      DELRscControllerGenericProfilesType_Tool, NewCurrentID
                | 
                |     Note: previous example is for CATScript. In case of VBA, the syntax is
                |     significantly different:
                | 
                |      Dim MyObj 'need to change typing due to early typing for
                |      VBA
                |      Set MyObj = MyControllerData
                |      MyObj.RemoveGenericProfile DELRscControllerGenericProfilesType_Tool,
                |      NewCurrentID

        :param int i_profile_type:
        :param str i_profile_name:
        :return: int
        """
        return self.com_object.RemoveGenericProfile(i_profile_type, i_profile_name)

    def set_current_generic_profile(self, i_profile_type: int, i_profile_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCurrentGenericProfile(DELRscControllerGenericProfilesType
                | iProfileType,CATBSTR iProfileName)
                |     Set the current generic profile.
                | 
                |     Example:
                | 
                |      Dim NewCurrentID As String
                |      NewCurrentID = "TEST"
                |      MyControllerData.SetCurrentGenericProfile
                |      DELRscControllerGenericProfilesType_Tool, NewCurrentID
                | 
                |     Note: previous example is for CATScript. In case of VBA, the syntax is
                |     significantly different:
                | 
                |      Dim NewCurrentID As String
                |      NewCurrentID = "TEST"
                |      MyControllerData.SetCurrentGenericProfile
                |      DELRscControllerGenericProfilesType_Tool, NewCurrentID
                |      Dim MyObj 'need to change typing due to early typing for
                |      VBA
                | 
                |     Note: previous example is for CATScript. In case of VBA, the syntax is
                |     significantly different:
                | 
                |      Set MyObj = MyControllerData
                |      MyObj.SetCurrentGenericProfile DELRscControllerGenericProfilesType_Tool,
                |      NewCurrentID

        :param int i_profile_type:
        :param str i_profile_name:
        :return: None
        """
        return self.com_object.SetCurrentGenericProfile(i_profile_type, i_profile_name)

    def __repr__(self):
        return f'RscGenericProfilesMgr(name="{ self.name }")'
