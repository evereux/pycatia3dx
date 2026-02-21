"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimFrequencyConstraint(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimFrequencyConstraint
                | 
                | Represents the frequency constraint object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimFrequencyConstraint as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyFrequencyConstraint As SimFrequencyConstraint
                |      Set MyFrequencyConstraint = MyFeatures.Add("SimFrequencyConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimFrequencyConstraint named "Frequency Constraint.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyFrequencyConstraint As SimFrequencyConstraint
                |      Set MyFrequencyConstraint = MyFeatures.Item("Frequency Constraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimFrequencyConstraint as following:
                | 
                |      ...
                |      MyFrequencyConstraint = MyFeatures.Add("SimFrequencyConstraint")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimFrequencyConstraint named "Frequency Constraint.1" as
                |     following:
                | 
                |      ...
                |      MyFrequencyConstraint = MyFeatures.Item("Frequency Constraint.1")
                |      
                | 
                | Warning:
                |     You will also have to take care of methods with array parameters. Refer
                |     "About Microsoft Automation Languages, Debug, and Compatibility" in the
                |     documentation. 
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def load_case(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LoadCase() As CATBaseDispatch (Read Only)
                |     Returns the Linear Loadcase.

        :return: AnyObject
        """

        return AnyObject(self.com_object.LoadCase)

    def get_maximum_frequency(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaximumFrequency() As CATSafeArrayVariant
                |     Gets the minimum frequency.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Maximum frequency value Quantity: REAL, units: None

        :return: tuple
        """
        return self.com_object.GetMaximumFrequency()

    def get_minimum_frequency(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMinimumFrequency() As CATSafeArrayVariant
                |     Gets the minimum frequency.
                | 
                |     Parameters:
                | 
                |         oVal
                |             [out] Minimum frequency value Quantity: REAL, units: None

        :return: tuple
        """
        return self.com_object.GetMinimumFrequency()

    def get_number_of_modes(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfModes() As long
                |     Gets the mode number.
                | 
                |     Parameters:
                | 
                |         oModeNumber
                |             [out] Number of minimum mode Quantity: REAL, units: None

        :return: int
        """
        return self.com_object.GetNumberOfModes()

    def set_maximum_frequency(self, i_val: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetMaximumFrequency(CATSafeArrayVariant iVal)
                |     Sets the minimum frequency.
                |
                |     Parameters:
                |
                |         iVal
                |             [in] Maximum frequency value Quantity: REAL, units: None

        :param tuple i_val:
        :return: None
        """
        return self.com_object.SetMaximumFrequency(i_val)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_maximum_frequency'
        # vba_code = """
        # Public Function set_maximum_frequency(sim_frequency_constraint)
        #     Dim iVal (2)
        #     sim_frequency_constraint.SetMaximumFrequency iVal
        #     set_maximum_frequency = iVal
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_minimum_frequency(self, i_val: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetMinimumFrequency(CATSafeArrayVariant iVal)
                |     Sets the minimum frequency.
                |
                |     Parameters:
                |
                |         iVal
                |             [in] Minimum frequency value Quantity: REAL, units: None

        :param tuple i_val:
        :return: None
        """
        return self.com_object.SetMinimumFrequency(i_val)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_minimum_frequency'
        # vba_code = """
        # Public Function set_minimum_frequency(sim_frequency_constraint)
        #     Dim iVal (2)
        #     sim_frequency_constraint.SetMinimumFrequency iVal
        #     set_minimum_frequency = iVal
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_number_of_modes(self, o_numberof_modes: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetNumberOfModes(long oNumberofModes)
                |     Sets the mode number.
                | 
                |     Parameters:
                | 
                |         iModeNumber
                |             [in] Number of maximum mode Quantity: REAL, units: None

        :param int o_numberof_modes:
        :return: None
        """
        return self.com_object.SetNumberOfModes(o_numberof_modes)

    def __repr__(self):
        return f'SimFrequencyConstraint(name="{self.name}")'
