"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimParameterSet(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimParameterSet
                | 
                | Represents a string-keyed set of parameters of varying type.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_double_array_parameter(self, i_parameter_name: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDoubleArrayParameter(CATBSTR iParameterName) As
                | CATSafeArrayVariant
                |     Gets the values of a parameter which is a list of reals.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                | 
                |     Returns:
                |         The parameter values.

        :param str i_parameter_name:
        :return: tuple
        """
        return self.com_object.GetDoubleArrayParameter(i_parameter_name)

    def get_double_parameter(self, i_parameter_name: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDoubleParameter(CATBSTR iParameterName) As double
                |     Gets the value of a parameter which is a single real.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                | 
                |     Returns:
                |         The parameter value.

        :param str i_parameter_name:
        :return: float
        """
        return self.com_object.GetDoubleParameter(i_parameter_name)

    def get_integer_array_parameter(self, i_parameter_name: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetIntegerArrayParameter(CATBSTR iParameterName) As
                | CATSafeArrayVariant
                |     Gets the values of a parameter which is a list of
                |     integers.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                | 
                |     Returns:
                |         The parameter values.

        :param str i_parameter_name:
        :return: tuple
        """
        return self.com_object.GetIntegerArrayParameter(i_parameter_name)

    def get_integer_parameter(self, i_parameter_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetIntegerParameter(CATBSTR iParameterName) As long
                |     Gets the value of a parameter which is a single integer.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                | 
                |     Returns:
                |         The parameter value.

        :param str i_parameter_name:
        :return: int
        """
        return self.com_object.GetIntegerParameter(i_parameter_name)

    def get_object_array_parameter(self, i_parameter_name: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetObjectArrayParameter(CATBSTR iParameterName) As
                | CATSafeArrayVariant
                |     Gets the values of a parameter which is a list of objects.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                | 
                |     Returns:
                |         The parameter values.

        :param str i_parameter_name:
        :return: tuple
        """
        return self.com_object.GetObjectArrayParameter(i_parameter_name)

    def get_object_parameter(self, i_parameter_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetObjectParameter(CATBSTR iParameterName) As
                | CATBaseDispatch
                |     Gets the value of a parameter which is a single object.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                | 
                |     Returns:
                |         The parameter value.

        :param str i_parameter_name:
        :return: AnyObject
        """
        return self.com_object.GetObjectParameter(i_parameter_name)

    def get_string_array_parameter(self, i_parameter_name: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetStringArrayParameter(CATBSTR iParameterName) As
                | CATSafeArrayVariant
                |     Gets the values of a parameter which is a list of strings.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                | 
                |     Returns:
                |         The parameter values.

        :param str i_parameter_name:
        :return: tuple
        """
        return self.com_object.GetStringArrayParameter(i_parameter_name)

    def get_string_parameter(self, i_parameter_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetStringParameter(CATBSTR iParameterName) As CATBSTR
                |     Gets the value of a parameter which is a single string.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                | 
                |     Returns:
                |         The parameter value.

        :param str i_parameter_name:
        :return: str
        """
        return self.com_object.GetStringParameter(i_parameter_name)

    def set_double_array_parameter(self, i_parameter_name: str, i_double_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDoubleArrayParameter(CATBSTR iParameterName,CATSafeArrayVariant
                | iDoubleValues)
                |     Sets the values of a parameter which is a list of reals.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                |         iDoubleValues:
                |             The parameter values.

        :param str i_parameter_name:
        :param tuple i_double_values:
        :return: None
        """
        return self.com_object.SetDoubleArrayParameter(i_parameter_name, i_double_values)

    def set_double_parameter(self, i_parameter_name: str, i_double_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDoubleParameter(CATBSTR iParameterName,double
                | iDoubleValue)
                |     Sets the value of a parameter which is a single real.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                |         iDoubleValue:
                |             The parameter value.

        :param str i_parameter_name:
        :param float i_double_value:
        :return: None
        """
        return self.com_object.SetDoubleParameter(i_parameter_name, i_double_value)

    def set_integer_array_parameter(self, i_parameter_name: str, i_integer_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetIntegerArrayParameter(CATBSTR iParameterName,CATSafeArrayVariant
                | iIntegerValues)
                |     Sets the values of a parameter which is a list of
                |     integers.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                |         iIntegerValues:
                |             The parameter values.

        :param str i_parameter_name:
        :param tuple i_integer_values:
        :return: None
        """
        return self.com_object.SetIntegerArrayParameter(i_parameter_name, i_integer_values)

    def set_integer_parameter(self, i_parameter_name: str, i_integer_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetIntegerParameter(CATBSTR iParameterName,long
                | iIntegerValue)
                |     Sets the value of a parameter which is a single integer.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                |         iIntegerValue:
                |             The parameter value.

        :param str i_parameter_name:
        :param int i_integer_value:
        :return: None
        """
        return self.com_object.SetIntegerParameter(i_parameter_name, i_integer_value)

    def set_object_array_parameter(self, i_parameter_name: str, i_object_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetObjectArrayParameter(CATBSTR iParameterName,CATSafeArrayVariant
                | iObjectValues)
                |     Sets the values of a parameter which is a list of objects.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                |         iObjectValues:
                |             The parameter values.

        :param str i_parameter_name:
        :param tuple i_object_values:
        :return: None
        """
        return self.com_object.SetObjectArrayParameter(i_parameter_name, i_object_values)

    def set_object_parameter(self, i_parameter_name: str, i_object_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetObjectParameter(CATBSTR iParameterName,CATBaseDispatch
                | iObjectValue)
                |     Sets the value of a parameter which is a single object.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                |         iObjectValue:
                |             The parameter value.

        :param str i_parameter_name:
        :param AnyObject i_object_value:
        :return: None
        """
        return self.com_object.SetObjectParameter(i_parameter_name, i_object_value.com_object)

    def set_string_array_parameter(self, i_parameter_name: str, i_string_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStringArrayParameter(CATBSTR iParameterName,CATSafeArrayVariant
                | iStringValues)
                |     Sets the values of a parameter which is a list of strings.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                |         iStringValues:
                |             The parameter values.

        :param str i_parameter_name:
        :param tuple i_string_values:
        :return: None
        """
        return self.com_object.SetStringArrayParameter(i_parameter_name, i_string_values)

    def set_string_parameter(self, i_parameter_name: str, i_string_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStringParameter(CATBSTR iParameterName,CATBSTR
                | iStringValue)
                |     Sets the value of a parameter which is a single string.
                | 
                |     Parameters:
                | 
                |         iParameterName:
                |             The parameter name. 
                |         iStringValue:
                |             The parameter value.

        :param str i_parameter_name:
        :param str i_string_value:
        :return: None
        """
        return self.com_object.SetStringParameter(i_parameter_name, i_string_value)

    def __repr__(self):
        return f'SimParameterSet()'
