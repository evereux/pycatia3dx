"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter


class StrParam(Parameter):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.Parameter
                |                         StrParam
                | 
                | Represents the string parameter.
                | 
                | See also:
                |     ParametersFactory.CreateString
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def value(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Value() As CATBSTR
                |     Returns or sets the string parameter value.
                | 
                |     Example:
                |         This example returns in myValue the value of the string parameter
                |         material:
                | 
                |          
                | 
                |          myValue = material.Value

        :return: str
        """

        return self.com_object.Value

    @value.setter
    def value(self, value: str):
        """
        :param str value:
        """

        self.com_object.Value = value

    def get_enumerate_values(self, o_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetEnumerateValues(CATSafeArrayVariant oSafeArray)
                |     Returns an array containing the different values that the real param can
                |     take in the case of multiple values.
                | 
                |     Parameters:
                | 
                |         oSafeArray
                |             The array
                | 
                |             Example:
                | 
                |                  Dim enumValues () as Variant
                |                  ReDim enumValues (aStrParameter.GetEnumerateValuesSize() -
                |                  1)
                |                  aStrParameter.GetEnumerateValues(enumValues)
                |                  For i = LBound(enumValues) to UBound(enumValues)
                |                    ...
                |                  Next

        :param tuple o_safe_array:
        :return: None
        """
        return self.com_object.GetEnumerateValues(o_safe_array)

    def get_enumerate_values_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetEnumerateValuesSize() As long
                |     Returns the number of enumerate values.
                | 
                |     Returns:
                |         the number of enumerate values.

        :return: int
        """
        return self.com_object.GetEnumerateValuesSize()

    def set_enumerate_values(self, i_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetEnumerateValues(CATSafeArrayVariant iSafeArray)
                |     Sets an array containing the different values that the StrParam object can
                |     take in the case of multiple values.
                | 
                |     Parameters:
                | 
                |         iSafeArray
                |             The array of enumerated values.

        :param tuple i_safe_array:
        :return: None
        """
        return self.com_object.SetEnumerateValues(i_safe_array)

    def suppress_enumerate_values(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SuppressEnumerateValues()
                |     Resets the status of the object to a single value object.

        :return: None
        """
        return self.com_object.SuppressEnumerateValues()

    def __repr__(self):
        return f'StrParam(name="{ self.name }")'
