"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class PcbObject(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PCBObject

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def electronic_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ElectronicType() As CatElectronicType (Read Only)
                |     Gets the electronic type: Available types for a product: catBOARD,catPANEL or catCOMPONENT, Available types for a Hole: catPCBHole or catFCBHole, Available types for a Pad: catPBCArea Available types for a Pattern : catPCBHole if the patterned feature is Hole, catPCBArea if the patterned feature is Pad
                | 
                |     Parameters:
                | 
                |         oType
                |             This parameter is the type of the object ( catBOARD, catPANEL,
                |             catCOMPONENT ) 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :return: CatElectronicType
        """

        return self.com_object.ElectronicType

    def remove_electronic_behaviour(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveElectronicBehaviour()
                |     Removes a PCB behaviour of an object.
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed 

        :return: None
        """
        return self.com_object.RemoveElectronicBehaviour()

    def __repr__(self):
        return f'PcbObject(name="{ self.name }")'
