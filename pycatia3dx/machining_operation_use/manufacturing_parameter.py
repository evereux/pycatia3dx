"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class ManufacturingParameter(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingParameter
                | 
                | This interface is used to handle with Enumeration Parameters for
                | Manufacturing
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_bool_value(self, i_name: str, o_value: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetBoolValue(CATBSTR iName,boolean oValue)
                |     Get boolean value of parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the parameter 
                |         oValue
                |             The boolean value

        :param str i_name:
        :param bool o_value:
        :return: None
        """
        return self.com_object.GetBoolValue(i_name, o_value)

    def get_double_value(self, i_name: str, o_value: float, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDoubleValue(CATBSTR iName,double oValue,long iUnit)
                |     Get double value of parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the parameter 
                |         oValue
                |             The double value 
                |         iUnit
                |             The unit value (default: 0)

        :param str i_name:
        :param float o_value:
        :param int i_unit:
        :return: None
        """
        return self.com_object.GetDoubleValue(i_name, o_value, i_unit)

    def get_long_value(self, i_name: str, o_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLongValue(CATBSTR iName,long oValue)
                |     Get integer value of parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the parameter 
                |         oValue
                |             The double value

        :param str i_name:
        :param int o_value:
        :return: None
        """
        return self.com_object.GetLongValue(i_name, o_value)

    def get_string_value(self, i_name: str, o_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetStringValue(CATBSTR iName,CATBSTR oValue)
                |     Get string value of parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the parameter 
                |         oValue
                |             The string value

        :param str i_name:
        :param str o_value:
        :return: None
        """
        return self.com_object.GetStringValue(i_name, o_value)

    def get_value(self, i_name: str, o_value: Parameter) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetValue(CATBSTR iName,Parameter oValue)
                |     Get CATICkeParm value of parameter
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the parameter 
                |         oValue
                |             The CATICkeParm value

        :param str i_name:
        :param Parameter o_value:
        :return: None
        """
        return self.com_object.GetValue(i_name, o_value.com_object)

    def __repr__(self):
        return f'ManufacturingParameter(name="{ self.name }")'
