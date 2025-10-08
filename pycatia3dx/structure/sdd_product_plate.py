"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.sdd_plate import SddPlate
from pycatia3dx.structure.str_material_mngt import StrMaterialMngt


class SddProductPlate(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SddProductPlate
                | 
                | Object for representing Structure Detail Design Product Plate.
                | Role: To manage SDD Plate at product level.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def sdd_plate(self) -> SddPlate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SddPlate() As SddPlate (Read Only)
                |     Returns the Plate geometric function into this SDD product
                |     Plate.
                | 
                |     Parameters:
                | 
                |         oMember
                |             Plate function.

        :return: SddPlate
        """

        return SddPlate(self.com_object.SddPlate)

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
                |              of the SddProductPlate
                |              
                | 
                |              Dim ObjSddProductPlate As SddProductPlate
                |              Set ObjSddProductPlate = ObjSddFactory.AddProductPlate(IsAdvPlate)
                |              Dim ObjStrMaterialMngt As StrMaterialMngt 
                |              Set ObjStrMaterialMngt = ObjSddProductPlate.StrMaterialMngt

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
        return f'SddProductPlate(name="{self.name}")'
