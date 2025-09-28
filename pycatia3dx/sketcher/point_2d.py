"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.geometry_2d import Geometry2D


class Point2D(Geometry2D):

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
                |                             Point2D
                | 
                | Class defining a point in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_coordinates(self, o_point: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetCoordinates(CATSafeArrayVariant oPoint)
                |     Returns the coordinates of the point.
                | 
                |     Parameters:
                | 
                |         oPoint
                | 
                |               oPoint[0]: The X Coordinate of the point
                |               oPoint[1]The Y Coordinate of the point

        :param tuple o_point:
        :return: None
        """
        return self.com_object.GetCoordinates(o_point)

    def set_data(self, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetData(double iX,double iY)
                |     Modifies the coordinates of the point.
                | 
                |     Parameters:
                | 
                |         iX
                |             The X Coordinate of the point 
                |         iY
                |             The Y Coordinate of the point
                |             The Y Coordinate of the point

        :param float i_x:
        :param float i_y:
        :return: None
        """
        return self.com_object.SetData(i_x, i_y)

    def __repr__(self):
        return f'Point2D(name="{ self.name }")'
