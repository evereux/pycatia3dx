"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.sma_spa_structural.sim_analysis_restart_step_property import SimAnalysisRestartStepProperty


class SimCoupledThermalStressExplicitStep(SimStep):

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
                |                         SimCoupledThermalStressExplicitStep
                | 
                | Represents the Coupled Thermal Stress Explicit Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a
                |     SimCoupledThermalStressExplicitStep as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyCoupledThermalStressExplicitStep As
                |      SimCoupledThermalStressExplicitStep
                |      Set MyCoupledThermalStressExplicitStep = MySteps.Add("SimCoupledThermalStressExplicitStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a
                |     SimCoupledThermalStressExplicitStep named "Coupled Thermal Stress Explicit
                |     Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyCoupledThermalStressExplicitStep As
                |      SimCoupledThermalStressExplicitStep
                |      Set MyCoupledThermalStressExplicitStep = MySteps.Item("Coupled Thermal Stress Explicit Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a
                |     SimCoupledThermalStressExplicitStep as following:
                | 
                |      ...
                |      myCoupledThermalStressExplicitStep = mySteps.Add("SimCoupledThermalStressExplicitStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a
                |     SimCoupledThermalStressExplicitStep named "Coupled Thermal Stress Explicit
                |     Step.1" as following:
                | 
                |      ...
                |      myCoupledThermalStressExplicitStep = mySteps.Item("Coupled Thermal Stress Explicit Step.1")
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
                |     Returns or sets the element by element flag.
                |     TRUE: Element by element time incrementation calculation is
                |     activated.
                |     FALSE: Element by element time incrementation calculation is deactivated.

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
    def geometric_non_linearity_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GeometricNonLinearityFlag() As boolean
                |     Returns or sets the flag that determines if the step is geometrically non
                |     linear.
                |     TRUE: the step is geometrically non linear.
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
                |     Returns or sets the improved DT method flag.
                |     TRUE: Improved DT method option is activated.
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
    def incrementation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IncrementationType() As SimTimeIncrementationScheme
                |     Returns or sets the incrementation type.

        :return: SimTimeIncrementationScheme
        """

        return self.com_object.IncrementationType

    @incrementation_type.setter
    def incrementation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.IncrementationType = value

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
                |     Returns or sets the maximum time for the increments of the Coupled Thermal
                |     Explicit Stress step.

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
                |     Returns the restart step property for the Coupled Thermal Explicit Stress
                |     step.

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
                |     Returns or sets the scale factor.

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
                |     Returns or sets the retrieved total time for the Coupled Thermal Explicit
                |     Stress step.

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
                |     Returns or sets the time increment for the Coupled Thermal Explicit Stress
                |     step. 

        :return: float
        """

        return self.com_object.TimeIncrement

    @time_increment.setter
    def time_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.TimeIncrement = value

    def __repr__(self):
        return f'SimCoupledThermalStressExplicitStep(name="{ self.name }")'
