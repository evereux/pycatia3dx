"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimLegend(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimLegend
                | 
                | Represents the field plot legend.
                | Role:Legend options determine the range of values displayed in a contour or
                | symbol plot.
                | Example:
                | 
                |  Given a SimFieldPlot object, you can retrieve a Legend object as
                |  following.
                |  
                | 
                |  Dim oLegend As SimLegend
                |  oLegend = oFieldPlot.Legend
                |  
                | 
                | See also:
                |     SimFieldPlot.Legend
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_data(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActiveData() As boolean (Read Only)
                |     Returns True if any active data is pointed by the legend.

        :return: bool
        """

        return self.com_object.ActiveData

    @property
    def nb_colors(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NbColors() As long
                |     Returns and sets the number of colors of this Legend.
                |     The number of colors will be used in the texturing of the 3D
                |     representations of the Data Display features pointed by this
                |     Legend.
                |     The default number of colors is 10 but it may be imposed.

        :return: int
        """

        return self.com_object.NbColors

    @nb_colors.setter
    def nb_colors(self, value: int):
        """
        :param int value:
        """

        self.com_object.NbColors = value

    @property
    def nb_significant_digits(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NbSignificantDigits(long inNbSignificantDigits) (Write
                | Only)
                |     Sets the number of significant digits of this Legend.

        :return: int
        """

        return self.com_object.NbSignificantDigits

    @nb_significant_digits.setter
    def nb_significant_digits(self, value: int):
        """
        :param int value:
        """

        self.com_object.NbSignificantDigits = value

    @property
    def number_format(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberFormat(long inNumberFormat) (Write Only)
                |     Sets the number format of this Legend.
                |     The available number format are: 0 = AUTOMATIC 1 = SCIENTIFIC 2 = DECIMAL

        :return: int
        """

        return self.com_object.NumberFormat

    @number_format.setter
    def number_format(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberFormat = value

    @property
    def style(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Style() As CATBSTR
                |     Returns and sets the display style of this Legend. The default style is
                |     simplified.

        :return: str
        """

        return self.com_object.Style

    @style.setter
    def style(self, value: str):
        """
        :param str value:
        """

        self.com_object.Style = value

    def are_min_max_values_imposed(self, ob_is_min_value_imposed: bool, ob_is_max_value_imposed: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AreMinMaxValuesImposed(boolean obIsMinValueImposed,boolean
                | obIsMaxValueImposed)
                |     Tells whether the minimum and maximum values are imposed or
                |     not.
                | 
                |     Parameters:
                | 
                |         obIsMinValueImposed
                |             The minimum value status. TRUE if it is imposed 
                |         obIsMaxValueImposed
                |             The maximum value status. TRUE if it is imposed 
                | 
                |     See also:
                |         GetMinValue, SetMinValue, ResetMinValue,
                |         StartAnimationRange

        :param bool ob_is_min_value_imposed:
        :param bool ob_is_max_value_imposed:
        :return: None
        """
        return self.com_object.AreMinMaxValuesImposed(ob_is_min_value_imposed, ob_is_max_value_imposed)

    def get_color_modifiers(self, ob_smooth: bool, ob_inverse: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetColorModifiers(boolean obSmooth,boolean obInverse)
                |     Gets the modifiers for the colors of this Legend.
                | 
                |     Parameters:
                | 
                |         obSmooth
                |             Do the legend colors transition smoothly 
                |         obInverse
                |             Is the order of the legend colors inverted 
                | 
                |     See also:
                |         SetColorModifiers

        :param bool ob_smooth:
        :param bool ob_inverse:
        :return: None
        """
        return self.com_object.GetColorModifiers(ob_smooth, ob_inverse)

    def get_colors(self, opn_colors: tuple, on_num_colors: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetColors(CATSafeArrayVariant opnColors,long onNumColors)
                |     Gets the colors of this Legend.
                |     The colors are used in the texturing of the 3D representations of the Data
                |     Display features pointed by this Legend.
                | 
                |     Parameters:
                | 
                |         opnColors
                |             The array of RGB color values. It is the responsibility of the
                |             caller to release the memory 
                |         onNumColors
                |             The number of colors. Is is one third the size of the returned
                |             opnColors array

        :param tuple opn_colors:
        :param int on_num_colors:
        :return: None
        """
        return self.com_object.GetColors(opn_colors, on_num_colors)

    def get_computed_min_max_range(self, od_min_value: float, od_max_value: float, ib_current_units: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetComputedMinMaxRange(double odMinValue,double odMaxValue,boolean
                | ibCurrentUnits)
                |     Gets the computed minimum and maximum values of this
                |     Legend.
                |     The automatically computed minimum and maximum values, the lower and upper
                |     bounds, of the range of the data displayed by all referenced Data Display
                |     features.
                | 
                |     Parameters:
                | 
                |         odMinValue
                |             The computed minimum value 
                |         odMaxValue
                |             The computed maximum value 
                |         ibCurrentUnits
                |             If FALSE (default) the returned values will be in MKS
                |             units.
                |             Else, they will be in the currently displayed units for the
                |             results. 
                | 
                |     See also:
                |         GetMinMaxValue, SetMinMaxValue, ResetMinMaxValue

        :param float od_min_value:
        :param float od_max_value:
        :param bool ib_current_units:
        :return: None
        """
        return self.com_object.GetComputedMinMaxRange(od_min_value, od_max_value, ib_current_units)

    def get_data_list(self, ib_visible_only: bool, o_data_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDataList(boolean ibVisibleOnly,CATSafeArrayVariant
                | oDataList)
                |     Gets the list of items/features pointed by this Legend.
                |     The items/features pointed by a Legend should be displayed in the
                |     view.
                | 
                |     Parameters:
                | 
                |         ibVisibleOnly
                |             If passed as TRUE (default is FALSE), only visible items/features
                |             will be returned in the list 
                |         oDataList
                |             The list of items/features

        :param bool ib_visible_only:
        :param tuple o_data_list:
        :return: None
        """
        return self.com_object.GetDataList(ib_visible_only, o_data_list)

    def get_linear_values(self, opd_values: tuple, on_num_values: int, ib_current_units: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLinearValues(CATSafeArrayVariant opdValues,long onNumValues,boolean
                | ibCurrentUnits)
                |     Gets the linear separation values of this Legend.
                |     The positions between min and max where color changes
                |     occur.
                | 
                |     Parameters:
                | 
                |         opdValues
                |             The array of values. It is the responsibility of
                |             the
                |             caller to release the memory. If returned as NULL,
                |             the color ramp is a solid color (min=max) 
                |         odNumValues
                |             The number of values. Is it equal to the size of
                |             the the returned opdValues array. If returned as
                |             0, the color ramp is a solid color (min=max). 
                |         ibCurrentUnits
                |             If FALSE (default) the returned values will be
                |             in MKS units. Else, they will be in the
                |             currently displayed units for the results.

        :param tuple opd_values:
        :param int on_num_values:
        :param bool ib_current_units:
        :return: None
        """
        return self.com_object.GetLinearValues(opd_values, on_num_values, ib_current_units)

    def get_min_max_value(self, od_min_value: float, od_max_value: float, ib_current_units: bool, ib_allow_invalid: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinMaxValue(double odMinValue,double odMaxValue,boolean
                | ibCurrentUnits,boolean ibAllowInvalid)
                |     Gets the minimum and maximum values of this Legend.
                |     The minimum and maximum values of a Legend are the lower and upper bounds
                |     of the
                |     range of the data displayed by the referenced Data Display
                |     features.
                |     Default values are automaticaly computed but it may be
                |     imposed.
                | 
                |     Parameters:
                | 
                |         odMinValue
                |             The minimum value 
                |         odMaxValue
                |             The maximum value 
                |         ibCurrentUnits
                |             If FALSE (default) the returned values will be in MKS
                |             units.
                |             Else, they will be in the currently displayed units for the results
                |             
                |         ibAllowInvalid
                |             If FALSE (default) a specified min or max value will be ignored
                |             if
                |             is invalid for the current state of the legend. The computed
                |             value
                |             will be returned instead 
                | 
                |     See also:
                |         SetMinMaxValue, ResetMinMaxValue

        :param float od_min_value:
        :param float od_max_value:
        :param bool ib_current_units:
        :param bool ib_allow_invalid:
        :return: None
        """
        return self.com_object.GetMinMaxValue(od_min_value, od_max_value, ib_current_units, ib_allow_invalid)

    def get_number_display(self, on_number_format: int, on_nb_significant_digits: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetNumberDisplay(long onNumberFormat,long
                | onNbSignificantDigits)
                |     Gets the number format and number of significant digits of this
                |     Legend.
                | 
                |     Parameters:
                | 
                |         onNumberFormat
                |             Number format 
                |         onNbSignificantDigits
                |             Number of significant digits

        :param int on_number_format:
        :param int on_nb_significant_digits:
        :return: None
        """
        return self.com_object.GetNumberDisplay(on_number_format, on_nb_significant_digits)

    def get_values(self, opd_values: tuple, on_num_values: int, ib_current_units: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetValues(CATSafeArrayVariant opdValues,long onNumValues,boolean
                | ibCurrentUnits)
                |     Gets the user specified values of this Legend.
                |     The values are used in the texturing of the 3D representations of
                |     the
                |     Data Display features pointed by this Legend when a linear
                |     separation
                |     between values is not desired.
                | 
                |     Parameters:
                | 
                |         opdValues
                |             The array of values. It is the responsibility of
                |             the
                |             caller to release the memory. If returned as NULL,
                |             no values have been set so a linear separation is expected
                |             
                |         odNumValues
                |             The number of values. Is it equal to the size of
                |             the the returned opdValues array. If returned as
                |             0, no values have been set so a linear separation
                |             is expected. @see #GetLinearValues 
                |         ibCurrentUnits
                |             If FALSE (default) the returned values will be
                |             in MKS units. Else, they will be in the
                |             currently displayed units for the results.

        :param tuple opd_values:
        :param int on_num_values:
        :param bool ib_current_units:
        :return: None
        """
        return self.com_object.GetValues(opd_values, on_num_values, ib_current_units)

    def has_empty_min_max_range(self, ib_computed: bool) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasEmptyMinMaxRange(boolean ibComputed) As boolean
                |     Determines if the minimum and maximum values of this Legend are not the
                |     same.
                |     The minimum and maximum values, the lower and upper
                |     bounds,
                |     of the range of the data displayed by all referenced Data Display features
                |     are evaluated
                |     to determine if they are nearly identical.
                | 
                |     Parameters:
                | 
                |         ibComputed
                |             If TRUE (default) the automatically computed range will be
                |             evaluated
                |             Else, any specified min or max value will be used for the
                |             evaluation 
                | 
                |     Returns:
                |         Returns True if the range is near zero 
                |     See also:
                |         GetComputedMinMaxRange

        :param bool ib_computed:
        :return: bool
        """
        return self.com_object.HasEmptyMinMaxRange(ib_computed)

    def reset_max_value(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResetMaxValue()
                |     Sets the maximum value of this Legend to its default, automatically
                |     computed, value.
                | 
                |     See also:
                |         GetMinMaxValue, SetMaxValue, SetMinMaxValue

        :return: None
        """
        return self.com_object.ResetMaxValue()

    def reset_min_max_value(self, ib_reset_min: bool, ib_reset_max: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResetMinMaxValue(boolean ibResetMin,boolean ibResetMax)
                |     Sets the minimum or maximum value of this Legend to its default,
                |     automatically computed, value.
                |     The minimum and maximum values of a Legend are the lower and upper bounds
                |     of the range
                |     of the data displayed by the referenced Data Display
                |     features.
                | 
                |     Parameters:
                | 
                |         ibResetMin
                |             Reset the minimum value to its default if TRUE (default)
                |             
                |         ibResetMax
                |             Reset the maximum value to its default if TRUE (default)
                |             
                | 
                |     See also:
                |         GetMinMaxValue, SetMinMaxValue

        :param bool ib_reset_min:
        :param bool ib_reset_max:
        :return: None
        """
        return self.com_object.ResetMinMaxValue(ib_reset_min, ib_reset_max)

    def reset_min_value(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResetMinValue()
                |     Sets the minimum value of this Legend to its default, automatically
                |     computed value.
                | 
                |     See also:
                |         GetMinMaxValue, SetMinValue, SetMinMaxValue

        :return: None
        """
        return self.com_object.ResetMinValue()

    def set_color_modifiers(self, ib_smooth: bool, ib_inverse: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetColorModifiers(boolean ibSmooth,boolean ibInverse)
                |     Sets the modifiers for the colors of this Legend.
                | 
                |     Parameters:
                | 
                |         ibSmooth
                |             Should the legend colors transition smoothly 
                |         ibInverse
                |             Should the order of the legend colors be inverted 
                | 
                |     See also:
                |         GetColorModifiers

        :param bool ib_smooth:
        :param bool ib_inverse:
        :return: None
        """
        return self.com_object.SetColorModifiers(ib_smooth, ib_inverse)

    def set_max_value(self, id_max_value: float, ib_current_units: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaxValue(double idMaxValue,boolean ibCurrentUnits)
                |     Sets the maximum value of this Legend.
                |     Setting the maximum value of a Legend will restrict the range of the data
                |     displayed by the referenced Data Display features.
                | 
                |     Parameters:
                | 
                |         idMaxValue
                |             The maximum value 
                |         ibCurrentUnits
                |             If FALSE (default) the input values will be
                |             treated as MKS units. Else, it will be treated
                |             as the currently displayed units for the results 
                | 
                |     See also:
                |         GetMinMaxValue, ResetMaxValue, ResetMinMaxValue

        :param float id_max_value:
        :param bool ib_current_units:
        :return: None
        """
        return self.com_object.SetMaxValue(id_max_value, ib_current_units)

    def set_min_max_value(self, id_min_value: float, id_max_value: float, ib_current_units: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinMaxValue(double idMinValue,double idMaxValue,boolean
                | ibCurrentUnits)
                |     Sets the minimum and maximum values of this Legend.
                |     Setting the minimum or maximum values of a Legend will restrict the range
                |     of the data displayed by the referenced Data Display
                |     features.
                | 
                |     Parameters:
                | 
                |         idMinValue
                |             The minimum value 
                |         idMaxValue
                |             The maximum value 
                |         ibCurrentUnits
                |             If FALSE (default) the input values will be
                |             treated as MKS units. Else, it will be treated
                |             as the currently displayed units for the results 
                | 
                |     See also:
                |         GetMinMaxValue, ResetMinMaxValue

        :param float id_min_value:
        :param float id_max_value:
        :param bool ib_current_units:
        :return: None
        """
        return self.com_object.SetMinMaxValue(id_min_value, id_max_value, ib_current_units)

    def set_min_value(self, id_min_value: float, ib_current_units: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinValue(double idMinValue,boolean ibCurrentUnits)
                |     Sets the minimum value of this Legend.
                |     Setting the minimum value of a Legend will restrict the
                |     range
                |     of the data displayed by the referenced Data Display
                |     features.
                | 
                |     Parameters:
                | 
                |         idMinValue
                |             The minimum value 
                |         ibCurrentUnits
                |             If FALSE (default) the input values will be treated as MKS
                |             units.
                |             Else, it will be treated as the currently displayed units for the
                |             results. 
                | 
                |     See also:
                |         GetMinMaxValue, ResetMinValue, ResetMinMaxValue

        :param float id_min_value:
        :param bool ib_current_units:
        :return: None
        """
        return self.com_object.SetMinValue(id_min_value, ib_current_units)

    def start_animation_range(self, id_min_value: float, id_max_value: float, ib_current_units: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub StartAnimationRange(double idMinValue,double idMaxValue,boolean
                | ibCurrentUnits)
                |     Sets the minimum and maximum values of this Legend to use for the duration
                |     of an animation.
                |     Setting the minimum and maximum animation range values of a Legend will
                |     restrict the range of the data displayed by the referenced Data Display
                |     features. These values will override individual frame computed ranges but will
                |     not override a minimum or maximum value imposed by calling SetMinValue,
                |     SetMaxValue, or SetMinMaxValue.
                | 
                |     Parameters:
                | 
                |         idMinValue
                |             The minimum value 
                |         idMaxValue
                |             The maximum value 
                |         ibCurrentUnits
                |             If FALSE (default) the input values will be
                |             treated as MKS units. Else, it will be treated
                |             as the currently displayed units for the results. 
                | 
                |     See also:
                |         GetMinMaxValue, SetMinValue, SetMaxValue, SetMinMaxValue,
                |         AreMinMaxValuesImposed

        :param float id_min_value:
        :param float id_max_value:
        :param bool ib_current_units:
        :return: None
        """
        return self.com_object.StartAnimationRange(id_min_value, id_max_value, ib_current_units)

    def stop_animation_range(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub StopAnimationRange()
                |     Discontinues using the minimum and maximum values specified for use during
                |     an animation.
                |     Undoes the effect of calling StartAnimationRange.
                | 
                |     See also:
                |         StartAnimationRange

        :return: None
        """
        return self.com_object.StopAnimationRange()

    def __repr__(self):
        return f'SimLegend(name="{ self.name }")'
