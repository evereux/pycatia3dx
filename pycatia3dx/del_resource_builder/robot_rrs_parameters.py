"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RobotRrsParameters(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RobotRRSParameters
                | 
                | Interface to access the controller attributes.
                | Role: This interface provides methods to access the controller
                | parameters.
                | This API retrieves the default attributes of the controller. There are used
                | before any simulation and must be modified before the simulation
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
                |        Dim MyControllerData As RobotRRSParameters
                |        MyControllerData = MySelectedResource.RetrieveControllerAttributesObject
                |      End If
                | 
                | See also:
                |     RscControllerAttributesAccess
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def list_rrs_parameters(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ListRRSParameters() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of RRS possible parameters whose values are
                |     strings.
                | 
                |     Returns:
                |         The list of RRS parameters.
                | 
                |         Example:
                | 
                |          Dim ListParametersID 'array for VBScript
                |          ListParametersID = MyControllerData.ListRRSParameters
                |          Dim NbParam As Integer
                |          NbParam = UBound(ListParametersID) + 1
                |          'uncomment next line to display value
                |          'MsgBox ("Number of parameters : " & CStr(NbParam))
                |          Dim ParameterID As String
                |          For II = LBound(ListParametersID) To UBound(ListParametersID)
                |            ParameterID = ListParametersID(II)
                |            'uncomment next line to display value
                |            'MsgBox ("Parameters[" & CStr(II) & "]=" &
                |            ParameterID)
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ListParametersID() As Variant 'array for VBA
                |          ListParametersID = MyControllerData.ListRRSParameters

        :return: tuple
        """

        return self.com_object.ListRRSParameters

    @property
    def list_rrs_parameters_boolean(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ListRRSParametersBoolean() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of RRS possible parameters whose values are
                |     boolean.
                | 
                |     Returns:
                |         The list of RRS parameters.
                | 
                |         Example:
                | 
                |          Dim ListParametersID 'array for VBScript
                |          ListParametersID = MyControllerData.ListRRSParametersBoolean
                |          Dim NbParam As Integer
                |          NbParam = UBound(ListParametersID) + 1
                |          'uncomment next line to display value
                |            'MsgBox ("Parameters[" & CStr(II) & "]=" &
                |            ParameterID)
                |          Dim ParameterID As String
                |          For II = LBound(ListParametersID) To UBound(ListParametersID)
                |            ParameterID = ListParametersID(II)
                |            'uncomment next line to display value
                |            'MsgBox ("Parameters ID:" & ParameterID)
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ListParametersID() As Variant 'array for VBA
                |          ListParametersID = MyControllerData.ListRRSParametersBoolean

        :return: tuple
        """

        return self.com_object.ListRRSParametersBoolean

    @property
    def list_rrs_parameters_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ListRRSParametersList() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of RRS possible parameters whose values are
                |     list.
                | 
                |     Returns:
                |         The list of RRS parameters.
                | 
                |         Example:
                | 
                |          Dim ListParametersID 'array for VBScript
                |          ListParametersID = MyControllerData.ListRRSParametersList
                |          Dim NbParam As Integer
                |          NbParam = UBound(ListParametersID) + 1
                |          'uncomment next line to display value
                |          'MsgBox ("Number of parameters : " & CStr(NbParam))
                |          Dim ParameterID As String
                |          For II = LBound(ListParametersID) To UBound(ListParametersID)
                |            ParameterID = ListParametersID(II)
                |            'uncomment next line to display value
                |            'MsgBox ("Parameters[" & CStr(II) & "]=" &
                |            ParameterID)
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ListParametersID() As Variant 'array for VBA
                |          ListParametersID = MyControllerData.ListRRSParametersList

        :return: tuple
        """

        return self.com_object.ListRRSParametersList

    def get_rrs_parameter(self, i_rrs_parameters_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRRSParameter(CATBSTR iRRSParametersName) As CATBSTR
                |     Retrieves the value of a RRS parameters. Available parameter names can be
                |     retrieved through the property ListRRSParameters.
                | 
                |     Parameters:
                | 
                |         iRRSParametersName
                |             Name of an RRS parameters. 
                | 
                |     Returns:
                |         String containing the parameter value
                | 
                |         Example:
                | 
                |          Dim MyRRSValue As String
                |          Dim MyRRSParameter As String
                |          MyRRSParameter = "RRSServerName"
                |          MyRRSValue = MyControllerData.GetRRSParameter(MyRRSParameter)

        :param str i_rrs_parameters_name:
        :return: str
        """
        return self.com_object.GetRRSParameter(i_rrs_parameters_name)

    def get_rrs_parameter_boolean(self, i_rrs_parameters_name: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRRSParameterBoolean(CATBSTR iRRSParametersName) As
                | boolean
                |     Retrieves the value of a RRS parameters. Available parameter names can be
                |     retrieved through the property ListRRSParametersBoolean.
                | 
                |     Parameters:
                | 
                |         iRRSParametersName
                |             Name of an RRS parameters. 
                | 
                |     Returns:
                |         String containing the parameter value
                | 
                |         Example:
                | 
                |          Dim MyRRSValue As Boolean
                |          Dim MyRRSParameter As String
                |          MyRRSParameter = "RRSServerName"
                |          MyRRSValue = MyControllerData.GetRRSParameterBoolean(MyRRSParameter)

        :param str i_rrs_parameters_name:
        :return: bool
        """
        return self.com_object.GetRRSParameterBoolean(i_rrs_parameters_name)

    def get_rrs_parameter_list(self, i_rrs_parameters_name: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRRSParameterList(CATBSTR iRRSParametersName) As
                | CATSafeArrayVariant
                |     Retrieves the value of a RRS parameter as a list. Available parameter names
                |     can be retrieved through the property
                |     ListRRSParametersList.
                | 
                |     Parameters:
                | 
                |         iRRSParametersName
                |             Name of an RRS parameters. 
                | 
                |     Returns:
                |         List of values for the requested parameter.
                | 
                |         Example:
                | 
                |          Dim MyRRSParameter As String
                |          MyRRSParameter = "RRSControlledMotionGroups"
                |          Dim ValueList 'array for VBScript
                |          ValueList = MyControllerData.GetRRSParameterList(MyRRSParameter)
                |          Dim ListIndex As Double
                |          For II = LBound(ValueList) To UBound(ValueList)
                |              Dim MyParamValue As String
                |              MyParamValue = ValueList(II)
                |              'uncomment next line to display value
                |              'MsgBox ("ListIndex:" & CStr(ListIndex))
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ValueList() As Variant 'array for VBA
                |          ValueList = MyControllerData.GetRRSParameterList(MyRRSParameter)

        :param str i_rrs_parameters_name:
        :return: tuple
        """
        return self.com_object.GetRRSParameterList(i_rrs_parameters_name)

    def set_rrs_parameter(self, i_rrs_parameters_name: str, i_rrs_parameter_value: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SetRRSParameter(CATBSTR iRRSParametersName,CATBSTR iRRSParameterValue) As
                | long
                |     Modify the value of a RRS parameters. Available parameter names can be
                |     retrieved through the property ListRRSParameters.
                | 
                |     Parameters:
                | 
                |         iRRSParametersName
                |             Name of an RRS parameters. 
                |         iRRSParameterValue
                |             Value to be applied. 
                | 
                |     Returns:
                |         Error value indicating if
                | 
                |             0: method succeeds
                |             1: argument invalid
                |             2: argument not applicable
                | 
                |         Example:
                | 
                |          Dim MyRRSValue As String
                |          Dim MyRRSParameter As String
                |          Dim iError As Integer
                |          MyRRSParameter = "RRSServerName"
                |          MyRRSParameter = "MyServer"
                | 
                |          iError = MyControllerData.SetRRSParameter(MyRRSParameter,MyRRSParameter)

        :param str i_rrs_parameters_name:
        :param str i_rrs_parameter_value:
        :return: int
        """
        return self.com_object.SetRRSParameter(i_rrs_parameters_name, i_rrs_parameter_value)

    def set_rrs_parameter_boolean(self, i_rrs_parameters_name: str, i_rrs_parameter_value: bool) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SetRRSParameterBoolean(CATBSTR iRRSParametersName,boolean
                | iRRSParameterValue) As long
                |     Modify the value of a RRS parameters. Available parameter names can be
                |     retrieved through the property ListRRSParametersBoolean.
                | 
                |     Parameters:
                | 
                |         iRRSParametersName
                |             Name of an RRS parameters. 
                |         iRRSParameterValue
                |             Value to be applied. 
                | 
                |     Returns:
                |         Error value indicating if
                | 
                |             0: method succeeds
                |             1: argument invalid
                |             2: argument not applicable
                | 
                |         Example:
                | 
                |          Dim MyRRSValue As Boolean
                |          Dim MyRRSParameter As String
                |          Dim iError As Integer
                |          MyRRSParameter = "RRSEnabled"
                |          MyRRSValue = False
                | 
                |          iError = MyControllerData.SetRRSParameterBoolean(MyRRSParameter,MyRRSValue)

        :param str i_rrs_parameters_name:
        :param bool i_rrs_parameter_value:
        :return: int
        """
        return self.com_object.SetRRSParameterBoolean(i_rrs_parameters_name, i_rrs_parameter_value)

    def set_rrs_parameter_list(self, i_rrs_parameters_name: str, i_values: tuple) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SetRRSParameterList(CATBSTR iRRSParametersName,CATSafeArrayVariant
                | iValues) As long
                |     Modify the value of a RRS parameters. Available parameter names can be
                |     retrieved through the property ListRRSParametersList.
                | 
                |     Parameters:
                | 
                |         iRRSParametersName
                |             Name of an RRS parameters. 
                |         iValues
                |             Values to be applied. 
                | 
                |     Returns:
                |         Error value indicating if
                | 
                |             0: method succeeds
                |             1: argument invalid
                |             2: argument not applicable
                | 
                |         Example:
                | 
                |          Dim MyRRSParameter As String
                |          Dim iError As Integer
                |          MyRRSParameter = "RRSControlledMotionGroups"
                |          Dim NewValues 'array for VBScript
                |          ReDim NewValues(2) 'array of size 3
                |          For KK = 0 To UBound(NewValues)
                |            NewValues(KK) = "MG1"
                |          Next
                | 
                |          iError = MyControllerData.SetRRSParameterList(MyRRSParameter,NewValues)
                |         Note: previous example is for CATScript. In case of VBA, the syntax
                |         
                |         is slightly different for array declaration: 
                | 
                |          Dim ValueList() As Variant 'array for VBA
                |          Dim MyObj 'need to change typing due to early typing for
                |          VBA
                |          Set MyObj = MyControllerData
                |          MyObj.SetRRSParameterList MyRRSParameter, ValueList

        :param str i_rrs_parameters_name:
        :param tuple i_values:
        :return: int
        """
        return self.com_object.SetRRSParameterList(i_rrs_parameters_name, i_values)

    def __repr__(self):
        return f'RobotRrsParameters(name="{ self.name }")'
