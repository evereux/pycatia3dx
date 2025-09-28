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


class HybridShapeSweepExplicit(HybridShapeSweep):

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
                |                             HybridShapeSweepExplicit
                | 
                | Represents the hybrid shape Sweep explicit feature object.
                | Role: To access the data of the hybrid shape sweep explicit feature
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | See also:
                |     HybridShapeFactory
    
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
                |     Returns or sets the angle law feature associated to the reference
                |     surface.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Angle law element. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference
                |     See also:
                |         HybridShapeFactory

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
                |     Returns or sets the angle law inversion information.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Angle law inversion information. 
                | 
                |     See also:
                |         HybridShapeFactory

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
                |     Returns or sets the angle law type associated to the reference
                |     surface.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Angle law type. 
                | 
                |     See also:
                |         HybridShapeFactory

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
    def first_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstGuideCrv() As Reference
                |     Gets the first guide curve.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Guide curve. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

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
    def guide_deviation(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property GuideDeviation() As Length (Read Only)
                |     Returns deviation value (length) from guide curves allowed during sweeping
                |     operation in order to smooth it.

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
                |     Returns or sets information whether a deviation from guide curves is
                |     allowed or not.
                |     Gives the information on performing smoothing during sweeping
                |     operation.
                |     TRUE or FALSE (FALSE if not specified).

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
    def guide_projection(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property GuideProjection() As boolean
                |     Returns or sets the projection of the guide curve onto the reference plane
                |     in order to use it as spine, in pulling direction case only. Removes Spine if
                |     GuideProjection is set to TRUE.
                |     Legal values: True projection is required and False if not
                | 
                |     Example:
                | 
                |          This example sets that the GuideProjection mode of
                |          the Sweep hybrid shape sweep explicit feature to
                |          True.
                |          
                | 
                |          Sweep.GuideProjection = True

        :return: bool
        """

        return self.com_object.GuideProjection

    @guide_projection.setter
    def guide_projection(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.GuideProjection = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Mode() As long
                |     Returns or sets positioning mode used for the profile.
                | 
                |     Parameters:
                | 
                |         oElem
                | 
                |             Values :
                |             = 1 - CATGSMPositionMode_NoneOrPositioned : no positioning,
                | 
                |             = 2 - CATGSMPositionMode_ExplicitSweep : the explicit profile is to be moved from its initial plane to the first sweep plane,
                | 
                |             = 3 - CATGSMPositionMode_Develop : === DO NOT USE IN THIS CASE === 
                | 
                |     See also:
                |         HybridShapeFactory

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
    def position_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PositionMode() As long
                |     Returns or sets positioning mode.
                |     Legal values:
                | 
                |     0
                |         CATGSMPositionMode_NoneOrPositioned. 
                |     1
                |         CATGSMPositionMode_ExplicitSweep. if a positioning operation is
                |         done.
                | 
                | Example:
                |     This example retrieves in oPosMode the position mode for the Sweep hybrid
                |     shape feature.
                | 
                |      oPosMode = Sweep.PositionMode

        :return: int
        """

        return self.com_object.PositionMode

    @position_mode.setter
    def position_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.PositionMode = value

    @property
    def positioned_profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PositionedProfile() As Reference
                |     Returns or sets the positioning transformation associated to the explicit
                |     swept surface and which result corresponds to the positioned
                |     profile.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Positioning transformation / positioned profile. return value for
                |             CATScript applications, with (IDLRETVAL) function type
                |             
                | 
                |     See also:
                |         Reference
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.com_object.PositionedProfile)

    @positioned_profile.setter
    def positioned_profile(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PositionedProfile = value

    @property
    def profile(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Profile() As Reference
                |     Gets the profile to be swept out.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Profile element. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.com_object.Profile)

    @profile.setter
    def profile(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Profile = value

    @property
    def profile_x_axis_computation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ProfileXAxisComputationMode() As long
                |     Returns or sets the computation mode of the X axis (or direction) of the
                |     initial axis system (on the profile). Default value is
                |     CATGSMPositionDirCompMode_None when PosDirection(OutputDirection) is not
                |     specified and CATGSMPositionDirCompMode_User if OutputDirection is
                |     specified.
                |     Legal values:
                | 
                |     0
                |         CATGSMPositionDirCompMode_None. No X axis specified. 
                |     1
                |         CATGSMPositionDirCompMode_Tangent: the X axis is implicitly the tangent
                |         of the profile at the origin (the origin then HAS to be on the
                |         profile)
                |     2
                |         CATGSMPositionDirCompMode_User: the X axis is specified by a direction
                |         via SetPosDirection(UserInputDirection, 1)
                | 
                | Example:
                |     This example retrieves in oDirCompMode the Profile X Axis ComputationMode
                |     for the Sweep hybrid shape feature.
                | 
                |      oDirCompMode = Sweep.ProfileXAxisComputationMode

        :return: int
        """

        return self.com_object.ProfileXAxisComputationMode

    @profile_x_axis_computation_mode.setter
    def profile_x_axis_computation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ProfileXAxisComputationMode = value

    @property
    def pulling_direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PullingDirection() As HybridShapeDirection
                |     Gets or sets the pulling direction
                |     If the direction is specified, the plane normal to this direction is taken
                |     as reference surface.
                | 
                |     Example:
                |         This example retrieves in ohDir the pulling direction feature for the
                |         Sweep hybrid shape feature.
                | 
                |          Dim ohDir As CATIAHybridShapeDirection
                |          Set ohDir = Sweep.PullingDirection

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.PullingDirection)

    @pulling_direction.setter
    def pulling_direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.PullingDirection = value

    @property
    def reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Reference() As Reference
                |     Returns or sets the reference surface (optional).
                | 
                |     Parameters:
                | 
                |         oElem
                |             Reference surface. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference

        :return: Reference
        """

        return Reference(self.com_object.Reference)

    @reference.setter
    def reference(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Reference = value

    @property
    def second_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondGuideCrv() As Reference
                |     Gets the second guide curve (optional).
                | 
                |     Parameters:
                | 
                |         oElem
                |             Guide curve. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

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
    def smooth_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SmoothActivity() As boolean
                |     Returns or sets information whether sweeping operation is smoothed or
                |     not.
                |     TRUE or FALSE (FALSE if not specified).

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
                |     Returns angular threshold.

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
                |     given explicit sweep case.
                |     For example: a explicit sweep with reference surface leads to four possible
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
                |     Returns or sets the spine (optional) for sweep operation.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Spine curve. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference
                |     See also:
                |         HybridShapeFactory

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
    def sub_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SubType() As long
                |     Returns or sets the explicit sweep subtype.
                |     Legal subtype values are:
                |     1 Explicit profile swept surface defined with reference
                |     surface
                |     2 Explicit profile swept surface defined with two guide
                |     curves
                |     3 Explicit profile swept surface defined with pulling
                |     direction

        :return: int
        """

        return self.com_object.SubType

    @sub_type.setter
    def sub_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SubType = value

    def get_angle_ref(self, ii: int) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetAngleRef(long ii) As Angle
                |     Gets the angle value associated to the reference surface.
                | 
                |     Parameters:
                | 
                |         iI
                |             Angle value index (1: start value, 2: end value). 
                |         oElem
                |             Angle value. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :return: Angle
        """
        return Angle(self.com_object.GetAngleRef(ii))

    def get_fitting_points(self, op_ia_elem_a: Reference, op_ia_elem_b: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetFittingPoints(Reference opIAElemA,Reference opIAElemB)
                |     Gets the fitting points : located in the profile plane, these points are used for two-guide swept surfaces to determine guide intersection locations.
                |     param opIAElem1 Fitting point associated to the first
                |     guide
                |     param opIAElem2 Fitting point associated to the second guide

        :param Reference op_ia_elem_a:
        :param Reference op_ia_elem_b:
        :return: None
        """
        return self.com_object.GetFittingPoints(op_ia_elem_a.com_object, op_ia_elem_b.com_object)

    def get_longitudinal_relimiters(self, op_ia_elem_a: Reference, op_ia_elem_b: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetLongitudinalRelimiters(Reference opIAElemA,Reference
                | opIAElemB)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepExplicit#GetRelimiters Returns the elements
                |         relimiting the spine (or the default spine).
                |         param : opIAElem1 First relimiting feature (plane or point)
                |         param : opIAElem2 Second relimiting feature (plane or point)

        :param Reference op_ia_elem_a:
        :param Reference op_ia_elem_b:
        :return: None
        """
        return self.com_object.GetLongitudinalRelimiters(op_ia_elem_a.com_object, op_ia_elem_b.com_object)

    def get_nb_angle(self, o_ang: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbAngle(long oAng)
                |     Returns the number of Angles.
                |     param : oAng Number of Angle.

        :param int o_ang:
        :return: None
        """
        return self.com_object.GetNbAngle(o_ang)

    def get_nb_guide(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbGuide(long oNum)
                |     Gets the number of guides curves.
                |     param : oNum Number of guide curves.

        :param int o_num:
        :return: None
        """
        return self.com_object.GetNbGuide(o_num)

    def get_nb_pos_angle(self, o_pos_ang: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbPosAngle(long oPosAng)
                |     Gets the number of numerical positioning parameters corresponding to angles
                |     from the default positions of the X axes.
                |     param : oPosAng Number of parameters

        :param int o_pos_ang:
        :return: None
        """
        return self.com_object.GetNbPosAngle(o_pos_ang)

    def get_nb_pos_coord(self, o_pos_coord: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbPosCoord(long oPosCoord)
                |     Gets the number of numerical positioning parameters corresponding to
                |     coordinates of the new axes systems origins.
                |     param oPosCoord Number of parameters

        :param int o_pos_coord:
        :return: None
        """
        return self.com_object.GetNbPosCoord(o_pos_coord)

    def get_pos_angle(self, ii: int) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPosAngle(long ii) As Angle
                |     Gets angles if both profile and first sweep plane axis systems from default
                |     positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             Index of numerical positioning coordinates in profile (value 1) or
                |             first sweep plane (value 2) axis system. 
                |         oElem
                |             Angle value. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :return: Angle
        """
        return Angle(self.com_object.GetPosAngle(ii))

    def get_pos_coord(self, ii: int) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPosCoord(long ii) As Length
                |     Gets translations coordinates if both profile axis system and first sweep
                |     plane axis system from default positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             Index of numerical positioning coordinates in profile (value 1 or
                |             2) or first sweep plane (value 3 or 4) axis system.
                |             
                |         oElem
                |             Coordinate value. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Length
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :return: Length
        """
        return Length(self.com_object.GetPosCoord(ii))

    def get_pos_direction(self, ii: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPosDirection(long ii) As Reference
                |     Gets the positioning directions : profile plane or first sweep plane X-axis direction.
                | 
                |     Parameters:
                | 
                |         iI
                |             Plane index : 1 for profile plane, 2 for first sweep plane. 
                |         oElem
                |             Direction element. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :return: Reference
        """
        return Reference(self.com_object.GetPosDirection(ii))

    def get_pos_point(self, ii: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPosPoint(long ii) As Reference
                |     Gets the points designated as the origins of the profile plane and first
                |     sweep plane.
                | 
                |     Parameters:
                | 
                |         iI
                |             Plane index : 1 for profile plane, 2 for first sweep plane. 
                |         oElem
                |             Origin point. return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Reference
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :return: Reference
        """
        return Reference(self.com_object.GetPosPoint(ii))

    def get_pos_swap_axes(self, ii: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPosSwapAxes(long ii) As long
                |     Gets axes inversion from previous definition for both profile plane and
                |     first sweep plane.
                | 
                |     Parameters:
                | 
                |         iI
                |             Axis system index (1 for profile plane, 2 for first sweep plane).
                |             
                |         oElem
                |             Inversion value:
                |             Inversion values :
                |             = 1 - CATGSMAxisInversionMode_None : no axis inverted.
                |             = 2 - CATGSMAxisInversionMode_X : only X axis inverted.
                |             = 3 - CATGSMAxisInversionMode_Y : only Y axis inverted.
                |             = 4 - CATGSMAxisInversionMode_Both : both axes inverted. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :return: int
        """
        return self.com_object.GetPosSwapAxes(ii)

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

    def is_sketch_axis_used_as_default(self, o_boolean: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub IsSketchAxisUsedAsDefault(boolean oBoolean)
                |     Queries status wherere Sketch axis used as default or not.
                |     In case of a sketch profile, specify if the 2D sketch axis must be used as
                |     default planar profile axis (for positioning purpose) or
                |     not.
                |     param oBoolean TRUE if the 2D sketch axis must be used, FALSE if not.

        :param bool o_boolean:
        :return: None
        """
        return self.com_object.IsSketchAxisUsedAsDefault(o_boolean)

    def remove_angle(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAngle()
                |     Removes an Angle.

        :return: None
        """
        return self.com_object.RemoveAngle()

    def remove_fitting_points(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveFittingPoints()
                |     Removes the fitting points.

        :return: None
        """
        return self.com_object.RemoveFittingPoints()

    def remove_guide(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveGuide()
                |     Removes a guide curve.

        :return: None
        """
        return self.com_object.RemoveGuide()

    def set_angle_ref(self, ii: int, elem: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngleRef(long ii,double Elem)
                |     Sets the angle value associated to the reference surface.
                | 
                |     Parameters:
                | 
                |         iI
                |             Angle value index (1: start value, 2: end value). 
                |         iElem
                |             Angle value. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param float elem:
        :return: None
        """
        return self.com_object.SetAngleRef(ii, elem)

    def set_fitting_points(self, ip_ia_elem_a: Reference, ip_ia_elem_b: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetFittingPoints(Reference ipIAElemA,Reference ipIAElemB)
                |     Sets the fitting points.
                |     Does not work with NULL_var values, Use RemoveFittingPoints() method
                |     instead.
                |     param ipIAElem1 Fitting point associated to the first guide (must not be
                |     equal to NULL_var)
                |     param ipIAElem2 Fitting point associated to the second guide (can be equal
                |     to NULL_var)

        :param Reference ip_ia_elem_a:
        :param Reference ip_ia_elem_b:
        :return: None
        """
        return self.com_object.SetFittingPoints(ip_ia_elem_a.com_object, ip_ia_elem_b.com_object)

    def set_guide_deviation(self, i_length: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetGuideDeviation(double iLength)
                |     Sets deviation value (length) from guide curves allowed during sweeping.
                |     operation in order to smooth it.
                |     param : iLength Numerical value.

        :param float i_length:
        :return: None
        """
        return self.com_object.SetGuideDeviation(i_length)

    def set_longitudinal_relimiters(self, ip_ia_elem_a: Reference, ip_ia_elem_b: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLongitudinalRelimiters(Reference ipIAElemA,Reference
                | ipIAElemB)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepExplicit#SetRelimiters Sets the elements
                |         relimiting the spine (or the default spine).
                |         param : ipIAElem1 First relimiting feature (plane or point)
                |         param : ipIAElem2 Second relimiting feature (plane or point)

        :param Reference ip_ia_elem_a:
        :param Reference ip_ia_elem_b:
        :return: None
        """
        return self.com_object.SetLongitudinalRelimiters(ip_ia_elem_a.com_object, ip_ia_elem_b.com_object)

    def set_pos_angle(self, ii: int, elem: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosAngle(long ii,double Elem)
                |     Sets angles if both profile and first sweep plane axis systems from default
                |     positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             Index of numerical positioning coordinates in profile (value 1) or
                |             first sweep plane (value 2) axis system. 
                |         iElem
                |             Angle value. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param float elem:
        :return: None
        """
        return self.com_object.SetPosAngle(ii, elem)

    def set_pos_coord(self, ii: int, elem: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosCoord(long ii,double Elem)
                |     Sets translations coordinates if both profile axis system and first sweep
                |     plane axis system from default positions.
                | 
                |     Parameters:
                | 
                |         iI
                |             Index of numerical positioning coordinates in profile (value 1 or
                |             2) or first sweep plane (value 3 or 4) axis system.
                |             
                |         iElem
                |             Coordinate value. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param float elem:
        :return: None
        """
        return self.com_object.SetPosCoord(ii, elem)

    def set_pos_direction(self, ii: int, elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosDirection(long ii,Reference Elem)
                |     Sets the positioning directions : profile plane or first sweep plane X-axis direction.
                | 
                |     Parameters:
                | 
                |         iI
                |             Plane index : 1 for profile plane, 2 for first sweep plane. 
                |         iElem
                |             Direction element. 
                | 
                |     See also:
                |         Reference
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param Reference elem:
        :return: None
        """
        return self.com_object.SetPosDirection(ii, elem.com_object)

    def set_pos_point(self, ii: int, elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosPoint(long ii,Reference Elem)
                |     Sets the points designated as the origins of the profile plane and first
                |     sweep plane.
                | 
                |     Parameters:
                | 
                |         iI
                |             Plane index : 1 for profile plane, 2 for first sweep plane. 
                |         iElem
                |             Origin point. 
                | 
                |     See also:
                |         Reference
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param Reference elem:
        :return: None
        """
        return self.com_object.SetPosPoint(ii, elem.com_object)

    def set_pos_swap_axes(self, ii: int, elem: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPosSwapAxes(long ii,long Elem)
                |     Sets axes inversion from previous definition for both profile plane and
                |     first sweep plane.
                | 
                |     Parameters:
                | 
                |         iI
                |             Axis system index (1 for profile plane, 2 for first sweep plane).
                |             
                |         iElem
                |             Inversion value:
                | 
                |             Inversion values :
                |             = 1 - CATGSMAxisInversionMode_None : no axis inverted.
                |             = 2 - CATGSMAxisInversionMode_X : only X axis inverted.
                |             = 3 - CATGSMAxisInversionMode_Y : only Y axis inverted.
                |             = 4 - CATGSMAxisInversionMode_Both : both axes inverted. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param int ii:
        :param int elem:
        :return: None
        """
        return self.com_object.SetPosSwapAxes(ii, elem)

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

    def set_smooth_angle_threshold(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSmoothAngleThreshold(double iAngle)
                |     Sets angular threshold.
                |     param : iAngle Numerical value.

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetSmoothAngleThreshold(i_angle)

    def use_sketch_axis_as_default(self, i_boolean: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub UseSketchAxisAsDefault(boolean iBoolean)
                |     Uses Sketch Axis As Default.
                |     In case of a sketch profile, specify if the 2D sketch axis must be used as
                |     default planar profile axis (for positioning purpose) or
                |     not.
                |     param iBoolean TRUE if the 2D sketch axis must be used, FALSE if not.

        :param bool i_boolean:
        :return: None
        """
        return self.com_object.UseSketchAxisAsDefault(i_boolean)

    def __repr__(self):
        return f'HybridShapeSweepExplicit(name="{ self.name }")'
