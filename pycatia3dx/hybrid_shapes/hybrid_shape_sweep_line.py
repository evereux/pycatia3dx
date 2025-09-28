"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.hybrid_shapes.hybrid_shape_sweep import HybridShapeSweep
from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapeSweepLine(HybridShapeSweep):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         CATGSMIDLItf.HybridShapeSweep
                |                             HybridShapeSweepLine
                | 
                | Represents the sweep line object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AngleLaw() As Reference
                |     Returns or sets the angular law.

        :return: Reference
        """

        return Reference(self.com_object.AngleLaw)

    @angle_law.setter
    def angle_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.AngleLaw = value

    @property
    def angle_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AngleLawInversion() As long
                |     Returns or sets whether the angular law has to be
                |     inverted.
                |     Legal angular law inversion values are:
                |     0 The angular law has NOT to be inverted
                |     1 The angular law has to be inverted

        :return: int
        """

        return self.com_object.AngleLawInversion

    @angle_law_inversion.setter
    def angle_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.com_object.AngleLawInversion = value

    @property
    def angle_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AngleLawType() As long
                |     Returns or sets the angular law type.
                |     Legal angular law type values are:
                |     0 Undefined law type (CATGSMBasicLawType_None)
                |     1 Constant law type (CATGSMBasicLawType_Constant)
                |     2 Linear law type (CATGSMBasicLawType_Linear)
                |     3 S law type (CATGSMBasicLawType_SType)
                |     4 Law specified by a GSD law feature
                |     (CATGSMBasicLawType_Advanced)

        :return: int
        """

        return self.com_object.AngleLawType

    @angle_law_type.setter
    def angle_law_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.AngleLawType = value

    @property
    def canonical_detection(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CanonicalDetection() As long
                |     Returns or sets whether canonical surfaces of the swept surface are
                |     detected.
                |     Legal values:
                |     0 No detection of canonical surface is performed.
                |     2 Detection of canonical surfaces is performed.

        :return: int
        """

        return self.com_object.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        """
        :param int value:
        """

        self.com_object.CanonicalDetection = value

    @property
    def context(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Context() As long
                |     Returns or sets the context on Sweep feature.
                | 
                |         0 This option creates Swept surface.
                |         1 This option creates Swept volume.
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example:
                |         This example retrieves in oContext the context for the Sweep hybrid
                |         shape feature.
                | 
                |          Dim oContext
                |          Set oContext = Sweep.Context

        :return: int
        """

        return self.com_object.Context

    @context.setter
    def context(self, value: int):
        """
        :param int value:
        """

        self.com_object.Context = value

    @property
    def draft_computation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DraftComputationMode() As long
                |     Returns or sets the draft computation mode.

        :return: int
        """

        return self.com_object.DraftComputationMode

    @draft_computation_mode.setter
    def draft_computation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.DraftComputationMode = value

    @property
    def draft_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DraftDirection() As HybridShapeDirection
                |     Returns or sets the draft direction.
                | 
                |     Example
                |     :
                |         This example retrieves in oDirection the direction of the LinearSweep
                |         feature.
                | 
                |          Dim oDirection As CATIAHybridShapeDirection
                |          Set oDirection = LinearSweep.DraftDirection

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.DraftDirection)

    @draft_direction.setter
    def draft_direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.DraftDirection = value

    @property
    def first_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstGuideCrv() As Reference
                |     Returns or sets the sweep operation first guide curve.

        :return: Reference
        """

        return Reference(self.com_object.FirstGuideCrv)

    @first_guide_crv.setter
    def first_guide_crv(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstGuideCrv = value

    @property
    def first_guide_surf(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstGuideSurf() As Reference
                |     Returns or sets the sweep operation first guide surface.

        :return: Reference
        """

        return Reference(self.com_object.FirstGuideSurf)

    @first_guide_surf.setter
    def first_guide_surf(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstGuideSurf = value

    @property
    def first_length_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstLengthLaw() As Reference
                |     Returns or sets the first length law useful in some linear sweep types.

        :return: Reference
        """

        return Reference(self.com_object.FirstLengthLaw)

    @first_length_law.setter
    def first_length_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstLengthLaw = value

    @property
    def first_length_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstLengthLawInversion() As long
                |     Returns or sets whether the first length law has to be
                |     inverted.
                |     Legal length law inversion values are:
                |     0 The length law has NOT to be inverted
                |     1 The length law has to be inverted

        :return: int
        """

        return self.com_object.FirstLengthLawInversion

    @first_length_law_inversion.setter
    def first_length_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.com_object.FirstLengthLawInversion = value

    @property
    def guide_deviation(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property GuideDeviation() As Length (Read Only)
                |     Returns the deviation value (length) from guide curves allowed during a
                |     sweeping operation in order to smooth it.

        :return: Length
        """

        return Length(self.com_object.GuideDeviation)

    @property
    def guide_deviation_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property GuideDeviationActivity() As boolean
                |     Returns or sets whether a deviation from guide curves is
                |     allowed.
                |     This property gives the information on performing smoothing during sweeping
                |     operation.
                |     TRUE if a deviation from guide curves is allowed, or FALSE otherwise (FALSE
                |     if not specified).

        :return: bool
        """

        return self.com_object.GuideDeviationActivity

    @guide_deviation_activity.setter
    def guide_deviation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.GuideDeviationActivity = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Mode() As long
                |     Returns or sets the linear sweep mode.
                |     Legal mode values are:
                |     0 Undefined linear profile swept surface
                |     (CATGSMLinearSweep_None)
                |     1 Linear profile swept surface defined by two guide curves
                |     (CATGSMLinearSweep_TwoGuides)
                |     2 Linear profile swept surface defined by a guide curve and an angle
                |     (CATGSMLinearSweep_GuideAndAngleCurve)
                |     3 Linear profile swept surface defined by a guide curve and a middle curve
                |     (CATGSMLinearSweep_GuideAndMiddle)
                |     4 Linear profile swept surface defined by a guide curve and an angle from
                |     a reference surface
                |     (CATGSMLinearSweep_GuideAndRefSurfaceAngle)
                |     5 Linear profile swept surface defined by a guide curve and a tangency
                |     surface (CATGSMLinearSweep_GuideAndTangencySurface)
                |     6 Linear profile swept surface defined by a guide curve and a draft
                |     directio (CATGSMLinearSweep_GuideAndDraftDirection)
                |     7 Linear profile swept surface defined by two tangency surfaces
                |     (CATGSMLinearSweep_TwoTangencySurfaces)

        :return: int
        """

        return self.com_object.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mode = value

    @property
    def second_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondGuideCrv() As Reference
                |     Returns or sets the sweep operation second guide curve.

        :return: Reference
        """

        return Reference(self.com_object.SecondGuideCrv)

    @second_guide_crv.setter
    def second_guide_crv(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondGuideCrv = value

    @property
    def second_guide_surf(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondGuideSurf() As Reference
                |     Returns or sets the sweep operation second guide surface.

        :return: Reference
        """

        return Reference(self.com_object.SecondGuideSurf)

    @second_guide_surf.setter
    def second_guide_surf(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondGuideSurf = value

    @property
    def second_length_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondLengthLaw() As Reference
                |     Returns or sets second length law useful in some linear sweep types.

        :return: Reference
        """

        return Reference(self.com_object.SecondLengthLaw)

    @second_length_law.setter
    def second_length_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondLengthLaw = value

    @property
    def second_length_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondLengthLawInversion() As long
                |     Returns or sets whether the second length law has to be
                |     inverted.
                |     Legal length law inversion values are:
                |     0 The length law has NOT to be inverted
                |     1 The length law has to be inverted

        :return: int
        """

        return self.com_object.SecondLengthLawInversion

    @second_length_law_inversion.setter
    def second_length_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.com_object.SecondLengthLawInversion = value

    @property
    def second_trim_option(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondTrimOption() As long
                |     Returns or sets the trim option for the second tangency
                |     surface.
                | 
                |     Legal trim option values are:
                |     0 No trim computed or trim undefined
                |     (CATGSMSweepTrimMode_None)
                |     1 Trim computed (CATGSMSweepTrimMode_On)

        :return: int
        """

        return self.com_object.SecondTrimOption

    @second_trim_option.setter
    def second_trim_option(self, value: int):
        """
        :param int value:
        """

        self.com_object.SecondTrimOption = value

    @property
    def smooth_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SmoothActivity() As boolean
                |     Returns whether the sweeping operation is smoothed.
                |     TRUE if the sweeping operation is smoothed, or FALSE otherwise (FALSE if
                |     not specified).

        :return: bool
        """

        return self.com_object.SmoothActivity

    @smooth_activity.setter
    def smooth_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SmoothActivity = value

    @property
    def smooth_angle_threshold(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SmoothAngleThreshold() As Angle (Read Only)
                |     Returns the angular threshold.

        :return: Angle
        """

        return Angle(self.com_object.SmoothAngleThreshold)

    @property
    def solution_no(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SolutionNo() As long
                |     Returns or sets the choice number, which corresponds to each solution of a
                |     given linear sweep case.
                |     For example: a linear sweep with reference surface leads to four possible
                |     solutions.

        :return: int
        """

        return self.com_object.SolutionNo

    @solution_no.setter
    def solution_no(self, value: int):
        """
        :param int value:
        """

        self.com_object.SolutionNo = value

    @property
    def spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Spine() As Reference
                |     Returns or sets the sweep operation spine (optional).

        :return: Reference
        """

        return Reference(self.com_object.Spine)

    @spine.setter
    def spine(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Spine = value

    @property
    def trim_option(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TrimOption() As long
                |     Returns or sets the trim option.
                | 
                |     Legal trim option values are:
                |     0 No trim computed or trim undefined
                |     (CATGSMSweepTrimMode_None)
                |     1 Trim computed (CATGSMSweepTrimMode_On)

        :return: int
        """

        return self.com_object.TrimOption

    @trim_option.setter
    def trim_option(self, value: int):
        """
        :param int value:
        """

        self.com_object.TrimOption = value

    def add_draft_angle_definition_location(self, ip_ia_loc_elem: Reference, i_ang: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddDraftAngleDefinitionLocation(Reference ipIALocElem,double
                | iAng)
                |     Adds a draft angle location.
                | 
                |     Parameters:
                | 
                |         ipIALocElem
                |             The geometric element where the draft angle applies
                |             
                |         iAng
                |             The draft angle

        :param Reference ip_ia_loc_elem:
        :param float i_ang:
        :return: None
        """
        return self.com_object.AddDraftAngleDefinitionLocation(ip_ia_loc_elem.com_object, i_ang)

    def get_angle(self, i_i: int) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetAngle(long iI) As Angle
                |     Returns the angle values useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The angle value index 
                | 
                |     Returns:
                |         The angle value

        :param int i_i:
        :return: Angle
        """
        return Angle(self.com_object.GetAngle(i_i))

    def get_angular_law(self, op_start_ang: Angle, op_end_ang: Angle, o_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetAngularLaw(Angle opStartAng,Angle opEndAng,long
                | oLawType)
                |     Retrieves the angular law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         opStartAng
                |             The angular law start value 
                |         opEndAng
                |             The angular law end value 
                |         oLawType
                |             The angular law type
                |             Legal angular law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param Angle op_start_ang:
        :param Angle op_end_ang:
        :param int o_law_type:
        :return: None
        """
        return self.com_object.GetAngularLaw(op_start_ang.com_object, op_end_ang.com_object, o_law_type)

    def get_choice_nb_surfaces(self, o_surf_ori1: int, o_surf_ori2: int, o_surf_coupl_ori1: int, o_surf_coupl_ori2: int, o_no: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetChoiceNbSurfaces(long oSurfOri1,long oSurfOri2,long oSurfCouplOri1,long
                | oSurfCouplOri2,long oNo)
                |     Gets a sequence which identifies a solution amongst all possibilities of a
                |     line-profile swept surface, case
                |     CATGSMLinearSweep_TwoTangencySurfaces.
                | 
                |     Parameters:
                | 
                |         oSurfOri1
                |             This orientation determines the location of the results with regard
                |             to the first surface. Possible values are:
                |             * +1 : the result is in the semi-space defined by the normal to the surface,
                |             * -1 : the result is in the semi-space defined by the opposite to the normal to the surface,
                |             * 0 : no orientation is specified, all the results are output,
                |             * 2 : the result changes of semi-space along the spine.
                |         oSurfOri2
                |             This orientation determines the location of the results with regard
                |             to the second surface. Possible values are as for oSurfOri1.
                |             
                |         oSurfCouplOri1
                |             This orientation determines the location of the results with regard
                |             to the trihedron defined by the the spine, the normal to the first surface and
                |             the tangent to the linear profile. Possible values
                |             are:
                |             * +1 : the output results are such that the triedron is counter clockwise,
                |             * -1 : the output results are such that the triedron is clockwise,
                |             * 0 : no orientation is specified, all the results are output,
                |             * 2 : the orientation of the trihedron changes along the spine. 
                |         oSurfCouplOri2
                |             This orientation determines the location of the results with regard
                |             to the trihedron defined by the the spine, the normal to the second surface and
                |             the tangent to the linear profile. Possible values are as for oSurfCouplOri1.
                |             
                |         oNo
                |             Given the previous orientations, solution number in a distance
                |             ordered list.

        :param int o_surf_ori1:
        :param int o_surf_ori2:
        :param int o_surf_coupl_ori1:
        :param int o_surf_coupl_ori2:
        :param int o_no:
        :return: None
        """
        return self.com_object.GetChoiceNbSurfaces(o_surf_ori1, o_surf_ori2, o_surf_coupl_ori1, o_surf_coupl_ori2, o_no)

    def get_choice_no(self, o_val1: int, o_val2: int, o_val3: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetChoiceNo(long oVal1,long oVal2,long oVal3)
                |     Retrieves the choice number associated with each solution of a given linear
                |     sweep case.
                |     Example: a linear sweep with one guide curve and a tangency surface may
                |     lead to several possible solutions.
                | 
                |     Parameters:
                | 
                |         oVal1
                |             The solution number (from 1 to n) 
                |         oVal2
                |             In the example, the shell orientation : -1, +1 or 0 (both +1 and -1) 
                |         val3
                |             In the example, the wire orientation : -1, +1 or 0 (both +1 and -1)

        :param int o_val1:
        :param int o_val2:
        :param int o_val3:
        :return: None
        """
        return self.com_object.GetChoiceNo(o_val1, o_val2, o_val3)

    def get_draft_angle_definition_location(self, i_loc: int, op_ia_element: Reference, o_angle: Angle) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetDraftAngleDefinitionLocation(long iLoc,Reference opIAElement,Angle
                | oAngle)
                |     Retrieves the draft angle location element.
                | 
                |     Parameters:
                | 
                |         iLoc
                |             The draft angle location position in the list 
                |         opIAElement
                |             The geometric element at that location and where the draft angle
                |             applies 
                |         oAngle
                |             The draft angle

        :param int i_loc:
        :param Reference op_ia_element:
        :param Angle o_angle:
        :return: None
        """
        return self.com_object.GetDraftAngleDefinitionLocation(i_loc, op_ia_element.com_object, o_angle.com_object)

    def get_draft_angle_definition_locations_nb(self, o_count: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetDraftAngleDefinitionLocationsNb(long oCount)
                |     Retrieves the draft angle location list size.
                | 
                |     Parameters:
                | 
                |         oCount
                |             The draft angle location list size

        :param int o_count:
        :return: None
        """
        return self.com_object.GetDraftAngleDefinitionLocationsNb(o_count)

    def get_first_length_definition_type(self, o_first_type: int, op_ia_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetFirstLengthDefinitionType(long oFirstType,Reference
                | opIAElem)
                |     Retrieves the first length definition type.
                | 
                |     Parameters:
                | 
                |         oFirstType
                |             The first length definition type
                |             Legal length definition types are:
                |             0 Undefined length type
                |             (CATGSMLinearSweepLengthType_None)
                |             1 Length of the swept line in the sweeping plane from the guide
                |             curve (CATGSMLinearSweepLengthType_Standard)
                |             2 No numerical value is required, equivalent to standard length at
                |             zero (CATGSMLinearSweepLengthType_FromCurve)
                |             3 Up to or from a geometrical reference (a surface)
                |             (CATGSMLinearSweepLengthType_Reference)
                |             4 Only for draft surfaces, the length is computed in the draft
                |             direction from an extremum point on the guide curve
                |             (CATGSMLinearSweepLengthType_FromExtremum)
                |             5 Only for draft surfaces, the length will be used in a way
                |             similar to euclidean parallel curve distance on the swept surface
                |             (CATGSMLinearSweepLengthType_AlongSurface)
                |         opIAElem
                |             The geometric element where the first length definition type
                |             applies

        :param int o_first_type:
        :param Reference op_ia_elem:
        :return: None
        """
        return self.com_object.GetFirstLengthDefinitionType(o_first_type, op_ia_elem.com_object)

    def get_first_length_law(self, o_length1: Length, o_length2: Length, o_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetFirstLengthLaw(Length oLength1,Length oLength2,long
                | oLawType)
                |     Retrieves the first length law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         oLength1
                |             The length law start value 
                |         oLength2
                |             The length law end value 
                |         oLawType
                |             The length law type
                |             Legal length law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param Length o_length1:
        :param Length o_length2:
        :param int o_law_type:
        :return: None
        """
        return self.com_object.GetFirstLengthLaw(o_length1.com_object, o_length2.com_object, o_law_type)

    def get_length(self, i_i: int) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetLength(long iI) As Length
                |     Returns the length values useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The length value index 
                | 
                |     Returns:
                |         The length value

        :param int i_i:
        :return: Length
        """
        return Length(self.com_object.GetLength(i_i))

    def get_length_law_types(self, o_first_type: int, o_second_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetLengthLawTypes(long oFirstType,long oSecondType)
                |     Gets length law types.
                | 
                |     Parameters:
                | 
                |         oFirstType
                |             First type of law. 
                |         oSecondType
                |             Second type of law. oFirstType and oSecondType = 0 : Undefined law type = 1 : Constant law type = 2 : Linear law type = 3 : S law type = 4 : Law specified by a GSD law feature = 5 : Law specified by a set of points and parameters

        :param int o_first_type:
        :param int o_second_type:
        :return: None
        """
        return self.com_object.GetLengthLawTypes(o_first_type, o_second_type)

    def get_longitudinal_relimiters(self, op_ia_elem1: Reference, op_ia_elem2: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetLongitudinalRelimiters(Reference opIAElem1,Reference
                | opIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepLine#GetRelimiters Retrieves the elements
                |         relimiting the spine (or the default spine). 
                |     Parameters:
                | 
                |         opIAElem1
                |             The first relimiting feature (plane or point) 
                |         opIAElem2
                |             The second relimiting feature (plane or point)

        :param Reference op_ia_elem1:
        :param Reference op_ia_elem2:
        :return: None
        """
        return self.com_object.GetLongitudinalRelimiters(op_ia_elem1.com_object, op_ia_elem2.com_object)

    def get_nb_angle(self, o_ang: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbAngle(long oAng)
                |     Retrieves the number of angles.
                | 
                |     Parameters:
                | 
                |         oAng
                |             The number of angles

        :param int o_ang:
        :return: None
        """
        return self.com_object.GetNbAngle(o_ang)

    def get_nb_guide_crv(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbGuideCrv(long oNum)
                |     Retrieves the number of guides curves.
                | 
                |     Parameters:
                | 
                |         oNum
                |             The number of guide curves

        :param int o_num:
        :return: None
        """
        return self.com_object.GetNbGuideCrv(o_num)

    def get_nb_guide_sur(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbGuideSur(long oNum)
                |     Retrieves the number of guide surfaces.
                | 
                |     Parameters:
                | 
                |         oNum
                |             The number of guides surfaces

        :param int o_num:
        :return: None
        """
        return self.com_object.GetNbGuideSur(o_num)

    def get_nb_length(self, o_len: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbLength(long oLen)
                |     Retrieves the number of lengths.
                | 
                |     Parameters:
                | 
                |         oLen
                |             The number of lengths

        :param int o_len:
        :return: None
        """
        return self.com_object.GetNbLength(o_len)

    def get_relimiters(self, op_ia_elem1: Reference, op_orient1: int, op_ia_elem2: Reference, op_orient2: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetRelimiters(Reference opIAElem1,long opOrient1,Reference opIAElem2,long
                | opOrient2)
                |     Retrieves the elements relimiting the spine (or the default
                |     spine).
                | 
                |     Parameters:
                | 
                |         opIAElem1
                |             The first relimiting feature (plane or point) 
                |         opOrient1
                |             Split direction for the first relimitation
                |             0 means that the beginning of the spine (considering its
                |             orientation) is removed, 1 means that the end of the spine is removed
                |             
                |         opIAElem2
                |             The second relimiting feature (plane or point) 
                |         opOrient2
                |             Split direction for the second relimitation

        :param Reference op_ia_elem1:
        :param int op_orient1:
        :param Reference op_ia_elem2:
        :param int op_orient2:
        :return: None
        """
        return self.com_object.GetRelimiters(op_ia_elem1.com_object, op_orient1, op_ia_elem2.com_object, op_orient2)

    def get_second_length_definition_type(self, o_second_type: int, op_ia_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetSecondLengthDefinitionType(long oSecondType,Reference
                | opIAElem)
                |     Retrieves the second length definition type.
                | 
                |     Parameters:
                | 
                |         oSecondType
                |             The second length definition type
                |             Legal length definition types are:
                |             0 Undefined length type
                |             (CATGSMLinearSweepLengthType_None)
                |             1 Length of the swept line in the sweeping plane from the guide
                |             curve (CATGSMLinearSweepLengthType_Standard)
                |             2 No numerical value is required, equivalent to standard length at
                |             zero (CATGSMLinearSweepLengthType_FromCurve)
                |             3 Up to or from a geometrical reference (a surface)
                |             (CATGSMLinearSweepLengthType_Reference)
                |             4 Only for draft surfaces, the length is computed in the draft
                |             direction from an extremum point on the guide curve
                |             (CATGSMLinearSweepLengthType_FromExtremum)
                |             5 Only for draft surfaces, the length will be used in a way
                |             similar to euclidean parallel curve distance on the swept surface
                |             (CATGSMLinearSweepLengthType_AlongSurface)
                |         opIAElem
                |             The geometric element where the second length definition type
                |             applies

        :param int o_second_type:
        :param Reference op_ia_elem:
        :return: None
        """
        return self.com_object.GetSecondLengthDefinitionType(o_second_type, op_ia_elem.com_object)

    def get_second_length_law(self, o_length1: Length, o_length2: Length, o_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetSecondLengthLaw(Length oLength1,Length oLength2,long
                | oLawType)
                |     Retrieves the second length law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         oLength1
                |             The length law start value 
                |         oLength2
                |             The length law end value 
                |         oLawType
                |             The length law type
                |             Legal length law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param Length o_length1:
        :param Length o_length2:
        :param int o_law_type:
        :return: None
        """
        return self.com_object.GetSecondLengthLaw(o_length1.com_object, o_length2.com_object, o_law_type)

    def insert_draft_angle_definition_location(self, i_elem: Reference, i_angle: Angle, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InsertDraftAngleDefinitionLocation(Reference iElem,Angle iAngle,long
                | iPos)
                |     Inserts a geometrical element and a value necessary for draft angle
                |     definition after a given position in the lists.
                | 
                |     Parameters:
                | 
                |         iElem
                |             Geometrical element 
                |         iAngle
                |             Angular parameter 
                |         iPos
                |             Position in lists. To insert in the beginning of the list put iPos = 0.

        :param Reference i_elem:
        :param Angle i_angle:
        :param int i_pos:
        :return: None
        """
        return self.com_object.InsertDraftAngleDefinitionLocation(i_elem.com_object, i_angle.com_object, i_pos)

    def remove_all_draft_angle_definition_locations(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllDraftAngleDefinitionLocations()
                |     Removes all geometrical elements and values necessary for draft angle
                |     definition.

        :return: None
        """
        return self.com_object.RemoveAllDraftAngleDefinitionLocations()

    def remove_angle(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAngle()
                |     Removes an angle.

        :return: None
        """
        return self.com_object.RemoveAngle()

    def remove_draft_angle_definition_location_position(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveDraftAngleDefinitionLocationPosition(long iPos)
                |     Removes a draft angle location.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position in the list of the draft angle location to remove

        :param int i_pos:
        :return: None
        """
        return self.com_object.RemoveDraftAngleDefinitionLocationPosition(i_pos)

    def remove_guide_crv(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveGuideCrv()
                |     Removes a guide curve.

        :return: None
        """
        return self.com_object.RemoveGuideCrv()

    def remove_guide_sur(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveGuideSur()
                |     Removes a guide surface.

        :return: None
        """
        return self.com_object.RemoveGuideSur()

    def remove_length(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveLength()
                |     Removes a length.

        :return: None
        """
        return self.com_object.RemoveLength()

    def set_angle(self, i_i: int, i_elem: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngle(long iI,double iElem)
                |     Sets the angle values useful in some linear sweep types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The angle value index 
                |         iElem
                |             The angle value

        :param int i_i:
        :param float i_elem:
        :return: None
        """
        return self.com_object.SetAngle(i_i, i_elem)

    def set_angular_law(self, i_start_ang: float, i_end_ang: float, i_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngularLaw(double iStartAng,double iEndAng,long
                | iLawType)
                |     Sets the angular law useful in some linear sweep types.
                | 
                |     Parameters:
                | 
                |         iStartAng
                |             The angular law start value 
                |         iEndAng
                |             The angular law end value 
                |         iLawType
                |             The angular law type
                |             Legal angular law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param float i_start_ang:
        :param float i_end_ang:
        :param int i_law_type:
        :return: None
        """
        return self.com_object.SetAngularLaw(i_start_ang, i_end_ang, i_law_type)

    def set_choice_nb_surfaces(self, i_surf_ori1: int, i_surf_ori2: int, i_surf_coupl_ori1: int, i_surf_coupl_ori2: int, i_no: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetChoiceNbSurfaces(long iSurfOri1,long iSurfOri2,long iSurfCouplOri1,long
                | iSurfCouplOri2,long iNo)
                |     Sets a sequence which identifies a solution amongst all possibilities of a
                |     line-profile swept surface, case
                |     CATGSMLinearSweep_TwoTangencySurfaces.
                | 
                |     Parameters:
                | 
                |         iSurfOri1
                |             This orientation determines the location of the results with regard
                |             to the first surface. Possible values are:
                |             * +1 : the result is in the semi-space defined by the normal to the surface,
                |             * -1 : the result is in the semi-space defined by the opposite to the normal to the ,
                |             * 0 : no orientation is specified, all the results are output,
                |             * 2 : the result changes of semi-space along the spine.
                |         iSurfOri2
                |             This orientation determines the location of the results with regard
                |             to the second surface. Possible values are as for iSurfOri1.
                |             
                |         iSurfCouplOri1
                |             This orientation determines the location of the results with regard
                |             to the trihedron defined by the the spine, the normal to the first surface and
                |             the tangent to the linear profile. Possible values
                |             are:
                |             * +1 : the output results are such that the triedron is counter clockwise,
                |             * -1 : the output results are such that the triedron is clockwise,
                |             * 0 : no orientation is specified, all the results are output,
                |             * 2 : the orientation of the trihedron changes along the spine. 
                |         iSurfCouplOri2
                |             This orientation determines the location of the results with regard
                |             to the trihedron defined by the the spine, the normal to the second surface and
                |             the tangent to the linear profile. Possible values are as for iSurfCouplOri2.
                |             
                |         iNo
                |             Given the previous orientations, solution number in a distance
                |             ordered list.

        :param int i_surf_ori1:
        :param int i_surf_ori2:
        :param int i_surf_coupl_ori1:
        :param int i_surf_coupl_ori2:
        :param int i_no:
        :return: None
        """
        return self.com_object.SetChoiceNbSurfaces(i_surf_ori1, i_surf_ori2, i_surf_coupl_ori1, i_surf_coupl_ori2, i_no)

    def set_choice_no(self, i_val1: int, i_val2: int, i_val3: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetChoiceNo(long iVal1,long iVal2,long iVal3)
                |     Sets the choice number associated with each solution of a given linear
                |     sweep case.
                |     Example: a linear sweep with one guide curve and a tangency surface may
                |     lead to several possible solutions.
                | 
                |     Parameters:
                | 
                |         iVal1
                |             The solution number (from 1 to n) 
                |         iVal2
                |             In the example, the shell orientation : -1, +1 or 0 (both +1 and -1) 
                |         iVal3
                |             In the example, the wire orientation : -1, +1 or 0 (both +1 and -1)

        :param int i_val1:
        :param int i_val2:
        :param int i_val3:
        :return: None
        """
        return self.com_object.SetChoiceNo(i_val1, i_val2, i_val3)

    def set_first_length_definition_type(self, i_first_type: int, ip_ia_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetFirstLengthDefinitionType(long iFirstType,Reference
                | ipIAElem)
                |     Sets the first length definition type.
                | 
                |     Parameters:
                | 
                |         iFirstType
                |             The first length definition type
                |             Legal length definition types are:
                |             0 Undefined length type
                |             (CATGSMLinearSweepLengthType_None)
                |             1 Length of the swept line in the sweeping plane from the guide
                |             curve (CATGSMLinearSweepLengthType_Standard)
                |             2 No numerical value is required, equivalent to standard length at
                |             zero (CATGSMLinearSweepLengthType_FromCurve)
                |             3 Up to or from a geometrical reference (a surface)
                |             (CATGSMLinearSweepLengthType_Reference)
                |             4 Only for draft surfaces, the length is computed in the draft
                |             direction from an extremum point on the guide curve
                |             (CATGSMLinearSweepLengthType_FromExtremum)
                |             5 Only for draft surfaces, the length will be used in a way
                |             similar to euclidean parallel curve distance on the swept surface
                |             (CATGSMLinearSweepLengthType_AlongSurface)
                |         ipIAElem
                |             The geometric element where the first length definition type
                |             applies

        :param int i_first_type:
        :param Reference ip_ia_elem:
        :return: None
        """
        return self.com_object.SetFirstLengthDefinitionType(i_first_type, ip_ia_elem.com_object)

    def set_first_length_law(self, i_length1: float, i_length2: float, i_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetFirstLengthLaw(double iLength1,double iLength2,long
                | iLawType)
                |     Sets the first length law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iLength1
                |             The length law start value 
                |         iLength2
                |             The length law end value 
                |         iLawType
                |             The length law type
                |             Legal length law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param float i_length1:
        :param float i_length2:
        :param int i_law_type:
        :return: None
        """
        return self.com_object.SetFirstLengthLaw(i_length1, i_length2, i_law_type)

    def set_guide_deviation(self, i_length: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetGuideDeviation(double iLength)
                |     Sets the deviation value (length) from guide curves allowed during sweeping
                |     operation in order to smooth it.
                | 
                |     Parameters:
                | 
                |         iLength
                |             The deviation value

        :param float i_length:
        :return: None
        """
        return self.com_object.SetGuideDeviation(i_length)

    def set_length(self, i_i: int, i_elem: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLength(long iI,double iElem)
                |     Sets the linear values useful in some linear sweep types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The linear value index 
                |         iElem
                |             The linear value

        :param int i_i:
        :param float i_elem:
        :return: None
        """
        return self.com_object.SetLength(i_i, i_elem)

    def set_length_law_types(self, i_first_type: int, i_second_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLengthLawTypes(long iFirstType,long iSecondType)
                |     Sets length law types.
                | 
                |     Parameters:
                | 
                |         iFirstType
                |             First type of law. 
                |         iSecondType
                |             Second type of law. iFirstType and iSecondType = 0 : Undefined law type = 1 : Constant law type = 2 : Linear law type = 3 : S law type = 4 : Law specified by a GSD law feature = 5 : Law specified by a set of points and parameters

        :param int i_first_type:
        :param int i_second_type:
        :return: None
        """
        return self.com_object.SetLengthLawTypes(i_first_type, i_second_type)

    def set_longitudinal_relimiters(self, ip_ia_elem1: Reference, ip_ia_elem2: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLongitudinalRelimiters(Reference ipIAElem1,Reference
                | ipIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepLine#SetRelimiters Sets the elements
                |         relimiting the spine (or the default spine). 
                |     Parameters:
                | 
                |         ipIAElem1
                |             The first relimiting feature (plane or point) 
                |         ipIAElem2
                |             The second relimiting feature (plane or point)

        :param Reference ip_ia_elem1:
        :param Reference ip_ia_elem2:
        :return: None
        """
        return self.com_object.SetLongitudinalRelimiters(ip_ia_elem1.com_object, ip_ia_elem2.com_object)

    def set_relimiters(self, ip_ia_elem1: Reference, ip_orient1: int, ip_ia_elem2: Reference, ip_orient2: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetRelimiters(Reference ipIAElem1,long ipOrient1,Reference ipIAElem2,long
                | ipOrient2)
                |     Sets the elements relimiting the spine (or the default
                |     spine).
                | 
                |     Parameters:
                | 
                |         ipIAElem1
                |             The first relimiting feature (plane or point) 
                |         ipOrient1
                |             Split direction for the first relimitation
                |             0 means that the beginning of the spine (considering its
                |             orientation) is removed, 1 means that the end of the spine is removed
                |             
                |         ipIAElem2
                |             The second relimiting feature (plane or point) 
                |         ipOrient2
                |             Split direction for the second relimitation

        :param Reference ip_ia_elem1:
        :param int ip_orient1:
        :param Reference ip_ia_elem2:
        :param int ip_orient2:
        :return: None
        """
        return self.com_object.SetRelimiters(ip_ia_elem1.com_object, ip_orient1, ip_ia_elem2.com_object, ip_orient2)

    def set_second_length_definition_type(self, i_second_type: int, ip_ia_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSecondLengthDefinitionType(long iSecondType,Reference
                | ipIAElem)
                |     Sets the second length definition type.
                | 
                |     Parameters:
                | 
                |         iSecondType
                |             The second length definition type
                |             Legal length definition types are:
                |             0 Undefined length type
                |             (CATGSMLinearSweepLengthType_None)
                |             1 Length of the swept line in the sweeping plane from the guide
                |             curve (CATGSMLinearSweepLengthType_Standard)
                |             2 No numerical value is required, equivalent to standard length at
                |             zero (CATGSMLinearSweepLengthType_FromCurve)
                |             3 Up to or from a geometrical reference (a surface)
                |             (CATGSMLinearSweepLengthType_Reference)
                |             4 Only for draft surfaces, the length is computed in the draft
                |             direction from an extremum point on the guide curve
                |             (CATGSMLinearSweepLengthType_FromExtremum)
                |             5 Only for draft surfaces, the length will be used in a way
                |             similar to euclidean parallel curve distance on the swept surface
                |             (CATGSMLinearSweepLengthType_AlongSurface)
                |         ipIAElem
                |             The geometric element where the second length definition type
                |             applies

        :param int i_second_type:
        :param Reference ip_ia_elem:
        :return: None
        """
        return self.com_object.SetSecondLengthDefinitionType(i_second_type, ip_ia_elem.com_object)

    def set_second_length_law(self, i_length1: float, i_length2: float, i_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSecondLengthLaw(double iLength1,double iLength2,long
                | iLawType)
                |     Sets the second length law useful in some linear sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iLength1
                |             The length law start value 
                |         iLength2
                |             The length law end value 
                |         iLawType
                |             The length law type
                |             Legal length law type values are:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)

        :param float i_length1:
        :param float i_length2:
        :param int i_law_type:
        :return: None
        """
        return self.com_object.SetSecondLengthLaw(i_length1, i_length2, i_law_type)

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSmoothAngleThreshold(double iAngle)
                |     Sets the angular threshold.
                | 
                |     Parameters:
                | 
                |         iAngle
                |             The angle numerical value

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetSmoothAngleThreshold(i_angle)

    def __repr__(self):
        return f'HybridShapeSweepLine(name="{ self.name }")'
