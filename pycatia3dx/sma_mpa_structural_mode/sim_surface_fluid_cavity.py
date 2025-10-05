"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_point import SimPoint
from pycatia3dx.system.any_object import AnyObject


class SimSurfaceFluidCavity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSurfaceFluidCavity
                | 
                | Represents the Surface Fluid Cavity object.
                | 
                | Example:
                |     Given a SimAbstractions object, you can create a SimSurfaceFluidCavity as
                |     following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MySurfaceFluidCavity As SimSurfaceFluidCavity
                |      Set MySurfaceFluidCavity = MyAbstractions.Add("SimSurfaceFluidCavity")
                |      
                | 
                |     Given a SimAbstractions object, you can retrieve a SimSurfaceFluidCavity
                |     named "Surface Fluid Cavity.1" as following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MySurfaceFluidCavity As SimSurfaceFluidCavity
                |      Set MySurfaceFluidCavity = MyAbstractions.Item("Surface Fluid Cavity.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAbstractions object myAbstractions, you can create a
                |     SimSurfaceFluidCavity as following:
                | 
                |      ...
                |      mySurfaceFluidCavity = myAbstractions.Add("SimSurfaceFluidCavity")
                |      
                | 
                |     Given a SimAbstractions object myAbstractions, you can retrieve a
                |     SimSurfaceFluidCavity named "Surface Fluid Cavity.1" as
                |     following:
                | 
                |      ...
                |      mySurfaceFluidCavity = myAbstractions.Item("Surface Fluid Cavity.1")
                |      
                | 
                | See also:
                |     SimAbstractions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def ambient_pressure(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AmbientPressure() As double
                |     Returns or sets the ambient pressure. Quantity: Pressure, units: N_m2.

        :return: float
        """

        return self.com_object.AmbientPressure

    @ambient_pressure.setter
    def ambient_pressure(self, value: float):
        """
        :param float value:
        """

        self.com_object.AmbientPressure = value

    @property
    def ambient_pressure_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AmbientPressureFlag() As boolean
                |     TRUE if the ambient pressure is specified and FALSE if it is not.

        :return: bool
        """

        return self.com_object.AmbientPressureFlag

    @ambient_pressure_flag.setter
    def ambient_pressure_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AmbientPressureFlag = value

    @property
    def cavity_ref_point(self) -> SimPoint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CavityRefPoint() As SimPoint (Read Only)
                |     Returns the point object for the reference point.

        :return: SimPoint
        """

        return SimPoint(self.com_object.CavityRefPoint)

    @property
    def check_normals_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CheckNormalsFlag() As boolean
                |     TRUE if the checking surface normals and FALSE if not.

        :return: bool
        """

        return self.com_object.CheckNormalsFlag

    @check_normals_flag.setter
    def check_normals_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CheckNormalsFlag = value

    @property
    def material_behavior(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialBehavior() As CATBaseDispatch
                |     Returns or sets the material behavior.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MaterialBehavior)

    @material_behavior.setter
    def material_behavior(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.MaterialBehavior = value

    @property
    def material_behavior_by_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialBehaviorByName() As CATBSTR
                |     Returns or sets the simulation material behavior by name.

        :return: str
        """

        return self.com_object.MaterialBehaviorByName

    @material_behavior_by_name.setter
    def material_behavior_by_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.MaterialBehaviorByName = value

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
        return f'SimSurfaceFluidCavity(name="{ self.name }")'
