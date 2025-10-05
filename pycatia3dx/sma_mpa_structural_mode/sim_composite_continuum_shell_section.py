"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimCompositeContinuumShellSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCompositeContinuumShellSection
                | 
                | Represents the Composite Continnum Shell Section object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a
                |     SimCompositeContinuumShellSection as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyCompositeContinuumShellSection As
                |      SimCompositeContinuumShellSection
                |      Set MyCompositeContinuumShellSection = MyProperties.Add("SimCompositeContinuumShellSection")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a
                |     SimCompositeContinuumShellSection named "Composite Continnum Shell Section.1"
                |     as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyCompositeContinuumShellSection As
                |      SimCompositeContinuumShellSection
                |      Set MyCompositeContinuumShellSection = MyProperties.Item("Composite Continnum Shell Section.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a
                |     SimCompositeContinuumShellSection as following:
                | 
                |      ...
                |      MyCompositeContinuumShellSection = myProperties.Add("SimCompositeContinuumShellSection")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimCompositeContinuumShellSection named "Composite Continnum Shell Section.1"
                |     as following:
                | 
                |      ...
                |      MyCompositeContinuumShellSection = myProperties.Item("Composite Continnum Shell Section.1")
                |      
                | 
                | See also:
                |     SimProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def composite_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CompositeSupport() As CATBaseDispatch (Read Only)
                |     Retrieves the composite support.
                | 
                |     Parameters:
                | 
                |         ospCompositeSupport
                |             [out] The composite support. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: AnyObject
        """

        return AnyObject(self.com_object.CompositeSupport)

    @property
    def core_sampling_depth(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CoreSamplingDepth() As double
                |     Returns or sets the core sampling depth. Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.CoreSamplingDepth

    @core_sampling_depth.setter
    def core_sampling_depth(self, value: float):
        """
        :param float value:
        """

        self.com_object.CoreSamplingDepth = value

    @property
    def core_sampling_depth_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CoreSamplingDepthFlag() As boolean
                |     Returns or sets the flag that determines if the core sampling depth is
                |     enabled.
                | 
                |     TRUE: the core sampling depth is enabled.
                | 
                |     FALSE: if the core sampling depth is not enabled.

        :return: bool
        """

        return self.com_object.CoreSamplingDepthFlag

    @core_sampling_depth_flag.setter
    def core_sampling_depth_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CoreSamplingDepthFlag = value

    @property
    def cut_pieces_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CutPiecesFlag() As boolean
                |     Returns or sets the flag that determines if the core sampling depth is
                |     enabled.
                | 
                |     TRUE: the core sampling depth is enabled.
                | 
                |     FALSE: if the core sampling depth is not enabled.

        :return: bool
        """

        return self.com_object.CutPiecesFlag

    @cut_pieces_flag.setter
    def cut_pieces_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CutPiecesFlag = value

    @property
    def fiber_orientations_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FiberOrientationsFlag() As boolean
                |     Returns the flag that determines if the fiber orientations computation is
                |     from manufacturing parameters.
                | 
                |     TRUE: the fiber orientations are computed using the manufacturing core
                |     sampling algorithm.
                | 
                |     FALSE: if the orientations are computed using a geometrical core sampling
                |     algorithm.

        :return: bool
        """

        return self.com_object.FiberOrientationsFlag

    @fiber_orientations_flag.setter
    def fiber_orientations_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FiberOrientationsFlag = value

    @property
    def integration_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntegrationScheme() As
                | SimShellSectionIntegrationScheme
                |     Returns or sets the integration method used for the section.

        :return: SimShellSectionIntegrationScheme
        """

        return self.com_object.IntegrationScheme

    @integration_scheme.setter
    def integration_scheme(self, value: int):
        """
        :param int value:
        """

        self.com_object.IntegrationScheme = value

    @property
    def layer_material_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LayerMaterialSupport() As CATBaseDispatch (Read Only)
                |     Returns the support of the layer material through which the simulation
                |     material behavior for each unique material can be
                |     specified.
                | 
                |     Parameters:
                | 
                |         oLayerMaterialSupport[out]
                |             The layer material support. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: AnyObject
        """

        return AnyObject(self.com_object.LayerMaterialSupport)

    @property
    def nonstructural_ply_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NonstructuralPlyAngle() As double
                |     Returns or sets the ply angle to be defined to the dummy plies.

        :return: float
        """

        return self.com_object.NonstructuralPlyAngle

    @nonstructural_ply_angle.setter
    def nonstructural_ply_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.NonstructuralPlyAngle = value

    @property
    def nonstructural_ply_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NonstructuralPlyFlag() As boolean
                |     Returns or sets the non structural plies flag.
                | 
                |     TRUE: the non structural plies are to be included.
                | 
                |     FALSE: if non structural plies arenot be included.

        :return: bool
        """

        return self.com_object.NonstructuralPlyFlag

    @nonstructural_ply_flag.setter
    def nonstructural_ply_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NonstructuralPlyFlag = value

    @property
    def nonstructural_ply_material(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NonstructuralPlyMaterial() As CATBaseDispatch
                |     Returns or sets the material to be applied to the dummy plies.

        :return: AnyObject
        """

        return AnyObject(self.com_object.NonstructuralPlyMaterial)

    @nonstructural_ply_material.setter
    def nonstructural_ply_material(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.NonstructuralPlyMaterial = value

    @property
    def nonstructural_ply_position(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NonstructuralPlyPosition() As
                | SimNonStructPlyPositionScheme
                |     Returns or sets the position at which the dummy plies is to be created.

        :return: int
        """

        return self.com_object.NonstructuralPlyPosition

    @nonstructural_ply_position.setter
    def nonstructural_ply_position(self, value: int):
        """
        :param int value:
        """

        self.com_object.NonstructuralPlyPosition = value

    @property
    def num_int_points(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumIntPoints() As long
                |     Returns or sets the number of integration points used for the section.

        :return: int
        """

        return self.com_object.NumIntPoints

    @num_int_points.setter
    def num_int_points(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumIntPoints = value

    @property
    def num_int_points_per_layer_material(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumIntPointsPerLayerMaterial() As CATSafeArrayVariant
                |     Returns or sets the number of integration points used for each unique
                |     material used by the composite ply layers.

        :return: tuple
        """

        return self.com_object.NumIntPointsPerLayerMaterial

    @num_int_points_per_layer_material.setter
    def num_int_points_per_layer_material(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.NumIntPointsPerLayerMaterial = value

    @property
    def poisson_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PoissonMethod() As SimShellSectionPoissonMethod
                |     Returns or sets the Poisson method used for the section.

        :return: SimShellSectionPoissonMethod
        """

        return self.com_object.PoissonMethod

    @poisson_method.setter
    def poisson_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.PoissonMethod = value

    @property
    def poisson_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PoissonValue() As double
                |     Poisson's ratio value. Quantity: Real, units: None

        :return: float
        """

        return self.com_object.PoissonValue

    @poisson_value.setter
    def poisson_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.PoissonValue = value

    @property
    def pre_integration_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PreIntegrationFlag() As boolean
                |     Returns or sets the flag that determines if the Composite Continnum Shell
                |     section is pre-integrated.
                | 
                |     TRUE: the Composite Continnum Shell section is
                |     pre-integrated.
                | 
                |     FALSE: the Composite Continnum Shell section is not pre-integrated.

        :return: bool
        """

        return self.com_object.PreIntegrationFlag

    @pre_integration_flag.setter
    def pre_integration_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PreIntegrationFlag = value

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
        return f'SimCompositeContinuumShellSection(name="{ self.name }")'
