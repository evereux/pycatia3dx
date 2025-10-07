"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.part.hole import Hole
from pycatia3dx.part.pad import Pad
from pycatia3dx.part.pattern import Pattern
from pycatia3dx.system.any_object import AnyObject


class PcbBoard(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PCBBoard

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def owner(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Owner() As CATBSTR
                |     Gets and sets the attribute owner of a Panel or a Board. The possible
                |     values are MCAD,ECAD,UNKNOWN.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: str
        """

        return self.com_object.Owner

    @owner.setter
    def owner(self, value: str):
        """
        :param str value:
        """

        self.com_object.Owner = value

    @property
    def part(self) -> Pad:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Part() As Pad
                |     Sets the pad of a Board or a Component or a Panel.

        :return: Pad
        """

        return Pad(self.com_object.Part)

    @part.setter
    def part(self, value: Pad):
        """
        :param Pad value:
        """

        self.com_object.Part = value

    def create_pcbhole(self, i_hole: Hole, iplating_style: str, i_associated_part_name: str, i_hole_type: str, i_hole_owner: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub create_pcbhole(Hole iHole,CATBSTR iplatingStyle,CATBSTR
                | iAssociatedPartName,CATBSTR iHoleType,CATBSTR iHoleOwner)
                |     Adds a Pcb hole to a board or a panel.
                | 
                |     Parameters:
                | 
                |         iHole
                |             This parameter represents the hole to transform in Pcb hole
                |             
                |         iplatingStyle
                |             This parameter represents the plating style of the hole. The
                |             differents values are PTH or NPTH 
                |         iAssociatedPartName
                |             This parameter represents name of the associated part to the
                |             hole.
                | 
                |                 The possible values are:
                |                 the name of the instance of component in which the hole is
                |                 defined.
                |                 BOARD if the hole is defined in the Board part
                |                 PANEL If the hole is defined in the Panel part
                |                 NOREFDES is the hole is defined in a non Electronic Part
                |                 
                | 
                |         iHoleType
                |             This parameter represents the function of the
                |             hole.
                | 
                |                 The possible values are:
                |                 PIN if the hole is associated with a component
                |                 pin
                |                 VIA if the hole is associated with a conductive
                |                 via
                |                 TOOL if the hole is used for tooling purposes
                |                 Other ( User defined ) 
                | 
                |         iHoleOwner
                |             The parameter represents the owner of the hole. The possible values are : MCAD, ECAD, UNOWNED 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param Hole i_hole:
        :param str iplating_style:
        :param str i_associated_part_name:
        :param str i_hole_type:
        :param str i_hole_owner:
        :return: None
        """
        return self.com_object.create_pcbhole(i_hole.com_object, iplating_style, i_associated_part_name, i_hole_type, i_hole_owner)

    def create_pcbpattern(self, i_pattern: Pattern, iplating_style: str, i_associated_part_name: str, i_hole_type: str, i_hole_owner: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub create_pcbpattern(Pattern iPattern,CATBSTR iplatingStyle,CATBSTR
                | iAssociatedPartName,CATBSTR iHoleType,CATBSTR iHoleOwner)
                |     Adds a Pcb pattern of hole to a board or a panel. If the motif hole of the
                |     pattern is pcb hole, the input value are not taken into
                |     account.
                | 
                |     Parameters:
                | 
                |         iPattern
                |             This parameter represents the Pattern to transform in Pcb Pattern.
                |             
                |         iplatingStyle
                |             This parameter represents the plating style of the pattern. The
                |             differents values are PTH or NPTH 
                |         iAssociatedPartName
                |             This parameter represents name of the associated part to the
                |             pattern.
                | 
                |                 The possible values are:
                |                 the name of the instance of component in which the pattern is
                |                 defined.
                |                 BOARD if the pattern is defined in the Board
                |                 part
                |                 PANEL If the pattern is defined in the Panel
                |                 part
                |                 NOREFDES is the pattern is defined in a non Electronic Part
                |                 
                | 
                |         iHoleType
                |             This parameter represents the function of the
                |             hole.
                | 
                |                 The possible values are:
                |                 PIN if the pattern is associated with a component
                |                 pin
                |                 VIA if the pattern is associated with a conductive
                |                 via
                |                 TOOL if the pattern is used for tooling
                |                 purposes
                |                 Other ( User defined ) 
                | 
                |         iHoleOwner
                |             The parameter represents the owner of the pattern. The possible values are : MCAD, ECAD, UNOWNED 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param Pattern i_pattern:
        :param str iplating_style:
        :param str i_associated_part_name:
        :param str i_hole_type:
        :param str i_hole_owner:
        :return: None
        """
        return self.com_object.create_pcbpattern(i_pattern.com_object, iplating_style, i_associated_part_name, i_hole_type, i_hole_owner)

    def create_zone(self, zonetype: str, i_pad: Pad) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub create_zone(CATBSTR zonetype,Pad iPad)
                |     Adds a constraint area to a board.
                | 
                |     Parameters:
                | 
                |         zonetype
                |             This parameter represents the type of the zone to
                |             create
                | 
                |                 The possible values are:
                |                 ROUTE_OUTLINE
                |                 PLACE_OUTLINE
                |                 OTHER_OUTLINE
                |                 VIA_KEEPOUT
                |                 PLACE_KEEPOUT
                |                 PLACE_REGION
                |                 ROUTE_KEEPOUT 
                | 
                |         iPad
                |             The pad shape on which the constraint area is added.
                |             
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed 

        :param str zonetype:
        :param Pad i_pad:
        :return: None
        """
        return self.com_object.create_zone(zonetype, i_pad.com_object)

    def __repr__(self):
        return f'PcbBoard(name="{ self.name }")'
