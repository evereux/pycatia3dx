"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import Variant


class RscHomePositions(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscHomePositions
                | 
                | Interface to access the home positions of a resource.
                | Role: This interface provides methods to manages home position on resource
                | having a motion controller. A home position is a predefined state of the
                | resource, used in programming. This state is characterized by the DOF values of
                | the resource. These API are specifically designated to manage home positions on
                | a given resource driven by a single mechanism.
                | 
                | Example:
                |     Let assume there is a robot opened as a root entity in a given
                |     editor.
                | 
                |     Dim MainResource As Variant
                |     Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |     Dim MyHomeResource As RscHomePositions
                |     Set MyHomeResource = MainResource.GetItem("CAARscHomePositions")
                |     If Not MyHomeResource Is Nothing Then
                | 
                |     End If
                | 
                | Note:API documentation will include sample code referring to MyHomeResource as
                | a variable of type RscHomePositions.
                | 
                | See also:
                |     RscMotionController
                | See also:
                |     DELRscJointType
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def home_position_dof_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HomePositionDOFCount() As long (Read Only)
                |     Retrieves the DOF count of the current resource. The DOF count will ignore
                |     all external axes.
                | 
                |     Returns:
                |         The number of DOF available for home position
                |         definition.
                | 
                |         Example:
                | 
                |          Dim iHomeDOFCount As Integer
                |          iHomeDOFCount = MyHomeResource.HomePositionDOFCount
                |          'uncomment next line to display value
                |          'MsgBox ("Home DOF count: " & CStr(iHomeDOFCount))

        :return: int
        """

        return self.com_object.HomePositionDOFCount

    @property
    def list_home_position_i_ds(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ListHomePositionIDs() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of home position names associated to the current
                |     resource.
                | 
                |     Returns:
                |         The list of home position name existing on the current
                |         resource.
                | 
                |         Example:
                | 
                |          Dim ListHomeID 'array for VBScript
                |          ListHomeID = MyHomeResource.ListHomePositionIDs
                |          Dim NbHome As Integer
                |          NbHome = UBound(ListHomeID) + 1
                |          'uncomment next line to display value
                |          'MsgBox ("Number of home position : " & CStr(NbHome))
                |          Dim HomeID As String
                |          For II = LBound(ListHomeID) To UBound(ListHomeID)
                |            HomeID = ListHomeID(II)
                |            'uncomment next line to display value
                |            'MsgBox ("HomeID:" & HomeID)
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ListHomeID() As Variant 'array for VBA
                |          ListHomeID = MyHomeResource.ListHomePositionIDs

        :return: tuple
        """

        return self.com_object.ListHomePositionIDs

    def create_home_position(self, i_home_position_name: str, i_home_values: tuple) -> Variant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateHomePosition(CATBSTR iHomePositionName,CATSafeArrayVariant
                | iHomeValues)
                |     Create a new home position values. Values are expressed in standard SI
                |     units (meters for length and radians for angle). To identify a given dimension,
                |     Use GetHomePositionDOFType.
                |     Note:the array index starts at 0 (due to the variant array management)
                |     Note:input name must be unique and not empty or the method will
                |     fail.
                | 
                |     Parameters:
                | 
                |         iHomePositionName
                |             Name of a new home position. Must be unique and not empty.
                |             
                |         iHomeValues
                |             The list of DOF values to apply on the newly created home
                |             position.
                | 
                |             Example:
                | 
                |              Dim NewHomeValues 'array for VBScript
                |              ReDim NewHomeValues(iHomeDOFCount-1)
                |              For KK = 0 To UBound(NewHomeValues)
                |                NewHomeValues(KK) = 0.5
                |              Next
                |              MyHomeResource.CreateHomePosition HomeID,
                |              NewHomeValues
                | 
                |             Note: previous example is for CATScript. In case of VBA, the syntax
                |             is significantly different:
                | 
                |              Dim NewHomeValues() As Variant 'array for VBA
                |              ReDim NewHomeValues(iHomeDOFCount-1)
                |              For KK = 0 To UBound(NewHomeValues)
                |                NewHomeValues(KK) = 0.5
                |              Next
                |              Dim MyObj 'need to change typing due to early typing for
                |              VBA
                |              Set MyObj = MyHomeResource
                |              MyObj.CreateHomePosition HomeID, NewHomeValues

        :param str i_home_position_name:
        :param tuple i_home_values:
        :return: Variant
        """
        return self.com_object.CreateHomePosition(i_home_position_name, i_home_values)

    def get_home_position_dof_type(self, i_dof_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetHomePositionDOFType(long iDOFIndex) As DELRscJointType
                |     Retrieve the type of joint for a given DOF index. The index must be within
                |     1 and SimulatedDOFCount included.
                | 
                |     Parameters:
                | 
                |         iDOFIndex
                |             DOF index. Ranges from 1 to the value returned by SimulatedDOFCount
                |             included. 
                | 
                |     Returns:
                |         The dimension of the requested DOF.
                | 
                |         Example:
                | 
                |          Dim MyHomeDOFType As DELRscJointType
                |          
                |          For JJ = 1 To iHomeDOFCount
                |              MyHomeDOFType = MyHomeResource.GetHomePositionDOFType(JJ)
                |              'uncomment next line to display value
                |              'MsgBox ("Home DOFType:" & CStr(MyHomeDOFType))
                |          Next
                | 
                |     See also:
                |         DELRscJointType

        :param int i_dof_index:
        :return: int
        """
        return self.com_object.GetHomePositionDOFType(i_dof_index)

    def get_home_position_index(self, i_home_position_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetHomePositionIndex(CATBSTR iHomePositionName) As long
                |     Remove an existing home position index. Available home position names can
                |     be retrieved through the property ListHomePositionIDs. Index starts at
                |     1.
                | 
                |     Parameters:
                | 
                |         iHomePositionName
                |             Name of an existing home position. 
                | 
                |     Returns:
                |         Index of the home position. Index starts at 1.
                | 
                |         Example:
                | 
                |          Dim iTestIndex As Integer
                |          iTestIndex = MyHomeResource.GetHomePositionIndex(HomeID)

        :param str i_home_position_name:
        :return: int
        """
        return self.com_object.GetHomePositionIndex(i_home_position_name)

    def get_home_position_values(self, i_home_position_name: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetHomePositionValues(CATBSTR iHomePositionName) As
                | CATSafeArrayVariant
                |     Retrieve the values for an existing home position. Values are expressed in
                |     standard SI units (meters for length and radians for angle). To identify a
                |     given dimension, Use GetHomePositionDOFType.
                |     Note:the array index starts at 0 (due to the variant array
                |     management)
                | 
                |     Parameters:
                | 
                |         iHomePositionName
                |             Name of a existing home position. 
                | 
                |     Returns:
                |         The list of DOF values associated with the requested home
                |         position.
                | 
                |         Example:
                | 
                |          Dim HomeValues 'array for VBScript
                |          HomeValues = MyHomeResource.GetHomePositionValues(HomeID)
                |          Dim HomeValueIndexed As Double
                |          For II = LBound(HomeValues) To UBound(HomeValues)
                |              HomeValueIndexed = HomeValues(II)
                |              'uncomment next line to display value
                |              'MsgBox ("HomeValueIndexed:" &
                |              CStr(HomeValueIndexed))
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim HomeValues() As Variant 'array for VBA
                |          HomeValues = MyHomeResource.GetHomePositionValues(HomeID)

        :param str i_home_position_name:
        :return: tuple
        """
        return self.com_object.GetHomePositionValues(i_home_position_name)

    def modify_home_position_index(self, i_home_position_name: str, i_new_home_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ModifyHomePositionIndex(CATBSTR iHomePositionName,long
                | iNewHomeIndex)
                |     Modify an existing home position index. Available home position names can
                |     be retrieved through the property ListHomePositionIDs. Index starts at 1.
                |     Method will fail if the input index is out of range.
                | 
                |     Parameters:
                | 
                |         iHomePositionName
                |             Name of an existing home position to be reordered.
                |             
                |         iNewHomeIndex
                |             Index of the new home position (must start at 1).
                | 
                |             Example:
                | 
                |              Dim iTestIndex As Integer
                |              iTestIndex = 1
                |              MyHomeResource.ModifyHomePositionIndex(HomeID)

        :param str i_home_position_name:
        :param int i_new_home_index:
        :return: None
        """
        return self.com_object.ModifyHomePositionIndex(i_home_position_name, i_new_home_index)

    def modify_home_position_name(self, i_home_position_old_name: str, i_home_position_new_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ModifyHomePositionName(CATBSTR iHomePositionOldName,CATBSTR
                | iHomePositionNewName)
                |     Modify an existing home position name. Available home position names can be
                |     retrieved through the property ListHomePositionIDs. New name must be
                |     unique.
                | 
                |     Parameters:
                | 
                |         iHomePositionOldName
                |             Name of an existing home position to be renamed. 
                |         iHomePositionNewName
                |             New name to apply to the requested home position.
                | 
                |             Example:
                | 
                |              Dim HomeID As String
                |              Dim NewHomeID As String
                |              NewHomeID = "TEST"
                |             
MyHomeResource.ModifyHomePositionName(HomeID,NewHomeID)

        :param str i_home_position_old_name:
        :param str i_home_position_new_name:
        :return: None
        """
        return self.com_object.ModifyHomePositionName(i_home_position_old_name, i_home_position_new_name)

    def remove_home_position(self, i_home_position_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveHomePosition(CATBSTR iHomePositionName)
                |     Remove an existing home position values from its name. Available home
                |     position names can be retrieved through the property
                |     ListHomePositionIDs.
                | 
                |     Parameters:
                | 
                |         iHomePositionName
                |             Name of an existing home position.
                | 
                |             Example:
                | 
                |              Dim ExistingHomeID As String
                |              MyHomeResource.RemoveHomePosition(ExistingHomeID)

        :param str i_home_position_name:
        :return: None
        """
        return self.com_object.RemoveHomePosition(i_home_position_name)

    def set_home_position_values(self, i_home_position_name: str, i_home_values: tuple) -> Variant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetHomePositionValues(CATBSTR iHomePositionName,CATSafeArrayVariant
                | iHomeValues)
                |     Modify an existing home position values. Values are expressed in standard
                |     SI units (meters for length and radians for angle). To identify a given
                |     dimension, Use GetHomePositionDOFType.
                |     Note:the array index starts at 0 (due to the variant array
                |     management)
                | 
                |     Parameters:
                | 
                |         iHomePositionName
                |             Name of a existing home position. 
                |         iHomeValues
                |             The list of DOF values to apply on the requested home
                |             position.
                | 
                |             Example:
                | 
                |              Dim iHomeDOFCount As Integer
                |              iHomeDOFCount = MyHomeResource.HomePositionDOFCount
                |              Dim NewHomeValues 'array for VBScript
                |              ReDim NewHomeValues(iHomeDOFCount-1)
                |              For KK = 0 To UBound(NewHomeValues)
                |                NewHomeValues(KK) = 0.5
                |              Next
                |              MyHomeResource.SetHomePositionValues HomeID,
                |              NewHomeValues
                | 
                |             Note: previous example is for CATScript. In case of VBA, the syntax
                |             is significantly different:
                | 
                |              Dim iHomeDOFCount As Integer
                |              iHomeDOFCount = MyHomeResource.HomePositionDOFCount
                |              Dim NewHomeValues() As Variant 'array for VBA
                |              ReDim NewHomeValues(iHomeDOFCount-1)
                |              For KK = 0 To UBound(NewHomeValues)
                |                NewHomeValues(KK) = 0.5
                |              Next
                |              Dim MyObj 'need to change typing due to early typing for
                |              VBA
                |              Set MyObj = MyHomeResource
                |              MyObj.SetHomePositionValues HomeID, NewHomeValues
                | 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param str i_home_position_name:
        :param tuple i_home_values:
        :return: Variant
        """
        return self.com_object.SetHomePositionValues(i_home_position_name, i_home_values)

    def __repr__(self):
        return f'RscHomePositions(name="{ self.name }")'
