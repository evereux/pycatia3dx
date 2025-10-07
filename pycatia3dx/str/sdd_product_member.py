"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.sdd_member import SddMember
from pycatia3dx.str.str_material_mngt import StrMaterialMngt


class SddProductMember(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SddProductMember
                | 
                | Object for representing Structure Detail Design Product
                | Member.
                | Role: To manage the SDD member at product level.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def sdd_member(self) -> SddMember:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SddMember() As SddMember (Read Only)
                |     Returns the Member geometric function into this SDD product
                |     Member.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjSddMember the SddMember
                |              object
                |              of the SddProductMember
                |              
                | 
                |              Dim ObjSddMember As SddMember 
                |              Set ObjSddMember = ObjSddProductMember.SddMember

        :return: SddMember
        """

        return SddMember(self.com_object.SddMember)

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
                |              This example retrieves in ObjMaterialMngt the StrMaterialMngt
                |              object
                |              of the SddProductMember
                |              
                | 
                |              Dim ObjSddProductMember As SddProductMember
                |              Set ObjSddProductMember = ObjSddFactory.AddProductMember
                |              Dim ObjMaterialMngt As StrMaterialMngt
                |              Set ObjMaterialMngt = ObjSddProductMember.StrMaterialMngt

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
        return f'SddProductMember(name="{ self.name }")'
