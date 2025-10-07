"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sde.ssm_cutting_inputs import SsmCuttingInputs


class SsmCuttingFamily(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SsmCuttingFamily
                | 
                | Role: This interface is specific to CuttingFamily Of Space
                | Manager
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_children(self, ol_child_objects: SsmCuttingInputs) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetChildren(SsmCuttingInputs olChildObjects)
                |     Get the list of children
                | 
                |     Parameters:
                | 
                |         olChildObjects
                |             output list of child 
                | 
                |     Returns:
                |         Error code of function. 

        :param SsmCuttingInputs ol_child_objects:
        :return: None
        """
        return self.com_object.GetChildren(ol_child_objects.com_object)

    def __repr__(self):
        return f'SsmCuttingFamily(name="{ self.name }")'
