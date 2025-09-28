"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.curve_2d import Curve2D
from pycatia3dx.sketcher.point_2d import Point2D


class Circle2D(Curve2D):

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
                |                                 Circle2D
                | 
                | Class defining a circle in 2D Space.
    
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
                |     Returns or Sets the center point of the circle.
                | 
                |     Example:
                | 
                |          This example sets the center of  myCircle2D circle.
                |          
                | 
                |          Dim myPoint2D As Point2D
                |          myPoint2D = ...
                |          Dim myCircle2D As Circle2D
                |          myCircle2D.CenterPoint = myPoint2D

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
    def radius(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Radius() As double (Read Only)
                |     Returns the radius of the circle.
                | 
                |     Example:
                | 
                |          This example gets the radius of  myCircle2D circle.
                |          
                | 
                |          Dim myRadius As double
                |          Dim myCircle2D As Circle2D
                |          myRadius = myCircle2D.Radius

        :return: float
        """

        return self.com_object.Radius

    def get_center(self, o_data: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetCenter(CATSafeArrayVariant oData)
                |     Returns the center of the circle.
                | 
                |     Parameters:
                | 
                |         oData
                | 
                |              oData[0]: The X Coordinate of the circle center point
                |              
                |              oData[1]: The Y Coordinate of the circle center point
                |              
                |              
                | 
                |     Example:
                | 
                |          
                | 
                |          The following example reads the coordinates of the
                |          center
                |          of the circle myCircle2D:
                |          double center(1)
                |          myCircle2D.GetCenter center

        :param tuple o_data:
        :return: None
        """
        return self.com_object.GetCenter(o_data)

    def set_data(self, i_center_x: float, i_center_y: float, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetData(double iCenterX,double iCenterY,double iRadius)
                |     Modifies the caracteristics of the circle.
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X Coordinate of the circle center 
                |         iCenterY
                |             The Y Coordinate of the circle center 
                |         iRadius
                |             The radius of the circle

        :param float i_center_x:
        :param float i_center_y:
        :param float i_radius:
        :return: None
        """
        return self.com_object.SetData(i_center_x, i_center_y, i_radius)

    def __repr__(self):
        return f'Circle2D(name="{ self.name }")'
