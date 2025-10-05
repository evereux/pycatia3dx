"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.sma_spa_structural.sim_analysis_restart_step_property import SimAnalysisRestartStepProperty


class SimExplicitDynamicStep(SimStep):

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
                |                         SimExplicitDynamicStep
                | 
                | Represents the Explicit Dynamic Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimExplicitDynamicStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyExplicitDynamicStep As SimExplicitDynamicStep
                |      Set MyExplicitDynamicStep = MySteps.Add("SimExplicitDynamicStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimExplicitDynamicStep named
                |     "Explicit Dynamic Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyExplicitDynamicStep As SimExplicitDynamicStep
                |      Set MyExplicitDynamicStep = MySteps.Item("Explicit Dynamic Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimExplicitDynamicStep as
                |     following:
                | 
                |      ...
                |      myExplicitDynamicStep = mySteps.Add("SimExplicitDynamicStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimExplicitDynamicStep
                |     named "Explicit Dynamic Step.1" as following:
                | 
                |      ...
                |      myExplicitDynamicStep = mySteps.Item("Explicit Dynamic Step.1")
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
    def adiabatic_heating_effects_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdiabaticHeatingEffectsFlag() As boolean
                | 
                |     TRUE: Adiabatic heating effects is activated.
                | 
                |     FALSE: Adiabatic heating effects is desactivated.

        :return: bool
        """

        return self.com_object.AdiabaticHeatingEffectsFlag

    @adiabatic_heating_effects_flag.setter
    def adiabatic_heating_effects_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AdiabaticHeatingEffectsFlag = value

    @property
    def bulk_viscosity_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BulkViscosityFlag() As boolean
                |     Returns or sets the flag that determines if the bulk viscosity parameters
                |     are enabled.
                | 
                |     TRUE: The bulk viscosity parameters are enabled.
                | 
                |     FALSE: The bulk viscosity parameters are disabled.

        :return: bool
        """

        return self.com_object.BulkViscosityFlag

    @bulk_viscosity_flag.setter
    def bulk_viscosity_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.BulkViscosityFlag = value

    @property
    def element_by_element_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ElementByElementFlag() As boolean
                | 
                |     TRUE: Element by element time incrementation calculation is
                |     activated.
                | 
                |     FALSE: Element by element time incrementation calculation is desactivate.

        :return: bool
        """

        return self.com_object.ElementByElementFlag

    @element_by_element_flag.setter
    def element_by_element_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ElementByElementFlag = value

    @property
    def fixed_incrementation_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FixedIncrementationScheme() As
                | SimExplicitDynamicStepFixedIncrementationTypeEnm
                |     Returns or sets the retrieved Fixed incrementation type.

        :return: SimExplicitDynamicStepFixedIncrementationTypeEnm
        """

        return self.com_object.FixedIncrementationScheme

    @fixed_incrementation_scheme.setter
    def fixed_incrementation_scheme(self, value: int):
        """
        :param int value:
        """

        self.com_object.FixedIncrementationScheme = value

    @property
    def geometric_non_linearity_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GeometricNonLinearityFlag() As boolean
                |     Returns or sets the flag that determines if the step is geometrically non
                |     linear.
                | 
                |     TRUE: the step is geometrically non linear.
                | 
                |     FALSE: the step is not geometrically non linear.

        :return: bool
        """

        return self.com_object.GeometricNonLinearityFlag

    @geometric_non_linearity_flag.setter
    def geometric_non_linearity_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.GeometricNonLinearityFlag = value

    @property
    def improved_dt_method_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ImprovedDTMethodFlag() As boolean
                | 
                |     TRUE: Improved DT method option is activated.
                | 
                |     FALSE: Improve DT method option is deactivated.

        :return: bool
        """

        return self.com_object.ImprovedDTMethodFlag

    @improved_dt_method_flag.setter
    def improved_dt_method_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ImprovedDTMethodFlag = value

    @property
    def linear_bulk_viscosity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LinearBulkViscosity() As double
                |     Returns or sets the linear bulk viscosity parameter.

        :return: float
        """

        return self.com_object.LinearBulkViscosity

    @linear_bulk_viscosity.setter
    def linear_bulk_viscosity(self, value: float):
        """
        :param float value:
        """

        self.com_object.LinearBulkViscosity = value

    @property
    def maximum_time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumTimeIncrement() As double
                |     Returns or sets the retrieved maximum increments.

        :return: float
        """

        return self.com_object.MaximumTimeIncrement

    @maximum_time_increment.setter
    def maximum_time_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumTimeIncrement = value

    @property
    def maximum_time_increment_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumTimeIncrementFlag() As boolean
                |     Returns or sets the flag that determines if the maximum time increment is
                |     enabled.
                | 
                |     TRUE: The maximum time increment is enabled.
                | 
                |     FALSE: The maximum time increment is disabled.

        :return: bool
        """

        return self.com_object.MaximumTimeIncrementFlag

    @maximum_time_increment_flag.setter
    def maximum_time_increment_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MaximumTimeIncrementFlag = value

    @property
    def quadratic_bulk_viscosity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property QuadraticBulkViscosity() As double
                |     Returns or sets the quadratic bulk viscosity parameter.

        :return: float
        """

        return self.com_object.QuadraticBulkViscosity

    @quadratic_bulk_viscosity.setter
    def quadratic_bulk_viscosity(self, value: float):
        """
        :param float value:
        """

        self.com_object.QuadraticBulkViscosity = value

    @property
    def restart_step_property(self) -> SimAnalysisRestartStepProperty:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RestartStepProperty() As SimAnalysisRestartStepProperty (Read
                | Only)
                |     Returns the restart step property for the Explicit Dynamic step.

        :return: SimAnalysisRestartStepProperty
        """

        return SimAnalysisRestartStepProperty(self.com_object.RestartStepProperty)

    @property
    def scale_factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScaleFactor() As double
                |     Returns or sets the retrieved scale factor.

        :return: float
        """

        return self.com_object.ScaleFactor

    @scale_factor.setter
    def scale_factor(self, value: float):
        """
        :param float value:
        """

        self.com_object.ScaleFactor = value

    @property
    def step_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StepTime() As double
                |     Returns or sets the retrieved total time for the Explicit dynamic step.

        :return: float
        """

        return self.com_object.StepTime

    @step_time.setter
    def step_time(self, value: float):
        """
        :param float value:
        """

        self.com_object.StepTime = value

    @property
    def time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeIncrement() As double
                |     Returns or sets the retrieved time increment for the Explicit Dynamic step.

        :return: float
        """

        return self.com_object.TimeIncrement

    @time_increment.setter
    def time_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.TimeIncrement = value

    @property
    def time_incrementation_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeIncrementationScheme() As
                | SimTimeIncrementationScheme
                |     Returns or sets the retrieved incrementation type for the Explicit Dynamic
                |     step. 

        :return: SimTimeIncrementationScheme
        """

        return self.com_object.TimeIncrementationScheme

    @time_incrementation_scheme.setter
    def time_incrementation_scheme(self, value: int):
        """
        :param int value:
        """

        self.com_object.TimeIncrementationScheme = value

    def __repr__(self):
        return f'SimExplicitDynamicStep(name="{ self.name }")'
