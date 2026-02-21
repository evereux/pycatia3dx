"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter


class RealParam(Parameter):
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
                |                         RealParam
                | 
                | Represents the real parameter.
                | The following example shows how to create it:
                | 
                |  Dim aParmFact as ParametersFactory
                |  Set aParmFact = ...
                |  Dim density As RealParam
                |  Set density = aParmFact.CreateReal("density", 2.5)
                |  
                | 
                | The real parameter is the base object for dimensions.
                | 
                | See also:
                |     Dimension, ParametersFactory.CreateReal
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def maximum_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property MaximumTolerance() As double
                |     Returns or sets the value of the maximum tolerance of a parameter. Units
                |     are expressed in the IS unit system.
                | 
                |     Example:
                |         This example sets the MaximumTolerance value to 0 if its value is
                |         bigger than 0:
                | 
                |          If (Length.MaximumTolerance < 0.0)  Then
                |              Length.MaximumTolerance = 0.0
                |          End If

        :return: float
        """

        return self.com_object.MaximumTolerance

    @maximum_tolerance.setter
    def maximum_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumTolerance = value

    @property
    def minimum_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property MinimumTolerance() As double
                |     Returns or sets the value of the minimum tolerance of a parameter. Units
                |     are expressed in the IS unit system.
                | 
                |     Example:
                |         This example sets the MinimumTolerance value to 0 if its value is
                |         bigger than 0:
                | 
                |          If (Length.MinimumTolerance > 0.0)  Then
                |              Length.MinimumTolerance = 0.0
                |          End If

        :return: float
        """

        return self.com_object.MinimumTolerance

    @minimum_tolerance.setter
    def minimum_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.MinimumTolerance = value

    @property
    def range_max(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property RangeMax() As double
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

        :return: float
        """

        return self.com_object.RangeMax

    @range_max.setter
    def range_max(self, value: float):
        """
        :param float value:
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
    def range_min(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property RangeMin() As double
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

        :return: float
        """

        return self.com_object.RangeMin

    @range_min.setter
    def range_min(self, value: float):
        """
        :param float value:
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
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Value() As double
                |     Returns or sets the value of the real parameter. Units are expressed in the
                |     IS unit system, except for lengths expressed in millimeters, and angles
                |     expressed in decimal degrees.
                | 
                |     Example:
                |         This example sets the density value to 1 if its value is greater than
                |         2.5:
                | 
                |          If (density.Value > 2.5)  Then
                |              density.Value = 1
                |          End If

        :return: float
        """

        return self.com_object.Value

    @value.setter
    def value(self, value: float):
        """
        :param float value:
        """

        self.com_object.Value = value

    def get_enumerate_values(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetEnumerateValues(CATSafeArrayVariant oSafeArray)
                |     Returns an array containing the different values that the real param can
                |     take in the case of multiple values.
                |
                |     Parameters:
                |
                |         oSafeArray
                |             the array containing the different values.
                |
                |             Example:
                |
                |                  Dim enumValues () as Variant
                |                  ReDim enumValues (aRealParameter.GetEnumerateValuesSize() -
                |                  1)
                |                  aRealParameter.GetEnumerateValues(enumValues)
                |                  For i = LBound(enumValues) to UBound(enumValues)
                |                    ...
                |                  Next

        :return: tuple
        """
        return self.com_object.GetEnumerateValues()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_enumerate_values'
        # vba_code = """
        # Public Function get_enumerate_values(real_param)
        #     Dim oSafeArray (2)
        #     real_param.GetEnumerateValues oSafeArray
        #     get_enumerate_values = oSafeArray
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_enumerate_values_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetEnumerateValuesSize() As long
                |     Returns the number of enumerate values.
                | 
                |     Returns:
                |         number of enumerate values

        :return: int
        """
        return self.com_object.GetEnumerateValuesSize()

    def is_equal_to(self, i_value_to_compare: float) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func IsEqualTo(double iValueToCompare) As boolean
                |     Tests the equality of the parameter value with a given
                |     value.
                | 
                |     Parameters:
                | 
                |         iValueToCompare
                |             The value to compare the parameter value with 
                | 
                |     Returns:
                |         Indicates if the parameter values are equal or not
                | 
                |         True
                |             If the current value of the parameter (the one get by the get_Value
                |             property, for dimensions notice that it is not the MKS value) is equal to the
                |             one given in argument. Notice that two values are considered as equal if their
                |             difference is insignificant faced with the two compared values. This method
                |             allows you to avoid problems due to computation
                |             errors.
                |         False
                |             If the two values are different.

        :param float i_value_to_compare:
        :return: bool
        """
        return self.com_object.IsEqualTo(i_value_to_compare)

    def set_enumerate_values(self, i_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetEnumerateValues(CATSafeArrayVariant iSafeArray)
                |     Sets an array containing the different values that the real param can take
                |     in the case of multiple values.
                |
                |     Parameters:
                |
                |         iSafeArray
                |             possible values

        :param tuple i_safe_array:
        :return: None
        """
        return self.com_object.SetEnumerateValues(i_safe_array)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_enumerate_values'
        # vba_code = """
        # Public Function set_enumerate_values(real_param)
        #     Dim iSafeArray (2)
        #     real_param.SetEnumerateValues iSafeArray
        #     set_enumerate_values = iSafeArray
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

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
        return f'RealParam(name="{self.name}")'
