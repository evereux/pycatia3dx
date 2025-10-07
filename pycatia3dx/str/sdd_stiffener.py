"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.str.sdd_support_plate_mngt import SddSupportPlateMngt
from pycatia3dx.str.str_stiffener import StrStiffener


class SddStiffener(StrStiffener):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATStrIDLItf.StructureProfile
                |                         CATStrIDLItf.StrStiffener
                |                             SddStiffener
                | 
                | Object to manage SDD Stiffener.
                | Role: Allows accessing and setting of Stiffener's data.
                | 
                | See also:
                |     SddStiffenerMngt
                | Example:
                | 
                | 
                |          This example retrieves in SddStiffener.
                |          
                | 
                |          Dim ObjSddStiffener As SddStiffener 
                |          Set ObjSddStiffener = ObjSddProductStiffener.SddStiffener
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def sdd_support_plate_mngt(self) -> SddSupportPlateMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SddSupportPlateMngt() As SddSupportPlateMngt (Read
                | Only)
                |     Returns the SddSupportPlateMngt object. 

        :return: SddSupportPlateMngt
        """

        return SddSupportPlateMngt(self.com_object.SddSupportPlateMngt)

    def __repr__(self):
        return f'SddStiffener(name="{ self.name }")'
