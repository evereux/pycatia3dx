"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_math_vector import SimMathVector
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_beam_profile import SimBeamProfile


class SimBeamSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimBeamSection
                | 
                | Represents the Beam Section object.
                | 
                | Example:
                |     Given a SimProperties object, you can create a SimBeamSection as
                |     following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyBeamSection As SimBeamSection
                |      Set MyBeamSection = MyProperties.Add("SimBeamSection")
                |      
                | 
                |     Given a SimProperties object, you can retrieve a SimBeamSection named "Beam
                |     Section.1" as following:
                | 
                |      Dim MyProperties As SimProperties
                |      ...
                |      Dim MyBeamSection As SimBeamSection
                |      Set MyBeamSection = MyProperties.Item("Beam Section.1")
                |      
                | 
                | Example in Python:
                |     Given a SimProperties object myProperties, you can create a SimBeamSection
                |     as following:
                | 
                |      ...
                |      myBeamSection = myProperties.Add("SimBeamSection")
                |      
                | 
                |     Given a SimProperties object myProperties, you can retrieve a
                |     SimBeamSection named "Beam Section.1" as following:
                | 
                |      ...
                |      myBeamSection = myProperties.Item("Beam Section.1")
                |      
                | 
                | See also:
                |     SimProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def beam_tangent_direction(self) -> SimMathVector:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BeamTangentDirection() As SimMathVector (Read Only)
                |     Returns the tangent direction vector of beam profile orientation used for
                |     the section.

        :return: SimMathVector
        """

        return SimMathVector(self.com_object.BeamTangentDirection)

    @property
    def lumped_mass_matrix_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LumpedMassMatrixFlag() As boolean
                |     Returns or sets the flag that determines if the Beam should use lumped mass
                |     matrix.
                | 
                |     TRUE: the Beam should use lumped mass matrix.
                | 
                |     FALSE: the Beam should use mass matrix based on cubic interpolation of
                |     deflection and quadratic interpolation of the rotation fields.

        :return: bool
        """

        return self.com_object.LumpedMassMatrixFlag

    @lumped_mass_matrix_flag.setter
    def lumped_mass_matrix_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.LumpedMassMatrixFlag = value

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
    def orientation_direction(self) -> SimMathVector:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientationDirection() As SimMathVector
                |     Returns or sets the beam profile orientation direction.

        :return: SimMathVector
        """

        return SimMathVector(self.com_object.OrientationDirection)

    @orientation_direction.setter
    def orientation_direction(self, value: SimMathVector):
        """
        :param SimMathVector value:
        """

        self.com_object.OrientationDirection = value

    @property
    def orientation_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientationMethod() As SimBeamSectionOrientation
                |     Returns or sets the method used to orient beam profile.

        :return: SimBeamSectionOrientation
        """

        return self.com_object.OrientationMethod

    @orientation_method.setter
    def orientation_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.OrientationMethod = value

    @property
    def orientation_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientationSupport() As CATBaseDispatch (Read Only)
                |     Returns the beam profile orientation support.

        :return: AnyObject
        """

        return AnyObject(self.com_object.OrientationSupport)

    @property
    def oriented_axis(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientedAxis() As SimBeamSectionCrossSectionAxis
                |     Returns or sets the beam section axis used for orientation.

        :return: SimBeamSectionCrossSectionAxis
        """

        return int(self.com_object.OrientedAxis)

    @oriented_axis.setter
    def oriented_axis(self, value: int):
        """
        :param int value:
        """

        self.com_object.OrientedAxis = value

    @property
    def poisson_ratio_for_cs_area_change(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PoissonRatioForCSAreaChange() As double
                |     Poisson's ratio value. Quantity: Real, units: None

        :return: float
        """

        return self.com_object.PoissonRatioForCSAreaChange

    @poisson_ratio_for_cs_area_change.setter
    def poisson_ratio_for_cs_area_change(self, value: float):
        """
        :param float value:
        """

        self.com_object.PoissonRatioForCSAreaChange = value

    @property
    def pre_integration_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PreIntegrationFlag() As boolean
                |     Returns or sets the flag that determines if the integration should be
                |     performed before analysis.
                | 
                |     TRUE: the integration should be performed before analysis.
                | 
                |     FALSE: the integration should be performed during the solution.

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
    def profile(self) -> SimBeamProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Profile() As SimBeamProfile
                |     Returns or sets the beam profile.

        :return: SimBeamProfile
        """

        return SimBeamProfile(self.com_object.Profile)

    @profile.setter
    def profile(self, value: SimBeamProfile):
        """
        :param SimBeamProfile value:
        """

        self.com_object.Profile = value

    @property
    def slenderness_option(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SlendernessOption() As
                | SimBeamSectionSlendernessOption
                |     Returns or sets the option used to define slenderness.

        :return: int
        """

        return self.com_object.SlendernessOption

    @slenderness_option.setter
    def slenderness_option(self, value: int):
        """
        :param int value:
        """

        self.com_object.SlendernessOption = value

    @property
    def slenderness_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SlendernessValue() As double
                |     Returns or sets the value of the slenderness compensation. Quantity: Real,
                |     units: None

        :return: float
        """

        return self.com_object.SlendernessValue

    @slenderness_value.setter
    def slenderness_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.SlendernessValue = value

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
    def transverse_shear_stiffness_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TransverseShearStiffnessMethod() As
                | SimBeamSectionTransverseShearStiffness
                |     Returns or sets the method used to define transverse shear stiffness.

        :return: int
        """

        return self.com_object.TransverseShearStiffnessMethod

    @transverse_shear_stiffness_method.setter
    def transverse_shear_stiffness_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.TransverseShearStiffnessMethod = value

    @property
    def transverse_shear_stiffness_values(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TransverseShearStiffnessValues() As
                | CATSafeArrayVariant
                |     Returns or sets the list of transverse shear stiffness values. Quantity:
                |     FORCE, Units: N For the various options used to define shear stiffness, The
                |     number of values and sequence of values will be as
                |     following:
                | 
                |         TransverseShearStiffness = Isotropic : {Transverse shear stiffness}
                |         TransverseShearStiffness = Orthotropic : {Transverse shear stiffness K13, Transverse stiffness K23}

        :return: tuple
        """

        return self.com_object.TransverseShearStiffnessValues

    @transverse_shear_stiffness_values.setter
    def transverse_shear_stiffness_values(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.TransverseShearStiffnessValues = value

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

    def get_offset_values(self, o_offset_x_value: float, o_offset_y_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOffsetValues(double oOffsetXValue,double oOffsetYValue)
                |     Retrieves the values of the beam profile offset. Offset will be considered
                |     with general beam profile.
                | 
                |     Parameters:
                | 
                |         oOffsetXValue
                |             [out] The offset in local x-direction of beam profile which is used
                |             for the beam section. Quantity: LENGTH, units: m 
                |         oOffsetYValue
                |             [out] The offset in local y-direction of beam profile which is used
                |             for the beam section. Quantity: LENGTH, units: m

        :param float o_offset_x_value:
        :param float o_offset_y_value:
        :return: None
        """
        return self.com_object.GetOffsetValues(o_offset_x_value, o_offset_y_value)

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

    def set_offset_values(self, i_offset_x_value: float, i_offset_y_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOffsetValues(double iOffsetXValue,double iOffsetYValue)
                |     Sets the values of the beam profile offset. Offset will be considered with
                |     general beam profile.
                | 
                |     Parameters:
                | 
                |         iOffsetXValue
                |             [in] The offset in local x-direction of beam profile which should
                |             be used for the beam section. Quantity: LENGTH, units: m
                |             
                |         iOffsetYValue
                |             [in] The offset in local y-direction of beam profile which should
                |             be used for the beam section. Quantity: LENGTH, units: m

        :param float i_offset_x_value:
        :param float i_offset_y_value:
        :return: None
        """
        return self.com_object.SetOffsetValues(i_offset_x_value, i_offset_y_value)

    def __repr__(self):
        return f'SimBeamSection(name="{ self.name }")'
