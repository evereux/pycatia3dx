"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class ManufacturingUserParam(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingUserParam
                | 
                | Management of Creation, Edition and Remove of user parameter
                | on operations Sample:
                |    ManufacturingUserParam userParam = activity as ManufacturingUserParam; userParam.
                |    AddParameter("USER_PARAM_BOOL", 0, -1);
                |    userParam.AddParameter("USER_PARAM_INT", 1, -1);
                |    userParam.AddParameter("USER_PARAM_REAL", 2, -1);
                |    userParam.AddParameter("USER_PARAM_ANGLE", 3, -1);
                |    userParam.AddParameter("USER_PARAM_LENGTH", 4, -1);
                |    userParam.AddParameter("USER_PARAM_STRING", 5, -1);
                |    userParam.SetValueBoolean("USER_PARAM_BOOL", true);
                |    userParam.SetValueLong("USER_PARAM_INT", 2020);
                |    userParam.SetValueDouble("USER_PARAM_REAL", 1.1);
                |    userParam.SetValueDouble("USER_PARAM_ANGLE", 2.2);
                |    userParam.SetValueDouble("USER_PARAM_LENGTH", 3.3);
                |    userParam.SetValueStr("USER_PARAM_STRING", "My user parameter value");
                |    bool userParamBool = userParam.GetValueBoolean("USER_PARAM_BOOL");
                |    int userParamInt = userParam.GetValueLong("USER_PARAM_INT");
                |    double userParamReal = userParam.GetValueDouble("USER_PARAM_REAL");
                |    string userParamAngle = userParam.GetValueParameter("USER_PARAM_ANGLE").ValueAsString();
                |    string userParamLength = userParam.GetValueParameter("USER_PARAM_LENGTH").ValueAsString();
                |    string userParamString = userParam.GetValueStr("USER_PARAM_STRING");
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_parameter(self, i_name: str, i_type: int, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddParameter(CATBSTR iName,long iType,long iPos)
                |     Create a new parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter. It must not contain " " (blank)
                |             
                |         iType
                |             The type of the parameter to create: Boolean = 0, Integer = 1, Real = 2, Angle = 3, Length = 4, String = 5 
                |         iPos
                |             By default -1 : the parameter is added at the end of list Else the parameter is added at the iPos position 
                | 
                |     Returns:
                |         Return E_FAIL if this parameter is already created.

        :param str i_name:
        :param int i_type:
        :param int i_pos:
        :return: None
        """
        return self.com_object.AddParameter(i_name, i_type, i_pos)

    def get_value_boolean(self, i_name: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueBoolean(CATBSTR iName) As boolean
                |     To get one parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to find. 
                |         oValue
                |             The parameter. 
                | 
                |     Returns:
                |         Return E_FAIL if this parameter doesn't exist, or if the type is wrong

        :param str i_name:
        :return: bool
        """
        return self.com_object.GetValueBoolean(i_name)

    def get_value_double(self, i_name: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueDouble(CATBSTR iName) As double
                |     To get one parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to find. 
                |         oValue
                |             The parameter. 
                | 
                |     Returns:
                |         Return E_FAIL if this parameter doesn't exist, or if the type is wrong

        :param str i_name:
        :return: float
        """
        return self.com_object.GetValueDouble(i_name)

    def get_value_long(self, i_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueLong(CATBSTR iName) As long
                |     To get one parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to find. 
                |         oValue
                |             The parameter. 
                | 
                |     Returns:
                |         Return E_FAIL if this parameter doesn't exist, or if the type is wrong

        :param str i_name:
        :return: int
        """
        return self.com_object.GetValueLong(i_name)

    def get_value_parameter(self, i_name: str) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueParameter(CATBSTR iName) As Parameter
                |     Retrieves value of a CATICkeParm attribute.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to find. 
                |         oValue
                |             The CKE value 
                | 
                |     See also:
                |         Parameter

        :param str i_name:
        :return: Parameter
        """
        return Parameter(self.com_object.GetValueParameter(i_name))

    def get_value_str(self, i_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueStr(CATBSTR iName) As CATBSTR
                |     To get one parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to find. 
                |         oValue
                |             The parameter. 
                | 
                |     Returns:
                |         Return E_FAIL if this parameter doesn't exist, or if the type is wrong

        :param str i_name:
        :return: str
        """
        return self.com_object.GetValueStr(i_name)

    def remove_parameter(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveParameter(CATBSTR iName)
                |     Remove parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to remove. 
                | 
                |     Returns:
                |         Return E_FAIL if this parameter doesn't exist.

        :param str i_name:
        :return: None
        """
        return self.com_object.RemoveParameter(i_name)

    def set_value_boolean(self, i_name: str, i_value: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueBoolean(CATBSTR iName,boolean iValue)
                |     To set a parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to set. 
                |         iValue
                |             The parameter value to be set. 
                | 
                |     Returns:
                |         Return E_FAIL if ivalue couldn't be assigned to the parameter

        :param str i_name:
        :param bool i_value:
        :return: None
        """
        return self.com_object.SetValueBoolean(i_name, i_value)

    def set_value_double(self, i_name: str, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueDouble(CATBSTR iName,double iValue)
                |     To set a parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to set. 
                |         iValue
                |             The parameter value to be set. 
                | 
                |     Returns:
                |         Return E_FAIL if ivalue couldn't be assigned to the parameter

        :param str i_name:
        :param float i_value:
        :return: None
        """
        return self.com_object.SetValueDouble(i_name, i_value)

    def set_value_long(self, i_name: str, i_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueLong(CATBSTR iName,long iValue)
                |     To set a parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to set. 
                |         iValue
                |             The parameter value to be set. 
                | 
                |     Returns:
                |         Return E_FAIL if ivalue couldn't be assigned to the parameter

        :param str i_name:
        :param int i_value:
        :return: None
        """
        return self.com_object.SetValueLong(i_name, i_value)

    def set_value_str(self, i_name: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueStr(CATBSTR iName,CATBSTR iValue)
                |     To set a parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter to set. 
                |         iValue
                |             The parameter value to be set. 
                | 
                |     Returns:
                |         Return E_FAIL if ivalue couldn't be assigned to the parameter

        :param str i_name:
        :param str i_value:
        :return: None
        """
        return self.com_object.SetValueStr(i_name, i_value)

    def __repr__(self):
        return f'ManufacturingUserParam(name="{ self.name }")'
