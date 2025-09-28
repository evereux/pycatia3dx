"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.curve_2d import Curve2D
from pycatia3dx.sketcher.point_2d import Point2D


class Spline2D(Curve2D):

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
                |                             CATSketcherIDLItf.Curve2D
                |                                 Spline2D
                | 
                | Class defining a spline in 2D Space.
                | A 2D spline is defined by its constituting control points.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_control_points(self, o_ctrl_points: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetControlPoints(CATSafeArrayVariant oCtrlPoints)
                |     Returns the control points making up the spline.
                | 
                |     Parameters:
                | 
                |         oCtrlPoints
                |             The control points of the spline 
                | 
                |     Example:
                | 
                |          The following example fetches the list of control points defining
                |          the
                | 
                |          splinemySpline:
                |          
                | 
                |          mySpline.GetControlPoints ControlPoints

        :param tuple o_ctrl_points:
        :return: None
        """
        return self.com_object.GetControlPoints(o_ctrl_points)

    def get_number_of_control_points(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetNumberOfControlPoints() As double
                |     Returns the number of Control Points of the Spline.
                | 
                |     Returns:
                |         oNumber The number of control points

        :return: float
        """
        return self.com_object.GetNumberOfControlPoints()

    def insert_control_point_after(self, i_ctrl_point: Point2D, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub InsertControlPointAfter(Point2D iCtrlPoint,long iPosition)
                |     Inserts control points in the spline. If a 2D point is given (and not a
                |     control
                |     point), a new control point is created and aggregated in the
                |     spline.
                | 
                |     Parameters:
                | 
                |         iCtrlPoint
                |             The new point to be inserted. (@see CATIAPoint2D and
                |             CATIAControlPoint2D
                |             for more information). 
                |         iPosition
                |             The position at which to insert the point.
                |             To insert a new control point as the first element, set iPosition
                |             to 0. 
                | 
                |     Example:
                | 
                |          The following example inserts a control point myCtrlPoint as the
                |          second
                | 
                |          element of the splinemySpline:
                |          
                | 
                |          call mySpline.InsertControlPointAfter (myCtrlPoint,
                |          1)

        :param Point2D i_ctrl_point:
        :param int i_position:
        :return: None
        """
        return self.com_object.InsertControlPointAfter(i_ctrl_point.com_object, i_position)

    def __repr__(self):
        return f'Spline2D(name="{ self.name }")'
