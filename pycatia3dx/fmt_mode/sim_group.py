"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class SimGroup(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGroup
                | 
                | Represents a simulation group.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def entity_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EntityType() As SimMeshEntityType
                |     Sets or retrieves the simulation entities type captured by the
                |     group.
                |     The group entity must be initialized before any update of feature.

        :return: int
        """

        return self.com_object.EntityType

    @entity_type.setter
    def entity_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.EntityType = value

    @property
    def group_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GroupType() As CATBSTR (Read Only)
                |     Retrieves the type of group. SimGroups

        :return: str
        """

        return self.com_object.GroupType

    @property
    def number_of_entities(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfEntities() As short (Read Only)
                |     Retrieves the number of entities that have been captured by the group.

        :return: int
        """

        return self.com_object.NumberOfEntities

    def add_boundary(self, i_boundary: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddBoundary(AnyObject iBoundary)
                |     Creates a new boundary and add it into the boundary description of the
                |     simulation group.
                |     Only available for simulation group by boundary.
                | 
                |     Parameters:
                | 
                |         iBoundary:
                |             The object that represents the boundary geometry to add.

        :param AnyObject i_boundary:
        :return: None
        """
        return self.com_object.AddBoundary(i_boundary.com_object)

    def get_attribute_value(self, i_attribute: str, o_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAttributeValue(CATBSTR iAttribute,CATVariant oValue)
                |     Retrieves the value corresponding to the given attribute.
                | 
                |     Parameters:
                | 
                |         iAttribute:
                |             The name of attribute. 
                | 
                |     Returns:
                |         The value of the attribute.

        :param str i_attribute:
        :param CATVariant o_value:
        :return: None
        """
        return self.com_object.GetAttributeValue(i_attribute, o_value)

    def get_numbering_labels(self, i_type: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberingLabels(SimMeshEntityType iType) As
                | CATSafeArrayVariant
                |     Retrieves all the numbering labels of current object
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of mesh entity: simMeshNodeEntity or simMeshElementEntity.

        :param int i_type:
        :return: tuple
        """
        return self.com_object.GetNumberingLabels(i_type)

    def remove_boundary(self, i_boundary: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveBoundary(AnyObject iBoundary)
                |     Removes a boundary to the boundary description of the simulation
                |     group.
                |     Only available for simulation group by boundary.
                | 
                |     Parameters:
                | 
                |         iBoundary:
                |             The object that represents the boundary geometry to remove.

        :param AnyObject i_boundary:
        :return: None
        """
        return self.com_object.RemoveBoundary(i_boundary.com_object)

    def remove_numbering(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveNumbering()
                |     Removes numbering specification.

        :return: None
        """
        return self.com_object.RemoveNumbering()

    def set_attribute_value(self, i_attribute_name: str, i_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttributeValue(CATBSTR iAttributeName,CATVariant
                | iValue)
                |     Sets the value corresponding to the given attribute.
                | 
                |     Parameters:
                | 
                |         iAttribute:
                |             The name of attribute. 
                |         iValue:
                |             The value of the attribute.

        :param str i_attribute_name:
        :param CATVariant i_value:
        :return: None
        """
        return self.com_object.SetAttributeValue(i_attribute_name, i_value)

    def set_group_type(self, i_group_type: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGroupType(CATBSTR iGroupType)
                | 
                |     Deprecated:
                |         R427 : Use EntityType property instead. Sets the type of the simulation group.
                |         This method must initialize the group content type before any update of
                |         feature. 
                |     Parameters:
                | 
                |         iGroupType:
                |             The type of the group.

        :param str i_group_type:
        :return: None
        """
        return self.com_object.SetGroupType(i_group_type)

    def __repr__(self):
        return f'SimGroup(name="{self.name}")'
