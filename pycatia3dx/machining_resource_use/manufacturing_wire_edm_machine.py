"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingWireEdmMachine(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingWireEDMMachine
                | 
                | Interface representing Wire EDM Machine.
                | Role: This interface retrieves data from Wire EDM Machine.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_techno_set_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTechnoSetList() As CATSafeArrayVariant
                |     Retrieves the TechnoSets defined on the Machine.
                | 
                |     Parameters:
                | 
                |         oListTechnoSets
                |             Techno Sets defined on the Machine. 
                | 
                |     Returns:
                |         Return code.
                |         Legal values:
                | 
                |             S_OK: the List is defined
                |             E_FAIL: otherwise

        :return: tuple
        """
        return self.com_object.GetTechnoSetList()

    def __repr__(self):
        return f'ManufacturingWireEdmMachine(name="{ self.name }")'
