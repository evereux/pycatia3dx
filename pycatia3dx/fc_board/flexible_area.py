"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class FlexibleArea(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FlexibleArea
                | 
                | Object representing a flexible constraint area.
    
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
                | Property AreaType() As CATBSTR
                |     Returns or sets the type of a flexible constraint area. The available
                |     values are:
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
                |         The result of the method:
                | 
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.AreaType

    @area_type.setter
    def area_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.AreaType = value

    @property
    def heightmax(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Heightmax() As double
                |     Returns or sets the maximum height of the flexible constraint area. This
                |     property is valid for the following constraints areas:
                | 
                |         OTHER_OUTLINE
                |         PLACE_REGION
                | 
                |     Returns:
                |         The result of the method:
                | 
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
                |     Returns or sets the minimum height of the flexible constraint area. This
                |     property is valid for the following constraints areas:
                | 
                |         PLACE_KEEPOUT
                | 
                |     Returns:
                |         The result of the method:
                | 
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
                |     Returns or sets the identifier of the flexible constraint area. This
                |     property is valid for the following constraints areas:
                | 
                |         OTHER_OUTLINE
                |         PLACE_REGION
                | 
                |     Returns:
                |         The result of the method:
                | 
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
                | Property LAYER() As CATBSTR
                |     Returns or sets the layer of the flexible constraint area. The available
                |     values are:
                | 
                |         STANDART
                |         BOTH
                |         INNER
                |         ALL
                | 
                |     It depends on the type of the constraints area according to the IDF format.
                |     This property is valid for the following constraints
                |     areas:
                | 
                |         OTHER_OUTLINE
                |         ROUTING_OUTLINE
                |         PLACE_OUTLINE
                |         ROUTE_KEEPOUT
                |         PLACE_KEEPOUT
                |         PLACE_REGION
                | 
                |     Returns:
                |         The result of the method:
                | 
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.LAYER

    @layer.setter
    def layer(self, value: str):
        """
        :param str value:
        """

        self.com_object.LAYER = value

    @property
    def owner(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OWNER() As CATBSTR
                |     Returns or sets the owner of the flexible constraint area. The available
                |     values are:
                | 
                |         MCAD
                |         ECAD
                |         UNOWNED
                | 
                |     Returns:
                |         The result of the method:
                | 
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

    def get_board(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBoard() As CATBaseDispatch
                |     Returns the Flexible Board on which the flexible constraint area
                |     lies.
                | 
                |     Parameters:
                | 
                |         The
                |             board reference 
                | 
                |     Returns:
                |         The result of the method:
                | 
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: AnyObject
        """
        return self.com_object.GetBoard()

    def get_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfile() As CATBaseDispatch
                |     Returns the profile of the flexible constraint area. The profile can be a
                |     Face of the flexible board or a sketch.
                | 
                |     Parameters:
                | 
                |         oProfileorFace
                |             The profile of the face input of the constraint area
                |             
                | 
                |     Returns:
                |         The result of the method:
                | 
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: AnyObject
        """
        return self.com_object.GetProfile()

    def set_profile(self, i_profileor_face: AnyObject, o_creation_view: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProfile(CATBaseDispatch iProfileorFace,CATBSTR
                | oCreationView)
                |     Sets the profile of the flexible constraint area. The profile can be a Face
                |     of the flexible board or a sketch.
                | 
                |     Parameters:
                | 
                |         iProfileorFace
                |             The profile of the face input of the constraint area
                |             
                |         oCreationView
                |             The view of the creation. The available values are MfDefault3DView
                |             or MfUnfoldedView 
                | 
                |     Returns:
                |         The result of the method:
                | 
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param AnyObject i_profileor_face:
        :param str o_creation_view:
        :return: None
        """
        return self.com_object.SetProfile(i_profileor_face.com_object, o_creation_view)

    def __repr__(self):
        return f'FlexibleArea(name="{self.name}")'
