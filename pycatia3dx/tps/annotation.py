"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.associated_ref_frame import AssociatedRefFrame
from pycatia3dx.tps.composite_tolerance import CompositeTolerance
from pycatia3dx.tps.controlled_radius import ControlledRadius
from pycatia3dx.tps.datum_simple import DatumSimple
from pycatia3dx.tps.datum_target import DatumTarget
from pycatia3dx.tps.default_annotation import DefaultAnnotation
from pycatia3dx.tps.dimension_3d import Dimension3D
from pycatia3dx.tps.dimension_limit import DimensionLimit
from pycatia3dx.tps.dimension_pattern import DimensionPattern
from pycatia3dx.tps.envelop_condition import EnvelopCondition
from pycatia3dx.tps.flag_note import FlagNote
from pycatia3dx.tps.free_state import FreeState
from pycatia3dx.tps.material_condition import MaterialCondition
from pycatia3dx.tps.noa import Noa
from pycatia3dx.tps.numerical_display_format import NumericalDisplayFormat
from pycatia3dx.tps.particular_tol_elem import ParticularTolElem
from pycatia3dx.tps.projected_tolerance_zone import ProjectedToleranceZone
from pycatia3dx.tps.reference_frame import ReferenceFrame
from pycatia3dx.tps.roughness import Roughness
from pycatia3dx.tps.shifted_profile_tolerance import ShiftedProfileTolerance
from pycatia3dx.tps.tangent_plane import TangentPlane
from pycatia3dx.tps.text import Text
from pycatia3dx.tps.tolerance_per_unit_basis_restrictive_value import TolerancePerUnitBasisRestrictiveValue
from pycatia3dx.tps.tolerance_unit_basis_value import ToleranceUnitBasisValue
from pycatia3dx.tps.tolerance_zone import ToleranceZone
from pycatia3dx.tps.tps_view import TPSView


class Annotation(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Annotation
                | 
                | Interface for the Technological Product Specification (TPS)
                | objects.
                | Leaf entity in the Design Pattern Composite. TPS modeler enables definition of
                | specification related to surfaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def super_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SuperType() As CATBSTR (Read Only)
                |     Get the Super Type.
                | 
                |     Parameters:
                | 
                |         oSuperType
                |             The Super Type. The list of SuperType available: "FTA_NonSemantic"
                |             "FTA_Form" "FTA_Dimension" "FTA_Position" "FTA_Datum" "FTA_Orientation"
                |             "FTA_RunOut"

        :return: str
        """

        return self.com_object.SuperType

    @property
    def tps_status(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TPSStatus() As CATBSTR (Read Only)
                |     Get the TPS Status.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             The Status.

        :return: str
        """

        return self.com_object.TPSStatus

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     Get the Type.
                | 
                |     Parameters:
                | 
                |         oType
                |             The Type. List of types available ordered by SuperType: SuperType = "FTA_NonSemantic" Type = "FTA_Text" Type = "FTA_FlagNote" Type = "FTA_Roughness" Type = "FTA_Weld" Type = "FTA_Noa" Type = "FTA_NonSemanticDatum" Type = "FTA_NonSemanticTarget" Type = "FTA_NonSemanticGDT" Type = "FTA_NonSemanticDimension" SuperType = "FTA_Form" Type = "FTA_Flatness" Type = "FTA_Straightness" Type = "FTA_Circularity" Type = "FTA_Cylindricity" Type = "FTA_ProfileOfAnyLine" Type = "FTA_ProfileOfASurface" Type = "FTA_PatternTruePos" SuperType = "FTA_Dimension" Type = "FTA_LinearDimension" Type = "FTA_AngularDimension" Type = "FTA_SecondLinearDimension" Type = "FTA_ChamferDimension" Type = "FTA_BasicDimension" SuperType = "FTA_Position" Type = "FTA_TruePosition" Type = "FTA_Concentricity" Type = "FTA_Symmetry" Type = "FTA_PositionOfAnyLine" Type = "FTA_PositionOfASurface" SuperType = "FTA_Datum" Type = "FTA_DatumSimple" Type = "FTA_DatumTarget" Type = "FTA_DatumSystem" Type = "FTA_ReferenceFrame" SuperType = "FTA_Orientation" Type = "FTA_Parallelism" Type = "FTA_Perpendicularity" Type = "FTA_Angularity" SuperType = "FTA_RunOut" Type = "FTA_TotalRunOut" Type = "FTA_CircularRunOut"

        :return: str
        """

        return self.com_object.Type

    @property
    def z(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Z(double iZ) (Write Only)
                |     method get_Z will never be exposed Set the offset of the
                |     annotation
                | 
                |     Parameters:
                | 
                |         iZ
                |             The offset.

        :return: None
        """

        return None

    @z.setter
    def z(self, value: float):
        """
        :param float value:
        """

        self.com_object.Z = value

    def add_leader(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddLeader()
                |     Add a leader.

        :return: None
        """
        return self.com_object.AddLeader()

    def apply_referenced_geom_color(self, i_releated_r: int, i_releated_g: int, i_releated_b: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ApplyReferencedGeomColor(long iReleatedR,long iReleatedG,long
                | iReleatedB)
                |     Apply a color to referenced geometry.

        :param int i_releated_r:
        :param int i_releated_g:
        :param int i_releated_b:
        :return: None
        """
        return self.com_object.ApplyReferencedGeomColor(i_releated_r, i_releated_g, i_releated_b)

    def apply_referenced_init_color(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ApplyReferencedInitColor()
                |     Apply the initial color to referenced geometry.

        :return: None
        """
        return self.com_object.ApplyReferencedInitColor()

    def associated_ref_frame(self) -> AssociatedRefFrame:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AssociatedRefFrame() As AssociatedRefFrame
                |     Get the annotation on the AssociatedRefFrame interface.

        :return: AssociatedRefFrame
        """
        return AssociatedRefFrame(self.com_object.AssociatedRefFrame())

    def composite_tolerance(self) -> CompositeTolerance:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CompositeTolerance() As CompositeTolerance
                |     Get the annotation on the CompositeTolerance interface.

        :return: CompositeTolerance
        """
        return CompositeTolerance(self.com_object.CompositeTolerance())

    def controled_radius(self) -> ControlledRadius:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ControledRadius() As ControledRadius
                |     Get the annotation on the ControledRadius interface.

        :return: ControledRadius
        """
        return ControlledRadius(self.com_object.ControlledRadius())

    def datum_simple(self) -> DatumSimple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DatumSimple() As DatumSimple
                |     Get the annotation on the DatumSimple interface.

        :return: DatumSimple
        """
        return DatumSimple(self.com_object.DatumSimple())

    def datum_target(self) -> DatumTarget:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DatumTarget() As DatumTarget
                |     Get the annotation on the DatumTarget interface.

        :return: DatumTarget
        """
        return DatumTarget(self.com_object.DatumTarget())

    def default_annotation(self) -> DefaultAnnotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefaultAnnotation() As DefaultAnnotation
                |     Get the annotation on the DefaultAnnotation interface.

        :return: DefaultAnnotation
        """
        return DefaultAnnotation(self.com_object.DefaultAnnotation())

    def dimension3_d(self) -> Dimension3D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Dimension3D() As Dimension3D
                |     Get the 3D Dimension on the 3D Dimension interface.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The 3D Dimension.

        :return: Dimension3D
        """
        return Dimension3D(self.com_object.Dimension3D())

    def dimension_limit(self) -> DimensionLimit:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DimensionLimit() As DimensionLimit
                |     Get the annotation on the DimensionLimit interface.

        :return: DimensionLimit
        """
        return DimensionLimit(self.com_object.DimensionLimit())

    def dimension_pattern(self) -> DimensionPattern:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DimensionPattern() As DimensionPattern
                |     Get the annotation on the DimensionPattern interface.

        :return: DimensionPattern
        """
        return DimensionPattern(self.com_object.DimensionPattern())

    def envelop_condition(self) -> EnvelopCondition:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func EnvelopCondition() As EnvelopCondition
                |     Get the annotation on the EnvelopCondition interface.

        :return: EnvelopCondition
        """
        return EnvelopCondition(self.com_object.EnvelopCondition())

    def flag_note(self) -> FlagNote:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FlagNote() As FlagNote
                |     Get the annotation on the FlagNote interface.
                | 
                |     Parameters:
                | 
                |         oFlagNote
                |             The annotation Flag Note.

        :return: FlagNote
        """
        return FlagNote(self.com_object.FlagNote())

    def free_state(self) -> FreeState:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FreeState() As FreeState
                |     Get the annotation on the FreeState interface.

        :return: FreeState
        """
        return FreeState(self.com_object.FreeState())

    def get_geometrical_component_name(self, i_index: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGeometricalComponentName(short iIndex) As CATBSTR
                |     Gets the Geometrical Component name at given index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the geometrical component; this value is greater or
                |             equal to 1 and lower or equal to the value returned by
                |             GetNbrOfGeometricalComponent. 
                |         oComponentName
                |             The name of the geometrical component.

        :param int i_index:
        :return: str
        """
        return self.com_object.GetGeometricalComponentName(i_index)

    def get_nbr_of_geometrical_component(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbrOfGeometricalComponent() As short
                |     Gets the number of geometrical components.
                | 
                |     Parameters:
                | 
                |         oGeomLinkNbr
                |             The number of links to the geometry employed by this
                |             annotation.
                |             The returned value is comprise in between 1 and N (N is at most the
                |             total of geometrical links existing under the
                |             annotation).
                |             The amount of Geometrical Component sent back may be different from
                |             the annotation total links to the geometry because
                |             sometimes
                |             the Group of Surfaces may point to the same geometrical component
                |             participating to the definition of several User Surfaces.

        :return: int
        """
        return self.com_object.GetNbrOfGeometricalComponent()

    def get_surfaces(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetSurfaces(CATSafeArrayVariant oSafeArray)
                |     Get the geometry on which the Annotation is applied to.

        :return: tuple
        """
        return self.com_object.GetSurfaces()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_surfaces'
        # vba_code = """
        # Public Function get_surfaces(annotation)
        #     Dim oSafeArray (2)
        #     annotation.GetSurfaces oSafeArray
        #     get_surfaces = oSafeArray
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_surfaces_count(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSurfacesCount() As double
                |     Count the geometry on which the Annotation is applied to.

        :return: float
        """
        return self.com_object.GetSurfacesCount()

    def has_a_controled_radius(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAControledRadius() As boolean
                |     To know if the Annotation has a Controled Radius.

        :return: bool
        """
        return self.com_object.HasAControledRadius()

    def has_a_free_state(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAFreeState() As boolean
                |     To know if the Annotation has a Free State.

        :return: bool
        """
        return self.com_object.HasAFreeState()

    def has_a_material_condition(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAMaterialCondition() As boolean
                |     To know if the Annotation has a Material Condition.

        :return: bool
        """
        return self.com_object.HasAMaterialCondition()

    def has_a_numerical_display_format(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasANumericalDisplayFormat() As boolean
                |     Checks if the Annotation has a Numerical Display Format.

        :return: bool
        """
        return self.com_object.HasANumericalDisplayFormat()

    def has_a_particular_tol_elem(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAParticularTolElem() As boolean
                |     To know if the Annotation has a Particuler Element.

        :return: bool
        """
        return self.com_object.HasAParticularTolElem()

    def has_a_tolerance_per_unit_basis_restrictive_value(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasATolerancePerUnitBasisRestrictiveValue() As boolean
                |     To know if the Annotation has a Tolerance Per Unit Basis Restricted Value.

        :return: bool
        """
        return self.com_object.HasATolerancePerUnitBasisRestrictiveValue()

    def has_an_envelop_condition(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAnEnvelopCondition() As boolean
                |     To know if the Annotation has an Envelop Condition.

        :return: bool
        """
        return self.com_object.HasAnEnvelopCondition()

    def has_dimension_limit(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasDimensionLimit() As boolean
                |     To know if the Annotation has a Dimension Limit.

        :return: bool
        """
        return self.com_object.HasDimensionLimit()

    def is_a_composite_tolerance(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsACompositeTolerance() As boolean
                |     To know if the Annotation is a composite Tolerance.

        :return: bool
        """
        return self.com_object.IsACompositeTolerance()

    def is_a_default_annotation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsADefaultAnnotation() As boolean
                |     To know if the Annotation is a Default Annotation.

        :return: bool
        """
        return self.com_object.IsADefaultAnnotation()

    def is_a_dimension_pattern(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsADimensionPattern() As boolean
                |     To know if the Annotation is a Dimension Pattern.

        :return: bool
        """
        return self.com_object.IsADimensionPattern()

    def is_a_projected_tolerance_zone(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAProjectedToleranceZone() As boolean
                |     To know if the Annotation is a Projected Zone.

        :return: bool
        """
        return self.com_object.IsAProjectedToleranceZone()

    def is_a_shifted_profile_tolerance(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAShiftedProfileTolerance() As boolean
                |     To know if the Annotation is a Shifted Profile Tolerance.

        :return: bool
        """
        return self.com_object.IsAShiftedProfileTolerance()

    def is_a_tangent_plane(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsATangentPlane() As boolean
                |     To know if the Annotation is a Tangent Plane.

        :return: bool
        """
        return self.com_object.IsATangentPlane()

    def is_a_tolerance_unit_basis_value(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAToleranceUnitBasisValue() As boolean
                |     To know if the Annotation is a Tolerance Unit Basis Value.

        :return: bool
        """
        return self.com_object.IsAToleranceUnitBasisValue()

    def is_a_tolerance_zone(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAToleranceZone() As boolean
                |     Is the a Tolerance Zone.

        :return: bool
        """
        return self.com_object.IsAToleranceZone()

    def is_an_associated_ref_frame(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAnAssociatedRefFrame() As boolean
                |     To know if the Annotation is an Associated Reference Frame.

        :return: bool
        """
        return self.com_object.IsAnAssociatedRefFrame()

    def material_condition(self) -> MaterialCondition:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func MaterialCondition() As MaterialCondition
                |     Get the annotation on the MaterialCondition interface.

        :return: MaterialCondition
        """
        return MaterialCondition(self.com_object.MaterialCondition())

    def modify_visu(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ModifyVisu()
                |     To refresh the 3D visualization.

        :return: None
        """
        return self.com_object.ModifyVisu()

    def noa(self) -> Noa:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Noa() As Noa
                |     Get the annotation on the Noa interface.

        :return: Noa
        """
        return Noa(self.com_object.Noa())

    def numerical_display_format(self) -> NumericalDisplayFormat:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func NumericalDisplayFormat() As NumericalDisplayFormat
                |     Gets the annotation on the NumericalDisplayFormat interface.

        :return: NumericalDisplayFormat
        """
        return NumericalDisplayFormat(self.com_object.NumericalDisplayFormat())

    def particular_tol_elem(self) -> ParticularTolElem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ParticularTolElem() As ParticularTolElem
                |     Get the annotation on the ParticularTolElem interface.

        :return: ParticularTolElem
        """
        return ParticularTolElem(self.com_object.ParticularTolElem())

    def projected_tolerance_zone(self) -> ProjectedToleranceZone:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ProjectedToleranceZone() As ProjectedToleranceZone
                |     Get the annotation on the ProjectedToleranceZone interface.

        :return: ProjectedToleranceZone
        """
        return ProjectedToleranceZone(self.com_object.ProjectedToleranceZone())

    def reference_frame(self) -> ReferenceFrame:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ReferenceFrame() As ReferenceFrame
                |     Get the annotation on the ReferenceFrame interface.

        :return: ReferenceFrame
        """
        return ReferenceFrame(self.com_object.ReferenceFrame())

    def roughness(self) -> Roughness:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Roughness() As Roughness
                |     Get the annotation on the Roughness interface.

        :return: Roughness
        """
        return Roughness(self.com_object.Roughness())

    def set_geometrical_component_name(self, i_index: int, i_new_name: str, i_check_name_unicity_option: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGeometricalComponentName(short iIndex,CATBSTR iNewName,boolean
                | iCheckNameUnicityOption)
                |     Sets the Geometrical Component name at given index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the geometrical component; this value is greater or
                |             equal to 1 and lower or equal to the value returned by
                |             GetNbrOfGeometricalComponent.
                |             The user is allowed to pass a 0 value as index; in this case, an
                |             automatic renaming is triggered.
                |             In this case the usual path of a geometrical component (for
                |             instance Face/Name of the feature/Body.1) is used to extract the logical name
                |             to apply "Name of the feature".
                |             Pay attention that geometrical component name must be unique; this
                |             method is exiting in error whenever the unicity is of geometrical component is
                |             broken.
                |             The renaming processing is given up without any change when an
                |             already existing name is passed to this method or when automatic processing
                |             faces naming ambiguity. 
                |         iNewName
                |             The string used to rename the geometrical component.
                |             
                |         iCheckNameUnicityOption
                |             Option to trigger an addition verification during renaming to
                |             guarantee that the entire set of Geometrical Components in the
                |             representation
                |             have a different name.

        :param int i_index:
        :param str i_new_name:
        :param bool i_check_name_unicity_option:
        :return: None
        """
        return self.com_object.SetGeometricalComponentName(i_index, i_new_name, i_check_name_unicity_option)

    def set_xy(self, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetXY(double iX,double iY)
                |     method GetXY will never be exposed Set TPS coordinates in the
                |     view
                | 
                |     Parameters:
                | 
                |         oX
                |             The X coordinate. 
                |         oY
                |             The Y coordinate.

        :param float i_x:
        :param float i_y:
        :return: None
        """
        return self.com_object.SetXY(i_x, i_y)

    def shifted_profile_tolerance(self) -> ShiftedProfileTolerance:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ShiftedProfileTolerance() As ShiftedProfileTolerance
                |     Get the annotation on the ShiftedProfileTolerance interface.

        :return: ShiftedProfileTolerance
        """
        return ShiftedProfileTolerance(self.com_object.ShiftedProfileTolerance())

    def tangent_plane(self) -> TangentPlane:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TangentPlane() As TangentPlane
                |     Get the annotation on the TangentPlane interface.

        :return: TangentPlane
        """
        return TangentPlane(self.com_object.TangentPlane())

    def text(self) -> Text:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Text() As Text
                |     Get the annotation on the Text interface.
                | 
                |     Parameters:
                | 
                |         oText
                |             The annotation Text.

        :return: Text
        """
        return Text(self.com_object.Text())

    def tolerance_per_unit_basis_restrictive_value(self) -> TolerancePerUnitBasisRestrictiveValue:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TolerancePerUnitBasisRestrictiveValue() As
                | TolerancePerUnitBasisRestrictiveValue
                |     Get the annotation on the TolerancePerUnitBasisRestrictiveValue interface.

        :return: TolerancePerUnitBasisRestrictiveValue
        """
        return TolerancePerUnitBasisRestrictiveValue(self.com_object.TolerancePerUnitBasisRestrictiveValue())

    def tolerance_unit_basis_value(self) -> ToleranceUnitBasisValue:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ToleranceUnitBasisValue() As ToleranceUnitBasisValue
                |     Get the annotation on the ToleranceUnitBasisValue interface.

        :return: ToleranceUnitBasisValue
        """
        return ToleranceUnitBasisValue(self.com_object.ToleranceUnitBasisValue())

    def tolerance_zone(self) -> ToleranceZone:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ToleranceZone() As ToleranceZone
                |     Get the annotation on the ToleranceZone interface.

        :return: ToleranceZone
        """
        return ToleranceZone(self.com_object.ToleranceZone())

    def transfert_to_view(self, i_view: TPSView) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub TransfertToView(TPSView iView)
                |     Move the annotation in another view.
                | 
                |     Parameters:
                | 
                |         iView
                |             The destination view. 

        :param TPSView i_view:
        :return: None
        """
        return self.com_object.TransfertToView(i_view.com_object)

    def __repr__(self):
        return f'Annotation(name="{self.name}")'
