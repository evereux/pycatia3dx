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


class HybridShapeSweepConic(HybridShapeSweep):

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
                |                             HybridShapeSweepConic
                | 
                | Represents the hybrid shape conic sweep feature.
                | Role: To access the data of the conic sweep feature .
                | 
                | Use the HybridShapeFactory.AddNewSweepConic to create a HybridShapeConicSweep
                | object.
    
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
    def fifth_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FifthGuideCrv() As Reference
                |     Returns or sets the fifth guide curve.

        :return: Reference
        """

        return Reference(self.com_object.FifthGuideCrv)

    @fifth_guide_crv.setter
    def fifth_guide_crv(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FifthGuideCrv = value

    @property
    def first_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstGuideCrv() As Reference
                |     Returns or sets the first guide curve.

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
    def fourth_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FourthGuideCrv() As Reference
                |     Returns or sets the fourth guide curve.

        :return: Reference
        """

        return Reference(self.com_object.FourthGuideCrv)

    @fourth_guide_crv.setter
    def fourth_guide_crv(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FourthGuideCrv = value

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
                |     Gives the information on performing smoothinh during sweeping
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
    def parameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Parameter() As double
                |     Returns or sets the parameter for conic sweep operation.
                |     if the parameter is a law, the method returns FALSE see
                |     HybridShapeLawDistProj

        :return: float
        """

        return self.com_object.Parameter

    @parameter.setter
    def parameter(self, value: float):
        """
        :param float value:
        """

        self.com_object.Parameter = value

    @property
    def parameter_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ParameterLaw() As Reference
                |     Returns or sets the parameter law useful in conic sweep operation.

        :return: Reference
        """

        return Reference(self.com_object.ParameterLaw)

    @parameter_law.setter
    def parameter_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ParameterLaw = value

    @property
    def parameter_law_inversion(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ParameterLawInversion() As boolean
                |     Returns or sets the parameter law inversion flag of conic sweep
                |     operation.
                |     TRUE if parameter law is inverted. Else it is FALSE. see
                |     HybridShapeLawDistProj

        :return: bool
        """

        return self.com_object.ParameterLawInversion

    @parameter_law_inversion.setter
    def parameter_law_inversion(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ParameterLawInversion = value

    @property
    def parameter_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ParameterLawType() As long
                |     Returns or sets the parameter law type in conic sweep operation.

        :return: int
        """

        return self.com_object.ParameterLawType

    @parameter_law_type.setter
    def parameter_law_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ParameterLawType = value

    @property
    def second_guide_crv(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondGuideCrv() As Reference
                |     Returns or sets the second guide curve.

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
                |     Returns angular threshold under which discontinuities .
                |     moving frame,tangency net on reference surface will be smoothed when
                |     sweeping.

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
                |     Returns or sets the spine (optional) for sweep operation.
                |     param : oElem Spine curve.
                | 
                |     See also:
                |         Reference

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
                |     Returns or sets the third guide curve.

        :return: Reference
        """

        return Reference(self.com_object.ThirdGuideCrv)

    @third_guide_crv.setter
    def third_guide_crv(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ThirdGuideCrv = value

    def get_longitudinal_relimiters(self, op_ia_elem1: Reference, op_ia_elem2: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetLongitudinalRelimiters(Reference opIAElem1,Reference
                | opIAElem2)
                | 
                |     Deprecated:
                |         V5R16 CATHybridShapeSweepConic#GetRelimiters Gets the elements
                |         relimiting the spine (or the default spine).
                |         param : opIAElem1 First relimiting feature (plane or point)
                |         param : opIAElem2 Second relimiting feature (plane or point)

        :param Reference op_ia_elem1:
        :param Reference op_ia_elem2:
        :return: None
        """
        return self.com_object.GetLongitudinalRelimiters(op_ia_elem1.com_object, op_ia_elem2.com_object)

    def get_nb_guides(self, o_num: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetNbGuides(long oNum)
                |     Gets the number of guides.
                |     param : oNum Number of guides curve.

        :param int o_num:
        :return: None
        """
        return self.com_object.GetNbGuides(o_num)

    def get_parameter_law(self, o_param_start: float, o_param_end: float, o_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetParameterLaw(double oParamStart,double oParamEnd,long
                | oLawType)
                |     Gets the parameter law used in conic sweep operation.
                |     param : oParamStart Parameter law start value.
                |     param : oParamEnd Parameter law end value.
                |     param : oLawType Parameter law type.

        :param float o_param_start:
        :param float o_param_end:
        :param int o_law_type:
        :return: None
        """
        return self.com_object.GetParameterLaw(o_param_start, o_param_end, o_law_type)

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

    def get_tangency(self, op_ia_elem: Reference, op_ia_angle_start: Angle, op_ia_angle_end: Angle, o_law_type: int, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetTangency(Reference opIAElem,Angle opIAAngleStart,Angle opIAAngleEnd,long
                | oLawType,long iIndex)
                |     Gets tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : opIAElem
                |     param : opIAAngleStart Start tangency angle from surface or curve reference.
                |     param : opIAAngleEnd End tangency angle from surface or curve reference.
                |     param : oLawType Type of law used for tangency angle from surface or curve reference.
                |     param : iIndex Guide curve index : 1 to 5.

        :param Reference op_ia_elem:
        :param Angle op_ia_angle_start:
        :param Angle op_ia_angle_end:
        :param int o_law_type:
        :param int i_index:
        :return: None
        """
        return self.com_object.GetTangency(op_ia_elem.com_object, op_ia_angle_start.com_object, op_ia_angle_end.com_object, o_law_type, i_index)

    def get_tangency_angle_law_inversion(self, i_index: int, o_inversion: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetTangencyAngleLawInversion(long iIndex,long oInversion)
                |     Gets information whether tangency angle law has to be inverted or not for a
                |     specified guide curve.
                |     param : iIndex Guide curve index : 1 to 5
                |     param : oInversion Non-Zero for TRUE and 0 for FALSE.

        :param int i_index:
        :param int o_inversion:
        :return: None
        """
        return self.com_object.GetTangencyAngleLawInversion(i_index, o_inversion)

    def get_tangency_law(self, op_ia_elem: Reference, op_ia_law: Reference, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetTangencyLaw(Reference opIAElem,Reference opIALaw,long
                | iIndex)
                |     Gets tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : opIAElem Tangency surface or curve feature.
                |     param : opIALaw Start tangency angle from surface or curve reference.
                |     param : iIndex Guide curve index : 1 to 5.

        :param Reference op_ia_elem:
        :param Reference op_ia_law:
        :param int i_index:
        :return: None
        """
        return self.com_object.GetTangencyLaw(op_ia_elem.com_object, op_ia_law.com_object, i_index)

    def remove_guide(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveGuide(long iIndex)
                |     Removes a guide curve given its index.
                |     it removes also tangency element if specified.
                |     param : iIndex Guide curve index : 1 to 5. If 0, all guides are removed.

        :param int i_index:
        :return: None
        """
        return self.com_object.RemoveGuide(i_index)

    def remove_parameter(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveParameter()
                |     Removes conical sweep parameter, whether it is a single value or a law.

        :return: None
        """
        return self.com_object.RemoveParameter()

    def remove_tangency(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveTangency(long iIndex)
                |     removes tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : iIndex Guide curve index : 1 to 5.

        :param int i_index:
        :return: None
        """
        return self.com_object.RemoveTangency(i_index)

    def set_guide_deviation(self, i_length: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetGuideDeviation(double iLength)
                |     Sets deviation value (length) from guide curves allowed during sweeping
                |     operation in order to smooth it.
                |     param : iLength Numerical value.

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
                |         V5R16 CATHybridShapeSweepConic#SetRelimiters Sets the elements
                |         relimiting the spine (or the default spine).
                |         param : ipIAElem1 First relimiting feature (plane or point)
                |         param : ipIAElem2 Second relimiting feature (plane or point)

        :param Reference ip_ia_elem1:
        :param Reference ip_ia_elem2:
        :return: None
        """
        return self.com_object.SetLongitudinalRelimiters(ip_ia_elem1.com_object, ip_ia_elem2.com_object)

    def set_parameter_law(self, i_param_start: float, i_param_end: float, i_law_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetParameterLaw(double iParamStart,double iParamEnd,long
                | iLawType)
                |     Sets the parameter law that will be used in conic sweep
                |     operation.
                |     param : iParamStart Parameter law start value.
                |     param : iParamEnd Parameter law end value.
                |     param : iLawType Parameter law type.

        :param float i_param_start:
        :param float i_param_end:
        :param int i_law_type:
        :return: None
        """
        return self.com_object.SetParameterLaw(i_param_start, i_param_end, i_law_type)

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
                |     Sets angular threshold under which discontinuities.
                |     note: moving frame,tangency net on reference surface will be smoothed when
                |     sweeping.
                |     param : iAngle Numerical value.

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetSmoothAngleThreshold(i_angle)

    def set_tangency(self, ip_ia_elem: Reference, i_angle_start: float, i_angle_end: float, ilaw_type: int, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTangency(Reference ipIAElem,double iAngleStart,double iAngleEnd,long
                | ilawType,long iIndex)
                |     Sets tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : ipIAElem Tangency surface or curve feature.
                |     param : iAngleStart Start tangency angle from surface or curve reference.
                |     param : iAngleEnd End tangency angle from surface or curve reference.
                |     param : iAngleLawType Type of law used for tangency angle from surface or curve reference.
                |     param : iIndex Guide curve index : 1 to 5.

        :param Reference ip_ia_elem:
        :param float i_angle_start:
        :param float i_angle_end:
        :param int ilaw_type:
        :param int i_index:
        :return: None
        """
        return self.com_object.SetTangency(ip_ia_elem.com_object, i_angle_start, i_angle_end, ilaw_type, i_index)

    def set_tangency_angle_law_inversion(self, i_index: int, i_inversion: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTangencyAngleLawInversion(long iIndex,long iInversion)
                |     Sets information whether tangency angle law has to be inverted or not for a
                |     specified guide curve.
                |     param : iIndex Guide curve index : 1 to 5
                |     param : iInversion 1 for TRUE and 0 for FALSE.

        :param int i_index:
        :param int i_inversion:
        :return: None
        """
        return self.com_object.SetTangencyAngleLawInversion(i_index, i_inversion)

    def set_tangency_law(self, ip_ia_elem: Reference, ip_ia_law: Reference, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTangencyLaw(Reference ipIAElem,Reference ipIALaw,long
                | iIndex)
                |     Sets tangency surface or curve and its angle given the guide curve
                |     index.
                |     param : ipIAElem Tangency surface or curve feature.
                |     param : ipIALaw Start tangency angle from surface or curve reference.
                |     param : iIndex Guide curve index : 1 to 5.

        :param Reference ip_ia_elem:
        :param Reference ip_ia_law:
        :param int i_index:
        :return: None
        """
        return self.com_object.SetTangencyLaw(ip_ia_elem.com_object, ip_ia_law.com_object, i_index)

    def __repr__(self):
        return f'HybridShapeSweepConic(name="{ self.name }")'
