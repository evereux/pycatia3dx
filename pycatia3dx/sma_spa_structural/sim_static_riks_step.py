"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.system.any_object import AnyObject


class SimStaticRiksStep(SimStep):

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
                |                         SimStaticRiksStep
                | 
                | Represents the Static Riks Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimStaticRiksStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyStaticRiksStep As SimStaticRiksStep
                |      Set MyStaticRiksStep = MySteps.Add("SimStaticRiksStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimStaticRiksStep named "Static
                |     Riks Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyStaticRiksStep As SimStaticRiksStep
                |      Set MyStaticRiksStep = MySteps.Item("Static Riks Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimStaticRiksStep as
                |     following:
                | 
                |      ...
                |      myStaticRiksStep = mySteps.Add("SimStaticRiksStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimStaticRiksStep named
                |     "Static Riks Step.1" as following:
                | 
                |      ...
                |      myStaticRiksStep = mySteps.Item("Static Riks Step.1")
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
    def geometric_non_linearity_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GeometricNonLinearityFlag() As boolean
                |     Returns or sets the flag that determines if the step is geometrically
                |     non-linear.
                | 
                |     TRUE: the step is geometrically non-linear.
                | 
                |     FALSE: the step is not geometrically non-linear.

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
    def initial_arc_length_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialArcLengthIncrement() As double
                |     Returns or sets the initial arc length increment for the Static Riks step.

        :return: float
        """

        return self.com_object.InitialArcLengthIncrement

    @initial_arc_length_increment.setter
    def initial_arc_length_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.InitialArcLengthIncrement = value

    @property
    def matrix_storage_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MatrixStorageScheme() As SimMatrixStorageScheme
                |     Returns or sets the type of the matrix storage for the Static Riks step.

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
    def maximum_arc_length_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumArcLengthIncrement() As double
                |     Returns or sets the maximum arc length increment for the Static Riks step.

        :return: float
        """

        return self.com_object.MaximumArcLengthIncrement

    @maximum_arc_length_increment.setter
    def maximum_arc_length_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumArcLengthIncrement = value

    @property
    def maximum_displacement_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumDisplacementType() As
                | SimStaticRiksStepDisplacementType
                |     Returns or sets the type of maximum displacement at the monitored node for
                |     the Static Riks step.

        :return: SimStaticRiksStepDisplacementType
        """

        return self.com_object.MaximumDisplacementType

    @maximum_displacement_type.setter
    def maximum_displacement_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.MaximumDisplacementType = value

    @property
    def maximum_increments(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumIncrements() As long
                |     Returns or sets the maximum number of increments for the Static Riks step.

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
    def maximum_load_proportionality_factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumLoadProportionalityFactor() As double
                |     Returns or sets the maximum load proportionality factor for the Static Riks
                |     step.

        :return: float
        """

        return self.com_object.MaximumLoadProportionalityFactor

    @maximum_load_proportionality_factor.setter
    def maximum_load_proportionality_factor(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumLoadProportionalityFactor = value

    @property
    def maximum_rotation(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumRotation() As double
                |     Returns or sets the maximum rotational displacement which, if crossed at
                |     the monitored node and DOF during an increment, ends the Static Riks step at
                |     the current increment.

        :return: float
        """

        return self.com_object.MaximumRotation

    @maximum_rotation.setter
    def maximum_rotation(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumRotation = value

    @property
    def maximum_translation(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumTranslation() As double
                |     Returns or sets the maximum translational displacement which, if crossed at
                |     the monitored node and DOF during an increment, ends the Static Riks step at
                |     the current increment.

        :return: float
        """

        return self.com_object.MaximumTranslation

    @maximum_translation.setter
    def maximum_translation(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumTranslation = value

    @property
    def minimum_arc_length_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumArcLengthIncrement() As double
                |     Returns or sets the minimum arc length increment for the Static Riks step.

        :return: float
        """

        return self.com_object.MinimumArcLengthIncrement

    @minimum_arc_length_increment.setter
    def minimum_arc_length_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.MinimumArcLengthIncrement = value

    @property
    def monitored_node_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MonitoredNodeSupport() As CATBaseDispatch (Read Only)
                |     Returns the support of the monitored node for the Static Riks step.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MonitoredNodeSupport)

    @property
    def monitored_rotational_dof(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MonitoredRotationalDOF() As SimDof
                |     Returns or sets the rotational degree of freedom of the node being
                |     monitored for the Static Riks step.

        :return: int
        """

        return self.com_object.MonitoredRotationalDOF

    @monitored_rotational_dof.setter
    def monitored_rotational_dof(self, value: int):
        """
        :param int value:
        """

        self.com_object.MonitoredRotationalDOF = value

    @property
    def monitored_translational_dof(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MonitoredTranslationalDOF() As SimDof
                |     Returns or sets the translational degree of freedom of the node being
                |     monitored for the Static Riks step.

        :return: int
        """

        return self.com_object.MonitoredTranslationalDOF

    @monitored_translational_dof.setter
    def monitored_translational_dof(self, value: int):
        """
        :param int value:
        """

        self.com_object.MonitoredTranslationalDOF = value

    @property
    def time_incrementation_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeIncrementationScheme() As
                | SimTimeIncrementationScheme
                |     Returns or sets the time incrementation type for the Static Riks step.

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
    def total_arc_length(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TotalArcLength() As double
                |     Returns or sets the total arc length scale factor associated with the
                |     Static Riks step. 

        :return: float
        """

        return self.com_object.TotalArcLength

    @total_arc_length.setter
    def total_arc_length(self, value: float):
        """
        :param float value:
        """

        self.com_object.TotalArcLength = value

    def __repr__(self):
        return f'SimStaticRiksStep(name="{ self.name }")'
