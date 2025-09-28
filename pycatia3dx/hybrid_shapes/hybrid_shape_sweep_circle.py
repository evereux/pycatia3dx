"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_sweep import HybridShapeSweep
from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapeSweepCircle(HybridShapeSweep):

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
                |                             HybridShapeSweepCircle
                | 
                | Represents the hybrid shape sweep circle feature object.
                | Role: To access the data of the hybrid shape sweep circle feature
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
    def choice_no(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ChoiceNo() As long
                |     Returns or sets the choice number, which corresponds to each solution of a
                |     given circular sweep case.
                |     For example: a circular sweep with two guide curves and a radius leads to
                |     four possible solutions.

        :return: int
        """

        return self.com_object.ChoiceNo

    @choice_no.setter
    def choice_no(self, value: int):
        """
        :param int value:
        """

        self.com_object.ChoiceNo = value

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
    def first_angle_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstAngleLaw() As Reference
                |     Returns or sets the first angle law useful in some circular sweep types.

        :return: Reference
        """

        return Reference(self.com_object.FirstAngleLaw)

    @first_angle_law.setter
    def first_angle_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstAngleLaw = value

    @property
    def first_angle_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstAngleLawInversion() As long
                |     Returns or sets the first angle law inversion information.

        :return: int
        """

        return self.com_object.FirstAngleLawInversion

    @first_angle_law_inversion.setter
    def first_angle_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.com_object.FirstAngleLawInversion = value

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
                |     Returns or sets information whether a deviation from guide curves is
                |     allowed or not.
                |     Gives the information on performing smoothing during sweeping
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
                |     Returns or sets the circular sweep mode.
                |     Legal mode values are:
                |     0 Undefined circular profile swept surface
                |     (CATGSMCircularSweep_None)
                |     2 Circular profile swept surface defined by three guide curves (4
                |     solutions) (CATGSMCircularSweep_ThreeGuides)
                |     3 Circular profile swept surface defined by a center curve and a reference
                |     curve (for angles and radius)
                |     (CATGSMCircularSweep_TwoGuidesAndRadius)
                |     5 Circular profile swept surface defined by a center curve and a reference
                |     curve (for angles and radius)
                |     (CATGSMCircularSweep_CenterAndAngleCurve)
                |     6 Circular profile swept surface defined by a center curve and a radius
                |     (CATGSMCircularSweep_CenterAndRadius)
                |     7 Circular profile swept surface defined by two guide curves with a
                |     tangency condition on the second one (with reference surface)
                |     (CATGSMCircularSweep_TwoGuidesAndTangency)
                |     8 Circular profile swept surface defined by a guide curve, a radius and a
                |     tangency surface
                |     (CATGSMCircularSweep_GuideAndTangencyAndRadius)

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
    def radius_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RadiusLaw() As Reference
                |     Returns or sets the radius law feature.

        :return: Reference
        """

        return Reference(self.com_object.RadiusLaw)

    @radius_law.setter
    def radius_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RadiusLaw = value

    @property
    def radius_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RadiusLawInversion() As long
                |     Returns or sets the radius law inversion information.

        :return: int
        """

        return self.com_object.RadiusLawInversion

    @radius_law_inversion.setter
    def radius_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.com_object.RadiusLawInversion = value

    @property
    def radius_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RadiusLawType() As long
                |     Returns or sets the radius law type.

        :return: int
        """

        return self.com_object.RadiusLawType

    @radius_law_type.setter
    def radius_law_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.RadiusLawType = value

    @property
    def reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Reference() As Reference
                |     Returns or sets the reference (functional curve or guide surface).

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
    def second_angle_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondAngleLaw() As Reference
                |     Returns or sets the second angle law useful in some circular sweep types.

        :return: Reference
        """

        return Reference(self.com_object.SecondAngleLaw)

    @second_angle_law.setter
    def second_angle_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondAngleLaw = value

    @property
    def second_angle_law_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondAngleLawInversion() As long
                |     Returns or sets the second angle law inversion information.

        :return: int
        """

        return self.com_object.SecondAngleLawInversion

    @second_angle_law_inversion.setter
    def second_angle_law_inversion(self, value: int):
        """
        :param int value:
        """

        self.com_object.SecondAngleLawInversion = value

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
    def smooth_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SmoothActivity() As boolean
                |     Returns or sets information whether a sweeping operation is smoothed or
                |     not.
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
    def third_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ThirdGuideCrv() As Reference
                |     Returns or sets the sweep operation third guide curve.

        :return: Reference
        """

        return Reference(self.com_object.ThirdGuideCrv)

    @third_guide_crv.setter
    def third_guide_crv(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ThirdGuideCrv = value

    @property
    def trim_option(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TrimOption() As long
                |     Returns or sets the trim option status.
                |     The trim option status legal values are:
                |     0 No trim computed or undefined
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

    def get_angle(self, i_i: int) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetAngle(long iI) As Angle
                |     Returns the angle values useful in some circular sweep
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

    def get_angle_law_types(self, o_first_type: int, o_second_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetAngleLawTypes(long oFirstType,long oSecondType)
                |     Retrieves angle law types.
                | 
                |     Parameters:
                | 
                |         oFirstType
                |             The first type of law (from CATGSMBasicLawType
                |             enumeration).
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)
                |         oSecondType
                |             The second type of law (from CATGSMBasicLawType
                |             enumeration).
                |             Same legal values as oFirstType

        :param int o_first_type:
        :param int o_second_type:
        :return: None
        """
        return self.com_object.GetAngleLawTypes(o_first_type, o_second_type)

    def get_first_angle_law(self, o_elem1: Angle, o_elem2: Angle, ol_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetFirstAngleLaw(Angle oElem1,Angle oElem2,long olLawType)
                |     Retrieves the first angle law useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         oElem1
                |             The angle law start value 
                |         oElem2
                |             The angle law end value 
                |         olLawType
                |             The angle law type

        :param Angle o_elem1:
        :param Angle o_elem2:
        :param int ol_law_type:
        :return: None
        """
        return self.com_object.GetFirstAngleLaw(o_elem1.com_object, o_elem2.com_object, ol_law_type)

    def get_longitudinal_relimiters(self, op_ia_elem1: Reference, op_ia_elem2: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetLongitudinalRelimiters(Reference opIAElem1,Reference
                | opIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepCircle#GetRelimiters Retrieves the elements
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

    def get_nb_guide(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbGuide(long oNum)
                |     Retrieves the number of guide curves.
                | 
                |     Parameters:
                | 
                |         oNum
                |             The number of guide curves

        :param int o_num:
        :return: None
        """
        return self.com_object.GetNbGuide(o_num)

    def get_nb_radius(self, o_rad: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbRadius(long oRad)
                |     Retrieves the number of radii.
                | 
                |     Parameters:
                | 
                |         oRad
                |             The number of radii

        :param int o_rad:
        :return: None
        """
        return self.com_object.GetNbRadius(o_rad)

    def get_radius(self, i_i: int) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetRadius(long iI) As Length
                |     Returns the radius value useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The radius value index (1: start value, 2: end value)
                |             
                | 
                |     Returns:
                |         The radius value

        :param int i_i:
        :return: Length
        """
        return Length(self.com_object.GetRadius(i_i))

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

    def get_second_angle_law(self, o_elem1: Angle, o_elem2: Angle, ol_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetSecondAngleLaw(Angle oElem1,Angle oElem2,long
                | olLawType)
                |     Retrieves the second angle law useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         oElem1
                |             The angle law start value 
                |         oElem2
                |             The angle law end value 
                |         olLawType
                |             The angle law type

        :param Angle o_elem1:
        :param Angle o_elem2:
        :param int ol_law_type:
        :return: None
        """
        return self.com_object.GetSecondAngleLaw(o_elem1.com_object, o_elem2.com_object, ol_law_type)

    def get_tangency_choice_no(self, o_no: int, o_shell_ori: int, o_guide_ori: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetTangencyChoiceNo(long oNo,long oShellOri,long
                | oGuideOri)
                |     Retrieves a sequence which identifies a solution among all possibilities of
                |     a circular profile sweep tangent to a surface. (case
                |     CATGSMCircularSweep_GuideAndTangencyAndRadius).
                | 
                |     Parameters:
                | 
                |         oNo
                |             Given the orientations, solution number in a distance ordered list.
                |             
                |         oShellOri
                |             This orientation allows to compute just the results that are
                |             tangent to a specific side of the shell. It can take three
                |             values:
                |             +1 The result is on the normal side of the shell
                |             -1 The result is on the side of the shell opposite to the
                |             normal
                |             0 No orientation is specified
                |         oGuideOri
                |             This orientation allows to compute just the results that are on the
                |             "left" or the "right" side of the shell, when looking in the guide direction.
                |             It can take three values:
                |             +1 The result is on the "left" side
                |             -1 The result is on the "right" side
                |             0 No orientation is specified

        :param int o_no:
        :param int o_shell_ori:
        :param int o_guide_ori:
        :return: None
        """
        return self.com_object.GetTangencyChoiceNo(o_no, o_shell_ori, o_guide_ori)

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

    def remove_radius(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveRadius()
                |     Removes a radius.

        :return: None
        """
        return self.com_object.RemoveRadius()

    def set_angle(self, i_i: int, i_elem: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngle(long iI,double iElem)
                |     Sets the angle values useful in some circular sweep types.
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

    def set_angle_law_types(self, i_first_type: int, i_second_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngleLawTypes(long iFirstType,long iSecondType)
                |     Sets angle law types.
                | 
                |     Parameters:
                | 
                |         iFirstType
                |             The first type of law (from CATGSMBasicLawType
                |             enumeration).
                |             Legal values:
                |             0 Undefined law type (CATGSMBasicLawType_None)
                |             1 Constant law type (CATGSMBasicLawType_Constant)
                |             2 Linear law type (CATGSMBasicLawType_Linear)
                |             3 S law type (CATGSMBasicLawType_SType)
                |             4 Law specified by a GSD law feature
                |             (CATGSMBasicLawType_Advanced)
                |         iSecondType
                |             The second type of law (from CATGSMBasicLawType
                |             enumeration).
                |             Same legal values as iFirstType

        :param int i_first_type:
        :param int i_second_type:
        :return: None
        """
        return self.com_object.SetAngleLawTypes(i_first_type, i_second_type)

    def set_first_angle_law(self, i_elem1: float, i_elem2: float, il_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetFirstAngleLaw(double iElem1,double iElem2,long
                | ilLawType)
                |     Sets the first angle law useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iElem1
                |             The angle law start value 
                |         iElem2
                |             The angle law end value 
                |         ilLawType
                |             The angle law type

        :param float i_elem1:
        :param float i_elem2:
        :param int il_law_type:
        :return: None
        """
        return self.com_object.SetFirstAngleLaw(i_elem1, i_elem2, il_law_type)

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

    def set_longitudinal_relimiters(self, ip_ia_elem1: Reference, ip_ia_elem2: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetLongitudinalRelimiters(Reference ipIAElem1,Reference
                | ipIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepCircle#SetRelimiters Sets the elements
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

    def set_radius(self, i_i: int, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetRadius(long iI,double iRadius)
                |     Sets the radius value useful in some circular sweep types.
                | 
                |     Parameters:
                | 
                |         iI
                |             The radius value index (1: start value, 2: end value)
                |             
                |         iRadius
                |             The radius value

        :param int i_i:
        :param float i_radius:
        :return: None
        """
        return self.com_object.SetRadius(i_i, i_radius)

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

    def set_second_angle_law(self, i_elem1: float, i_elem2: float, il_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSecondAngleLaw(double iElem1,double iElem2,long
                | ilLawType)
                |     Sets the second angle law useful in some circular sweep
                |     types.
                | 
                |     Parameters:
                | 
                |         iElem1
                |             The angle law start value 
                |         iElem2
                |             The angle law end value 
                |         ilLawType
                |             Tha angle law type

        :param float i_elem1:
        :param float i_elem2:
        :param int il_law_type:
        :return: None
        """
        return self.com_object.SetSecondAngleLaw(i_elem1, i_elem2, il_law_type)

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
                |             The angular threshold

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetSmoothAngleThreshold(i_angle)

    def set_tangency_choice_no(self, i_shell_ori: int, i_guide_ori: int, i_no: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTangencyChoiceNo(long iShellOri,long iGuideOri,long
                | iNo)
                |     Sets a sequence which identifies a solutionamong all possibilities of a
                |     circular profile sweep tangent to a surface.
                | 
                |     Parameters:
                | 
                |         iNo
                |             Given the orientations, solution number in a distance ordered list.
                |             
                |         iShellOri
                |             This orientation allows to compute just the results that are
                |             tangent to a specific side of the shell. It can take three
                |             values:
                |             +1 The result is on the normal side of the shell
                |             -1 The result is on the side of the shell opposite to the
                |             normal
                |             0 No orientation is specified
                |         iGuideOri
                |             This orientation allows to compute just the results that are on the
                |             "left" or the "right" side of the shell, when looking in the guide direction.
                |             It can take three values:
                |             +1 The result is on the "left" side
                |             -1 The result is on the "right" side
                |             0 No orientation is specified

        :param int i_shell_ori:
        :param int i_guide_ori:
        :param int i_no:
        :return: None
        """
        return self.com_object.SetTangencyChoiceNo(i_shell_ori, i_guide_ori, i_no)

    def __repr__(self):
        return f'HybridShapeSweepCircle(name="{ self.name }")'
