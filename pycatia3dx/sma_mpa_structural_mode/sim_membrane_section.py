"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_scalar_field import SimScalarField
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_orientation import SimOrientation
from pycatia3dx.sma_mpa_structural_mode.sim_rebar_layers import SimRebarLayers


class SimMembraneSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMembraneSection
                | 
                | Represents the Membrane Section object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a SimMembraneSection as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyMembraneSection As SimMembraneSection
                |      Set MyMembraneSection = MyProperties.Add("SimMembraneSection")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a SimMembraneSection named
                |     "Membrane Section.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyMembraneSection As SimMembraneSection
                |      Set MyMembraneSection = MyProperties.Item("Membrane Section.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a
                |     SimMembraneSection as following:
                | 
                |      ...
                |      myMembraneSection = myProperties.Add("SimMembraneSection")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimMembraneSection named "Membrane Section.1" as
                |     following:
                | 
                |      ...
                |      myMembraneSection = myProperties.Item("Membrane Section.1")
                |      
                | 
                | See also:
                |     SimProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def all_rebar_layers(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllRebarLayers() As CATSafeArrayVariant (Read Only)
                |     Returns the Rebar Layers associated with the section.

        :return: tuple
        """

        return self.com_object.AllRebarLayers

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
    def poisson_value_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PoissonValueFlag() As boolean
                |     Returns or sets the flag that determines if the poisson value for membrane
                |     section is set.
                | 
                |     TRUE: the poisson value for membrane section is set.
                | 
                |     FALSE: the poisson value for membrane section is not set.

        :return: bool
        """

        return self.com_object.PoissonValueFlag

    @poisson_value_flag.setter
    def poisson_value_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PoissonValueFlag = value

    @property
    def rebar_layers_orientation(self) -> SimOrientation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RebarLayersOrientation() As SimOrientation (Read
                | Only)
                |     Returns the Orientation of the Rebar Layers associated with the section.

        :return: SimOrientation
        """

        return SimOrientation(self.com_object.RebarLayersOrientation)

    @property
    def rebars(self) -> SimRebarLayers:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Rebars() As SimRebarLayers (Read Only)
                |     Returns the Rebar Layers associated with the section.

        :return: SimRebarLayers
        """

        return SimRebarLayers(self.com_object.Rebars)

    @property
    def reduced_integration_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReducedIntegrationFlag() As boolean
                |     Returns or sets the flag that determines if the ReducedIntegrationFlag is
                |     set.
                | 
                |     TRUE: the ReducedIntegrationFlag is set.
                | 
                |     FALSE: the ReducedIntegrationFlag is not set.

        :return: bool
        """

        return self.com_object.ReducedIntegrationFlag

    @reduced_integration_flag.setter
    def reduced_integration_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ReducedIntegrationFlag = value

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
    def thickness_field(self) -> SimScalarField:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThicknessField() As SimScalarField (Read Only)
                |     Returns the thickness field.

        :return: SimScalarField
        """

        return SimScalarField(self.com_object.ThicknessField)

    @property
    def uniform_thickness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformThickness() As double
                |     Returns or sets the uniform thickness value used for the section. Quantity:
                |     LENGTH, units: m

        :return: float
        """

        return self.com_object.UniformThickness

    @uniform_thickness.setter
    def uniform_thickness(self, value: float):
        """
        :param float value:
        """

        self.com_object.UniformThickness = value

    @property
    def uniform_thickness_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformThicknessFlag() As boolean (Read Only)
                |     Returns or sets the flag that determines if the membrane thickness is
                |     uniform.
                | 
                |     TRUE: the membrane thickness is uniform.
                | 
                |     FALSE: the membrane thickness is not uniform.

        :return: bool
        """

        return self.com_object.UniformThicknessFlag

    def add_rebar_layer(self, i_type: str, o_feature: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddRebarLayer(CATBSTR iType,CATBaseDispatch oFeature)
                |     Adds a Rebar Layer to the section. 

        :param str i_type:
        :param AnyObject o_feature:
        :return: None
        """
        return self.com_object.AddRebarLayer(i_type, o_feature.com_object)

    def __repr__(self):
        return f'SimMembraneSection(name="{ self.name }")'
