"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.sma_spa_structural.sim_analysis_restart_step_property import SimAnalysisRestartStepProperty


class SimImplicitDynamicStep(SimStep):

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
                |                         SimImplicitDynamicStep
                | 
                | Represents the Implicit Dynamic Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimImplicitDynamicStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyImplicitDynamicStep As SimImplicitDynamicStep
                |      Set MyImplicitDynamicStep = MySteps.Add("SimImplicitDynamicStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimImplicitDynamicStep named
                |     "Implicit Dynamic Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyImplicitDynamicStep As SimImplicitDynamicStep
                |      Set MyImplicitDynamicStep = MySteps.Item("Implicit Dynamic Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimImplicitDynamicStep as
                |     following:
                | 
                |      ...
                |      myImplicitDynamicStep = mySteps.Add("SimImplicitDynamicStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimImplicitDynamicStep
                |     named "Implicit Dynamic Step.1" as following:
                | 
                |      ...
                |      myImplicitDynamicStep = mySteps.Item("Implicit Dynamic Step.1")
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
    def application_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ApplicationType() As SimApplicationType
                |     Returns or sets the application type for the Implicit Dynamic step.

        :return: SimApplicationType
        """

        return self.com_object.ApplicationType

    @application_type.setter
    def application_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ApplicationType = value

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
    def initial_time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialTimeIncrement() As double
                |     Returns or sets the initial time for the increments of the Implicit Dynamic
                |     step.

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
                |     Returns or sets the type of the matrix storage for the Implicit Dynamic
                |     step.

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
                |     Returns or sets the maximum number of increments for the Implicit Dynamic
                |     step.

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
                |     Returns or sets the maximum time for the increments of the Implicit Dynamic
                |     step.

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
                |     Returns or sets the minimum time for the increments of the Implicit Dynamic
                |     step.

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
    def restart_step_property(self) -> SimAnalysisRestartStepProperty:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RestartStepProperty() As SimAnalysisRestartStepProperty (Read
                | Only)
                |     Returns the restart step property for the Implicit Dynamic step.

        :return: SimAnalysisRestartStepProperty
        """

        return SimAnalysisRestartStepProperty(self.com_object.RestartStepProperty)

    @property
    def step_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StepTime() As double
                |     Returns or sets the retrieved total time for the Implicit dynamic step.

        :return: float
        """

        return self.com_object.StepTime

    @step_time.setter
    def step_time(self, value: float):
        """
        :param float value:
        """

        self.com_object.StepTime = value

    def __repr__(self):
        return f'SimImplicitDynamicStep(name="{ self.name }")'
