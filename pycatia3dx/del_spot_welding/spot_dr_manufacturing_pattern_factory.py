"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotDrManufacturingPatternFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrManufacturingPatternFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_dr_manufacturing_pattern(self, oh_mfg_pattern: AnyObject, i_list_of_mfg_fasteners: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateDRManufacturingPattern(AnyObject ohMfgPattern,CATSafeArrayVariant
                | iListOfMfgFasteners)
                |     Creates a DR Manufacturing pattern.
                | 
                |     Parameters:
                | 
                |         ohMfgPattern
                |             The newly created pattern. 
                |         iListOfMfgFasteners
                |             List of manufacturing fasteners to add in the pattern. Array of
                |             CATIABase pointers

        :param AnyObject oh_mfg_pattern:
        :param tuple i_list_of_mfg_fasteners:
        :return: None
        """
        return self.com_object.CreateDRManufacturingPattern(oh_mfg_pattern.com_object, i_list_of_mfg_fasteners)

    def delete_dr_manufacturing_pattern(self, ih_mfg_pattern: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteDRManufacturingPattern(AnyObject ihMfgPattern)
                |     Deletes a DR Manufacturing pattern.
                | 
                |     Parameters:
                | 
                |         ihMfgPattern
                |             Pattern to be deleted. 

        :param AnyObject ih_mfg_pattern:
        :return: None
        """
        return self.com_object.DeleteDRManufacturingPattern(ih_mfg_pattern.com_object)

    def __repr__(self):
        return f'SpotDrManufacturingPatternFactory(name="{ self.name }")'
