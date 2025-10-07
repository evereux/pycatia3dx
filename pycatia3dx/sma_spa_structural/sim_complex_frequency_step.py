"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep


class SimComplexFrequencyStep(SimStep):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaFoundationIDLItf.SimStep
                |                         SimComplexFrequencyStep
                | 
                | Represents the Complex Frequency Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimComplexFrequencyStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyComplexFrequencyStep As SimComplexFrequencyStep
                |      Set MyComplexFrequencyStep = MySteps.Add("SimComplexFrequencyStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimComplexFrequencyStep named
                |     "Complex Frequency Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyComplexFrequencyStep As SimComplexFrequencyStep
                |      Set MyComplexFrequencyStep = MySteps.Item("Complex Frequency Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimComplexFrequencyStep
                |     as following:
                | 
                |      ...
                |      myComplexFrequencyStep = mySteps.Add("SimComplexFrequencyStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimComplexFrequencyStep
                |     named "Complex Frequency Step.1" as following:
                | 
                |      ...
                |      myComplexFrequencyStep = mySteps.Item("Complex Frequency Step.1")
                |      
                | 
                | See also:
                |     SimSteps
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activated() As boolean
                |     Returns or sets the activation status.

        :return: bool
        """

        return self.com_object.Activated

    @activated.setter
    def activated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activated = value

    @property
    def cutoff_frequency(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CutoffFrequency() As double
                |     Returns or sets the cut off frequency. Quantity: HERTZ, units: Hz.

        :return: float
        """

        return self.com_object.CutoffFrequency

    @cutoff_frequency.setter
    def cutoff_frequency(self, value: float):
        """
        :param float value:
        """

        self.com_object.CutoffFrequency = value

    @property
    def cutoff_frequency_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CutoffFrequencyFlag() As boolean
                |     Returns or sets the flag that determines if the cut off frequency is
                |     specified.
                |     TRUE : the cut off frequency is specified.
                |     FALSE : the cut off frequency is not specified.

        :return: bool
        """

        return self.com_object.CutoffFrequencyFlag

    @cutoff_frequency_flag.setter
    def cutoff_frequency_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CutoffFrequencyFlag = value

    @property
    def friction_damping_authorization_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrictionDampingAuthorizationFlag() As boolean
                |     Returns or sets the flag that determines if the friction-induced damping
                |     option is used.
                |     TRUE : the friction-induced damping option is used.
                |     FALSE : the friction-induced damping option is not used.

        :return: bool
        """

        return self.com_object.FrictionDampingAuthorizationFlag

    @friction_damping_authorization_flag.setter
    def friction_damping_authorization_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FrictionDampingAuthorizationFlag = value

    @property
    def matrix_storage_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MatrixStorageScheme() As SimMatrixStorageScheme
                |     Returns or sets the type of the matrix storage for the static step.

        :return: int
        """

        return self.com_object.MatrixStorageScheme

    @matrix_storage_scheme.setter
    def matrix_storage_scheme(self, value: int):
        """
        :param int value:
        """

        self.com_object.MatrixStorageScheme = value

    @property
    def maximum_frequency(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumFrequency() As double
                |     Returns or sets the maximum frequency. Quantity: FREQUENCY, units: Hz.

        :return: float
        """

        return self.com_object.MaximumFrequency

    @maximum_frequency.setter
    def maximum_frequency(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumFrequency = value

    @property
    def maximum_frequency_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumFrequencyFlag() As boolean
                |     Returns or sets the flag that determines if the maximum frequency is
                |     specified.
                |     TRUE : the maximum frequency is specified.
                |     FALSE : the maximum frequency is not specified.

        :return: bool
        """

        return self.com_object.MaximumFrequencyFlag

    @maximum_frequency_flag.setter
    def maximum_frequency_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MaximumFrequencyFlag = value

    @property
    def minimum_frequency(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumFrequency() As double
                |     Returns or sets the minimum frequency. Quantity: FREQUENCY, units: Hz.

        :return: float
        """

        return self.com_object.MinimumFrequency

    @minimum_frequency.setter
    def minimum_frequency(self, value: float):
        """
        :param float value:
        """

        self.com_object.MinimumFrequency = value

    @property
    def minimum_frequency_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumFrequencyFlag() As boolean
                |     Returns or sets the flag that determines if the minimum frequency is
                |     specified.
                |     TRUE : the minimum frequency is specified.
                |     FALSE : the minimum frequency is not specified.

        :return: bool
        """

        return self.com_object.MinimumFrequencyFlag

    @minimum_frequency_flag.setter
    def minimum_frequency_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MinimumFrequencyFlag = value

    @property
    def number_of_modes(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfModes() As long
                |     Returns or sets the number of modes.

        :return: int
        """

        return self.com_object.NumberOfModes

    @number_of_modes.setter
    def number_of_modes(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfModes = value

    @property
    def property_evaluation(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PropertyEvaluation() As double
                |     Returns or sets the property evaluation. Quantity: HERTZ, units: Hz.

        :return: float
        """

        return self.com_object.PropertyEvaluation

    @property_evaluation.setter
    def property_evaluation(self, value: float):
        """
        :param float value:
        """

        self.com_object.PropertyEvaluation = value

    @property
    def property_evaluation_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PropertyEvaluationFlag() As boolean
                |     Returns or sets the flag that determines if the property evaluation is
                |     specified.
                |     TRUE : the property evaluation is specified.
                |     FALSE : the property evaluation is not specified.

        :return: bool
        """

        return self.com_object.PropertyEvaluationFlag

    @property_evaluation_flag.setter
    def property_evaluation_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PropertyEvaluationFlag = value

    @property
    def shift_point(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShiftPoint() As double
                |     Returns or sets the shift point. Quantity: HERTZSQUARE, units: Hz2.

        :return: float
        """

        return self.com_object.ShiftPoint

    @shift_point.setter
    def shift_point(self, value: float):
        """
        :param float value:
        """

        self.com_object.ShiftPoint = value

    @property
    def shift_point_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShiftPointFlag() As boolean
                |     Returns or sets the flag that determines if the shift point is
                |     specified.
                |     TRUE : the shift point is specified.
                |     FALSE : the shift point is not specified.

        :return: bool
        """

        return self.com_object.ShiftPointFlag

    @shift_point_flag.setter
    def shift_point_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ShiftPointFlag = value

    @property
    def specified_modes_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecifiedModesFlag() As boolean
                |     Returns or sets the flag that determines if the number of eigenvalues to be
                |     calculated is specified.
                |     TRUE : the number of eigenvalues to be calculated is specified.
                |     FALSE : all the eigenvalues from the minimum frequency of interest up to the maximum frequency of interest will be calculated. 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :return: bool
        """

        return self.com_object.SpecifiedModesFlag

    @specified_modes_flag.setter
    def specified_modes_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SpecifiedModesFlag = value

    def __repr__(self):
        return f'SimComplexFrequencyStep(name="{ self.name }")'
