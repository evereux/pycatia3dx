"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.curve_2d import Curve2D
from pycatia3dx.sketcher.point_2d import Point2D


class Ellipse2D(Curve2D):

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
                |                                 Ellipse2D
                | 
                | Class defining an ellipse in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def center_point(self) -> Point2D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property CenterPoint() As Point2D
                |     Returns or Sets the center point of the ellipse.
                | 
                |     Example:
                | 
                |            The following example sets the center point of the
                |            ellispe.
                |          
                | 
                |           Dim myPoint2D As Point2D
                |           Set myPoint2D = ...
                |           Dim myEllipse2D As Curve2D
                |           myEllipse2D.CenterPoint = myPoint2D

        :return: Point2D
        """

        return Point2D(self.com_object.CenterPoint)

    @center_point.setter
    def center_point(self, value: Point2D):
        """
        :param Point2D value:
        """

        self.com_object.CenterPoint = value

    @property
    def major_radius(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property MajorRadius() As double (Read Only)
                |     Returns the radius of the ellipse major axis.
                | 
                |     Example:
                | 
                |            The following example returns the radius of the ellispe major
                |            axis.
                |          
                | 
                |           Dim myRadius As double
                |           Dim myEllipse2D As Curve2D
                |           myRadius = myEllipse2D.MajorRadius

        :return: float
        """

        return self.com_object.MajorRadius

    @property
    def minor_radius(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property MinorRadius() As double (Read Only)
                |     Returns the radius of the ellipse minor axis.
                | 
                |     Example:
                | 
                |            The following example returns the radius of the ellispe minor
                |            axis.
                |          
                | 
                |           Dim myRadius As double
                |           Dim myEllipse2D As Curve2D
                |           myRadius = myEllipse2D.MinorRadius

        :return: float
        """

        return self.com_object.MinorRadius

    def get_center(self, o_center: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetCenter(CATSafeArrayVariant oCenter)
                |     Returns the center of the ellipse in 2D space.
                | 
                |     Parameters:
                | 
                |         oCenter[0]
                |             The X Coordinate of the center point of the ellipse
                |             
                |         oCenter[1]
                |             The Y Coordinate of the center point of the ellipse

        :param tuple o_center:
        :return: None
        """
        return self.com_object.GetCenter(o_center)

    def get_major_axis(self, o_major_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetMajorAxis(CATSafeArrayVariant oMajorAxis)
                |     Returns the unit vector of the major axis of the ellipse in 2D
                |     space.
                | 
                |     Parameters:
                | 
                |         oMajorAxis[0]
                |             The length of the major axis 
                |         oMajorAxis[1]
                |             The length of the major axis

        :param tuple o_major_axis:
        :return: None
        """
        return self.com_object.GetMajorAxis(o_major_axis)

    def get_minor_axis(self, o_major_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetMinorAxis(CATSafeArrayVariant oMajorAxis)
                |     Returns the unit vector of the minor axis of the ellipse in 2D
                |     space.
                | 
                |     Parameters:
                | 
                |         oMinorAxis[0]
                |             The length of the major axis 
                |         oMinorAxis[1]
                |             The length of the major axis

        :param tuple o_major_axis:
        :return: None
        """
        return self.com_object.GetMinorAxis(o_major_axis)

    def set_data(self, i_center_x: float, i_center_y: float, i_major_x: float, i_major_y: float, i_major_radius: float, i_minor_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetData(double iCenterX,double iCenterY,double iMajorX,double
                | iMajorY,double iMajorRadius,double iMinorRadius)
                |     Modifies the caracteristics of the ellipse.
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X Coordinate of the ellipse center 
                |         iCenterY
                |             The Y Coordinate of the ellipse center 
                |         iMajorX
                |             The X coordinate of the Major axis direction 
                |         iMajorY
                |             The Y coordinate of the Major axis direction 
                |         iMajorRadius
                |             The length of the major axis 
                |         iMinorRadius
                |             The length of the minor axis

        :param float i_center_x:
        :param float i_center_y:
        :param float i_major_x:
        :param float i_major_y:
        :param float i_major_radius:
        :param float i_minor_radius:
        :return: None
        """
        return self.com_object.SetData(i_center_x, i_center_y, i_major_x, i_major_y, i_major_radius, i_minor_radius)

    def __repr__(self):
        return f'Ellipse2D(name="{ self.name }")'
