"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingActivityParameters(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingActivityParameters
                | 
                | Interface to manage parameters of a manufacturing operation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def find_element(self, i_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindElement(CATBSTR iName) As AnyObject
                |     Retrieves , if possible , CKE object describing parameter on the
                |     manufacturing operation or enum parameter.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         oParm
                |             The parameter value modelized by a Parameter or
                |             ManufacturingEnumParameter

        :param str i_name:
        :return: AnyObject
        """
        return AnyObject(self.com_object.FindElement(i_name))

    def find_element2(self, i_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindElement2(CATBSTR iName) As AnyObject
                | 
                |     Deprecated:
                |         R424 use DELMIAMfgActivityParameters#FindElement Retrieves , if
                |         possible , CKE object describing parameter on the manufacturing operation or
                |         enum parameter. 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         oParm
                |             The parameter value modelized by a Parameter or
                |             ManufacturingEnumParameter

        :param str i_name:
        :return: AnyObject
        """
        return AnyObject(self.com_object.FindElement2(i_name))

    def get_feedrate_unit(self, i_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFeedrateUnit(CATBSTR iName) As CATBSTR
                |     Retrieves , if possible , the string value describing unit parameter on the
                |     manufacturing operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         oValue
                |             The unit value (LINEARFEEDRATE, ANGULARFEEDRATE)

        :param str i_name:
        :return: str
        """
        return self.com_object.GetFeedrateUnit(i_name)

    def get_value_boolean(self, i_name: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueBoolean(CATBSTR iName) As boolean
                |     Retrieves the value for a string type parameter on the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         oValue
                |             The parameter value

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
                |     Retrieves the value for a double type parameter on the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         oValue
                |             The parameter value

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
                |     Retrieves the value for an integer type parameter on the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         oValue
                |             The parameter value

        :param str i_name:
        :return: int
        """
        return self.com_object.GetValueLong(i_name)

    def get_value_str(self, i_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueStr(CATBSTR iName) As CATBSTR
                |     Retrieves the value for a string type parameter on the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         oValue
                |             The parameter value

        :param str i_name:
        :return: str
        """
        return self.com_object.GetValueStr(i_name)

    def set_feedrate_unit(self, i_name: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFeedrateUnit(CATBSTR iName,CATBSTR iValue)
                |     Sets the value for a unit parameter on the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter unit value (LINEARFEEDRATE, ANGULARFEEDRATE)

        :param str i_name:
        :param str i_value:
        :return: None
        """
        return self.com_object.SetFeedrateUnit(i_name, i_value)

    def set_value_boolean(self, i_name: str, i_value: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueBoolean(CATBSTR iName,boolean iValue)
                |     Sets the value for a string type parameter on the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value

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
                |     Sets the value for a double type parameter on the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value

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
                |     Sets the value for an integer type parameter on the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value

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
                |     Sets the value for a string type parameter on the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value

        :param str i_name:
        :param str i_value:
        :return: None
        """
        return self.com_object.SetValueStr(i_name, i_value)

    def __repr__(self):
        return f'ManufacturingActivityParameters(name="{ self.name }")'
