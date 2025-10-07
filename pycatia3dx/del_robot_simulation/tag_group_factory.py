"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_robot_simulation.tag_group import TagGroup


class TagGroupFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TagGroupFactory
                | 
                | Interface representing a TagGroup Factory.
                | 
                | Role: This interface is used to create tag groups.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_tag_group(self, i_tag_group_name: str) -> TagGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTagGroup(CATBSTR iTagGroupName) As TagGroup
                |     Creates a Tag Group.
                | 
                |     Parameters:
                | 
                |         iTagGroupName
                |             Name of the TagGroup to be created. 
                | 
                |     Returns:
                |         oTagGroup Newly created TagGroup. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTagGroupFactory As TagGroupFactory
                |                   ......
                |         Dim NameTagGroup As String
                |                   ......
                |         Set oTagGroup = oTagGroupFactory.CreateTagGroup(NameTagGroup)

        :param str i_tag_group_name:
        :return: TagGroup
        """
        return TagGroup(self.com_object.CreateTagGroup(i_tag_group_name))

    def __repr__(self):
        return f'TagGroupFactory(name="{ self.name }")'
