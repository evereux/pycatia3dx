"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.curve_2d import Curve2D


class Parabola2D(Curve2D):

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
                |                                 Parabola2D
                | 
                | Class defining an parabola in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def focal_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property FocalDistance() As double (Read Only)
                |     Returns the focal distance of the parabola in 2D space.
                | 
                |     Returns:
                |         oFocal The focal distance of the parabola

        :return: float
        """

        return self.com_object.FocalDistance

    def get_axis(self, o_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetAxis(CATSafeArrayVariant oAxis)
                |     Returns the axis vector direction of the parabola in 2D
                |     space.
                | 
                |     Parameters:
                | 
                |         oAxis
                | 
                |               oAxis[0]: The X coordinate of the axis vector
                |               direction
                |               oAxis[1]: The Y coordinate of the axis vector
                |               direction

        :param tuple o_axis:
        :return: None
        """
        return self.com_object.GetAxis(o_axis)

    def get_center(self, o_center: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetCenter(CATSafeArrayVariant oCenter)
                |     Returns the center of the parabola in 2D space.
                | 
                |     Parameters:
                | 
                |         oCenter
                | 
                |               oCenter[0]: The X Coordinate of the center point of the
                |               parabola
                |               oCenter[1]: The Y Coordinate of the center point of the
                |               parabola

        :param tuple o_center:
        :return: None
        """
        return self.com_object.GetCenter(o_center)

    def set_data(self, i_center_x: float, i_center_y: float, i_axis_x: float, i_axis_y: float, i_focal_distance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub SetData(double iCenterX,double iCenterY,double iAxisX,double iAxisY,double
                | iFocalDistance)
                |     Modifies the caracteristics of the parabola.
                | 
                |     Parameters:
                | 
                |         iCenterX
                |             The X Coordinate of the parabola center 
                |         iCenterY
                |             The Y Coordinate of the parabola center 
                |         iAxisX
                |             The X coordinate of the axis vector direction 
                |         iAxisY
                |             The Y coordinate of the axis vector direction 
                |         iFocalDistance
                |             The focal distance of the parabola

        :param float i_center_x:
        :param float i_center_y:
        :param float i_axis_x:
        :param float i_axis_y:
        :param float i_focal_distance:
        :return: None
        """
        return self.com_object.SetData(i_center_x, i_center_y, i_axis_x, i_axis_y, i_focal_distance)

    def __repr__(self):
        return f'Parabola2D(name="{ self.name }")'
