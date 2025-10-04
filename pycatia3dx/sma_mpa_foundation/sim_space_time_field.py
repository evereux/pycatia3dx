"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_port_region import SimPortRegion
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_foundation.sim_analysis_case import SimAnalysisCase
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep


class SimSpaceTimeField(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSpaceTimeField
                | 
                | Represents the Space Time Field object.
                | 
                | See also:
                |     SimPortRegion
    
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
                |     Returns or sets the absolute exterior tolerance.
                |     The absolute exterior tolerance is used to classify if a consumer node is
                |     outside the region of the producer elements. When this value is zero, the
                |     relative exterior tolerance is used.

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
    def driving_elset(self) -> SimPortRegion:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrivingElset() As SimPortRegion
                |     Returns or sets the driving elset.

        :return: SimPortRegion
        """

        return SimPortRegion(self.com_object.DrivingElset)

    @driving_elset.setter
    def driving_elset(self, value: SimPortRegion):
        """
        :param SimPortRegion value:
        """

        self.com_object.DrivingElset = value

    @property
    def increment(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Increment() As long
                |     Returns or sets the increment.
                |     The producer step increment that is used for initial conditions.

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
    def interpolate_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterpolateFlag() As boolean
                |     Returns or sets the interpolate flag.
                |     The interpolate flag allows the producer and consumer meshes to be
                |     different. Many simulation features create internal nodes. These are not
                |     visible to the user and can make the producer simulation mesh differ from the
                |     consumer simulation mesh, even when the mesh parts are identical. This option
                |     is not exposed in the user interface. The interpolate flag is mutually
                |     exclusive to the midside flag.
                |     TRUE: interpolation is used (meshes can differ).
                |     FALSE: interpolation is not used (meshes must be identical).

        :return: bool
        """

        return self.com_object.InterpolateFlag

    @interpolate_flag.setter
    def interpolate_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.InterpolateFlag = value

    @property
    def midside_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MidsideFlag() As boolean
                |     Returns or sets the midside flag.
                |     The midside flag specifies that second order elements should interpolate
                |     the field values of the midside nodes from the corner nodes. This option is not
                |     exposed in the user interface, and applies only to Abaqus/Standard. The midside
                |     flag is mutually exclusive to the interpolate flag.
                |     TRUE: interpolation of midside nodes from corner node field
                |     values.
                |     FALSE: mapping of midsides nodes from producer nodes

        :return: bool
        """

        return self.com_object.MidsideFlag

    @midside_flag.setter
    def midside_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MidsideFlag = value

    @property
    def relative_exterior_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RelativeExteriorTolerance() As double
                |     Returns or sets the relative exterior tolerance.
                |     The relative exterior tolerance is the fraction of the average consumer
                |     element size used to classify if a producer node is outside the region of the
                |     consumer elements.

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
    def scenario_analysis_case(self) -> SimAnalysisCase:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScenarioAnalysisCase() As SimAnalysisCase
                |     Returns or sets the scenario analysis case.
                |     The producer analysis case that is used for initial conditions.

        :return: SimAnalysisCase
        """

        return SimAnalysisCase(self.com_object.ScenarioAnalysisCase)

    @scenario_analysis_case.setter
    def scenario_analysis_case(self, value: SimAnalysisCase):
        """
        :param SimAnalysisCase value:
        """

        self.com_object.ScenarioAnalysisCase = value

    @property
    def scenario_step(self) -> SimStep:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScenarioStep() As SimStep
                |     Returns or sets the scenario step.
                |     The step of producer analysis case that is used for initial conditions.

        :return: SimStep
        """

        return SimStep(self.com_object.ScenarioStep)

    @scenario_step.setter
    def scenario_step(self, value: SimStep):
        """
        :param SimStep value:
        """

        self.com_object.ScenarioStep = value

    @property
    def use_driving_elset_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseDrivingElsetFlag() As boolean
                |     Returns or sets the use driving elset flag.
                |     TRUE: use driving elset.
                |     FALSE: do not use driving elset.

        :return: bool
        """

        return self.com_object.UseDrivingElsetFlag

    @use_driving_elset_flag.setter
    def use_driving_elset_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseDrivingElsetFlag = value

    def __repr__(self):
        return f'SimSpaceTimeField(name="{ self.name }")'
