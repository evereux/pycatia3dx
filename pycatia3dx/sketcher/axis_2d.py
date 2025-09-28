"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.geometry_2d import Geometry2D
from pycatia3dx.sketcher.line_2d import Line2D
from pycatia3dx.sketcher.point_2d import Point2D


class Axis2D(Geometry2D):

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
                |                             Axis2D
                | 
                | Interface defining a coordinate system in the 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def horizontal_reference(self) -> Line2D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property HorizontalReference() As Line2D (Read Only)
                |     Returns the 2D coordinate system horizontal axis.
                | 
                |     Returns:
                |         oHorizontal The horizontal 2D line.

        :return: Line2D
        """

        return Line2D(self.com_object.HorizontalReference)

    @property
    def origin(self) -> Point2D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Origin() As Point2D (Read Only)
                |     Returns the 2D coordinate system origin.
                | 
                |     Returns:
                |         oOrigin The origin 2D point.

        :return: Point2D
        """

        return Point2D(self.com_object.Origin)

    @property
    def vertical_reference(self) -> Line2D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property VerticalReference() As Line2D (Read Only)
                |     Returns the 2D coordinate system vertical axis.
                | 
                |     Returns:
                |         oVertical The vertical 2D line.

        :return: Line2D
        """

        return Line2D(self.com_object.VerticalReference)

    def __repr__(self):
        return f'Axis2D(name="{ self.name }")'
