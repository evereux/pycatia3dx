"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingMachineMotion(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingMachineMotion
                | 
                | Interface dedicated to machine positioning.
                | Role: This interface offers services to move the machine at applicative
                | positions.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def move_to(self, i_position_coordinates: tuple, i_direction_coordinates: tuple) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func MoveTo(CATSafeArrayVariant iPositionCoordinates,CATSafeArrayVariant
                | iDirectionCoordinates) As boolean
                |     Move the current machine at given position.
                | 
                |     Parameters:
                | 
                |         iPositionCoordinates
                |             The point where to move the machine, as an array of 3 values.
                |             
                |         iDirectionCoordinates
                |             The axial direction where to move the machine, as an array of 3
                |             values. 
                |         obIsReachable
                |             Get whether the position is reachable. 
                | 
                |     Returns:
                |         Return code.
                |         Legal values:
                | 
                |             S_OK: move is successful
                |             E_FAIL: otherwise

        :param tuple i_position_coordinates:
        :param tuple i_direction_coordinates:
        :return: bool
        """
        return self.com_object.MoveTo(i_position_coordinates, i_direction_coordinates)

    def move_to_manufacturing_fastener(self, i_manufacturing_fastener: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func MoveToManufacturingFastener(AnyObject iManufacturingFastener) As
                | boolean
                |     Move the current machine at position of given manufacturing
                |     fastener.
                | 
                |     Parameters:
                | 
                |         iManufacturingFastener
                |             The manufacturing fastener where to move the machine.
                |             
                |         obIsReachable
                |             Get whether the position is reachable.

        :param AnyObject i_manufacturing_fastener:
        :return: bool
        """
        return self.com_object.MoveToManufacturingFastener(i_manufacturing_fastener.com_object)

    def restore_position(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RestorePosition()
                |     Restore the machine at its original position.

        :return: None
        """
        return self.com_object.RestorePosition()

    def __repr__(self):
        return f'ManufacturingMachineMotion(name="{ self.name }")'
