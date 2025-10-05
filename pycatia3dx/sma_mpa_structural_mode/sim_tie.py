"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimTie(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimTie
                | 
                | Represents the Tie object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimTie as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyTie As SimTie
                |      Set MyTie = MyMCXProperties.Add("SimTie")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimTie named "Tie.1" as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyTie As SimTie
                |      Set MyTie = MyMCXProperties.Item("Tie.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a SimTie as
                |     following:
                | 
                |      ...
                |      myTie = myMCXProperties.Add("SimTie")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a SimTie
                |     named "Tie.1" as following:
                | 
                |      ...
                |      myTie = myMCXProperties.Item("Tie.1")
                |      
                | 
                | See also:
                |     SimMCXProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def adjust_secondary_surface_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdjustSecondarySurfaceFlag() As boolean
                |     Returns or sets the flag that determines if the secondary surface inital
                |     position adjustment is applied.
                | 
                |     TRUE: the secondary surface inital position adjustment is
                |     applied.
                | 
                |     FALSE: the secondary surface inital position adjustment is not applied.

        :return: bool
        """

        return self.com_object.AdjustSecondarySurfaceFlag

    @adjust_secondary_surface_flag.setter
    def adjust_secondary_surface_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AdjustSecondarySurfaceFlag = value

    @property
    def adjust_slave_surface_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdjustSlaveSurfaceFlag() As boolean
                |     deprecated R425

        :return: bool
        """

        return self.com_object.AdjustSlaveSurfaceFlag

    @adjust_slave_surface_flag.setter
    def adjust_slave_surface_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AdjustSlaveSurfaceFlag = value

    @property
    def constraint_ratio(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConstraintRatio() As double
                |     Returns or sets the constraint ratio. Quantity: Real, units: None.

        :return: float
        """

        return self.com_object.ConstraintRatio

    @constraint_ratio.setter
    def constraint_ratio(self, value: float):
        """
        :param float value:
        """

        self.com_object.ConstraintRatio = value

    @property
    def constraint_ratio_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConstraintRatioFlag() As boolean
                | 
                |     TRUE: constraint ratio is applied.
                | 
                |     FALSE: constraint ratio is not applied.

        :return: bool
        """

        return self.com_object.ConstraintRatioFlag

    @constraint_ratio_flag.setter
    def constraint_ratio_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ConstraintRatioFlag = value

    @property
    def discretization_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DiscretizationMethod() As SimTieDiscretizationMethod
                |     Returns or sets the discretization method.

        :return: int
        """

        return self.com_object.DiscretizationMethod

    @discretization_method.setter
    def discretization_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.DiscretizationMethod = value

    @property
    def fluid_potential_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FluidPotentialFlag() As boolean
                |     Returns or sets the flag that determines if the fluid electric potential
                |     DOF is applied.
                | 
                |     TRUE: the fluid electric potential DOF is applied.
                | 
                |     FALSE: the fluid electric potential DOF is not applied.

        :return: bool
        """

        return self.com_object.FluidPotentialFlag

    @fluid_potential_flag.setter
    def fluid_potential_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FluidPotentialFlag = value

    @property
    def ion_concentration_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IonConcentrationFlag() As boolean
                |     Returns or sets the flag that determines if the ion concentration DOF is
                |     applied.
                | 
                |     TRUE: the ion concentration DOF is applied.
                | 
                |     FALSE: the ion concentration DOF is not applied.

        :return: bool
        """

        return self.com_object.IonConcentrationFlag

    @ion_concentration_flag.setter
    def ion_concentration_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IonConcentrationFlag = value

    @property
    def pore_pressure_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PorePressureFlag() As boolean
                |     Returns or sets the flag that determines if the pore pressure DOF is
                |     applied.
                | 
                |     TRUE: the pore pressure DOF is applied.
                | 
                |     FALSE: the pore pressure DOF is not applied.

        :return: bool
        """

        return self.com_object.PorePressureFlag

    @pore_pressure_flag.setter
    def pore_pressure_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PorePressureFlag = value

    @property
    def position_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionTolerance() As double
                |     Returns or sets the position tolerance. Quantity: LENGTH, units: m.

        :return: float
        """

        return self.com_object.PositionTolerance

    @position_tolerance.setter
    def position_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.PositionTolerance = value

    @property
    def position_tolerance_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionToleranceFlag() As boolean
                |     Returns or sets the flag that determines if the position tolerance is
                |     applied.
                | 
                |     TRUE: the position tolerance is applied.
                | 
                |     FALSE: the position tolertance is not applied.

        :return: bool
        """

        return self.com_object.PositionToleranceFlag

    @position_tolerance_flag.setter
    def position_tolerance_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PositionToleranceFlag = value

    @property
    def shell_thickness_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShellThicknessFlag() As boolean
                |     Returns or sets the flag that determines if the shell thickness is
                |     used.
                | 
                |     TRUE: the shell thickness is used.
                | 
                |     FALSE: the shell thickness is not used.

        :return: bool
        """

        return self.com_object.ShellThicknessFlag

    @shell_thickness_flag.setter
    def shell_thickness_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ShellThicknessFlag = value

    @property
    def solid_potential_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SolidPotentialFlag() As boolean
                |     Returns or sets the flag that determines if the solid electric potential
                |     DOF is applied.
                | 
                |     TRUE: the solid electric potential DOF is applied.
                | 
                |     FALSE: the solid electric potential DOF is not applied.

        :return: bool
        """

        return self.com_object.SolidPotentialFlag

    @solid_potential_flag.setter
    def solid_potential_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SolidPotentialFlag = value

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. Possible values are:
                | 
                |         Abstractions
                |         Amplitudes
                |         Controls
                |         Connections
                |         Damping
                |         ElementTypeAssignments
                |         Envelopes
                |         FieldPlots
                |         FlowConditions
                |         HistoryPlots
                |         InitialConditions
                |         Interactions
                |         LinearLoadCases
                |         Loads
                |         LoadSets
                |         OutputRequests
                |         PredefinedFields
                |         Properties
                |         Restraints
                |         Sensors
                |         Streams
                |         ThermalConditions
                |         NotDefined

        :return: str
        """

        return self.com_object.SpecTreeCategory

    @property
    def swap_main_secondary(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SwapMainSecondary() As boolean
                |     Returns or sets the flag that determines if the main and secondary surfaces
                |     are swapped.
                | 
                |     TRUE: the main and secondary surfaces are swapped.
                | 
                |     FALSE: the main and secondary surfaces are not swapped.

        :return: bool
        """

        return self.com_object.SwapMainSecondary

    @swap_main_secondary.setter
    def swap_main_secondary(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SwapMainSecondary = value

    @property
    def swap_master_slave(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SwapMasterSlave() As boolean
                |     deprecated R425

        :return: bool
        """

        return self.com_object.SwapMasterSlave

    @swap_master_slave.setter
    def swap_master_slave(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SwapMasterSlave = value

    @property
    def temperature_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TemperatureFlag() As boolean
                |     Returns or sets the flag that determines if the temperature DOF is
                |     applied.
                | 
                |     TRUE: the temperature DOF is applied.
                | 
                |     FALSE: the temperature DOF is not applied.

        :return: bool
        """

        return self.com_object.TemperatureFlag

    @temperature_flag.setter
    def temperature_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TemperatureFlag = value

    @property
    def tie_rotational_do_fs_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TieRotationalDOFsFlag() As boolean
                | 
                |     TRUE: tie rotational DOFs is applied.
                | 
                |     FALSE: tie rotational DOFs is not applied. 

        :return: bool
        """

        return self.com_object.TieRotationalDOFsFlag

    @tie_rotational_do_fs_flag.setter
    def tie_rotational_do_fs_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TieRotationalDOFsFlag = value

    def __repr__(self):
        return f'SimTie(name="{ self.name }")'
