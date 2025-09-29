"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class FCBHole(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FCBHole

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def associated_part_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AssociatedPartName() As CATBSTR
                |     Gets and sets the Associated Part of the hole.
                | 
                |         The possible values are:
                |         the name of the instance of component in which the hole is
                |         defined.
                |         BOARD if the hole is defined in the Board part
                |         PANEL If the hole is defined in the Panel part
                |         NOREFDES is the hole is defined in a non Electronic Part.
                |         
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.AssociatedPartName

    @associated_part_name.setter
    def associated_part_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.AssociatedPartName = value

    @property
    def hole_owner(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HoleOwner() As CATBSTR
                |     Gets and sets the owner of the hole.
                | 
                |         The possible value are:
                |         MCAD
                |         ECAD
                |         UNOWNED. 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.HoleOwner

    @hole_owner.setter
    def hole_owner(self, value: str):
        """
        :param str value:
        """

        self.com_object.HoleOwner = value

    @property
    def hole_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HoleType() As CATBSTR
                |     Gets and sets the function of the hole.
                | 
                |         The possible values are :
                |         PIN if the hole is associated with a component pin
                |         VIA if the hole is associated with a conductive via
                |         MTG if the hole is used for mounting purposes
                |         TOOL if the hole is used for tooling purposes
                |         Other ( User defined ) 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.HoleType

    @hole_type.setter
    def hole_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.HoleType = value

    @property
    def plating_style(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlatingStyle() As CATBSTR
                |     Gets and sets the Plating Style of a hole.
                | 
                |         The possible values are:
                |         PTH
                |         NPTH 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.PlatingStyle

    @plating_style.setter
    def plating_style(self, value: str):
        """
        :param str value:
        """

        self.com_object.PlatingStyle = value

    def get_board(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBoard() As CATBaseDispatch
                |     Gets the Board drilled by the hole.
                | 
                |     Parameters:
                | 
                |         oBoard
                |             The board reference 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: AnyObject
        """
        return self.com_object.GetBoard()

    def __repr__(self):
        return f'FcbHole(name="{self.name}")'
