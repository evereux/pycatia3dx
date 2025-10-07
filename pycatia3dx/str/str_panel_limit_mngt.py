"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.str_parameters import StrParameters


class StrPanelLimitMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrPanelLimitMngt
                | 
                | Object to manage Structure Functional Modeler limits for
                | Panel.
                | A limit can be:
                | - curve / surface
                | - Panel
                | - Profile
                | Role: To manage Panel's limits.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_limiting_object(self, i_index_limit: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLimitingObject(long iIndexLimit) As Reference
                |     Returns the Limiting Object on the Panel. Limiting Object Can be a
                |     geometric curves, surfaces or a SFD Profile, or a SFD
                |     Panel.
                | 
                |     Parameters:
                | 
                |         iIndexLimit
                |             Position of the limit to be retrieved. Provide default value -1
                |             
                | 
                |     Example:
                | 
                | 
                |              This example retrieves LimitingObject of the
                |              SfdPanel.
                |              
                | 
                |              Set RefLimitingObject = ObjStrPanelLimitMngt.GetLimitingObject(-1)

        :param int i_index_limit:
        :return: Reference
        """
        return Reference(self.com_object.GetLimitingObject(i_index_limit))

    def get_limiting_objects(self, o_limiting_objects: References, o_list_of_orientations: tuple, o_list_of_offset: StrParameters, o_list_of_limit_types: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLimitingObjects(References oLimitingObjects,CATSafeArrayVariant
                | oListOfOrientations,StrParameters oListOfOffset,CATSafeArrayVariant
                | oListOfLimitTypes)
                |     Returns the list of Limiting Objects, the limit orientations and the limit
                |     offsets on the Panel
                | 
                |     Parameters:
                | 
                |         oLimitingObjects
                |             Can be a geometric curves, surfaces or a SFD Profile, or a SFD
                |             Panel. The exported feature is retrieved if possible, otherwise the import.
                |             
                |         oListOfOrientations
                |             List of the Limit Orientations. 
                |         oListOfOffset
                |             List of the Limit offsets .list of knowledge parameters. see
                |             CATIAParameters. 
                |         oListOfLimitTypes
                |             List of the Limit types. 
                | 
                |     Example:
                | 
                | 
                |              This example sets LimitingObject for the
                |              SfdPanel.
                |              
                | 
                |               Dim LimitingObjects As References
                |               Dim Orientations() As Variant
                |               Dim ListOfOffsets As SfdParameters
                |               ObjStrPanelLimitMngt.GetLimitingObjects LimitingObjects,
                |               Orientations, ListOfOffsets

        :param References o_limiting_objects:
        :param tuple o_list_of_orientations:
        :param StrParameters o_list_of_offset:
        :param tuple o_list_of_limit_types:
        :return: tuple
        """
        return self.com_object.GetLimitingObjects(o_limiting_objects.com_object, o_list_of_orientations, o_list_of_offset.com_object, o_list_of_limit_types)

    def get_offset(self, i_index_limit: int) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOffset(long iIndexLimit) As Parameter
                |     Returns the Offset for a limit at the position iIndexLimit on the
                |     Panel.
                | 
                |     Parameters:
                | 
                |         iIndexLimit
                |             Position of the offset's limit.
                |             If iIndexLimit == -1 (default value): the last limit orientation is
                |             retrieved.
                |             If iIndexLimit > 0 : the index of the limit the user wish to retrieve. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the Offset of the last limit of
                |              panel.
                |              
                | 
                |               Dim OffsetParm As Parameter
                |               Set OffsetParm = ObjStrPanelLimitMngt.GetOffset -1

        :param int i_index_limit:
        :return: Parameter
        """
        return Parameter(self.com_object.GetOffset(i_index_limit))

    def get_orientation(self, i_index_limit: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrientation(long iIndexLimit) As long
                |     Returns the Orientation for a limit at the position iIndexLimit on the
                |     Panel.
                | 
                |     Parameters:
                | 
                |         iIndexLimit
                |             Position of the orientation's limit. If iIndexLimit == -1 (default value): the last limit orientation is retrieved. If iIndexLimit > 0 : the index of the limit the wish to retrieve.
                |             Orientation values can be:
                |             -1 = InvertOrientation
                |             0 = UnknownOrientation
                |             1 = SameOrientation
                |             2 = X+ ( X+ vector = ( 1, 0, 0) )
                |             3 = X- ( X- vector = (-1, 0, 0) )
                |             4 = Y+ ( Y+ vector = ( 0, 1, 0) )
                |             5 = Y- ( Y- vector = ( 0,-1, 0) )
                |             6 = Z+ ( Z+ vector = ( 0, 0, 1) )
                |             7 = Z- ( Z- vector = ( 0, 0,-1) )
                |             8 = Inside
                |             9 = Outside
                |             10 = Inboard ( Toward center line )
                |             11 = Outboard ( Opposite of previous one )
                |             12 = Inboard ( Toward midship )
                |             13 = Outboard ( Opposite of previous one ) 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the Orientation of the last limit of
                |              panel.
                |              
                | 
                |              lOrientation = ObjStrPanelLimitMngt.GetOrientation -1

        :param int i_index_limit:
        :return: int
        """
        return self.com_object.GetOrientation(i_index_limit)

    def invert_limit(self, i_index_limit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InvertLimit(long iIndexLimit)
                |     Inverts the Limit Orientation for a limit at the position iIndexLimit on
                |     the Panel.
                | 
                |     Parameters:
                | 
                |         iIndexLimit
                |             Position of the limit.
                |             If iIndexLimit == -1 (default value): the last limit orientation is
                |             inverted
                |             If iIndexLimit > 0 : the index of the limit orientation the user wish to invert. 
                | 
                |     Example:
                | 
                | 
                |              This example Inverts the last set limit of panel.
                |              
                | 
                |               ObjStrPanelLimitMngt.InvertLimit -1

        :param int i_index_limit:
        :return: None
        """
        return self.com_object.InvertLimit(i_index_limit)

    def remove_limit(self, i_index_limit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveLimit(long iIndexLimit)
                |     Removes the limit at the position iIndexLimit.
                | 
                |     Parameters:
                | 
                |         iIndexLimit
                |             Position of the Limit.
                |             if iIndexLimit = -1, the last Limit is removed
                |             if iIndexLimit = -99, all the limits are removed 
                | 
                |     Example:
                | 
                | 
                |              This example removes the last limit of the panel.
                |              
                | 
                |              Dim ObjStrPanelLimitMngt As StrPanelLimitMngt
                |              Set ObjStrPanelLimitMngt = ObjSfdPanel.StrPanelLimitMngt
                |              ObjStrPanelLimitMngt.RemoveLimit -1

        :param int i_index_limit:
        :return: None
        """
        return self.com_object.RemoveLimit(i_index_limit)

    def set_limiting_object(self, i_limiting_object: Reference, i_index_limit: int, i_orientation: int, i_limit_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLimitingObject(Reference iLimitingObject,long iIndexLimit,long
                | iOrientation,long iLimitType)
                |     Sets the Limiting Object on the Panel. The orientation is automatically
                |     computed.
                | 
                |     Parameters:
                | 
                |         iLimitingObject
                |             Limit Feature to be set on the panel Can be a geometric curves,
                |             surfaces or a SFD Profile, or a SFD Panel. 
                |         iIndexLimit
                | 
                |             If iIndexLimit == -1 (default value): the new limit is
                |             added.
                |             If iIndexLimit > 0 : the new limit is set at the position iIndexLimit. 
                |         iOrientation
                |             Current orientation of the plate limit. if iOrientation == 0, the
                |             value of the Orientation is automatically computed, depending on the value Set
                |             in the PRM ressources. We advised to use the default value, so that the
                |             automatic computation is performed. 
                |         iLimitType
                |             Cutting strategy.
                |             values :
                |             -1 - limit is undefined
                |             0 - ShortPoint
                |             1 - LongPoint
                |             2 - Weld 
                | 
                |     Example:
                | 
                | 
                |              This example sets LimitingObject for the
                |              SfdPanel.
                |              
                | 
                |              Set ObjLimit1 = ObjStrService.GetReferencePlane(ObjPart, 1, "DECK.6")
                |              Set Limit1 = ObjPart.CreateReferenceFromObject(ObjLimit1)
                |              ObjStrPanelLimitMngt.SetLimitingObject Limit1, -1, 0,
                |              2

        :param Reference i_limiting_object:
        :param int i_index_limit:
        :param int i_orientation:
        :param int i_limit_type:
        :return: None
        """
        return self.com_object.SetLimitingObject(i_limiting_object.com_object, i_index_limit, i_orientation, i_limit_type)

    def set_limiting_object2(self, i_limiting_object: Reference, i_index_limit: int, i_orientation: int, i_limit_type: int, i_key: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLimitingObject2(Reference iLimitingObject,long iIndexLimit,long
                | iOrientation,long iLimitType,CATBSTR iKey)
                |     Sets the Limiting Object on the Panel. The orientation is automatically
                |     computed.
                | 
                |     Parameters:
                | 
                |         iLimitingObject
                |             Limit Feature to be set on the panel Can be a geometric curves,
                |             surfaces or a SFD Profile, or a SFD Panel. 
                |         iIndexLimit
                | 
                |             If iIndexLimit == -1 (default value): the new limit is
                |             added.
                |             If iIndexLimit > 0 : the new limit is set at the position iIndexLimit. 
                |         iOrientation
                |             Current orientation of the plate limit. if iOrientation == 0, the
                |             value of the Orientation is automatically computed, depending on the value Set
                |             in the PRM ressources. We advised to use the default value, so that the
                |             automatic computation is performed. 
                |         iLimitType
                |             Cutting strategy.
                |             values :
                |             -1 - limit is undefined
                |             0 - ShortPoint
                |             1 - LongPoint
                |             2 - Weld 
                |         iKey
                |             Key corresponds the face of feature.
                |             values :
                |             2 - Plate (Corresponds to one face of the Plate)
                |             22 - Stiffener (Corresponds to top face of flange of the Stiffener)
                |             
                | 
                |     Example:
                | 
                | 
                |              This example sets LimitingObject for the
                |              SfdPanel.
                |              
                | 
                |              Set ObjLimit1 = ObjStrService.GetReferencePlane(ObjPart, 1, "DECK.6")
                |              Set Limit1 = ObjPart.CreateReferenceFromObject(ObjLimit1)
                |              ObjStrPanelLimitMngt.SetLimitingObject2 Limit1, -1, 0, 2,
                |              "22"

        :param Reference i_limiting_object:
        :param int i_index_limit:
        :param int i_orientation:
        :param int i_limit_type:
        :param str i_key:
        :return: None
        """
        return self.com_object.SetLimitingObject2(i_limiting_object.com_object, i_index_limit, i_orientation, i_limit_type, i_key)

    def __repr__(self):
        return f'StrPanelLimitMngt(name="{ self.name }")'
