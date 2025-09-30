"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingSpecializedResource(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingSpecializedResource
                | 
                | Interface dedicated to manage specialized attributes to a machine and tool
                | resources.
                | Role: This interface offers services to manage specialized attributes to
                | machine and tool resources.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_attr_boolean(self, i_att_name: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAttrBoolean(CATBSTR iAttName) As boolean
                |     Get boolean type specialized attribute from a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             : Attribute name. 
                |         oValue
                |             : Boolean value.

        :param str i_att_name:
        :return: bool
        """
        return self.com_object.GetAttrBoolean(i_att_name)

    def get_attr_double(self, i_att_name: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAttrDouble(CATBSTR iAttName) As double
                |     Get double type specialized attribute from a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             : Attribute name. 
                |         oValue
                |             : Double value.

        :param str i_att_name:
        :return: float
        """
        return self.com_object.GetAttrDouble(i_att_name)

    def get_attr_integer(self, i_att_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAttrInteger(CATBSTR iAttName) As long
                |     Get integer type specialized attribute from a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             : Attribute name. 
                |         oValue
                |             : Integer value.

        :param str i_att_name:
        :return: int
        """
        return self.com_object.GetAttrInteger(i_att_name)

    def get_attr_string(self, i_att_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAttrString(CATBSTR iAttName) As CATBSTR
                |     Get string type specialized attribute from a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             : Attribute name. 
                |         oValue
                |             : String value.

        :param str i_att_name:
        :return: str
        """
        return self.com_object.GetAttrString(i_att_name)

    def get_attr_time(self, i_att_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAttrTime(CATBSTR iAttName) As long
                |     Get CATTime type specialized attribute from a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             : Attribute name. 
                |         oValue
                |             : CATTime value.

        :param str i_att_name:
        :return: int
        """
        return self.com_object.GetAttrTime(i_att_name)

    def get_list_of_specialized_attributes(self, o_list_att_names: tuple, o_list_att_values: tuple, o_list_catia_parameter: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetListOfSpecializedAttributes(CATSafeArrayVariant
                | oListAttNames,CATSafeArrayVariant oListAttValues,CATSafeArrayVariant
                | oListCATIAParameter)
                |     Get List of specialized attribute names, its values in string type and
                |     corresponding CATIAParameter from a PLM object.
                | 
                |     Parameters:
                | 
                |         oListAttNames
                |             : List of specialized attribute names. 
                |         oListAttValues
                |             : List of attribute values in string format irrespective of its actual type. 
                |         oListCATIAParameter
                |             : List of CATIAParameter.

        :param tuple o_list_att_names:
        :param tuple o_list_att_values:
        :param tuple o_list_catia_parameter:
        :return: None
        """
        return self.com_object.GetListOfSpecializedAttributes(o_list_att_names, o_list_att_values, o_list_catia_parameter)

    def set_attr_boolean(self, i_att_name: str, i_value: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttrBoolean(CATBSTR iAttName,boolean iValue)
                |     Set boolean type specialized attribute to a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             : Attribute name. 
                |         iValue
                |             : Boolean value to be set.

        :param str i_att_name:
        :param bool i_value:
        :return: None
        """
        return self.com_object.SetAttrBoolean(i_att_name, i_value)

    def set_attr_double(self, i_att_name: str, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttrDouble(CATBSTR iAttName,double iValue)
                |     Set double type specialized attribute to a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             :Attribute name. 
                |         iValue
                |             : Double value to be set.

        :param str i_att_name:
        :param float i_value:
        :return: None
        """
        return self.com_object.SetAttrDouble(i_att_name, i_value)

    def set_attr_integer(self, i_att_name: str, i_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttrInteger(CATBSTR iAttName,long iValue)
                |     Set integer type specialized attribute to a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             : Attribute name. 
                |         iValue
                |             : Integer value to be set.

        :param str i_att_name:
        :param int i_value:
        :return: None
        """
        return self.com_object.SetAttrInteger(i_att_name, i_value)

    def set_attr_string(self, i_att_name: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttrString(CATBSTR iAttName,CATBSTR iValue)
                |     Set string type specialized attribute to a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             : Attribute name. 
                |         iValue
                |             : String value to be set.

        :param str i_att_name:
        :param str i_value:
        :return: None
        """
        return self.com_object.SetAttrString(i_att_name, i_value)

    def set_attr_time(self, i_att_name: str, i_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttrTime(CATBSTR iAttName,long iValue)
                |     Set CATTime type specialized attribute to a PLM object.
                | 
                |     Parameters:
                | 
                |         iAttName
                |             : Attribute name. 
                |         iValue
                |             : CATTime value to be set.

        :param str i_att_name:
        :param int i_value:
        :return: None
        """
        return self.com_object.SetAttrTime(i_att_name, i_value)

    def __repr__(self):
        return f'ManufacturingSpecializedResource(name="{ self.name }")'
