"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter


class IntParam(Parameter):

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
                |                         IntParam
                | 
                | Represents the integer parameter.
                | 
                | See also:
                |     ParametersFactory.CreateInteger
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def range_max(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property RangeMax() As long
                |     Returns or sets the value of the upper bound that the parameter object
                |     value can take.
                | 
                |     Example:
                |         This example sets the RangeMax value to 0 if its value is smaller than
                |         0:
                | 
                |          If (Length.RangeMax < 0.0 and Length.RangeMaxValidity <> 0) 
                |          Then
                |              Length.RangeMax = 0.0
                |          End If

        :return: int
        """

        return self.com_object.RangeMax

    @range_max.setter
    def range_max(self, value: int):
        """
        :param int value:
        """

        self.com_object.RangeMax = value

    @property
    def range_max_validity(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property RangeMaxValidity() As long
                |     Returns or sets the type of the upper bound of the
                |     parameter.
                | 
                |     0
                |         the upper bound is meaningless 
                |     1
                |         the upper bound can be reached 
                |     2
                |         the upper bound cannot be reached

        :return: int
        """

        return self.com_object.RangeMaxValidity

    @range_max_validity.setter
    def range_max_validity(self, value: int):
        """
        :param int value:
        """

        self.com_object.RangeMaxValidity = value

    @property
    def range_min(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property RangeMin() As long
                |     Returns or sets the value of the lower bound that the parameter object
                |     value can take.
                | 
                |     Example:
                |         This example sets the RangeMin value to 0 if its value is bigger than
                |         0:
                | 
                |          If (Length.RangeMin > 0.0 and Length.RangeMinValidity <> 0) 
                |          Then
                |              Length.RangeMin = 0.0
                |          End If

        :return: int
        """

        return self.com_object.RangeMin

    @range_min.setter
    def range_min(self, value: int):
        """
        :param int value:
        """

        self.com_object.RangeMin = value

    @property
    def range_min_validity(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property RangeMinValidity() As long
                |     Returns or sets the type of the lower bound of the
                |     parameter.
                | 
                |     0
                |         the lower bound is meaningless 
                |     1
                |         the lower bound can be reached 
                |     2
                |         the lower bound cannot be reached

        :return: int
        """

        return self.com_object.RangeMinValidity

    @range_min_validity.setter
    def range_min_validity(self, value: int):
        """
        :param int value:
        """

        self.com_object.RangeMinValidity = value

    @property
    def value(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Value() As long
                |     Returns or sets the value of the integer parameter. Units are expressed in
                |     the IS unit system.
                | 
                |     Example:
                |         This example sets the year value to 0 if its value is equal to
                |         2000:
                | 
                |          If (year.Value = 2000)  Then
                |              year.Value = 0
                |          End If

        :return: int
        """

        return self.com_object.Value

    @value.setter
    def value(self, value: int):
        """
        :param int value:
        """

        self.com_object.Value = value

    def get_enumerate_values(self, o_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetEnumerateValues(CATSafeArrayVariant oSafeArray)
                |     Returns an array containing the different values that the int param can
                |     take in the case of multiple values.
                | 
                |     Parameters:
                | 
                |         oSafeArray
                |             the array
                | 
                |             Example:
                | 
                |                  Dim enumValues () as Variant
                |                  ReDim enumValues (anIntegerParameter.GetEnumerateValuesSize()
                |                  - 1)
                |                 anIntegerParameter.GetEnumerateValues(enumValues)
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
                |     Sets an array containing the different values that the real param can take
                |     in the case of multiple values.
                | 
                |     Parameters:
                | 
                |         iSafeArray
                |             the different possible values

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
        return f'IntParam(name="{ self.name }")'
