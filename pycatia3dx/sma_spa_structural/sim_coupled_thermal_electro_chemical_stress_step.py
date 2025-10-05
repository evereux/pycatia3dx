"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.sma_spa_structural.sim_analysis_restart_step_property import SimAnalysisRestartStepProperty
from pycatia3dx.sma_spa_structural.sim_stabilization import SimStabilization


class SimCoupledThermalElectroChemicalStressStep(SimStep):

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
                |                        SimCoupledThermalElectroChemicalStressStep
                | 
                | Represents the Coupled Thermal Electro Chemical Stress Step
                | object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a
                |     SimCoupledThermalElectroChemicalStressStep as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyCoupledThermalElectroChemicalStressStep As
                |      SimCoupledThermalElectroChemicalStressStep
                |      Set MyCoupledThermalElectroChemicalStressStep = MySteps.Add("SimCoupledThermalElectroChemicalStressStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a
                |     SimCoupledThermalElectroChemicalStressStep named "Coupled Thermal Electro
                |     Chemical Stress Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyCoupledThermalElectroChemicalStressStep As
                |      SimCoupledThermalElectroChemicalStressStep
                |      Set MyCoupledThermalElectroChemicalStressStep = MySteps.Item("Coupled Thermal Electro Chemical Stress Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a
                |     SimCoupledThermalElectroChemicalStressStep as following:
                | 
                |      ...
                |      myCoupledThermalElectroChemicalStressStep = mySteps.Add("SimCoupledThermalElectroChemicalStressStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a
                |     SimCoupledThermalElectroChemicalStressStep named "Coupled Thermal Electro
                |     Chemical Stress Step.1" as following:
                | 
                |      ...
                |      myCoupledThermalElectroChemicalStressStep = mySteps.Item("Coupled Thermal Electro Chemical Stress Step.1")
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
    def creep_behavior_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CreepBehaviorFlag() As boolean
                |     Returns or sets the creep behavior flag.
                |     TRUE: the step uses creep behavior.
                |     FALSE: the step does not use creep behavior.

        :return: bool
        """

        return self.com_object.CreepBehaviorFlag

    @creep_behavior_flag.setter
    def creep_behavior_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CreepBehaviorFlag = value

    @property
    def creep_integration(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CreepIntegration() As SimCoupledCreepIntegration
                |     Returns or sets the creep integration.

        :return: SimCoupledCreepIntegration
        """

        return self.com_object.CreepIntegration

    @creep_integration.setter
    def creep_integration(self, value: int):
        """
        :param int value:
        """

        self.com_object.CreepIntegration = value

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
    def initial_time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialTimeIncrement() As double
                |     Returns or sets the initial time for the increments of the Coupled Thermal
                |     Electro-Chemical Stress step. Only applicable when the incrementation scheme is
                |     Automatic.

        :return: float
        """

        return self.com_object.InitialTimeIncrement

    @initial_time_increment.setter
    def initial_time_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.InitialTimeIncrement = value

    @property
    def matrix_storage_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MatrixStorageScheme() As SimMatrixStorageScheme
                |     Returns or sets the matrix storage scheme.

        :return: SimMatrixStorageScheme
        """

        return self.com_object.MatrixStorageScheme

    @matrix_storage_scheme.setter
    def matrix_storage_scheme(self, value: int):
        """
        :param int value:
        """

        self.com_object.MatrixStorageScheme = value

    @property
    def maximum_creep_strain_rate_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumCreepStrainRateIncrement() As double
                |     Returns or sets the maximum creep strain rate increment. Only applicable
                |     when the thermal response type is transient.

        :return: float
        """

        return self.com_object.MaximumCreepStrainRateIncrement

    @maximum_creep_strain_rate_increment.setter
    def maximum_creep_strain_rate_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumCreepStrainRateIncrement = value

    @property
    def maximum_increments(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumIncrements() As long
                |     Returns or sets the maximum number of increments for the Coupled Thermal
                |     Electro-Chemical Stress step. Only applicable when the incrementation scheme is
                |     Automatic.

        :return: int
        """

        return self.com_object.MaximumIncrements

    @maximum_increments.setter
    def maximum_increments(self, value: int):
        """
        :param int value:
        """

        self.com_object.MaximumIncrements = value

    @property
    def maximum_temperature_change(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumTemperatureChange() As double
                |     Returns or sets the maximum temperature change. Only applicable when the
                |     incrementation scheme is automatic, and the thermal response type is transient.

        :return: float
        """

        return self.com_object.MaximumTemperatureChange

    @maximum_temperature_change.setter
    def maximum_temperature_change(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumTemperatureChange = value

    @property
    def maximum_time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumTimeIncrement() As double
                |     Returns or sets the maximum time for the increments of the Coupled Thermal
                |     Electro-Chemical Stress step. Only applicable when the incrementation scheme is
                |     Automatic.

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
    def minimum_time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumTimeIncrement() As double
                |     Returns or sets the minimum time for the increments of the Coupled Thermal
                |     Electro-Chemical Stress step. Only applicable when the incrementation scheme is
                |     Automatic.

        :return: float
        """

        return self.com_object.MinimumTimeIncrement

    @minimum_time_increment.setter
    def minimum_time_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.MinimumTimeIncrement = value

    @property
    def rate_dependence(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RateDependence() As boolean
                |     Returns or sets the flag for strain rate-dependence and slip
                |     rate-dependence consideration.
                |     TRUE: Strain rate and slip rate dependence is applied.
                |     FALSE: Strain rate and slip rate dependence is not applied.

        :return: bool
        """

        return self.com_object.RateDependence

    @rate_dependence.setter
    def rate_dependence(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RateDependence = value

    @property
    def restart_step_property(self) -> SimAnalysisRestartStepProperty:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RestartStepProperty() As SimAnalysisRestartStepProperty (Read
                | Only)
                |     Returns the restart step property for the Coupled Thermal Electro-Chemical
                |     Stress step.

        :return: SimAnalysisRestartStepProperty
        """

        return SimAnalysisRestartStepProperty(self.com_object.RestartStepProperty)

    @property
    def solution_technique(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SolutionTechnique() As SimCoupledSolutionTechnique
                |     Returns or sets the solution technique.

        :return: SimCoupledSolutionTechnique
        """

        return self.com_object.SolutionTechnique

    @solution_technique.setter
    def solution_technique(self, value: int):
        """
        :param int value:
        """

        self.com_object.SolutionTechnique = value

    @property
    def stabilization(self) -> SimStabilization:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Stabilization() As SimStabilization (Read Only)
                |     Returns the stabilization.

        :return: SimStabilization
        """

        return SimStabilization(self.com_object.Stabilization)

    @property
    def step_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StepTime() As double
                |     Returns or sets the step time for the Coupled Thermal Electro-Chemical
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
    def thermal_response_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThermalResponseType() As
                | SimCoupledThermalResponseType
                |     Returns or sets the thermal response type.

        :return: SimCoupledThermalResponseType
        """

        return self.com_object.ThermalResponseType

    @thermal_response_type.setter
    def thermal_response_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ThermalResponseType = value

    @property
    def time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeIncrement() As double
                |     Returns or sets the time increment of the Coupled Thermal Electro-Chemical
                |     Stress step. Only applicable when the incrementation scheme is Fixed.

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
                |     Returns or sets the time incrementation scheme. 

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
        return f'SimCoupledThermalElectroChemicalStressStep(name="{ self.name }")'
