"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_orientation import SimOrientation


class SimSphParticles(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSPHParticles
                | 
                | Represents the SPH particles object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a SimSPHParticles as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MySPHParticles As SimSPHParticles
                |      Set MySPHParticles = MyProperties.Add("SimSPHParticles")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a SimSPHParticles named "SPH
                |     particles.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MySPHParticles As SimSPHParticles
                |      Set MySPHParticles = MyProperties.Item("SPH particles.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a SimSPHParticles
                |     as following:
                | 
                |      ...
                |      MySPHParticles = myProperties.Add("SimSPHParticles")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimSPHParticles named "SPH particles.1" as following:
                | 
                |      ...
                |      MySPHParticles = myProperties.Item("SPH particles.1")
                |      
                | 
                | See also:
                |     SimProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the Axis System used for the section.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def conversion_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConversionType() As SimConversionType
                |     Returns or Sets the Conversion Type used for the Section.

        :return: int
        """

        return self.com_object.ConversionType

    @conversion_type.setter
    def conversion_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ConversionType = value

    @property
    def function_order(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FunctionOrder() As SimFunctionOrder
                |     Returns or sets the Threshold. Quantity: LENGTH, units: m

        :return: int
        """

        return self.com_object.FunctionOrder

    @function_order.setter
    def function_order(self, value: int):
        """
        :param int value:
        """

        self.com_object.FunctionOrder = value

    @property
    def grid_spacing(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GridSpacing() As double
                |     Returns or sets the Grid Spacing. Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.GridSpacing

    @grid_spacing.setter
    def grid_spacing(self, value: float):
        """
        :param float value:
        """

        self.com_object.GridSpacing = value

    @property
    def material_behavior(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialBehavior() As CATBaseDispatch
                |     Returns or sets the simulation material behavior.

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
    def orientation(self) -> SimOrientation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Orientation() As SimOrientation (Read Only)
                |     Returns the orientation used for the section.

        :return: SimOrientation
        """

        return SimOrientation(self.com_object.Orientation)

    @property
    def particles_per_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ParticlesPerDirection() As long
                |     Returns or sets the number of Particles Per Direction used for the section.
                |     This api works only if ConversionType is set to SimParticlesPerDirection

        :return: int
        """

        return self.com_object.ParticlesPerDirection

    @particles_per_direction.setter
    def particles_per_direction(self, value: int):
        """
        :param int value:
        """

        self.com_object.ParticlesPerDirection = value

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
    def thickness_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThicknessType() As SimThicknessType
                |     Returns or Sets the Thickness Type used for the Section.

        :return: int
        """

        return self.com_object.ThicknessType

    @thickness_type.setter
    def thickness_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ThicknessType = value

    @property
    def threshold(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Threshold() As double
                |     Returns or sets the Threshold. Quantity: LENGTH, units: m This api works
                |     only if ConversionType is set to SimParticlesPerDirection 

        :return: float
        """

        return self.com_object.Threshold

    @threshold.setter
    def threshold(self, value: float):
        """
        :param float value:
        """

        self.com_object.Threshold = value

    def __repr__(self):
        return f'SimSphParticles(name="{ self.name }")'
