"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeCurveSmooth(HybridShape):

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
                |                         HybridShapeCurveSmooth
                | 
                | Represents the hybrid shape curve smoothing operation feature.
                | Role: To access the data of the curve smoothing operation.of the hybrid shape
                | curve parameter object. This data includes:
                | 
                |     The curve to smooth
                |     The support (if exist )
                |     The tangent tolerance value (threshold)
                |     The curvature tolerance value (threshold)
                |     The info if curvature threshold is activated
                |     The maximum deviation accepted
                |     The info if maxcimum deviation is activated
                |     The fixed points
                |     The fixed segments
                |     The info if topology simplification is activated
                | 
                | Use the HybridShapeFactory.AddNewCurveSmooth to create a HybridShapeCurveSmooth
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def correction_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CorrectionMode() As long
                |     Returns or sets the correction mode (threshold, point, tangency or
                |     curvature) applied to the smoothed curve.
                |     Legal values:
                | 
                |     0
                |         CATGSMCSCorrectionMode_Threshold. no continuity 
                |     1
                |         CATGSMCSCorrectionMode_Point. continuity in point
                |         (C0).
                |     2
                |         CATGSMCSCorrectionMode_Tangency. continuity in tangency
                |         (C1).
                |     3
                |         CATGSMCSCorrectionMode_Curvature. continuity in curvature
                |         (C2).
                | 
                | Example:
                |     This example retrieves in oMode the correction mode for the
                |     hybShpCurveSmooth hybrid shape feature.
                | 
                |      oMode = hybShpCurveSmooth.CorrectionMode

        :return: int
        """

        return self.com_object.CorrectionMode

    @correction_mode.setter
    def correction_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.CorrectionMode = value

    @property
    def curvature_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CurvatureThreshold() As double
                |     Returns or sets the CurvatureThreshold.
                | 
                |     Example: This example retrieves the CurvatureThreshold of the
                |     hybShpCurveSmooth in CurvatureThH.
                | 
                |      Dim CurvatureThH as double
                |      CurvatureThH = hybShpCurvePar.CurvatureThreshold

        :return: float
        """

        return self.com_object.CurvatureThreshold

    @curvature_threshold.setter
    def curvature_threshold(self, value: float):
        """
        :param float value:
        """

        self.com_object.CurvatureThreshold = value

    @property
    def curvature_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CurvatureThresholdActivity() As boolean
                |     Returns or sets the CurvatureThresholdActivity.
                | 
                |     Example: This example retrieves the CurvatureThresholdActivity of the
                |     hybShpCurveSmooth in CurvatureActivity .
                | 
                |      Dim CurvatureActivity as boolean 
                |      CurvatureActivity = hybShpCurvePar.CurvatureThresholdActivity

        :return: bool
        """

        return self.com_object.CurvatureThresholdActivity

    @curvature_threshold_activity.setter
    def curvature_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CurvatureThresholdActivity = value

    @property
    def curve_to_smooth(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CurveToSmooth() As Reference
                |     Returns or sets the curve to smooth.
                | 
                |     Example: This example retrieves the curve to smooth object of the
                |     hybShpCurveSmooth in Curve.
                | 
                |      Dim Curve as CATIAReference 
                |      Curve  = hybShpCurvePar.CurveToSmooth

        :return: Reference
        """

        return Reference(self.com_object.CurveToSmooth)

    @curve_to_smooth.setter
    def curve_to_smooth(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.CurveToSmooth = value

    @property
    def end_extremity_continuity(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndExtremityContinuity() As long
                |     Returns or sets the continuity condition (curvature, tangency or point)
                |     applied to the smoothed curve with regard to the input curve at the end
                |     extremity of the input curve.
                |     Legal values:
                | 
                |     0
                |         CATGSMContinuity_Point. continuity in point (C0). 
                |     1
                |         CATGSMContinuity_Tangency. continuity in tangency
                |         (C1).
                |     2
                |         CATGSMContinuity_Curvature. continuity in curvature
                |         (C2).
                | 
                | Example:
                |     This example retrieves in oContinuity the continuity at the end extremity
                |     for the hybShpCurveSmooth hybrid shape feature.
                | 
                |      oContinuity = hybShpCurveSmooth.EndExtremityContinuity

        :return: int
        """

        return self.com_object.EndExtremityContinuity

    @end_extremity_continuity.setter
    def end_extremity_continuity(self, value: int):
        """
        :param int value:
        """

        self.com_object.EndExtremityContinuity = value

    @property
    def maximum_deviation(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property MaximumDeviation() As Length (Read Only)
                |     Returns the MaximumDeviation.
                | 
                |     Example: This example retrieves the MaximumDeviation of the
                |     hybShpCurveSmooth in MaximumDeviationVal.
                | 
                |      Dim MaximumDeviationVal as CATIALength
                |      MaximumDeviationVal  = hybShpCurvePar.MaximumDeviation

        :return: Length
        """

        return Length(self.com_object.MaximumDeviation)

    @property
    def maximum_deviation_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property MaximumDeviationActivity() As boolean
                |     Returns or sets the MaximumDeviationActivity.
                | 
                |     Example: This example retrieves the MaximumDeviationActivity of the
                |     hybShpCurveSmooth in MaxActivity .
                | 
                |      Dim MaxActivity as boolean
                |      MaxActivity  = hybShpCurvePar.MaximumDeviationActivity

        :return: bool
        """

        return self.com_object.MaximumDeviationActivity

    @maximum_deviation_activity.setter
    def maximum_deviation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MaximumDeviationActivity = value

    @property
    def start_extremity_continuity(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property StartExtremityContinuity() As long
                |     Returns or sets the continuity condition (curvature, tangency or point)
                |     applied to the smoothed curve with regard to the input curve at the start
                |     extremity of the input curve.
                |     Legal values:
                | 
                |     0
                |         CATGSMContinuity_Point. continuity in point (C0). 
                |     1
                |         CATGSMContinuity_Tangency. continuity in tangency
                |         (C1).
                |     2
                |         CATGSMContinuity_Curvature. continuity in curvature
                |         (C2).
                | 
                | Example:
                |     This example retrieves in oContinuity the continuity at the start extremity
                |     for the hybShpCurveSmooth hybrid shape feature.
                | 
                |      oContinuity = hybShpCurveSmooth.StartExtremityContinuity

        :return: int
        """

        return self.com_object.StartExtremityContinuity

    @start_extremity_continuity.setter
    def start_extremity_continuity(self, value: int):
        """
        :param int value:
        """

        self.com_object.StartExtremityContinuity = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the support of the curve.
                |     if Suppport == nothing no support associated to the curve
                | 
                |     Example: This example retrieves the support of curve to smooth object of
                |     the hybShpCurveSmooth in Support.
                | 
                |      Dim Support  as CATIAReference 
                |      Support   = ybShpCurveSmooth.Support

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    @property
    def tangency_threshold(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TangencyThreshold() As Angle (Read Only)
                |     Returns the TangencyThreshold.
                | 
                |     Example: This example retrieves the curve to smooth object of the
                |     hybShpCurveSmooth in AngleThH.
                | 
                |      Dim Curve as CATIAAngle  
                |      AngleThH  = ybShpCurveSmooth.TangencyThreshold

        :return: Angle
        """

        return Angle(self.com_object.TangencyThreshold)

    @property
    def topology_simplification_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TopologySimplificationActivity() As boolean
                |     Returns or sets the TopologySimplificationActivity.
                | 
                |     Example: This example retrieves the TopologySimplificationActivity of the
                |     hybShpCurveSmooth in TopSimplifyAct.
                | 
                |      Dim TopSimplifyAct as boolean 
                |      TopSimplifyAct  = hybShpCurvePar.TogologySimplificationActivity

        :return: bool
        """

        return self.com_object.TopologySimplificationActivity

    @topology_simplification_activity.setter
    def topology_simplification_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TopologySimplificationActivity = value

    def add_frozen_curve_segment(self, i_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddFrozenCurveSegment(Reference iCurve)
                |     Adds a frozen curve to the hybrid shape curve smooth feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iCurve
                |             The curve to be added to the hybrid shape curve smooth feature
                |             object. 
                | 
                |     Example:
                |         The following example adds the iCurve curve to the hybShpCurveSmooth
                |         object.
                | 
                |          hybShpCurveSmooth.AddFrozenCurveSegment iCurve

        :param Reference i_curve:
        :return: None
        """
        return self.com_object.AddFrozenCurveSegment(i_curve.com_object)

    def add_frozen_point(self, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddFrozenPoint(Reference iPoint)
                |     Adds a frozen points to the hybrid shape curve smooth feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The frozen point to be added to the hybrid shape curve smooth
                |             feature object. 
                | 
                |     Example:
                |         The following example adds the iPoint frozen point to the
                |         hybShpCurveSmooth object.
                | 
                |          hybShpCurveSmooth.AddFrozenPoint iPoint

        :param Reference i_point:
        :return: None
        """
        return self.com_object.AddFrozenPoint(i_point.com_object)

    def get_frozen_curve_segment(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetFrozenCurveSegment(long iPos) As Reference
                |     Retrieves the Frozen Curve Segment at specified position in the hybrid
                |     shape curve smooth object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the Frozen Curve Segment to retrieve.
                |             
                | 
                |     Example:
                |         The following example gets the oCurve Frozen Curve Segment of the
                |         hybShpCurveSmooth object at the position iPos.
                | 
                |          Dim oCurve As Reference
                |          Set oCurve = hybShpCurveSmooth.GetFrozenCurveSegment (iPos).

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.GetFrozenCurveSegment(i_pos))

    def get_frozen_curve_segments_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetFrozenCurveSegmentsSize() As long
                |     Returns the number of frozen curve segments in the curve smooth
                |     object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of frozen curve segments in the curve
                |             smooth.
                | 
                |             Example:
                |                 This example retrieves the number of frozen curve segments. in
                |                 the hybShpCurveSmooth hybrid shape curve
                |                 smooth.
                | 
                |                  Dim oSize As  long
                |                  oSize = hybShpCurveSmooth.GetFrozenCurveSegmentsSize

        :return: int
        """
        return self.com_object.GetFrozenCurveSegmentsSize()

    def get_frozen_point(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetFrozenPoint(long iPos) As Reference
                |     Retrieves the Frozen Point at specified position in the hybrid shape curve
                |     smooth object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the Frozen Point to retrieve. 
                | 
                |     Example:
                |         The following example gets the oPoint Frozen Point of the
                |         hybShpCurveSmooth object at the position iPos.
                | 
                |          Dim oPoint As Reference
                |          Set oPoint = hybShpCurveSmooth.GetFrozenPoint (iPos).

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.GetFrozenPoint(i_pos))

    def get_frozen_points_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetFrozenPointsSize() As long
                |     Returns the number of Frozen Points in the curve smooth
                |     object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of Frozen Points in the curve smooth.
                | 
                |             Example:
                |                 This example retrieves the number of Frozen Points. in the
                |                 hybShpCurveSmooth hybrid shape curve smooth.
                | 
                |                  Dim oSize As  long
                |                  oSize = hybShpCurveSmooth.GetFrozenPointsSize

        :return: int
        """
        return self.com_object.GetFrozenPointsSize()

    def remove_all_frozen_curve_segments(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllFrozenCurveSegments()
                |     Removes all Frozen Curve Segment of the hybrid shape curve smooth object.
                |     
                | Example:
                |     The following example removes all Frozen Curve Segments of the
                |     hybShpCurveSmooth object.
                | 
                |      hybShpCurveSmooth.RemoveAllFrozenCurveSegments

        :return: None
        """
        return self.com_object.RemoveAllFrozenCurveSegments()

    def remove_all_frozen_points(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllFrozenPoints()
                |     Removes all Frozen Points of the hybrid shape curve smooth object.
                |     
                | Example:
                |     The following example removes all Frozen Points of the hybShpCurveSmooth
                |     object.
                | 
                |      hybShpCurveSmooth.RemoveAllFrozenPoints

        :return: None
        """
        return self.com_object.RemoveAllFrozenPoints()

    def remove_frozen_curve_segment(self, i_curve: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveFrozenCurveSegment(Reference iCurve)
                |     Removes Frozen Curve Segment from the list of Forzen curves in hybrid shape
                |     curve smooth object.
                | 
                |     Parameters:
                | 
                |         iCurve
                |             The Frozen Curve Segment to remove. 
                | 
                |     Example:
                |         The following example removes the Frozen Curve Segment from the
                |         hybShpCurveSmooth object.
                | 
                |          hybShpCurveSmooth.RemoveFrozenCurveSegment iCurve.

        :param Reference i_curve:
        :return: None
        """
        return self.com_object.RemoveFrozenCurveSegment(i_curve.com_object)

    def remove_frozen_point(self, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveFrozenPoint(Reference iPoint)
                |     Removes Frozen Point from the list of frozen points in hybrid shape curve
                |     smooth object.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The Frozen Point to remove. 
                | 
                |     Example:
                |         The following example removes the Frozen Point from the
                |         hybShpCurveSmooth object.
                | 
                |          hybShpCurveSmooth.RemoveFrozenPoint iPoint.

        :param Reference i_point:
        :return: None
        """
        return self.com_object.RemoveFrozenPoint(i_point.com_object)

    def set_maximum_deviation(self, i_max_deviation: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetMaximumDeviation(double iMaxDeviation)
                |     Sets the maximum deviation.
                | 
                |     Parameters:
                | 
                |         iMaxDeviation
                |             The maximium deviation

        :param float i_max_deviation:
        :return: None
        """
        return self.com_object.SetMaximumDeviation(i_max_deviation)

    def set_tangency_threshold(self, i_tangency_threshold: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTangencyThreshold(double iTangencyThreshold)
                |     Sets the tangency threshold.
                | 
                |     Parameters:
                | 
                |         iTangencyThreshold
                |             The tangency threshold

        :param float i_tangency_threshold:
        :return: None
        """
        return self.com_object.SetTangencyThreshold(i_tangency_threshold)

    def __repr__(self):
        return f'HybridShapeCurveSmooth(name="{ self.name }")'
