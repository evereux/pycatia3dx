"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_del_robot_simulation.tag_point import TagPoint


class TagGroup(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TagGroup
                | 
                | Interface representing a Tag Group.
                | 
                | Role: This interface is used to retrieve/assign the attributes from the tag
                | group.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def owner(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Owner() As AnyObject (Read Only)
                |     This property returns the owner of the tag group
                | 
                |     Returns:
                |         oOwner The first occurrence of the owner.
                |     Example:
                | 
                |            
                | 
                |            Dim objTagGroup As TagGroup
                |                   ......
                |         Dim oOwner As AnyObject
                |         Set oOwner = objTagGroup.Owner

        :return: AnyObject
        """

        return AnyObject(self.com_object.Owner)

    @property
    def tag_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TagCount() As long (Read Only)
                |     This property returns the number of tags under the tag
                |     group
                | 
                |     Returns:
                |         oTagCount The number of tags under the tag group. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTagGroup As TagGroup
                |                   ......
                |         Dim oTagCount
                |         oTagCount = oTagGroup.TagCount

        :return: int
        """

        return self.com_object.TagCount

    @property
    def tag_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TagList() As CATSafeArrayVariant (Read Only)
                |     This property returns the tag list under the tag group
                | 
                |     Returns:
                |         oTagList The List of tags. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTagGroup As TagGroup
                |                   ......
                |         Dim oTagList
                |         oTagList = oTagGroup.TagList

        :return: tuple
        """

        return self.com_object.TagList

    def delete_tag(self, i_tag: TagPoint) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteTag(TagPoint iTag)
                |     Deletes a Tag
                | 
                |     Parameters:
                | 
                |         ioTag
                |             Tag to be deleted 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objTagGroup As TagGroup
                |                   ......
                |         Dim oTag As Tag
                |                   ......
                |         Call objTagGroup.DeleteTag(oTag)

        :param TagPoint i_tag:
        :return: None
        """
        return self.com_object.DeleteTag(i_tag.com_object)

    def empty(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Empty()
                |     Empties a Tag Group
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objTagGroup As TagGroup
                |                   ......
                |         Call objTagGroup.Empty

        :return: None
        """
        return self.com_object.Empty()

    def get_tag(self, index: int) -> TagPoint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTag(short index) As TagPoint
                |     Returns a Tag by Index.
                | 
                |     Parameters:
                | 
                |         index
                |             Index of the Required Tag. 
                | 
                |     Returns:
                |         oTag Returned Tag. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTagGroup As TagGroup
                |                   ......
                |         Dim oTag As Tag
                |         Dim iIndex As Integer
                |                   ......
                |         Set oTag = oTagGroup.GetTag(iIndex)
                |                   ......

        :param int index:
        :return: TagPoint
        """
        return TagPoint(self.com_object.GetTag(index))

    def __repr__(self):
        return f'TagGroup(name="{ self.name }")'
