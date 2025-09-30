"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingContainer(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingContainer
                | 
                | Interface to manage the machining activities container.
                | Role: This interface allows to initialize the machining activities
                | container.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_part_operations(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPartOperations() As CATSafeArrayVariant
                |     Retrieves Part operations
                | 
                |     Parameters:
                | 
                |         oListOfPartOperations
                |             List of Part Operations

        :return: tuple
        """
        return self.com_object.GetPartOperations()

    def __repr__(self):
        return f'ManufacturingContainer(name="{ self.name }")'
