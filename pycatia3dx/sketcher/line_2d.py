"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.curve_2d import Curve2D


class Line2D(Curve2D):

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
                |                                 Line2D
                | 
                | Class defining a line in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_direction(self, o_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetDirection(CATSafeArrayVariant oDirection)
                |     Returns the unit-vector pointing in the direction of the
                |     line.
                | 
                |     Parameters:
                | 
                |         oDirection
                | 
                |               oDirection[0]: The X Coordinate of the unit vector pointing in
                |               the 
                |               direction of the line
                |               oDirection[1]
                |               oDirection[1] The Y Coordinate of the unit vector pointing in
                |               the
                |               direction of the line

        :param tuple o_direction:
        :return: None
        """
        return self.com_object.GetDirection(o_direction)

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetOrigin(CATSafeArrayVariant oOrigin)
                |     Returns a point lying on the line.
                | 
                |     Parameters:
                | 
                |         oPoint
                | 
                |               oPoint[0]: The X Coordinate of a point lying on the
                |               line
                |               oPoint[1]: The Y Coordinate of a point lying on the
                |               line

        :param tuple o_origin:
        :return: None
        """
        return self.com_object.GetOrigin(o_origin)

    def set_data(self, i_x: float, i_y: float, i_x_direction: float, i_y_direction: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetData(double iX,double iY,double iXDirection,double
                | iYDirection)
                |     Modifies the caracteristics of the infinite line.
                | 
                |     Parameters:
                | 
                |         iX
                |             The X Coordinate of a point lying on the line 
                |         iY
                |             The Y Coordinate of a point lying on the line 
                |         iXDirection
                |             The X Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         iYDirection
                |             The Y Coordinate of the unit vector pointing in the direction of
                |             the line

        :param float i_x:
        :param float i_y:
        :param float i_x_direction:
        :param float i_y_direction:
        :return: None
        """
        return self.com_object.SetData(i_x, i_y, i_x_direction, i_y_direction)

    def __repr__(self):
        return f'Line2D(name="{ self.name }")'
