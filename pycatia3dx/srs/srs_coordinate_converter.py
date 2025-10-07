"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SrsCoordinateConverter(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SrsCoordinateConverter
                | 
                | Object for SrsCoordinateConverter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def convert_absolute_coord_to_srs_coord(self, i_x: float, i_y: float, i_z: float, olu_srs_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ConvertAbsoluteCoordToSrsCoord(double iX,double iY,double
                | iZ,CATSafeArrayVariant oluSrsCoordinates)
                |     Convert Absolute Coordinate To SRS Coordinate
                | 
                |     Parameters:
                | 
                |         iX
                |             [in] X coordinate expressed in absolute coordinate (in mm).
                |             
                |         iY
                |             [in] Y coordinate expressed in absolute coordinate (in mm).
                |             
                |         iZ
                |             [in] Z coordinate expressed in absolute coordinate (in mm).
                |             
                |         oluSrsCoordinates
                |             [out] SRS Coordinates as a list of strings (Plane name + distance
                |             to plane) with correct units. The order of the output is CROSS, LONG, DECK.
                |             
                | 
                |     Returns:
                |         Error code of function.

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param tuple olu_srs_coordinates:
        :return: None
        """
        return self.com_object.ConvertAbsoluteCoordToSrsCoord(i_x, i_y, i_z, olu_srs_coordinates)

    def convert_srs_coord_to_absolute_coord(self, ilu_srs_coordinates: tuple, o_x: float, o_y: float, o_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ConvertSrsCoordToAbsoluteCoord(CATSafeArrayVariant iluSrsCoordinates,double
                | oX,double oY,double oZ)
                |     Convert SRS Coordinate To Absolute Coordinate
                | 
                |     Parameters:
                | 
                |         iluSrsCoordinates
                |             [in] SRS Coordinates as a list of strings (Plane name + distance to
                |             plane) with correct units. The order of the intput should be CROSS, LONG, DECK.
                |             
                |         oX
                |             [out] X coordinate expressed in absolute coordinate (in mm).
                |             
                |         oY
                |             [out] Y coordinate expressed in absolute coordinate (in mm).
                |             
                |         oZ
                |             [out] Z coordinate expressed in absolute coordinate (in mm).
                |             
                | 
                |     Returns:
                |         Error code of function. 

        :param tuple ilu_srs_coordinates:
        :param float o_x:
        :param float o_y:
        :param float o_z:
        :return: None
        """
        return self.com_object.ConvertSrsCoordToAbsoluteCoord(ilu_srs_coordinates, o_x, o_y, o_z)

    def __repr__(self):
        return f'SrsCoordinateConverter(name="{ self.name }")'
