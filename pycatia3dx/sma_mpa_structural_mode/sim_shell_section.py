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


class SimShellSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimShellSection
                | 
                | Represents the Shell Section object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a SimShellSection as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyShellSection As SimShellSection
                |      Set MyShellSection = MyProperties.Add("SimShellSection")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a SimShellSection named
                |     "Shell Section.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyShellSection As SimShellSection
                |      Set MyShellSection = MyProperties.Item("Shell Section.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a SimShellSection
                |     as following:
                | 
                |      ...
                |      myShellSection = myProperties.Add("SimShellSection")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimShellSection named "Shell Section.1" as following:
                | 
                |      ...
                |      myShellSection = myProperties.Item("Shell Section.1")
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
    def field_point_specified(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FieldPointSpecified() As boolean
                |     Returns or sets the FieldPointSpecified flag .
                |     TRUE: the FieldPointSpecified flag is set .
                | 
                |     FALSE: the FieldPointSpecified flag is not set .

        :return: bool
        """

        return self.com_object.FieldPointSpecified

    @field_point_specified.setter
    def field_point_specified(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FieldPointSpecified = value

    @property
    def field_points(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FieldPoints() As long
                |     Returns or sets the number of integration points used for the section.

        :return: int
        """

        return self.com_object.FieldPoints

    @field_points.setter
    def field_points(self, value: int):
        """
        :param int value:
        """

        self.com_object.FieldPoints = value

    @property
    def infinite_max_thickness_interval_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InfiniteMaxThicknessIntervalFlag() As boolean
                |     deprecated R426. Please use IntervalFlag PROPERTY

        :return: bool
        """

        return self.com_object.InfiniteMaxThicknessIntervalFlag

    @infinite_max_thickness_interval_flag.setter
    def infinite_max_thickness_interval_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.InfiniteMaxThicknessIntervalFlag = value

    @property
    def integration_scheme(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntegrationScheme() As
                | SimShellSectionIntegrationScheme
                |     Returns or sets the integration method used for the section.

        :return: int
        """

        return self.com_object.IntegrationScheme

    @integration_scheme.setter
    def integration_scheme(self, value: int):
        """
        :param int value:
        """

        self.com_object.IntegrationScheme = value

    @property
    def interval(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Interval() As double
                |     Returns or sets the interval value. Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.Interval

    @interval.setter
    def interval(self, value: float):
        """
        :param float value:
        """

        self.com_object.Interval = value

    @property
    def interval_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntervalFlag() As boolean (Read Only)
                |     Returns the flag that determines if the thickness interval range value is
                |     taken as "Unlimited" or as specified by the user.
                |     TRUE: the thickness interval range value is considered as unlimited and
                |     user must not specify any value.
                | 
                |     FALSE: the thickness interval range value is to be specified by
                |     user.

        :return: bool
        """

        return self.com_object.IntervalFlag

    @property
    def map_thickness_to_nodes_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MapThicknessToNodesFlag() As boolean
                |     Returns or sets the MapThicknessToNodes flag .
                |     TRUE: the MapThicknessToNodes flag is set .
                | 
                |     FALSE: the MapThicknessToNodes flag is not set .

        :return: bool
        """

        return self.com_object.MapThicknessToNodesFlag

    @map_thickness_to_nodes_flag.setter
    def map_thickness_to_nodes_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MapThicknessToNodesFlag = value

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
    def offset_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OffsetMethod() As SimShellSectionOffsetMethod
                |     Returns or sets the offset method used for the section.

        :return: int
        """

        return self.com_object.OffsetMethod

    @offset_method.setter
    def offset_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.OffsetMethod = value

    @property
    def offset_ratio(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OffsetRatio() As double
                |     Returns or sets the offset ratio used for section. Quantity: Real, units:
                |     None

        :return: float
        """

        return self.com_object.OffsetRatio

    @offset_ratio.setter
    def offset_ratio(self, value: float):
        """
        :param float value:
        """

        self.com_object.OffsetRatio = value

    @property
    def offset_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OffsetValue() As double
                |     Returns or sets the offset value used for the section. Quantity: LENGTH,
                |     units: m

        :return: float
        """

        return self.com_object.OffsetValue

    @offset_value.setter
    def offset_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.OffsetValue = value

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
    def poisson_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PoissonMethod() As SimShellSectionPoissonMethod
                |     Poisson method used for the section.

        :return: int
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
                |     Returns or sets the flag that determines if the shell is integrated before
                |     analysis.
                | 
                |     TRUE: the shell is integrated before analysis.
                | 
                |     FALSE: the shell is integrated during the solution.

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
    def round_off_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RoundOffFlag() As boolean
                |     Returns or sets the round off flag that rounds off the thickness or offset
                |     values upto 4 decimal places.
                |     TRUE: the thickness interval range value is rounded off.
                | 
                |     FALSE: the thickness interval range value is not rounded
                |     off.

        :return: bool
        """

        return self.com_object.RoundOffFlag

    @round_off_flag.setter
    def round_off_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RoundOffFlag = value

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
    def split_by_thickness_offset_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SplitByThicknessOffsetFlag() As boolean
                |     Returns or sets the interval flag that determines whether the section is to
                |     be grouped according to thickness interval or not.
                |     TRUE: the section will be grouped in different sections.
                | 
                |     FALSE: the section will not be grouped in different
                |     sections.

        :return: bool
        """

        return self.com_object.SplitByThicknessOffsetFlag

    @split_by_thickness_offset_flag.setter
    def split_by_thickness_offset_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SplitByThicknessOffsetFlag = value

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
    def thickness_grouping_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThicknessGroupingFlag() As boolean
                |     deprecated R426. Please use SplitByThicknessOffsetFlag PROPERTY

        :return: bool
        """

        return self.com_object.ThicknessGroupingFlag

    @thickness_grouping_flag.setter
    def thickness_grouping_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ThicknessGroupingFlag = value

    @property
    def thickness_grouping_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThicknessGroupingValue() As double
                |     deprecated R426. Please use Interval PROPERTY

        :return: float
        """

        return self.com_object.ThicknessGroupingValue

    @thickness_grouping_value.setter
    def thickness_grouping_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.ThicknessGroupingValue = value

    @property
    def thickness_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThicknessType() As SimShellSectionThicknessType
                |     Returns or sets the thickness type.

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
    def transverse_shear_stiffness_option_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TransverseShearStiffnessOptionFlag() As boolean
                |     CATBoolean TRUE the transverse shear stiffness option is enabled FALSE the
                |     transverse shear stiffness option is disabled

        :return: bool
        """

        return self.com_object.TransverseShearStiffnessOptionFlag

    @transverse_shear_stiffness_option_flag.setter
    def transverse_shear_stiffness_option_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TransverseShearStiffnessOptionFlag = value

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
                |     Returns or sets the flag that determines if the shell thickness is
                |     uniform.
                | 
                |     TRUE: the shell thickness is uniform.
                | 
                |     FALSE: the shell thickness is not uniform.

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

    def get_material_behavior(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialBehavior() As CATBaseDispatch
                | 
                |     Deprecated:
                |         R418 Retrieves the material behavior. 
                |     Returns:
                |         The material behavior. 
                |     Returns:
                |         S_OK if successful.

        :return: AnyObject
        """
        return self.com_object.GetMaterialBehavior()

    def get_transverse_shear_stiffness_values(self, o_k11_value: float, o_k22_value: float, o_k12_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTransverseShearStiffnessValues(double oK11Value,double oK22Value,double
                | oK12Value)
                |     Retrieves the shell section's transverse shear stiffness
                |     values.
                | 
                |     Parameters:
                | 
                |         oK11Value
                |             [out] Shear stiffness K11. Quantity: FORCE, Units: N
                |             
                |         oK22Value
                |             [out] Shear stiffness K22. Quantity: FORCE, Units: N
                |             
                |         oK12Value
                |             [out] Shear stiffness K12. Quantity: FORCE, Units: N

        :param float o_k11_value:
        :param float o_k22_value:
        :param float o_k12_value:
        :return: None
        """
        return self.com_object.GetTransverseShearStiffnessValues(o_k11_value, o_k22_value, o_k12_value)

    def set_material_behavior(self, i_behavior_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaterialBehavior(CATBSTR iBehaviorName)
                | 
                |     Deprecated:
                |         R418 Sets the material behavior. 
                |     Parameters:
                | 
                |         iBehaviorName
                |             [in] Alias (name) of the simulation material behavior. Default
                |             behavior is set if the specified behavior is not found. If multiple behaviors
                |             have the same alias, the first one found is selected.
                |             
                | 
                |     Returns:
                |         S_OK if successful.

        :param str i_behavior_name:
        :return: None
        """
        return self.com_object.SetMaterialBehavior(i_behavior_name)

    def set_transverse_shear_stiffness_values(self, i_k11_value: float, i_k22_value: float, i_k12_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTransverseShearStiffnessValues(double iK11Value,double iK22Value,double
                | iK12Value)
                |     Sets the shell section's transverse shear stiffness
                |     values.
                | 
                |     Parameters:
                | 
                |         iK11Value
                |             [in] Shear stiffness K11. Quantity: FORCE, Units: N
                |             
                |         iK22Value
                |             [in] Shear stiffness K22. Quantity: FORCE, Units: N
                |             
                |         iK12Value
                |             [in] Shear stiffness K12. Quantity: FORCE, Units: N

        :param float i_k11_value:
        :param float i_k22_value:
        :param float i_k12_value:
        :return: None
        """
        return self.com_object.SetTransverseShearStiffnessValues(i_k11_value, i_k22_value, i_k12_value)

    def __repr__(self):
        return f'SimShellSection(name="{ self.name }")'
