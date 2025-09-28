"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeConic(HybridShape):

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
                |                         HybridShapeConic
                | 
                | Represents the hybrid shape conic object.
                | Role: To access the data of the hybrid shape conic object. This data
                | includes:
                | 
                |     The start point and its associated tangent contraint
                |     The end point and its associated tangent contraint
                |     The supporting plane
                |     The tangent intersection point
                |     The conic parameter: p = 0.5 (parabola), 0<=p<=0.5 (ellipse), 0.5<= p <=1.0 (hyperbola)
                | 
                | Use the HybridShapeFactory to create a HybridShapeConic
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def conic_parameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ConicParameter() As double
                |     Returns or sets the conic parameter.
                | 
                |     Example:
                |         This example retrieves in conicParm the conic parameter of the conic
                |         hybConic.
                | 
                |          Dim conicParm As double 
                |          Set conicParm = hybConic.ConicParameter

        :return: float
        """

        return self.com_object.ConicParameter

    @conic_parameter.setter
    def conic_parameter(self, value: float):
        """
        :param float value:
        """

        self.com_object.ConicParameter = value

    @property
    def conic_user_tol(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ConicUserTol() As Length (Read Only)
                |     Gets or sets the conic User Tolerance.
                | 
                |     Example:
                |         This example retrieves in conicUserTol the conic user tolerance of the
                |         conic HybridShapeConic.
                | 
                |          Dim oConicUserTol As  CATIALength 
                |          Set oConicUserTol = HybridShapeConic.conicUserTol
                |          
                | 
                |     See also:
                |         Length

        :return: Length
        """

        return Length(self.com_object.ConicUserTol)

    @property
    def end_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndPoint() As Reference
                |     Returns or sets the conic end point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in endPt the end point of the conic
                |         hybConic.
                | 
                |          Dim endPt As Reference 
                |          Set endPt = hybConic.EndPoint

        :return: Reference
        """

        return Reference(self.com_object.EndPoint)

    @end_point.setter
    def end_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.EndPoint = value

    @property
    def end_tangent(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndTangent() As HybridShapeDirection
                |     Returns or sets the tangent direction at the conic end
                |     point.
                | 
                |     Example:
                |         This example retrieves in endTgt the tangent direction associated with
                |         the end point of the conic hybConic.
                | 
                |          Dim endTgt As Reference 
                |          Set endTgt = hybConic.EndTangent

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.EndTangent)

    @end_tangent.setter
    def end_tangent(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.EndTangent = value

    @property
    def start_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property StartPoint() As Reference
                |     Returns or sets the conic start point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example sets startPt as the start point of the conic
                |         hybConic.
                | 
                |          Dim startPt As Reference
                |          ... ' Value startPt
                |          hybConic.StartPoint startPt

        :return: Reference
        """

        return Reference(self.com_object.StartPoint)

    @start_point.setter
    def start_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.StartPoint = value

    @property
    def start_tangent(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property StartTangent() As HybridShapeDirection
                |     Returns or sets the tangent direction at the conic start
                |     point.
                | 
                |     Example:
                |         This example sets startTgt as the tangent direction at the start point
                |         of the conic hybConic.
                | 
                |          Dim startTgt As Reference
                |          ... ' Value startTangent
                |          hybConic.StartTangent startTgt

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.StartTangent)

    @start_tangent.setter
    def start_tangent(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.StartTangent = value

    @property
    def support_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SupportPlane() As Reference
                |     Returns or sets the conic supporting plane.
                |     Sub-element(s) supported (see Boundary object):
                |     PlanarFace.
                | 
                |     Example:
                |         This example retrieves in supportPln the supporting plane of the conic
                |         hybConic.
                | 
                |          Dim supportPln As Reference 
                |          Set supportPln = hybConic.SupportPlane

        :return: Reference
        """

        return Reference(self.com_object.SupportPlane)

    @support_plane.setter
    def support_plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SupportPlane = value

    @property
    def tangent_int_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TangentIntPoint() As Reference
                |     Returns or sets the conic tangent intersection point.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in tgtIntPt the tangent intersection point of
                |         the conic hybConic.
                | 
                |          Dim tgtIntPt As Reference 
                |          Set tgtIntPt = hybConic.TangentIntPoint

        :return: Reference
        """

        return Reference(self.com_object.TangentIntPoint)

    @tangent_int_point.setter
    def tangent_int_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.TangentIntPoint = value

    def get_end_tangent_direction_flag(self, o_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetEndTangentDirectionFlag(long oOrientation)
                |     Retrieves the tangent direction orientation at the conic end
                |     point.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             The direction orientation applied to the tangent direction at the
                |             conic end point
                |             Legal values: 1 if the tangent direction is used as is, and -1 if
                |             it is inverted 
                | 
                |     Example:
                | 
                |          This example retrieves the direction orientation of the tangent at the
                |          end point of
                |          the conic hybConic.
                |          
                | 
                |          Dim endPtTgtOrient As long
                |          hybConic.GetEndTangentDirectionFlag endPtTgtOrient

        :param int o_orientation:
        :return: None
        """
        return self.com_object.GetEndTangentDirectionFlag(o_orientation)

    def get_intermed_tangent(self, i_index_point: int) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetIntermedTangent(long iIndexPoint) As
                | HybridShapeDirection
                |     Retrieves the tangent direction at one of the conic intermediate passing
                |     points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                |         oTgtDir
                |             The retrieved tangent direction at the given passing point
                |             
                | 
                |     Example:
                | 
                |          This example retrieves in tgtDir the tangent direction at point
                |          passingPtIdx 
                |          through which the conic hybConic passes.
                |          
                | 
                |          Dim tgtDir As Reference
                |          passingPtIdx = 1
                |          Set tgtDir = hybConic.GetIntermedTangent (passingPtIdx)

        :param int i_index_point:
        :return: HybridShapeDirection
        """
        return HybridShapeDirection(self.com_object.GetIntermedTangent(i_index_point))

    def get_intermediate_point(self, i_index_point: int, o_end_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetIntermediatePoint(long iIndexPoint,Reference oEndPoint)
                |     Retrieves one of the conic intermediate passing points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, 2 for the second one,
                |             and 3 for the third one 
                |         oEndPoint
                |             The retrieved passing point 
                | 
                |     Example:
                | 
                |          This example retrieves in passingPt the second point through
                |          which
                |          the conic hybConic passes.
                |          
                | 
                |          Dim passingPt As Reference
                |          passingPtIdx = 2
                |          hybConic.GetIntermediatePoint passingPtIdx, passingPt

        :param int i_index_point:
        :param Reference o_end_point:
        :return: None
        """
        return self.com_object.GetIntermediatePoint(i_index_point, o_end_point.com_object)

    def get_intermediate_tangent_direction_flag(self, i_index_point: int, o_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetIntermediateTangentDirectionFlag(long iIndexPoint,long
                | oOrientation)
                |     Retrieves the tangent direction orientation of one of the conic
                |     intermediate points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                |         oOrientation
                |             The direction orientation applied to the tangent direction at the
                |             intermediate passing point
                |             Legal values: 1 if the tangent direction is used as is, and -1 if
                |             it is inverted 
                | 
                |     Example:
                | 
                |          This example retrieves the direction orientation of the tangent at the
                |          first point through which
                |          the conic hybConic passes.
                |          
                | 
                |          passingPtIdx = 1
                |          Dim passingPtTgtOrient As long
                |          hybConic.GetIntermediateTangentDirectionFlag passingPtIdx,
                |          passingPtTgtOrient

        :param int i_index_point:
        :param int o_orientation:
        :return: None
        """
        return self.com_object.GetIntermediateTangentDirectionFlag(i_index_point, o_orientation)

    def get_start_tangent_direction_flag(self, o_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetStartTangentDirectionFlag(long oOrientation)
                |     Retrieves the tangent direction orientation at the conic start
                |     point.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             The direction orientation applied to the tangent direction at the
                |             conic start point
                |             Legal values: 1 if the tangent direction is used as is, and -1 if
                |             it is inverted 
                | 
                |     Example:
                | 
                |          This example retrieves the direction orientation of the tangent at the
                |          start point of
                |          the conic hybConic.
                |          
                | 
                |          Dim startPtTgtOrient As long
                |          hybConic.GetStartTangentDirectionFlag
                |          startPtTgtOrient

        :param int o_orientation:
        :return: None
        """
        return self.com_object.GetStartTangentDirectionFlag(o_orientation)

    def set_end_tangent_direction_flag(self, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetEndTangentDirectionFlag(long iOrientation)
                |     Sets the tangent direction orientation at the conic end
                |     point.
                | 
                |     Parameters:
                | 
                |         iOrientation
                |             The direction orientation to be applied to the tangent direction at
                |             the conic end point
                |             Legal values: 1 if the tangent direction is to be used as is, and
                |             -1 if it must be inverted 
                | 
                |     Example:
                | 
                |          This example sets the direction orientation of the tangent at the end
                |          point of
                |          the conic hybConic to the one of the direction used
                |          for
                |          the tangent.
                |          
                | 
                |          endPtTgtOrient = 1
                |          hybConic.SetEndTangentDirectionFlag endPtTgtOrient

        :param int i_orientation:
        :return: None
        """
        return self.com_object.SetEndTangentDirectionFlag(i_orientation)

    def set_intermediate_point(self, i_index_point: int, i_end_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetIntermediatePoint(long iIndexPoint,Reference iEndPoint)
                |     Sets one of the conic intermediate passing points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, 2 for the second one,
                |             and 3 for the third one 
                |         iEndPoint
                |             The passing point to set.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                | 
                |     Example:
                | 
                |          This example sets passingPt as the first point through
                |          which
                |          the conic hybConic must pass.
                |          
                | 
                |          Dim passingPt As Reference
                |          ... ' Value passingPt
                |          passingPtIdx = 1
                |          hybConic.SetIntermediatePoint passingPtIdx, passingPt

        :param int i_index_point:
        :param Reference i_end_point:
        :return: None
        """
        return self.com_object.SetIntermediatePoint(i_index_point, i_end_point.com_object)

    def set_intermediate_tangent(self, i_index_point: int, i_tgt_dir: HybridShapeDirection) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetIntermediateTangent(long iIndexPoint,HybridShapeDirection
                | iTgtDir)
                |     Sets the tangent direction at one of the conic intermediate passing
                |     points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point where the tangent
                |             direction is to be set
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                |         iTgtDir
                |             The direction to set as the tangent direction at the given passing
                |             point 
                | 
                |     Example:
                | 
                |          This example sets tgtDir as the tangent direction at the first point
                |          through which
                |          the conic hybConic passes.
                |          
                | 
                |          Dim tgtDir As Reference
                |          ... ' Value tgtDir
                |          passingPtIdx = 1
                |          hybConic.SetIntermediateTangent passingPtIdx, tgtDir

        :param int i_index_point:
        :param HybridShapeDirection i_tgt_dir:
        :return: None
        """
        return self.com_object.SetIntermediateTangent(i_index_point, i_tgt_dir.com_object)

    def set_intermediate_tangent_direction_flag(self, i_index_point: int, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetIntermediateTangentDirectionFlag(long iIndexPoint,long
                | iOrientation)
                |     Sets the tangent direction orientation of one of the conic intermediate
                |     points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point to
                |             retrieve
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                |         iOrientation
                |             The direction orientation to be applied to the tangent direction at
                |             the intermediate passing point
                |             Legal values: 1 if the tangent direction is to be used as is, and
                |             -1 if it must be inverted 
                | 
                |     Example:
                | 
                |          This example sets the direction orientation of the tangent at the
                |          first point through which
                |          the conic hybConic passes to the inverse of the one of the direction
                |          used for
                |          the tangent.
                |          
                | 
                |          passingPtIdx = 1
                |          passingPtTgtOrient = -1
                |          hybConic.SetIntermediateTangentDirectionFlag passingPtIdx,
                |          passingPtTgtOrient

        :param int i_index_point:
        :param int i_orientation:
        :return: None
        """
        return self.com_object.SetIntermediateTangentDirectionFlag(i_index_point, i_orientation)

    def set_start_and_end_tangents_plus_conic_parameter(self, i_start_tgt: HybridShapeDirection, i_end_tgt: HybridShapeDirection, i_conic_param: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetStartAndEndTangentsPlusConicParameter(HybridShapeDirection
                | iStartTgt,HybridShapeDirection iEndTgt,double iConicParam)
                |     Sets the tangent directions at conic start and end points, and the conic
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iStartTgt
                |             The tangent direction at the start point 
                |         iEndTgt
                |             The tangent direction at the end point 
                |         iConicParam
                |             The conic parameter
                |             Legal values: p = 0.5 (parabola), 0<=p<=0.5 (ellipse), 0.5<= p <=1.0 (hyperbola) 
                | 
                |     Example:
                | 
                |          This example sets firstDir and secondDir as the tangent directions at
                |          the start
                |          and end points of the conic hybConic, and conicParm as the conic
                |          parameter.
                |          
                | 
                |          hybConic.SetStartAndEndTangentsPlusConicParameter firstDir, secondDir,
                |          conicParm

        :param HybridShapeDirection i_start_tgt:
        :param HybridShapeDirection i_end_tgt:
        :param float i_conic_param:
        :return: None
        """
        return self.com_object.SetStartAndEndTangentsPlusConicParameter(i_start_tgt.com_object, i_end_tgt.com_object, i_conic_param)

    def set_start_and_end_tangents_plus_passing_point(self, i_start_tgt: HybridShapeDirection, i_end_tgt: HybridShapeDirection, i_passing_pt: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetStartAndEndTangentsPlusPassingPoint(HybridShapeDirection
                | iStartTgt,HybridShapeDirection iEndTgt,Reference iPassingPt)
                |     Sets the tangent directions at conic start and end points, and a passing
                |     point.
                | 
                |     Parameters:
                | 
                |         iStartTgt
                |             The tangent direction at the start point.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                |         iEndTgt
                |             The tangent direction at the end point 
                |         iPassingPt
                |             A point through which the conic must pass.
                |             Legal values: This point must differ from the start and end points.
                |             
                | 
                |     Example:
                | 
                |          This example sets firstDir and secondDir as the tangent directions at
                |          the start
                |          and end points of the conic hybConic, and passingPoint as a point
                |          through
                |          which the conic must pass.
                |          
                | 
                |          hybConic.SetStartAndEndTangentsPlusPassingPoint firstDir, secondDir,
                |          passingPoint

        :param HybridShapeDirection i_start_tgt:
        :param HybridShapeDirection i_end_tgt:
        :param Reference i_passing_pt:
        :return: None
        """
        return self.com_object.SetStartAndEndTangentsPlusPassingPoint(i_start_tgt.com_object, i_end_tgt.com_object, i_passing_pt.com_object)

    def set_start_tangent_direction_flag(self, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetStartTangentDirectionFlag(long iOrientation)
                |     Sets the tangent direction orientation at the conic start
                |     point.
                | 
                |     Parameters:
                | 
                |         iOrientation
                |             The direction orientation to be applied to the tangent direction at
                |             the conic start point
                |             Legal values: 1 if the tangent direction is to be used as is, and
                |             -1 if it must be inverted 
                | 
                |     Example:
                | 
                |          This example sets the direction orientation of the tangent at the
                |          start point of
                |          the conic hybConic to the inverse of the one of the direction used
                |          for
                |          the tangent.
                |          
                | 
                |          startPtTgtOrient = -1
                |          hybConic.SetStartTangentDirectionFlag
                |          startPtTgtOrient

        :param int i_orientation:
        :return: None
        """
        return self.com_object.SetStartTangentDirectionFlag(i_orientation)

    def set_tangent_intersect_point_plus_conic_parm(self, i_tgt_int: Reference, i_conic_param: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTangentIntersectPointPlusConicParm(Reference iTgtInt,double
                | iConicParam)
                |     Sets the intersection point of the conic tangents to the start and end
                |     points, and the conic parameter.
                | 
                |     Parameters:
                | 
                |         iTgtInt
                |             The point intersection of the conic tangents to the start and end
                |             point.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                |         iConicParam
                |             The conic parameter
                |             Legal values: p = 0.5 (parabola), 0<=p<=0.5 (ellipse), 0.5<= p <=1.0 (hyperbola) 
                | 
                |     Example:
                | 
                |          This example sets tgtIntPoint as the intersection point of the
                |          tangents
                |          to the start and end points of the conic hybConic, and conicParm as
                |          the conic parameter.
                |          
                | 
                |          hybConic.SetTangentIntersectPointPlusConicParm tgtIntPoint,
                |          conicParm

        :param Reference i_tgt_int:
        :param float i_conic_param:
        :return: None
        """
        return self.com_object.SetTangentIntersectPointPlusConicParm(i_tgt_int.com_object, i_conic_param)

    def set_tangent_intersect_point_plus_passing_point(self, i_tgt_int: Reference, i_passing_pt: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTangentIntersectPointPlusPassingPoint(Reference iTgtInt,Reference
                | iPassingPt)
                |     Sets the intersection point of the conic tangents to the start and end
                |     points, and a passing point.
                | 
                |     Parameters:
                | 
                |         iTgtInt
                |             The point intersection of the conic tangents to the start and end
                |             point.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                |         iPassingPt
                |             A point through which the conic must pass.
                |             Legal values: This point must differ from the start and end
                |             points.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                | 
                |     Example:
                | 
                |          This example sets tgtIntPoint as the intersection point of the
                |          tangents
                |          to the start and end points of the conic hybConic, and passingPoint as
                |          a point through
                |          which the conic must pass.
                |          
                | 
                |          hybConic.SetTangentIntersectPointPlusPassingPoint tgtIntPoint,
                |          passingPoint

        :param Reference i_tgt_int:
        :param Reference i_passing_pt:
        :return: None
        """
        return self.com_object.SetTangentIntersectPointPlusPassingPoint(i_tgt_int.com_object, i_passing_pt.com_object)

    def set_three_intermediate_passing_points(self, i_pass_pt1: Reference, i_pass_pt2: Reference, i_pass_pt3: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetThreeIntermediatePassingPoints(Reference iPassPt1,Reference
                | iPassPt2,Reference iPassPt3)
                |     Sets three conic intermediate passing points.
                | 
                |     Parameters:
                | 
                |         iPassPt1
                |             The first intermediate passing point.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                |         iPassPt2
                |             The second intermediate passing point.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                |         iPassPt3
                |             The third intermediate passing point.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                | 
                |     Example:
                | 
                |          This example sets passingPoint1, passingPoint2, and passingPoint3 as
                |          the
                |          three intermediate points through which the conic hybConic must
                |          pass.
                |          
                | 
                |          hybConic.SetThreeIntermediatePassingPoints passingPoint1,
                |          passingPoint2, passingPoint3

        :param Reference i_pass_pt1:
        :param Reference i_pass_pt2:
        :param Reference i_pass_pt3:
        :return: None
        """
        return self.com_object.SetThreeIntermediatePassingPoints(i_pass_pt1.com_object, i_pass_pt2.com_object, i_pass_pt3.com_object)

    def set_two_intermediate_passing_points_plus_one_tangent(self, i_pass_pt1: Reference, i_pass_pt2: Reference, i_tgt_dir: HybridShapeDirection, i_index_point: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTwoIntermediatePassingPointsPlusOneTangent(Reference iPassPt1,Reference
                | iPassPt2,HybridShapeDirection iTgtDir,long iIndexPoint)
                |     Sets two conic intermediate passing points and a tangent at one of the
                |     passing points.
                | 
                |     Parameters:
                | 
                |         iPassPt1
                |             The first intermediate passing point.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                |         iPassPt2
                |             The second intermediate passing point.
                |             Sub-element(s) supported (see Boundary object): Vertex.
                |             
                |         iTgtDir
                |             The tangent direction at one of the intermediate passing points
                |             
                |         iIndexPoint
                |             An index indicating the passing point to which the tangent
                |             direction applies
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                | 
                |     Example:
                | 
                |          This example sets passingPoint1 and passingPoint2 as
                |          two
                |          intermediate points through which the conic hybConic must
                |          pass,
                |          tgtDir as the tangent direction at the passing point designated by
                |          passingPointIdx.
                |          
                | 
                |          hybConic.SetTwoIntermediatePassingPointsPlusOneTangent passingPoint1,
                |          passingPoint2, tgtDir, passingPointIdx

        :param Reference i_pass_pt1:
        :param Reference i_pass_pt2:
        :param HybridShapeDirection i_tgt_dir:
        :param int i_index_point:
        :return: None
        """
        return self.com_object.SetTwoIntermediatePassingPointsPlusOneTangent(i_pass_pt1.com_object, i_pass_pt2.com_object, i_tgt_dir.com_object, i_index_point)

    def switch_end_tangent_direction(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SwitchEndTangentDirection()
                |     Inverts the tangent direction orientation at the conic end
                |     point.
                | 
                |     Example:
                | 
                |          This example inverts the direction orientation of the tangent at the
                |          end point of
                |          the conic hybConic.
                |          
                | 
                |          hybConic.SwitchEndTangentDirection

        :return: None
        """
        return self.com_object.SwitchEndTangentDirection()

    def switch_intermediate_tangent_direction(self, i_index_point: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SwitchIntermediateTangentDirection(long iIndexPoint)
                |     Inverts the tangent direction orientation of one of the conic intermediate
                |     points.
                | 
                |     Parameters:
                | 
                |         iIndexPoint
                |             An index that designates the passing point where the tangent
                |             direction is to be inverted
                |             Legal values: 1 for the first passing point, and 2 for the second
                |             one 
                | 
                |     Example:
                | 
                |          This example inverts the direction orientation of the tangent at the
                |          first point through which
                |          the conic hybConic passes.
                |          
                | 
                |          passingPtIdx = 1
                |          hybConic.SwitchIntermediateTangentDirection
                |          passingPtIdx

        :param int i_index_point:
        :return: None
        """
        return self.com_object.SwitchIntermediateTangentDirection(i_index_point)

    def switch_start_tangent_direction(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SwitchStartTangentDirection()
                |     Inverts the tangent direction orientation at the conic start
                |     point.
                | 
                |     Example:
                | 
                |          This example inverts the direction orientation of the tangent at the
                |          start point of
                |          the conic hybConic.
                |          
                | 
                |          hybConic.SwitchStartTangentDirection

        :return: None
        """
        return self.com_object.SwitchStartTangentDirection()

    def __repr__(self):
        return f'HybridShapeConic(name="{ self.name }")'
