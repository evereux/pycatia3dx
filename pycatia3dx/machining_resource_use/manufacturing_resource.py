"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class ManufacturingResource(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingResource
                | 
                | Interface dedicated to resource objects management.
                | Role: This interface offers services to manage parameters.
                | Common attributes are declared in constants header files.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_default_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDefaultName() As CATBSTR
                |     Retrieves the default name of the resource object.
                | 
                |     Parameters:
                | 
                |         oName
                |             The default name of the resource object

        :return: str
        """
        return self.com_object.GetDefaultName()

    def get_linked_object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLinkedObject() As AnyObject
                |     Retrieves the linked object associated on the resource
                |     object.
                | 
                |     Parameters:
                | 
                |         oObject
                |             The external object associated on the resource. 
                | 
                |     Returns:
                |         Return code.
                |         Legal values:
                | 
                |             S_OK: the object exists
                |             E_FAIL: otherwise

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetLinkedObject())

    def get_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetName() As CATBSTR
                |     Retrieves the name of the resource object.
                | 
                |     Parameters:
                | 
                |         oName
                |             The name of the resource object

        :return: str
        """
        return self.com_object.GetName()

    def get_parametrization(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParametrization() As CATSafeArrayVariant
                |     Retrieves the parametrization set of the resource object.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The list of parametrization on the resource. Each string is one
                |             parametrization rule. 
                | 
                |     Returns:
                |         Return code.
                |         Legal values:
                | 
                |             S_OK: the parametrization exists
                |             E_FAIL: otherwise

        :return: tuple
        """
        return self.com_object.GetParametrization()

    def get_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetType() As CATBSTR
                |     Retrieves the type of the resource object.
                | 
                |     Parameters:
                | 
                |         oType
                |             The internal type of the resource object

        :return: str
        """
        return self.com_object.GetType()

    def get_value_boolean(self, i_attribute: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueBoolean(CATBSTR iAttribute) As boolean
                |     Retrieves value of a boolean attribute of the resource
                |     object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the attribute 
                |         oValue
                |             The boolean value

        :param str i_attribute:
        :return: bool
        """
        return self.com_object.GetValueBoolean(i_attribute)

    def get_value_double(self, i_attribute: str, i_unit: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueDouble(CATBSTR iAttribute,long iUnit) As double
                |     Retrieves value of a double attribute of the resource
                |     object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the attribute 
                |         oValue
                |             The double value 
                |         iUnit
                |             Unit to express value
                |             Legal values:
                | 
                |                 0 (default) : values expressed as they are stored in the model (for example, 'mm' for length)
                |                 1 : values expressed in current unit of session
                |                 2 : values expressed in MKS system

        :param str i_attribute:
        :param int i_unit:
        :return: float
        """
        return self.com_object.GetValueDouble(i_attribute, i_unit)

    def get_value_long(self, i_attribute: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueLong(CATBSTR iAttribute) As long
                |     Retrieves value of an integer attribute of the resource
                |     object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the attribute 
                |         oValue
                |             The integer value

        :param str i_attribute:
        :return: int
        """
        return self.com_object.GetValueLong(i_attribute)

    def get_value_parameter(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueParameter(CATBSTR iAttribute) As Parameter
                |     Retrieves value of a CATICkeParm attribute of the resource
                |     object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the attribute 
                |         oValue
                |             The CKE value 
                | 
                |     See also:
                |         CATICkeParm

        :param str i_attribute:
        :return: Parameter
        """
        return Parameter(self.com_object.GetValueParameter(i_attribute))

    def get_value_str(self, i_attribute: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValueStr(CATBSTR iAttribute) As CATBSTR
                |     Retrieves value of a string attribute of the resource
                |     object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the attribute 
                |         oValue
                |             The string value

        :param str i_attribute:
        :return: str
        """
        return self.com_object.GetValueStr(i_attribute)

    def get_values(self, i_list_attributes: tuple, o_list_type_values: tuple, o_list_nb_values: tuple, o_list_int_values: tuple, o_list_dbl_values: tuple, o_list_str_values: tuple, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetValues(CATSafeArrayVariant iListAttributes,CATSafeArrayVariant
                | oListTypeValues,CATSafeArrayVariant oListNbValues,CATSafeArrayVariant
                | oListIntValues,CATSafeArrayVariant oListDblValues,CATSafeArrayVariant
                | oListStrValues,long iUnit)
                |     Retrieves values of parameters of the resource object.
                | 
                |     Parameters:
                | 
                |         iListAttributes
                |             List containing attribute names to read (if List is empty, all
                |             attributes are read) 
                |         oListTypeValues
                | 
                |             Legal values:
                | 
                |                 0: boolean
                |                 1: integer
                |                 2: double
                |                 3: string
                | 
                |         oListNbValues
                |             List containing number of values for each attribute
                |             
                |         oListIntValues
                |             List containing integer type values 
                |         oListDblValues
                |             List containing double type values 
                |         oListStrValues
                |             List containing string type values 
                |         iUnit
                |             Unit to express value
                |             Legal values:
                | 
                |                 0 (default) : values expressed as they are stored in the model (for example, 'mm' for length)
                |                 1 : values expressed in current unit of session
                |                 2 : values expressed in MKS system

        :param tuple i_list_attributes:
        :param tuple o_list_type_values:
        :param tuple o_list_nb_values:
        :param tuple o_list_int_values:
        :param tuple o_list_dbl_values:
        :param tuple o_list_str_values:
        :param int i_unit:
        :return: None
        """
        return self.com_object.GetValues(i_list_attributes, o_list_type_values, o_list_nb_values, o_list_int_values, o_list_dbl_values, o_list_str_values, i_unit)

    def get_version(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetVersion() As long
                |     Retrieves the version of the resource object.
                | 
                |     Parameters:
                | 
                |         oVersion
                |             The internal version of the resource object

        :return: int
        """
        return self.com_object.GetVersion()

    def set_default_name(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDefaultName()
                |     Sets the default name of the resource object.

        :return: None
        """
        return self.com_object.SetDefaultName()

    def set_default_values(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDefaultValues()
                |     Sets default values to parameters of the resource object.

        :return: None
        """
        return self.com_object.SetDefaultValues()

    def set_linked_object(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLinkedObject(AnyObject iObject)
                |     Sets the link to the object on the resource object.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The external object to associate on the resource. 
                | 
                |     Returns:
                |         Return code.
                |         Legal values:
                | 
                |             S_OK: the object could be added
                |             E_FAIL: otherwise

        :param AnyObject i_object:
        :return: None
        """
        return self.com_object.SetLinkedObject(i_object.com_object)

    def set_name(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetName(CATBSTR iName)
                |     Sets the name of the resource object.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the resource object

        :param str i_name:
        :return: None
        """
        return self.com_object.SetName(i_name)

    def set_parametrization(self, i_value: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParametrization(CATSafeArrayVariant iValue)
                |     Sets the parametrization set of the resource object.
                | 
                |     Parameters:
                | 
                |         iValue
                |             The list of parametrization to be added to the resource. One string
                |             is one parametrization rule. 
                | 
                |     Returns:
                |         Return code.
                |         Legal values:
                | 
                |             S_OK: the parametrization could be added
                |             E_FAIL: otherwise

        :param tuple i_value:
        :return: None
        """
        return self.com_object.SetParametrization(i_value)

    def set_value_boolean(self, i_attribute: str, i_value: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueBoolean(CATBSTR iAttribute,boolean iValue)
                |     Sets value to a boolean attribute of the resource object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the attribute 
                |         iValue
                |             The boolean value

        :param str i_attribute:
        :param bool i_value:
        :return: None
        """
        return self.com_object.SetValueBoolean(i_attribute, i_value)

    def set_value_double(self, i_attribute: str, i_value: float, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueDouble(CATBSTR iAttribute,double iValue,long
                | iUnit)
                |     Sets value to a double attribute of the resource object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the attribute 
                |         iValue
                |             The double value 
                |         iUnit
                |             Unit to express value
                |             Legal values:
                | 
                |                 0 (default) : values expressed as they are stored in the model (for example, 'mm' for length)
                |                 1 : values expressed in current unit of session
                |                 2 : values expressed in MKS system

        :param str i_attribute:
        :param float i_value:
        :param int i_unit:
        :return: None
        """
        return self.com_object.SetValueDouble(i_attribute, i_value, i_unit)

    def set_value_long(self, i_attribute: str, i_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueLong(CATBSTR iAttribute,long iValue)
                |     Sets value to an integer attribute of the resource object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the attribute 
                |         iValue
                |             The integer value

        :param str i_attribute:
        :param int i_value:
        :return: None
        """
        return self.com_object.SetValueLong(i_attribute, i_value)

    def set_value_parameter(self, i_attribute: str, i_value: Parameter) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueParameter(CATBSTR iAttribute,Parameter iValue)
                |     Sets value to a CATICkeParm attribute of the resource
                |     object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             : The name of the attribute 
                |         iValue
                |             : The CKE value 
                | 
                |     See also:
                |         CATICkeParm

        :param str i_attribute:
        :param Parameter i_value:
        :return: None
        """
        return self.com_object.SetValueParameter(i_attribute, i_value.com_object)

    def set_value_str(self, i_attribute: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValueStr(CATBSTR iAttribute,CATBSTR iValue)
                |     Sets value to a string attribute of the resource object.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the attribute 
                |         oValue
                |             The string value

        :param str i_attribute:
        :param str i_value:
        :return: None
        """
        return self.com_object.SetValueStr(i_attribute, i_value)

    def set_values(self, i_list_attributes: tuple, i_list_type_values: tuple, i_list_nb_values: tuple, i_list_int_values: tuple, i_list_dbl_values: tuple, i_list_str_values: tuple, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValues(CATSafeArrayVariant iListAttributes,CATSafeArrayVariant
                | iListTypeValues,CATSafeArrayVariant iListNbValues,CATSafeArrayVariant
                | iListIntValues,CATSafeArrayVariant iListDblValues,CATSafeArrayVariant
                | iListStrValues,long iUnit)
                |     Sets values to parameters of the resource object.
                | 
                |     Parameters:
                | 
                |         iListAttributes
                |             List containing attribute names to valuate 
                |         iListTypeValues
                |             List containing type of value for each attribute
                |             Legal values:
                | 
                |                 0: boolean
                |                 1: integer
                |                 2: double
                |                 3: string
                | 
                |         iListNbValues
                |             List containing number of values for each attribute
                |             
                |         iListIntValues
                |             List containing integer type values 
                |         iListDblValues
                |             List containing double type values 
                |         iListStrValues
                |             List containing string type values 
                |         iUnit
                |             Unit to express value (default 0)
                |             Legal values:
                | 
                |                 0 (default) : values expressed as they are stored in the model (for example, 'mm' for length)
                |                 1 : values expressed in current unit of session
                |                 2 : values expressed in MKS system

        :param tuple i_list_attributes:
        :param tuple i_list_type_values:
        :param tuple i_list_nb_values:
        :param tuple i_list_int_values:
        :param tuple i_list_dbl_values:
        :param tuple i_list_str_values:
        :param int i_unit:
        :return: None
        """
        return self.com_object.SetValues(i_list_attributes, i_list_type_values, i_list_nb_values, i_list_int_values, i_list_dbl_values, i_list_str_values, i_unit)

    def __repr__(self):
        return f'ManufacturingResource(name="{ self.name }")'
