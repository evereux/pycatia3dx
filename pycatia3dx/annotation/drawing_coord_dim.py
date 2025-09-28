"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_text_properties import DrawingTextProperties
from pycatia3dx.system.any_object import AnyObject


class DrawingCoordDim(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingCoordDim
                | 
                | Represents a drawing Coordinate Dimension in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Angle() As double
                |     Returns or sets the angle of the drawing coordinate dimension. The angle is
                |     measured between the axis system of the drawing view and the local axis system
                |     of the drawing coordinate dimension. The angle is measured in radians and is
                |     counted counterclockwise.
                | 
                |     Example:
                |         This example sets the angle of the MyCoordDim drawing Text to 90
                |         degrees clockwise. You first need to compute the angle in degrees and set the
                |         minus sign to indicate the rotation is clockwise.
                | 
                |          Angle90Clockwise = -90
                |          MyCoordDim.Angle = Angle90Clockwise

        :return: float
        """

        return self.com_object.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.Angle = value

    @property
    def text_properties(self) -> DrawingTextProperties:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TextProperties() As DrawingTextProperties (Read Only)
                |     Returns the text properties of the drawing coordinate
                |     dimension.
                | 
                |     Example:
                |         This example retrieves in TextProperties the text properties of the
                |         MyCoordDim drawing coordinate dimension..
                | 
                |          Dim TextProperties As DrawingTextProperties
                |          Set TextProperties = MyCoordDim.TextProperties

        :return: DrawingTextProperties
        """

        return DrawingTextProperties(self.com_object.TextProperties)

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property x() As double
                |     Returns or sets the x coordinate of the drawing coordinate dimension. It is
                |     expressed with respect to the current view coordinate system. This coordinate,
                |     like any length, is measured in millimeters.
                | 
                |     Example:
                |         This example retrieves in X the x coordinate of the MyCoordDim drawing
                |         coordinate dimension.
                | 
                |          X = MyCoordDim.x

        :return: float
        """

        return self.com_object.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.com_object.x = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property y() As double
                |     Returns or sets the y coordinate of the drawing coordinate dimension. It is
                |     expressed with respect to the current view coordinate system. This coordinate,
                |     like any length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the y coordinate of the MyCoordDim drawing coordinate
                |         dimension to 5 inches. You need first to convert the 5 inches into
                |         millmeters.
                | 
                |          NewYCoordinate = 5*25.4/1000
                |          MyCoordDim.y = NewYCoordinate

        :return: float
        """

        return self.com_object.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.com_object.y = value

    def get_coord_values(self, o_type: int, o_x: float, o_y: float, o_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetCoordValues(long oType,double oX,double oY,double oZ)
                |     Returns the value of the drawing coordinate dimension.
                | 
                |     Parameters:
                | 
                |         oType
                |             oType (0: 2D coordinate dimension, 1: 3D coordinate dimension).
                |             
                |         oX
                |             X value. 
                |         oY
                |             Y value. 
                |         oZ
                |             Z value (=0. if 2D coordinate dimension).
                | 
                |             Example:
                |                 This example gets the type, x, y and z of the MyCoordDim
                |                 drawing CoordDim
                | 
                |                  MyCoordDim.GetCoordValues(oType, oX, oY, oZ)

        :param int o_type:
        :param float o_x:
        :param float o_y:
        :param float o_z:
        :return: None
        """
        return self.com_object.GetCoordValues(o_type, o_x, o_y, o_z)

    def __repr__(self):
        return f'DrawingCoordDim(name="{ self.name }")'
