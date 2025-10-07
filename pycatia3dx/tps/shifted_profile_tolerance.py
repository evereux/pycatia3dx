"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ShiftedProfileTolerance(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ShiftedProfileTolerance
                | 
                | Interface for accessing shifted tolerance zone informations of a
                | TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def shift_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShiftValue() As double
                |     Retrieves or sets shift value of tolerance zone (in millimeters). The shift
                |     value is the distance between the toleranced surface and the median surface of
                |     tolerance zone. The value is always positive because shift side is given by
                |     GetShiftSide method.

        :return: float
        """

        return self.com_object.ShiftValue

    @shift_value.setter
    def shift_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.ShiftValue = value

    def get_shift_direction(self, op_direction: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetShiftDirection(CATSafeArrayVariant opDirection)
                |     Retrieves the shift direction by two points.
                | 
                |     Parameters:
                | 
                |         opDirection
                |             The first 3 values of opDirection correspond to the X,Y and Z
                |             values of the start point respectively and the next 3 values correspond to the
                |             X, Y and Z values of the end point respectively. 
                | 
                |     Example:
                | 
                |          This example gets the start and end points in a VB
                |          Script
                |          Dim oTab(6) As CATSafeArrayVariant
                |          Set shiftTol = annotation.ShiftedProfileTolerance
                |          shiftTol.GetShiftDirection(oTab)
                |          oStream.Write "      Shifted Direction Start Point : "& oTab(0) & " " & oTab(1) & " " & oTab(2) & sLF
                |          oStream.Write "      Shifted Direction End Point : "& oTab(3) & " " & oTab(4) & " " & oTab(5) & sLF

        :param tuple op_direction:
        :return: tuple
        """
        return self.com_object.GetShiftDirection(op_direction)

    def get_shift_side(self, op_point: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetShiftSide(CATSafeArrayVariant opPoint)
                |     Retrieves shift side.
                | 
                |     Parameters:
                | 
                |         opPoint
                |             a mathematical point located on the shift side of surface. The 3
                |             values of opPoint correspond to the X,Y and Z values of the point located on
                |             the shift side of surface. 
                | 
                |     Example:
                | 
                |          This example gets the shift side point in a VB Script
                |          Dim oShiftTab(3) As CATSafeArrayVariant
                |          Set shiftTol = annotation.ShiftedProfileTolerance
                |          shiftTol.GetShiftSide(oShiftTab)
                |          oStream.Write "      Shifted Side Point : "& oShiftTab(0) & " " & oShiftTab(1) & " " & oShiftTab(2) & sLF

        :param tuple op_point:
        :return: tuple
        """
        return self.com_object.GetShiftSide(op_point)

    def __repr__(self):
        return f'ShiftedProfileTolerance(name="{ self.name }")'
