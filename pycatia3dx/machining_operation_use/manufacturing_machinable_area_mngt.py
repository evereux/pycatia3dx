"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingMachinableAreaMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingMachinableAreaMngt
                | 
                | Interface dedicated to machinable area feature managment.
                | Role: This interface delivers services on machinable area
                | features
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_all_datas(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAllDatas() As CATSafeArrayVariant
                |     Gets all the data in the Manufacturing Machinable Feature.
                | 
                |     Parameters:
                | 
                |         oDatas
                |             The list of data

        :return: tuple
        """
        return self.com_object.GetAllDatas()

    def __repr__(self):
        return f'ManufacturingMachinableAreaMngt(name="{ self.name }")'
