"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.geometry_2d import Geometry2D
from pycatia3dx.sketcher.point_2d import Point2D


class Curve2D(Geometry2D):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATSketcherIDLItf.GeometricElement
                |                         CATSketcherIDLItf.Geometry2D
                |                             Curve2D
                | 
                | Class defining a curve in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def continuity(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Continuity() As short (Read Only)
                |     Returns the highest level of geometric continuity the curve
                |     possesses.
                | 
                |     Parameters:
                | 
                |         oLevel
                |             The maximum geometric continuity level

        :return: int
        """

        return self.com_object.Continuity

    @property
    def end_point(self) -> Point2D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property EndPoint() As Point2D
                |     Returns or Sets the end point of the curve. The end point is decided with
                |     respect to the logical flow imposed on the curve by the
                |     object.
                | 
                |     Example:
                | 
                |           The following example sets the end point of the
                |           curve.
                |           
                | 
                |           Dim myPoint2D As Point2D
                |           Set myPoint2D = ...
                |           Dim myCurve2D As Curve2D
                |           myCurve2D.EndPoint = myPoint2D

        :return: Point2D
        """

        return Point2D(self.com_object.EndPoint)

    @end_point.setter
    def end_point(self, value: Point2D):
        """
        :param Point2D value:
        """

        self.com_object.EndPoint = value

    @property
    def period(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Period() As double (Read Only)
                |     Returns the period of a periodic curve.
                | 
                |     Parameters:
                | 
                |         oPeriod
                |             The period of the curve.

        :return: float
        """

        return self.com_object.Period

    @property
    def start_point(self) -> Point2D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property StartPoint() As Point2D
                |     Returns or sets the start point of the curve. The start point is decided
                |     with respect to the logical flow imposed on the curve by the
                |     object.
                | 
                |     Example:
                | 
                |           The following example sets the start point of the
                |           curve.
                |           
                | 
                |           Dim myPoint2D As Point2D
                |           Set myPoint2D = ...
                |           Dim myCurve2D As Curve2D
                |           myCurve2D.StartPoint = myPoint2D

        :return: Point2D
        """

        return Point2D(self.com_object.StartPoint)

    @start_point.setter
    def start_point(self, value: Point2D):
        """
        :param Point2D value:
        """

        self.com_object.StartPoint = value

    def get_curvature(self, i_param: float, o_curvature: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetCurvature(double iParam,CATSafeArrayVariant oCurvature)
                |     Returns the curvature and curvature direction at the parameter
                |     specified.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The parameter of the chosen point on the curve. 
                |         oCurvature
                | 
                |               oCurvature[0]: The curvature at the specified
                |               parameter.
                |               oCurvature[1;2]: The unit-vector of curvature direction at the
                |               specified parameter.

        :param float i_param:
        :param tuple o_curvature:
        :return: None
        """
        return self.com_object.GetCurvature(i_param, o_curvature)

    def get_derivatives(self, i_param: float, o_derivative: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetDerivatives(double iParam,CATSafeArrayVariant
                | oDerivative)
                |     Returns the first, second and third derivatives at the parameter
                |     specified.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The parameter of the chosen point on the curve. 
                |         oDerivative[0]
                | 
                |               oDerivative[0]: First degree derivative.
                |               oDerivative[1]: Second degree derivative.
                |               oDerivative[2]: Third degree derivative.

        :param float i_param:
        :param tuple o_derivative:
        :return: None
        """
        return self.com_object.GetDerivatives(i_param, o_derivative)

    def get_end_points(self, o_end_points: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetEndPoints(CATSafeArrayVariant oEndPoints)
                |     Returns the end-points of the curve. The start point and the end point are
                |     decided with respect to the logical flow imposed on the curve by the
                |     object.
                | 
                |     Parameters:
                | 
                |         oEndPoints
                | 
                |               oEndPoints[0]: The x coordinate of the start
                |               point
                |               oEndPoints[1]: The y coordinate of the start
                |               point
                |               oEndPoints[2]: The x coordinate of the end point
                |               oEndPoints[3]: The y coordinate of the end point

        :param tuple o_end_points:
        :return: None
        """
        return self.com_object.GetEndPoints(o_end_points)

    def get_length_at_param(self, i_from_param: float, i_to_param: float) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetLengthAtParam(double iFromParam,double iToParam) As
                | double
                |     Returns the length, measured along the curve, from a given parameter to a
                |     given parameter.
                | 
                |     Parameters:
                | 
                |         iFromParam
                |             The parameter from which the length is to be measured.
                |             
                |         iToParam
                |             The parameter to which the length is to be measured.
                |             
                |         oLength
                |             The length between the parameters

        :param float i_from_param:
        :param float i_to_param:
        :return: float
        """
        return self.com_object.GetLengthAtParam(i_from_param, i_to_param)

    def get_param_at_length(self, i_from_param: float, i_length: float) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetParamAtLength(double iFromParam,double iLength) As
                | double
                |     Returns the parameter at a given length, measured along the curve, starting
                |     from a given parameter. The direction of measurement is always in the direction
                |     of the logical flow of the curve. If no inherent logical flow can be assigned
                |     the direction is the direction of increasing
                |     parameterization.
                | 
                |     Parameters:
                | 
                |         iFromParam
                |             The parameter from which the length needs to be measured.
                |             
                |         iLength
                |             The length of the curve to be measured from iFromParam in the
                |             logical flow direction of the curve. 
                |         oParam
                |             The computed parameter.

        :param float i_from_param:
        :param float i_length:
        :return: float
        """
        return self.com_object.GetParamAtLength(i_from_param, i_length)

    def get_param_extents(self, o_params: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetParamExtents(CATSafeArrayVariant oParams)
                |     Returns the parametric extents of the curve. This is the parametric
                |     equivalent of the end-points.
                | 
                |     Parameters:
                | 
                |         oParams
                | 
                |               oParams[0]: The parameter associated with the start point of the
                |               curve
                |               oParams[1]: The parameter associated with the end point of the
                |               curve

        :param tuple o_params:
        :return: None
        """
        return self.com_object.GetParamExtents(o_params)

    def get_point_at_param(self, i_param: float, o_point: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetPointAtParam(double iParam,CATSafeArrayVariant oPoint)
                |     Returns a point on the curve computed from an input
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iParam
                |             parameter 
                |         oPoint
                |             The X and Y coordinates of the computed 2D space point.

        :param float i_param:
        :param tuple o_point:
        :return: None
        """
        return self.com_object.GetPointAtParam(i_param, o_point)

    def get_range_box(self, o_bound_point: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetRangeBox(CATSafeArrayVariant oBoundPoint)
                |     Returns the range box (or bounding box) of the object
                |     The box is axially aligned within the local coordinate system of the
                |     server.
                | 
                |     Parameters:
                | 
                |         oBoundPoint
                | 
                |               oBoundPoint[0]: The minimum x point of the box
                |               oBoundPoint[1]: The minimum y point of the box
                |               oBoundPoint[2]: The maximum x point of the box
                |               oBoundPoint[3]: The maximum y point of the box

        :param tuple o_bound_point:
        :return: None
        """
        return self.com_object.GetRangeBox(o_bound_point)

    def get_tangent(self, i_param: float, o_tangency: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetTangent(double iParam,CATSafeArrayVariant oTangency)
                |     Returns the unit-vector tangent at the parameter
                |     specified.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The parameter of the chosen point on the curve. 
                |         oTangency
                |             The X and Y coordinates of the unit-vector tangent at the specified
                |             parameter.

        :param float i_param:
        :param tuple o_tangency:
        :return: None
        """
        return self.com_object.GetTangent(i_param, o_tangency)

    def is_periodic(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func IsPeriodic() As boolean
                |     Specifies whether a curve is periodic or not.
                | 
                |     Parameters:
                | 
                |         oPeriodic
                |             Returns true if the curve is periodic.

        :return: bool
        """
        return self.com_object.IsPeriodic()

    def __repr__(self):
        return f'Curve2D(name="{ self.name }")'
