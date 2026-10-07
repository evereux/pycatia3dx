"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.system.any_object import AnyObject


class FCBService(Service):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         FCBService

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_flexible_board(self, i_part: Part, i_create_axissystem: bool) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateFlexibleBoard(Part iPart,boolean iCreateAxissystem) As
                | CATBaseDispatch
                |     Creates a Flexible Board.
                | 
                |     Parameters:
                | 
                |         iPart
                |             Mechanical Part that will become a flexible board.
                |             
                |         iCreateAxissystem
                |             if true, the axis system is automatically created 
                |         oFlexibleBoard
                |             The Flexible board created 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param Part i_part:
        :param bool i_create_axissystem:
        :return: AnyObject
        """
        return self.com_object.CreateFlexibleBoard(i_part.com_object, i_create_axissystem)

    def get_flexible_board(self, i_part: Part) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFlexibleBoard(Part iPart) As CATBaseDispatch
                |     Gets the flexible board from the CATIAPart
                | 
                |     Parameters:
                | 
                |         iPart
                |             Mechanical Part that will become a flexible board.
                |             
                |         oFlexibleBoard
                |             The Flexible board 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param Part i_part:
        :return: AnyObject
        """
        return self.com_object.GetFlexibleBoard(i_part.com_object)

    def __repr__(self):
        return f'FcbService(name="{self.name}")'
