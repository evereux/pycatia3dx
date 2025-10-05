"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_scalar_field import SimScalarField
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.sma_mpa_foundation.sim_thermal_analysis_case import SimThermalAnalysisCase
from pycatia3dx.system.any_object import AnyObject


class SimInitialTemperature(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimInitialTemperature
                | 
                | Represents the Initial Temperature object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimInitialTemperature as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyInitialTemperature As SimInitialTemperature
                |      Set MyInitialTemperature = MyFeatures.Add("SimInitialTemperature")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimInitialTemperature named
                |     "Initial Temperature.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyInitialTemperature As SimInitialTemperature
                |      Set MyInitialTemperature = MyFeatures.Item("Initial Temperature.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimInitialTemperature as following:
                | 
                |      ...
                |      myInitialTemperature = myFeatures.Add("SimInitialTemperature")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimInitialTemperature named "Initial Temperature.1" as
                |     following:
                | 
                |      ...
                |      myInitialTemperature = myFeatures.Item("Initial Temperature.1")
                |      
                | 
                | See also:
                |     SimFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def absolute_exterior_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AbsoluteExteriorTolerance() As double
                |     Returns or sets the Absolute Exterior Tolerance. This is the value that
                |     nodes of the structural model can be outside the region of the elements of the
                |     thermal model. If this value is zero, the value for the relative exterior
                |     tolerance is used.

        :return: float
        """

        return self.com_object.AbsoluteExteriorTolerance

    @absolute_exterior_tolerance.setter
    def absolute_exterior_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.AbsoluteExteriorTolerance = value

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
    def analysis_case(self) -> SimThermalAnalysisCase:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnalysisCase() As SimThermalAnalysisCase
                |     Returns or sets the Thermal Analysis Case.

        :return: SimThermalAnalysisCase
        """

        return SimThermalAnalysisCase(self.com_object.AnalysisCase)

    @analysis_case.setter
    def analysis_case(self, value: SimThermalAnalysisCase):
        """
        :param SimThermalAnalysisCase value:
        """

        self.com_object.AnalysisCase = value

    @property
    def from_step_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FromStepFlag() As boolean
                |     Returns or sets the flag for an initial temperature from a
                |     SimThermalAnalysisCase and SimStep. This example demonstrates how to use the
                |     SimInitialTemperature object with a temperature field.
                | 
                |      Dim MyInitialTemperature As SimInitialTemperature
                |      Dim MyThermalAnalysisCase As SimThermalAnalysisCase
                |      Dim MySteadyStateHeatTransferStep As
                |      SimSteadyStateHeatTransferStep
                |      ...
                |      MyInitialTemperature.FromStepFlag = True
                |      MyInitialTemperature.AnalysisCase = MyThermalAnalysisCase
                |      MyInitialTemperature.Step = MySteadyStateHeatTransferStep
                |      MyInitialTemperature.Increment = 999999
                |      MyInitialTemperature.AbsoluteExteriorTolerance = 0.0
                |      MyInitialTemperature.RelativeExteriorTolerance = 0.1

        :return: bool
        """

        return self.com_object.FromStepFlag

    @from_step_flag.setter
    def from_step_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FromStepFlag = value

    @property
    def increment(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Increment() As long
                |     Returns or sets the Increment. Use 1 for the first increment. Use 999999
                |     for the last increment.

        :return: int
        """

        return self.com_object.Increment

    @increment.setter
    def increment(self, value: int):
        """
        :param int value:
        """

        self.com_object.Increment = value

    @property
    def relative_exterior_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RelativeExteriorTolerance() As double
                |     Returns or sets the Relative Exterior Tolerance. This is the fraction of
                |     the average element size that nodes of the structural model can be outside the
                |     region of the elements of the thermal model.

        :return: float
        """

        return self.com_object.RelativeExteriorTolerance

    @relative_exterior_tolerance.setter
    def relative_exterior_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.RelativeExteriorTolerance = value

    @property
    def scalar_field(self) -> SimScalarField:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScalarField() As SimScalarField (Read Only)
                |     Returns the scalar field.

        :return: SimScalarField
        """

        return SimScalarField(self.com_object.ScalarField)

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. See SimFeatures.GetSpecTreeCategory for usage.

        :return: str
        """

        return self.com_object.SpecTreeCategory

    @property
    def step(self) -> SimStep:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Step() As SimStep
                |     Returns or sets the Step.

        :return: SimStep
        """

        return SimStep(self.com_object.Step)

    @step.setter
    def step(self, value: SimStep):
        """
        :param SimStep value:
        """

        self.com_object.Step = value

    @property
    def uniform_magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformMagnitude() As double
                |     Temperature value. Quantity: TEMPRTRE, units: Kdeg

        :return: float
        """

        return self.com_object.UniformMagnitude

    @uniform_magnitude.setter
    def uniform_magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.UniformMagnitude = value

    @property
    def uniform_magnitude_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformMagnitudeFlag() As boolean (Read Only)
                |     Returns or sets the flag that determines if the magnitude is
                |     uniform.
                |     TRUE: the magnitude is uniform.
                |     FALSE: the magnitude is not uniform. 

        :return: bool
        """

        return self.com_object.UniformMagnitudeFlag

    def __repr__(self):
        return f'SimInitialTemperature(name="{ self.name }")'
