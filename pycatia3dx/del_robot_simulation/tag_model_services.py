"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_robot_simulation.tag_group import TagGroup


class TagModelServices(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TagModelServices
                | 
                | Interface representing services exposed by Tag Model Entities and
                | Context.
                | 
                | Role: This interface is used to provide servives to access tag model entities
                | in a given context.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def delete_tag_group(self, i_tag_group: TagGroup) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteTagGroup(TagGroup iTagGroup)
                |     Deletes a Tag Group in a given context.
                | 
                |     Parameters:
                | 
                |         iTagGroup
                |             The Tag Group to delete 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objTagModelServices As TagModelServices
                |                   ......
                |         Dim oTagGroup As TagGroup
                |                   ......
                |         Call objTagModelServices.DeleteTagGroup(oTagGroup)

        :param TagGroup i_tag_group:
        :return: None
        """
        return self.com_object.DeleteTagGroup(i_tag_group.com_object)

    def get_all_tag_groups(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAllTagGroups() As CATSafeArrayVariant
                |     Retreives the list of tag groups in a give context
                | 
                |     Returns:
                |         oTagGroupList The List of Tag Groups 
                |     Example:
                |
                |         Dim objTagModelServices As TagModelServices
                |                   ......
                |         Dim oTaggroups
                |         oTaggroups = oTagModelServices.GetAllTagGroups()

        :return: tuple
        """
        return self.com_object.GetAllTagGroups()

    def __repr__(self):
        return f'TagModelServices(name="{ self.name }")'
