"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_del_robot_simulation.tag_point import TagPoint


class TagFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TagFactory
                | 
                | Interface representing a Tag Factory.
                | 
                | Role: This interface is used to create tags.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_tag(self, i_tag_name: str) -> TagPoint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTag(CATBSTR iTagName) As TagPoint
                |     Creates a Tag. Each Tag is associated with a Name and a parent
                |     TagGroup.
                | 
                |     Parameters:
                | 
                |         iTagName
                |             Name of the Tag to be created. 
                | 
                |     Returns:
                |         oTag Newly created Tag. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTagFactory As TagFactory
                |                   ......
                |         Dim oTag As Tag
                |         Dim NameTag As String
                |         Set oTag = objTagFactory.CreateTag(NameTag)

        :param str i_tag_name:
        :return: TagPoint
        """
        return TagPoint(self.com_object.CreateTag(i_tag_name))

    def __repr__(self):
        return f'TagFactory(name="{ self.name }")'
