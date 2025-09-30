"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_machining_use.manufacturing_view import ManufacturingView


class ManufacturingFeatureContainer(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingFeatureContainer
                | 
                | Interface to manage the feature container.
                | Role: This interface allows to initialize the feature
                | container.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_manufacturing_view(self) -> ManufacturingView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingView() As ManufacturingView
                |     Retrieves the manufacturing view
                | 
                |     Parameters:
                | 
                |         oMfgView
                |             Manufacturing View

        :return: ManufacturingView
        """
        return ManufacturingView(self.com_object.GetManufacturingView())

    def __repr__(self):
        return f'ManufacturingFeatureContainer(name="{ self.name }")'
