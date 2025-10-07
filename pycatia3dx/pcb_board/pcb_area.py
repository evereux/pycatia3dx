"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class PcbArea(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PCBArea

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def area_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AreaType() As CATBSTR (Read Only)
                |     Gets the Type of a constraint area. The available values
                |     are:
                | 
                |         OTHER_OUTLINE
                |         ROUTE_OUTLINE
                |         PLACE_OUTLINE
                |         ROUTE_KEEPOUT
                |         PLACE_KEEPOUT
                |         PLACE_REGION
                |         VIA_KEEPOUT 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.AreaType

    @property
    def heightmax(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Heightmax() As double
                |     Gets and sets the Height max of the constraint area This property is valid
                |     for the following constraints areas:
                |     OTHER_OUTLINE,PLACE_REGION
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: float
        """

        return self.com_object.Heightmax

    @heightmax.setter
    def heightmax(self, value: float):
        """
        :param float value:
        """

        self.com_object.Heightmax = value

    @property
    def heightmin(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Heightmin() As double
                |     Gets and sets the Height min of the constraint area This property is valid
                |     for the following constraints areas: PLACE_KEEPOUT
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: float
        """

        return self.com_object.Heightmin

    @heightmin.setter
    def heightmin(self, value: float):
        """
        :param float value:
        """

        self.com_object.Heightmin = value

    @property
    def identifier(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Identifier() As CATBSTR
                |     Gets and sets the Identifier of the constraint area This property is valid
                |     for the following constraints areas:
                |     OTHER_OUTLINE,PLACE_REGION
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.Identifier

    @identifier.setter
    def identifier(self, value: str):
        """
        :param str value:
        """

        self.com_object.Identifier = value

    @property
    def layer(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LAYER() As CATBSTR (Read Only)
                |     Gets the position of a hole. The available values are :
                | 
                |         TOP
                |         BOTTOM
                |         BOTH
                |         INNER
                |         ALL It depends on the the type of the constraints area according to the
                |         IDF format. This property is valid for the following constraints
                |         areas:
                |             OTHER_OUTLINE
                |             ROUTING_OUTLINE
                |             PLACE_OUTLINE
                |             ROUTE_KEEPOUT
                |             PLACE_KEEPOUT
                |             PLACE_REGION 
                | 
                |         Returns:
                |                 The result of the method:
                |                 S_OK if succeeded
                |                 E_FAIL if failed

        :return: str
        """

        return self.com_object.LAYER

    @property
    def owner(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OWNER() As CATBSTR
                |     Gets and sets the OWNER of the constraint area The available values are
                |     MCAD,ECAD, UNOWNED
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.OWNER

    @owner.setter
    def owner(self, value: str):
        """
        :param str value:
        """

        self.com_object.OWNER = value

    def get_boardor_panel(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBoardorPanel() As CATBaseDispatch
                |     Gets the Board on which the constraint area lies.
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
        return self.com_object.GetBoardorPanel()

    def __repr__(self):
        return f'PcbArea(name="{ self.name }")'
