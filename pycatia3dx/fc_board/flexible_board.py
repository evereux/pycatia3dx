"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class FlexibleBoard(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FlexibleBoard

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_flexible_area_area(self, i_father: Body, i_view_of_creation: str, i_profileor_face: AnyObject,
                                  i_type: str, i_layer: str, i_identifier: str, i_owner: str, i_max: float,
                                  i_min: float) -> FlexibleArea:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func create_FlexibleAreaArea(Body iFather,CATBSTR
                | iViewOfCreation,CATBaseDispatch iProfileorFace,CATBSTR iType,CATBSTR
                | iLayer,CATBSTR iIdentifier,CATBSTR iOwner,double iMax,double iMin) As
                | FlexibleArea
                |     Creates a flexible constraint area on a flexible board.
                | 
                |     Parameters:
                | 
                |         iFather
                |             the body under which the constraint area will be created
                |             
                |         iViewOfCreation
                |             the view of creation of the flexible board. The possible value are
                |             MfUnfoldedView and MfDefault3DView 
                |         iProfileorFace
                |             iProfile or Face of the constraint area 
                |         iType
                |             Type of the constraint area ( ROUTE_OUTLINE,PLACE_OUTLINE,
                |             OTHER_OUTLINE, VIA_KEEPOUT, PLACE_KEEPOUT, PLACE_REGION,ROUTE_KEEPOUT)
                |             
                |         iLayer
                |             Layer convering of the Constraint area ( can be standart, both,
                |             inner, All 
                |         iIdentifier
                |             iIdentifier of the constraint area 
                |         iOwner
                |             Owner of the constraint area ( ECAD or MCAD ) 
                |         iMax
                |             Height Max of Constraint area 
                |         iMin
                |             Height Min of Constraint area 
                |         oConstraintArea
                |             The Constraint area created 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param Body i_father:
        :param str i_view_of_creation:
        :param AnyObject i_profileor_face:
        :param str i_type:
        :param str i_layer:
        :param str i_identifier:
        :param str i_owner:
        :param float i_max:
        :param float i_min:
        :return: FlexibleArea
        """
        return FlexibleArea(self.com_object.create_FlexibleAreaArea(i_father.com_object, i_view_of_creation,
                                                                    i_profileor_face.com_object, i_type, i_layer,
                                                                    i_identifier, i_owner, i_max, i_min))

    def create_hole(self, i_view_of_creation: str, i_diametre: float, i_x: float, i_y: float, i_type: str,
                    i_associated_part: str, i_owner: str, i_plating_style: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func create_Hole(CATBSTR iViewOfCreation,double iDiametre,double iX,double
                | iY,CATBSTR iType,CATBSTR iAssociatedPart,CATBSTR iOwner,CATBSTR iPlatingStyle)
                | As CATBaseDispatch
                |     Adds a SM hole on the board.
                | 
                |     Parameters:
                | 
                |         iViewOfCreation
                |             The view for creating the Hole 
                |         iDiametre;
                |             Diameter of the hole 
                |         iX
                |             X coordinate of the center of the hole in the input view
                |             
                |         iY
                |             Y coordinate of the center of the hole in the input view
                |             
                |         iZ
                |             Z coordinate of the center of the hole in the input view
                |             
                |         iType;
                |             Type of the hole
                | 
                |                 The possible values are :
                |                 PIN if the hole is associated with a component
                |                 pin
                |                 VIA if the hole is associated with a conductive
                |                 via
                |                 MTG if the hole is used for mounting purposes
                |                 TOOL if the hole is used for tooling purposes
                |                 Other ( User defined ) 
                | 
                |         iAssociatedPart
                |             The Associated Part of the hole:
                | 
                |                 The possible values are :
                |                 the name of the instance of component in which the hole is
                |                 defined.
                |                 BOARD if the hole is defined in the Board part
                |                 PANEL If the hole is defined in the Panel part
                |                 NOREFDES is the hole is defined in a non Electronic Part.
                |                 
                | 
                |         iOwner
                |             The available values are MCAD,ECAD, UNOWNED 
                |         iPlatingStyle
                |             Set the Plating Style of a hole The available values are: PTH, NPTH
                |             
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param str i_view_of_creation:
        :param float i_diametre:
        :param float i_x:
        :param float i_y:
        :param str i_type:
        :param str i_associated_part:
        :param str i_owner:
        :param str i_plating_style:
        :return: AnyObject
        """
        return self.com_object.create_Hole(i_view_of_creation, i_diametre, i_x, i_y, i_type, i_associated_part, i_owner,
                                           i_plating_style)

    def place_component(self, i_view_of_placement: str, i_component_instance: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub place_Component(CATBSTR iViewOfPlacement,CATBaseDispatch
                | iComponentInstance)
                |     Places a component on a flexible Board.
                | 
                |     Parameters:
                | 
                |         iViewOfPlacement
                |             the view for placing of the component 
                |         iViewOfPlacement
                |             The first instance of the component 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed 
                | 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param str i_view_of_placement:
        :param AnyObject i_component_instance:
        :return: None
        """
        return self.com_object.place_Component(i_view_of_placement, i_component_instance.com_object)

    def __repr__(self):
        return f'FlexibleBoard(name="{self.name}")'
