"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.references import References
from pycatia3dx.system.any_object import AnyObject


class SsmToolSet(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmToolSet
                | 
                | Role: This interface is specific to InternalSpaceSet,SpaceCellSet Of Space
                | Manager
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_children(self, ol_child_objects: References) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetChildren(References olChildObjects)
                |     Get the list of children
                |
                |     Parameters:
                |
                |         olChildObjects
                |             output list of child
                |
                |     Returns:
                |         Error code of function.

        :param References ol_child_objects:
        :return: None
        """
        return self.com_object.GetChildren(ol_child_objects.com_object)

    def __repr__(self):
        return f'SsmToolSet(name="{ self.name }")'
