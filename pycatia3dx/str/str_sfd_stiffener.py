"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.str.sfd_convert_stiffener import SfdConvertStiffener
from pycatia3dx.str.str_material_mngt import StrMaterialMngt
from pycatia3dx.str.str_stiffener import StrStiffener


class StrSfdStiffener(StrStiffener):

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
                |                             StrSfdStiffener
                | 
                | Object to manage Structure Functional Modeler Stiffener.
                | Role: Allows accessing and setting of Stiffener's data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def sfd_convert_stiffener(self) -> SfdConvertStiffener:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SfdConvertStiffener() As SfdConvertStiffener (Read
                | Only)
                |     Returns the SfdConvertStiffener object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjSfdConvertStiffener the
                |              SfdConvertStiffener object
                |              of the SfdStiffener.
                |              
                | 
                |              Dim ObjSfdStiffener As SfdStiffener
                |              Set ObjSfdStiffener = ObjSfdStiffeners.AddStiffener
                |              Dim ObjSfdConvertStiffener As SfdConvertStiffener
                |              Set ObjSfdConvertStiffener = ObjSfdStiffener.SfdConvertStiffener

        :return: SfdConvertStiffener
        """

        return SfdConvertStiffener(self.com_object.SfdConvertStiffener)

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
                |              of the SfdStiffener
                |              
                | 
                |              Dim ObjSfdStiffener As SfdStiffener
                |              Set ObjSfdStiffener = ObjSfdStiffeners.AddStiffener
                |              Dim ObjStrMaterialMngt As StrMaterialMngt
                |              Set ObjStrMaterialMngt = ObjSfdStiffener.StrMaterialMngt

        :return: StrMaterialMngt
        """

        return StrMaterialMngt(self.com_object.StrMaterialMngt)

    def __repr__(self):
        return f'StrSfdStiffener(name="{ self.name }")'
