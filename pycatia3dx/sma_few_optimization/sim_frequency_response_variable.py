"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_few_optimization.sim_non_parametric_response_variable import SimNonParametricResponseVariable


class SimFrequencyResponseVariable(SimNonParametricResponseVariable):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    SMAFeaOptimizationIDLItf.SimDesignImprovementResponseVariable
                |                        SMAFeaOptimizationIDLItf.SimNonParametricResponseVariable
                |                             SimFrequencyResponseVariable
                | 
                | Represents the Frequency response variable object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimFrequencyResponseVariable as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyFrequencyResponseVariable As
                |      SimFrequencyResponseVariable
                |      Set MyFrequencyResponseVariable = MyFeatures.Add("SimFrequencyResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimFrequencyResponseVariable named "Frequency Response Variable.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim SimFrequencyResponseVariable As
                |      SimFrequencyResponseVariable
                |      Set MyFrequencyResponseVariable = MyFeatures.Item("Frequency Response Variable.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimFrequencyResponseVariable as following:
                | 
                |      ...
                |      MyFrequencyResponseVariable = MyFeatures.Add("SimFrequencyResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimFrequencyResponseVariable named "Frequency Response Variable.1" as
                |     following:
                | 
                |      ...
                |      MyFrequencyResponseVariable = MyFeatures.Item("Frequency Response Variable.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimFrequencyResponseVariableType
                |     Returns or sets the type of frequency force design response.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def get_max_mode(self, o_max_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMaxMode(short oMaxMode)
                |     Gets the maximum mode.
                | 
                |     Parameters:
                | 
                |         oMaxMode
                |             [out] Number of maximum mode Quantity: REAL, units: None

        :param int o_max_mode:
        :return: None
        """
        return self.com_object.GetMaxMode(o_max_mode)

    def get_min_mode(self, o_min_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinMode(short oMinMode)
                |     Gets the minimum mode.
                | 
                |     Parameters:
                | 
                |         oMinMode
                |             [out] Number of minimum mode Quantity: REAL, units: None

        :param int o_min_mode:
        :return: None
        """
        return self.com_object.GetMinMode(o_min_mode)

    def get_mode_number(self, o_mode_number: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetModeNumber(short oModeNumber)
                |     Gets the mode number.
                | 
                |     Parameters:
                | 
                |         oModeNumber
                |             [out] Number of minimum mode Quantity: REAL, units: None

        :param int o_mode_number:
        :return: None
        """
        return self.com_object.GetModeNumber(o_mode_number)

    def set_max_mode(self, i_max_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaxMode(short iMaxMode)
                |     Sets the maximum mode.
                | 
                |     Parameters:
                | 
                |         iMaxMode
                |             [in] Number of maximum mode Quantity: REAL, units: None

        :param int i_max_mode:
        :return: None
        """
        return self.com_object.SetMaxMode(i_max_mode)

    def set_min_mode(self, i_min_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMinMode(short iMinMode)
                |     Sets the minimum mode.
                | 
                |     Parameters:
                | 
                |         iMinMode
                |             [in] Number of minimum mode Quantity: REAL, units: None

        :param int i_min_mode:
        :return: None
        """
        return self.com_object.SetMinMode(i_min_mode)

    def set_mode_number(self, i_mode_number: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetModeNumber(short iModeNumber)
                |     Sets the mode number.
                | 
                |     Parameters:
                | 
                |         iModeNumber
                |             [in] Number of maximum mode Quantity: REAL, units: None

        :param int i_mode_number:
        :return: None
        """
        return self.com_object.SetModeNumber(i_mode_number)

    def __repr__(self):
        return f'SimFrequencyResponseVariable(name="{ self.name }")'
