"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.point_2d import Point2D


class ControlPoint2D(Point2D):

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
                |                             CATSketcherIDLItf.Point2D
                |                                 ControlPoint2D
                | 
                | Class defining a spline control point in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.control_point2_d = com_object

    @property
    def curvature(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Curvature() As double
                |     Returns or Sets the curvature properties of the spline control
                |     point.
                | 
                |     Example:
                | 
                |          The following example sets the curvature of the tangent determined at
                |          the control point.
                |          
                | 
                |          double myCurvature(1)
                |          myControlPoint2D As ControlPoint2D
                |          Set myControlPoint2D = ...
                |          myControlPoint2D.Curvature myCurvature

        :return: float
        """

        return self.control_point2_d.Curvature

    @curvature.setter
    def curvature(self, value: float):
        """
        :param float value:
        """

        self.control_point2_d.Curvature = value

    def get_tangent(self, o_tangent: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetTangent(CATSafeArrayVariant oTangent)
                |     Returns the tangent properties of the spline control point
                | 
                |     Parameters:
                | 
                |         oTangent[0]
                |             The X Coordinate of the tangent determined at the control point
                |             
                |         oTangent[1]
                |             The Y Coordinate of the tangent determined at the control point

        :param tuple o_tangent:
        """
        return self.control_point2_d.GetTangent(o_tangent)

    def set_tangent(self, i_tangent_x: float, i_tangent_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetTangent(double iTangentX,double iTangentY)
                |     Imposes the tangent properties of the spline control
                |     point.
                | 
                |     Parameters:
                | 
                |         iTangentX
                |             The X Coordinate of the tangent determined at the control point
                |             
                |         iTangentY
                |             The Y Coordinate of the tangent determined at the control point

        :param float i_tangent_x:
        :param float i_tangent_y:
        :return: None
        """
        return self.control_point2_d.SetTangent(i_tangent_x, i_tangent_y)

    def unset_curvature(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub UnsetCurvature()
                |     Unsets the curvature properties of the spline control point

        :return: None
        """
        return self.control_point2_d.UnsetCurvature()

    def unset_tangent(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub UnsetTangent()
                |     Unsets the tangent properties of the spline control point.

        :return: None
        """
        return self.control_point2_d.UnsetTangent()

    def __repr__(self):
        return f'ControlPoint2D(name="{ self.name }")'
