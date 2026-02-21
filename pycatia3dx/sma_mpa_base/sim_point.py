"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimPoint(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimPoint
                | 
                | Represents the Point object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def point_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PointType() As SimPointDefinitionMode
                |     Returns or sets the type of point.

        :return: int
        """

        return self.com_object.PointType

    @point_type.setter
    def point_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.PointType = value

    def get_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCoordinates(double oX1,double oX2,double oX3)
                |     Retrieves the coordinates of the point.
                | 
                |     Parameters:
                | 
                |         oX1[out]
                |             The X coordinate of the point. 
                |         oX2[out]
                |             The Y coordinate of the point. 
                |         oX3[out]
                |             The Z coordinate of the point.

        :return: tuple
        """
        # todo: check this method, does it require system service?
        return self.com_object.GetCoordinates()

    def set_coordinates(self, i_x1: float, i_x2: float, i_x3: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCoordinates(double iX1,double iX2,double iX3)
                |     Sets the coordinates of the point. Works only if
                |     TypeEnum==Coordinates
                | 
                |     Parameters:
                | 
                |         iX1[in]
                |             The X coordinate of the point. 
                |         iX2[in]
                |             The Y coordinate of the point. 
                |         iX3[in]
                |             The Z coordinate of the point. 
                | 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param float i_x1:
        :param float i_x2:
        :param float i_x3:
        :return: None
        """
        return self.com_object.SetCoordinates(i_x1, i_x2, i_x3)

    def __repr__(self):
        return f'SimPoint(name="{self.name}")'
