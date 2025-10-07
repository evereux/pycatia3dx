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
from pycatia3dx.tps.free_state import FreeState
from pycatia3dx.tps.material_condition import MaterialCondition
from pycatia3dx.tps.median_feature import MedianFeature
from pycatia3dx.tps.particular_tol_elem import ParticularTolElem
from pycatia3dx.tps.projected_tolerance_zone import ProjectedToleranceZone
from pycatia3dx.tps.semantic_gdt_frame_extension import SemanticGDTFrameExtension
from pycatia3dx.tps.semantic_gdt_nx_display import SemanticGDTNxDisplay
from pycatia3dx.tps.shifted_profile_tolerance import ShiftedProfileTolerance
from pycatia3dx.tps.tangent_plane import TangentPlane
from pycatia3dx.tps.tolerance_per_unit_basis_restrictive_value import TolerancePerUnitBasisRestrictiveValue
from pycatia3dx.tps.tolerance_unit_basis_value import ToleranceUnitBasisValue
from pycatia3dx.tps.tolerance_zone import ToleranceZone
from pycatia3dx.tps.tps_parallel_on_screen import TPSParallelOnScreen


class SemanticGDT(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDT
                | 
                | Interface managing Semantic GDT.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def associated_ref_frame(self) -> AssociatedRefFrame:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AssociatedRefFrame() As AssociatedRefFrame
                | 
                |     Role: Returns the annotation on the AssociatedRefFrame
                |     interface.
                | 
                |     Parameters:
                | 
                |         oAssRefFra
                |             The AssociatedRefFrame.

        :return: AssociatedRefFrame
        """
        return AssociatedRefFrame(self.com_object.AssociatedRefFrame())

    def composite_tolerance(self) -> CompositeTolerance:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CompositeTolerance() As CompositeTolerance
                | 
                |     Role: Returns the CompositeTolerance interface.
                | 
                |     Parameters:
                | 
                |         oCompTol
                |             The CompositeTolerance.

        :return: CompositeTolerance
        """
        return CompositeTolerance(self.com_object.CompositeTolerance())

    def frame_extensions(self, i_frame_extent_index: int) -> SemanticGDTFrameExtension:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FrameExtensions(long iFrameExtentIndex) As
                | SemanticGDTFrameExtension
                | 
                |     Role: Gets the Auxiliary Features at given Index applied on
                |     GDT.
                | 
                |     Parameters:
                | 
                |         iFrameExtentIndex
                |             Index of the Frame Extension to retrieve. 
                |         oAuxiliaryFeatures
                |             The list of Auxiliary Features specified on GDT (implies ISO
                |             Standard applied).

        :param int i_frame_extent_index:
        :return: SemanticGDTFrameExtension
        """
        return SemanticGDTFrameExtension(self.com_object.FrameExtensions(i_frame_extent_index))

    def free_state(self) -> FreeState:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FreeState() As FreeState
                | 
                |     Role: Returns the FreeState interface.
                | 
                |     Parameters:
                | 
                |         oFreeState
                |             The FreeState.

        :return: FreeState
        """
        return FreeState(self.com_object.FreeState())

    def has_a_centered_element(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasACenteredElement() As boolean
                | 
                |     Role: Checks if the geometrical specification has a centered
                |     element.
                |     Precondition: Median Feature characteristics is valid only for ISO
                |     standard
                | 
                |     Parameters:
                | 
                |         oHasCenterElt
                | 
                |                 TRUE: The GDT has a center element
                |                 FALSE: The GDT has not a center element or standard different
                |                 from ISO.

        :return: bool
        """
        return self.com_object.HasACenteredElement()

    def has_a_frame_extension(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAFrameExtension() As long
                | 
                |     Role: Checks if the geometrical specification wears a frame extension
                |     specification.
                |     Precondition: Intersection Plane, Orientation Plane, Collection Plane or
                |     Direction Feature are only meaningful in ISO Standard.
                | 
                |     Parameters:
                | 
                |         oFrameExtentNumber
                | 
                |                 Greater than 0: The GDT has oFrameExtentNumber frame
                |                 extensions
                |                 Equal or less than 0: The GDT has not a frame extension or
                |                 standard different from ISO (value is -1).

        :return: int
        """
        return self.com_object.HasAFrameExtension()

    def has_a_free_state(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAFreeState() As boolean
                | 
                |     Role: Checks if the GDT has a Free State.
                | 
                |     Parameters:
                | 
                |         oHasAFreeState
                | 
                |                 TRUE: There is a Free State
                |                 FALSE: There is no Free State

        :return: bool
        """
        return self.com_object.HasAFreeState()

    def has_a_material_condition(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAMaterialCondition() As boolean
                | 
                |     Role: Checks if the GDT has a Material Condition.
                | 
                |     Parameters:
                | 
                |         oHasMatCond
                | 
                |                 TRUE: A Material Condition exits
                |                 FALSE: There is no Material Condition

        :return: bool
        """
        return self.com_object.HasAMaterialCondition()

    def has_a_particular_tol_elem(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAParticularTolElem() As boolean
                | 
                |     Role: Checks if the GDT has a Particuler Element.
                | 
                |     Parameters:
                | 
                |         oHasAParTolElem
                | 
                |                 TRUE: There is a Particuler Element
                |                 FALSE: There is no Particuler Element

        :return: bool
        """
        return self.com_object.HasAParticularTolElem()

    def has_a_tangent_plane(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasATangentPlane() As boolean
                | 
                |     Role: Checks if the GDT has a Tangent Plane Modifier.
                | 
                |     Parameters:
                | 
                |         oIsATangentPlane
                | 
                |                 TRUE: There has a Tangent Plane
                |                 FALSE: There has not Tangent Plane

        :return: bool
        """
        return self.com_object.HasATangentPlane()

    def has_a_tolerance_per_unit_basis_restrictive_value(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasATolerancePerUnitBasisRestrictiveValue() As boolean
                | 
                |     Role: Checks if the GDT has a Tolerance Per Unit Basis Restricted
                |     Value.
                | 
                |     Parameters:
                | 
                |         oHasATolRes
                | 
                |                 TRUE: There is a Tolerance Per Unit Basis Restricted
                |                 Value
                |                 FALSE: There is no Tolerance Per Unit Basis Restricted
                |                 Value

        :return: bool
        """
        return self.com_object.HasATolerancePerUnitBasisRestrictiveValue()

    def is_a_composite_tolerance(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsACompositeTolerance() As boolean
                | 
                |     Role: Checks if the GDT is a Composite Tolerance.
                | 
                |     Parameters:
                | 
                |         oIsACompTol
                | 
                |                 TRUE: There is a Composite Tolerance
                |                 FALSE: There is no Composite Tolerance

        :return: bool
        """
        return self.com_object.IsACompositeTolerance()

    def is_a_projected_tolerance_zone(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAProjectedToleranceZone() As boolean
                | 
                |     Role: Checks if the GDT is a Projected Zone.
                | 
                |     Parameters:
                | 
                |         oIsAProjTolZone
                | 
                |                 TRUE: There is a Projected Zone
                |                 FALSE: There is no Projected Zone

        :return: bool
        """
        return self.com_object.IsAProjectedToleranceZone()

    def is_a_shifted_profile_tolerance(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAShiftedProfileTolerance() As boolean
                | 
                |     Role: Checks if the GDT is a Shifted Profile Tolerance.
                | 
                |     Parameters:
                | 
                |         oIsAShiftProTol
                | 
                |                 TRUE: There is a Shifted Profile Tolerance
                |                 FALSE: There is no Shifted Profile Tolerance

        :return: bool
        """
        return self.com_object.IsAShiftedProfileTolerance()

    def is_a_tolerance_unit_basis_value(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAToleranceUnitBasisValue() As boolean
                | 
                |     Role: Checks if the GDT is a Tolerance Unit Basis Value.
                | 
                |     Parameters:
                | 
                |         oIsATolUnitBas
                | 
                |                 TRUE: A Tolerance Zone exits
                |                 FALSE: There is no Tolerance Zone

        :return: bool
        """
        return self.com_object.IsAToleranceUnitBasisValue()

    def is_a_tolerance_zone(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAToleranceZone() As boolean
                | 
                |     Role: Checks if a Tolerance Zone exists.
                | 
                |     Parameters:
                | 
                |         oIsATolZone
                | 
                |                 TRUE: A Tolerance Zone exits
                |                 FALSE: There is no Tolerance Zone

        :return: bool
        """
        return self.com_object.IsAToleranceZone()

    def is_an_associated_ref_frame(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAnAssociatedRefFrame() As boolean
                | 
                |     Role: Checks if the GDT is an Associated Reference Frame.
                | 
                |     Parameters:
                | 
                |         oIsAnAssRefFra
                | 
                |                 TRUE: There is an Associated Reference Frame
                |                 FALSE: There is no Associated Reference Frame

        :return: bool
        """
        return self.com_object.IsAnAssociatedRefFrame()

    def is_applied_on_multiple_entities(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAppliedOnMultipleEntities() As boolean
                | 
                |     Role: Checks if the geometrical specification is applied onto multiple
                |     geometries.
                | 
                |     Parameters:
                | 
                |         oIsAPattern
                | 
                |                 TRUE: The GDT is applied on Nx elements
                |                 FALSE: The GDT is applied on a unique surface.

        :return: bool
        """
        return self.com_object.IsAppliedOnMultipleEntities()

    def material_condition(self) -> MaterialCondition:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func MaterialCondition() As MaterialCondition
                | 
                |     Role: Returns the MaterialCondition interface.
                | 
                |     Parameters:
                | 
                |         oMatCond
                |             The Material Condition.

        :return: MaterialCondition
        """
        return MaterialCondition(self.com_object.MaterialCondition())

    def median_feature(self) -> MedianFeature:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func MedianFeature() As MedianFeature
                | 
                |     Role: Gets the GDT on the Median Feature interface.
                | 
                |     Parameters:
                | 
                |         oMedianFeat
                |             The Median Feature.

        :return: MedianFeature
        """
        return MedianFeature(self.com_object.MedianFeature())

    def nx_display(self) -> SemanticGDTNxDisplay:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func NxDisplay() As SemanticGDTNxDisplay
                | 
                |     Role: Gets the GDT on the handle to read Nx instance count, Collection or
                |     Separate type of the geometrical specification.
                | 
                |     Parameters:
                | 
                |         oNxDisplay
                |             Behavior to qualify Nx application context of this GDT.

        :return: SemanticGDTNxDisplay
        """
        return SemanticGDTNxDisplay(self.com_object.NxDisplay())

    def particular_tol_elem(self) -> ParticularTolElem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ParticularTolElem() As ParticularTolElem
                | 
                |     Role: Returns the ParticularTolElem interface.
                | 
                |     Parameters:
                | 
                |         oParTolElem
                |             The ParticularTolElem.

        :return: ParticularTolElem
        """
        return ParticularTolElem(self.com_object.ParticularTolElem())

    def projected_tolerance_zone(self) -> ProjectedToleranceZone:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ProjectedToleranceZone() As ProjectedToleranceZone
                | 
                |     Role: Returns the ProjectedToleranceZone interface.
                | 
                |     Parameters:
                | 
                |         oProjTolZone
                |             The ProjectedToleranceZone.

        :return: ProjectedToleranceZone
        """
        return ProjectedToleranceZone(self.com_object.ProjectedToleranceZone())

    def shifted_profile_tolerance(self) -> ShiftedProfileTolerance:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ShiftedProfileTolerance() As ShiftedProfileTolerance
                | 
                |     Role: Returns the ShiftedProfileTolerance interface.
                | 
                |     Parameters:
                | 
                |         oShiftProTol
                |             The ShiftedProfileTolerance.

        :return: ShiftedProfileTolerance
        """
        return ShiftedProfileTolerance(self.com_object.ShiftedProfileTolerance())

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TPSParallelOnScreen() As TPSParallelOnScreen
                | 
                |     Role: Gets the annotation on TPSParallelOnScreen interface.

        :return: TpsParallelOnScreen
        """
        return TPSParallelOnScreen(self.com_object.TPSParallelOnScreen())

    def tangent_plane(self) -> TangentPlane:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TangentPlane() As TangentPlane
                | 
                |     Role: Returns the Tangent Plane interface.
                | 
                |     Parameters:
                | 
                |         oTangentPlane
                |             The Tangent Plane.

        :return: TangentPlane
        """
        return TangentPlane(self.com_object.TangentPlane())

    def tolerance_per_unit_basis_restrictive_value(self) -> TolerancePerUnitBasisRestrictiveValue:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TolerancePerUnitBasisRestrictiveValue() As
                | TolerancePerUnitBasisRestrictiveValue
                | 
                |     Role: Returns the TolerancePerUnitBasisRestrictiveValue
                |     interface.
                | 
                |     Parameters:
                | 
                |         oTolRes
                |             The TolerancePerUnitBasisRestrictiveValue.

        :return: TolerancePerUnitBasisRestrictiveValue
        """
        return TolerancePerUnitBasisRestrictiveValue(self.com_object.TolerancePerUnitBasisRestrictiveValue())

    def tolerance_unit_basis_value(self) -> ToleranceUnitBasisValue:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ToleranceUnitBasisValue() As ToleranceUnitBasisValue
                | 
                |     Role: Returns the ToleranceUnitBasisValue interface.
                | 
                |     Parameters:
                | 
                |         oTolUnitBas
                |             The Tolerance Unit Basis Value.

        :return: ToleranceUnitBasisValue
        """
        return ToleranceUnitBasisValue(self.com_object.ToleranceUnitBasisValue())

    def tolerance_zone(self) -> ToleranceZone:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ToleranceZone() As ToleranceZone
                | 
                |     Role: Returns the ToleranceZone interface.
                | 
                |     Parameters:
                | 
                |         oTolZone
                |             The Tolerance Zone. 

        :return: ToleranceZone
        """
        return ToleranceZone(self.com_object.ToleranceZone())

    def __repr__(self):
        return f'SemanticGdt(name="{ self.name }")'
