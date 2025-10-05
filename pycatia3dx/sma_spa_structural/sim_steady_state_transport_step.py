"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_spa_structural.sim_analysis_restart_step_property import SimAnalysisRestartStepProperty
from pycatia3dx.sma_spa_structural.sim_stabilization import SimStabilization


class SimSteadyStateTransportStep(SimStep):

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
                |                         SimSteadyStateTransportStep
                | 
                | Represents the Steady State Transport Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimSteadyStateTransportStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MySteadyStateTransportStep As
                |      SimSteadyStateTransportStep
                |      Set MySteadyStateTransportStep = MySteps.Add("SimSteadyStateTransportStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimSteadyStateTransportStep
                |     named "Steady State Transport Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MySteadyStateTransportStep As
                |      SimSteadyStateTransportStep
                |      Set MySteadyStateTransportStep = MySteps.Item("Steady State Transport Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a
                |     SimSteadyStateTransportStep as following:
                | 
                |      ...
                |      mySteadyStateTransportStep = mySteps.Add("SimSteadyStateTransportStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a
                |     SimSteadyStateTransportStep named "Steady State Transport Step.1" as
                |     following:
                | 
                |      ...
                |      mySteadyStateTransportStep = mySteps.Item("Steady State Transport Step.1")
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
    def eulerian_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EulerianSupport() As CATBaseDispatch (Read Only)
                |     Returns the Eulerian support on which spatial rigid body motion is applied.

        :return: AnyObject
        """

        return AnyObject(self.com_object.EulerianSupport)

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
    def inertia_effect(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InertiaEffect() As
                | SimSteadyStateTransportStepInertiaEffect
                |     Returns or sets the inertia effect.

        :return: SimSteadyStateTransportStepInertiaEffect
        """

        return self.com_object.InertiaEffect

    @inertia_effect.setter
    def inertia_effect(self, value: int):
        """
        :param int value:
        """

        self.com_object.InertiaEffect = value

    @property
    def inertia_stabilization_factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InertiaStabilizationFactor() As double
                |     Returns or sets the inertia stabilization factor. Quantity: DIMENSIONLESS,
                |     Units: None.

        :return: float
        """

        return self.com_object.InertiaStabilizationFactor

    @inertia_stabilization_factor.setter
    def inertia_stabilization_factor(self, value: float):
        """
        :param float value:
        """

        self.com_object.InertiaStabilizationFactor = value

    @property
    def initial_time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialTimeIncrement() As double
                |     Returns or sets the initial time for the increments of the Steady State
                |     Transport step.

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
                |     Returns or sets the type of the matrix storage for the Steady State
                |     Transport step.

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
    def maximum_increments(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumIncrements() As long
                |     Returns or sets the maximum number of increments for the Steady State
                |     Transport step.

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
    def maximum_time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumTimeIncrement() As double
                |     Returns or sets the maximum time for the increments of the Steady State
                |     Transport step.

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
                |     Returns or sets the minimum time for the increments of the Steady State
                |     Transport step.

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
    def mullins_effect(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MullinsEffect() As
                | SimSteadyStateTransportStepMullinsEffect
                |     Returns or sets the Mullins effect.

        :return: SimSteadyStateTransportStepMullinsEffect
        """

        return self.com_object.MullinsEffect

    @mullins_effect.setter
    def mullins_effect(self, value: int):
        """
        :param int value:
        """

        self.com_object.MullinsEffect = value

    @property
    def restart_step_property(self) -> SimAnalysisRestartStepProperty:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RestartStepProperty() As SimAnalysisRestartStepProperty (Read
                | Only)
                |     Returns the restart step property for the Steady State Transport step.

        :return: SimAnalysisRestartStepProperty
        """

        return SimAnalysisRestartStepProperty(self.com_object.RestartStepProperty)

    @property
    def stabilization(self) -> SimStabilization:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Stabilization() As SimStabilization (Read Only)
                |     Returns the stabilization for the Steady State Transport step.

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
                |     Returns or sets the total time for the Steady State Transport step.

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
    def time_incrementation_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeIncrementationScheme() As
                | SimTimeIncrementationScheme
                |     Returns or sets the time incrementation type for the Steady State Transport
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

    @property
    def use_instantaneous_elastic_response_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseInstantaneousElasticResponseFlag() As boolean
                |     Returns or sets the use instantaneous elastic response flag. Applicable
                |     only when either time-domain viscoelastic or two-layer viscoplastic behaviors
                |     are active.
                |     TRUE: use the instantaneous elastic response of the
                |     material.
                |     FALSE: use long term elastic response.

        :return: bool
        """

        return self.com_object.UseInstantaneousElasticResponseFlag

    @use_instantaneous_elastic_response_flag.setter
    def use_instantaneous_elastic_response_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseInstantaneousElasticResponseFlag = value

    @property
    def use_quasi_steady_state_procedure_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseQuasiSteadyStateProcedureFlag() As boolean
                |     Returns or sets the use quasi steady state procedure flag.
                |     TRUE: obtain steady-state solution.
                |     FALSE: obtain solution directly. 

        :return: bool
        """

        return self.com_object.UseQuasiSteadyStateProcedureFlag

    @use_quasi_steady_state_procedure_flag.setter
    def use_quasi_steady_state_procedure_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseQuasiSteadyStateProcedureFlag = value

    def __repr__(self):
        return f'SimSteadyStateTransportStep(name="{ self.name }")'
