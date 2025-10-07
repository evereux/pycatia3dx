"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class StrAdvPanel(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrAdvPanel
                | 
                | Object to filter the Structure Advanced Panel.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def set_as_last_limit(self, i_position_of_limit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAsLastLimit(long iPositionOfLimit)
                |     Sets a limit to the last position in the list of limits.
                | 
                |     Parameters:
                | 
                |         iPositionOfLimit
                |             Index of the limit to promote. 
                | 
                |     Example:
                | 
                | 
                |              This example Sets 3rd limit as the last limit of the Advanced
                |              Panel.
                |              
                | 
                |              Dim ObjStrAdvPanel As StrAdvPanel
                |              Set ObjStrAdvPanel = ObjSfdPanel.StrAdvPanel
                |              ObjStrAdvPanel.SetAsLastLimit 3

        :param int i_position_of_limit:
        :return: None
        """
        return self.com_object.SetAsLastLimit(i_position_of_limit)

    def __repr__(self):
        return f'StrAdvPanel(name="{ self.name }")'
