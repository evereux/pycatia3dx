"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.sdd_stiffener import SddStiffener
from pycatia3dx.structure.str_material_mngt import StrMaterialMngt


class SddProductStiffener(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SddProductStiffener
                | 
                | Object for representing Structure Detail Design Product
                | Stiffener.
                | Role: To manage SDD Stiffener at product level.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def sdd_stiffener(self) -> SddStiffener:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SddStiffener() As SddStiffener (Read Only)
                |     Returns the Stiffener geometric function into this SDD product Stiffener.

        :return: SddStiffener
        """

        return SddStiffener(self.com_object.SddStiffener)

    @property
    def str_material_mngt(self) -> StrMaterialMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrMaterialMngt() As StrMaterialMngt (Read Only)
                |     Returns the StrMaterialMngt object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrMaterialMngt the StrMaterialMngt
                |              object
                |              of the SddProductStiffener
                |              
                | 
                |              Dim ObjSddProductStiffener As SddProductStiffener
                |              Set ObjSddProductStiffener = ObjSddStiffenerMngt.AddStiffener
                |              Dim ObjStrMaterialMngt As StrMaterialMngt 
                |              Set ObjStrMaterialMngt = ObjSddProductStiffener.StrMaterialMngt

        :return: StrMaterialMngt
        """

        return StrMaterialMngt(self.com_object.StrMaterialMngt)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Updates the plate 

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'SddProductStiffener(name="{self.name}")'
