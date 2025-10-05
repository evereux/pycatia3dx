"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmContourFromPoints(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmContourFromPoints
                | 
                | Interface representing a Contour created from Points.
                | 
                | Role: This interface is used to get and set the parameters of a contour created
                | from a Tag group.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def tag_group(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TagGroup() As AnyObject
                |     Get the tag group that provided the initial tags.
                | 
                |     Parameters:
                | 
                |         ospTagGroup
                |             The tag group. 
                | 
                |     Returns:
                |         The tag group 

        :return: AnyObject
        """

        return AnyObject(self.com_object.TagGroup)

    @tag_group.setter
    def tag_group(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.TagGroup = value

    def __repr__(self):
        return f'CtmContourFromPoints(name="{ self.name }")'
