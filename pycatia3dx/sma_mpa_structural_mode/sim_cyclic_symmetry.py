"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis import SimAxis
from pycatia3dx.system.any_object import AnyObject


class SimCyclicSymmetry(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCyclicSymmetry
                | 
                | Represents the Cyclic Symmetry object.
                | 
                | Example:
                |     Given a SimAbstractions object, you can create a SimCyclicSymmetry as
                |     following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyCyclicSymmetry As SimCyclicSymmetry
                |      Set MyCyclicSymmetry = MyAbstractions.Add("SimCyclicSymmetry")
                |      
                | 
                |     Given a SimAbstractions object, you can retrieve a SimCyclicSymmetry named
                |     "Cyclic Symmetry.1" as following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyCyclicSymmetry As SimCyclicSymmetry
                |      Set MyCyclicSymmetry = MyAbstractions.Item("Cyclic Symmetry.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAbstractions object myAbstractions, you can create a
                |     SimCyclicSymmetry as following:
                | 
                |      ...
                |      myCyclicSymmetry = myAbstractions.Add("SimCyclicSymmetry")
                |      
                | 
                |     Given a SimAbstractions object myAbstractions, you can retrieve a
                |     SimCyclicSymmetry named "Cyclic Symmetry.1" as following:
                | 
                |      ...
                |      myCyclicSymmetry = myAbstractions.Item("Cyclic Symmetry.1")
                |      
                | 
                | See also:
                |     SimAbstractions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def adjust_secondary_surface_initial_position_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdjustSecondarySurfaceInitialPositionFlag() As
                | boolean
                |     Retrieves a flag that determines whether the adjustment of the initial
                |     position of the secondary surface is enabled or not.
                |     TRUE: all tied nodes are moved in the initial
                |     configuration.
                | 
                |     FALSE: prevents all tied nodes on the secondary surface from moving onto
                |     the main surface.

        :return: bool
        """

        return self.com_object.AdjustSecondarySurfaceInitialPositionFlag

    @adjust_secondary_surface_initial_position_flag.setter
    def adjust_secondary_surface_initial_position_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AdjustSecondarySurfaceInitialPositionFlag = value

    @property
    def adjust_slave_surface_initial_position_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdjustSlaveSurfaceInitialPositionFlag() As boolean
                |     deprecated R425

        :return: bool
        """

        return self.com_object.AdjustSlaveSurfaceInitialPositionFlag

    @adjust_slave_surface_initial_position_flag.setter
    def adjust_slave_surface_initial_position_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AdjustSlaveSurfaceInitialPositionFlag = value

    @property
    def axis_of_symmetry(self) -> SimAxis:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisOfSymmetry() As SimAxis (Read Only)
                |     Returns the axis of symmetry. The graphical user interface editor for this
                |     feature only supports geometric axis types. See SimAxisAxisType for additional
                |     information.

        :return: SimAxis
        """

        return SimAxis(self.com_object.AxisOfSymmetry)

    @property
    def main_surface(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MainSurface() As CATBaseDispatch (Read Only)
                |     Returns the main surface.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MainSurface)

    @property
    def master_surface(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MasterSurface() As CATBaseDispatch (Read Only)
                |     deprecated R425.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MasterSurface)

    @property
    def number_of_sectors(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfSectors() As long
                |     Returns or sets the number of sectors.

        :return: int
        """

        return self.com_object.NumberOfSectors

    @number_of_sectors.setter
    def number_of_sectors(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfSectors = value

    @property
    def position_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionTolerance() As double
                |     Returns or sets the position tolerance, which is the distance within which
                |     slave nodes will be tied to the master surface. Quantity: LENGTH, units: mm

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
                |     Returns or Sets the flag that determines whether the position tolerance is
                |     used to tie nodes.
                |     TRUE: specifying position tolerance is allowed.
                | 
                |     FALSE: position tolerance will be calculated automatically based on the
                |     element formulations and types of surfaces used in the constraints.

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
    def secondary_surface(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondarySurface() As CATBaseDispatch (Read Only)
                |     Returns the secondary surface.

        :return: AnyObject
        """

        return AnyObject(self.com_object.SecondarySurface)

    @property
    def slave_surface(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SlaveSurface() As CATBaseDispatch (Read Only)
                |     deprecated R425

        :return: AnyObject
        """

        return AnyObject(self.com_object.SlaveSurface)

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

    def __repr__(self):
        return f'SimCyclicSymmetry(name="{ self.name }")'
