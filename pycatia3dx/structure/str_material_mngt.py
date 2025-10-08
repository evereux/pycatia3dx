"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class StrMaterialMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrMaterialMngt
                | 
                | Object to manage Structure Functional Modeler functions
                | material.
                | Role: To access material of structure object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_material(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterial() As CATBSTR
                |     Returns the material and grade as a string on this
                |     function.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the material of object.
                |              
                | 
                |              Dim ObjStrMaterialMngt As StrMaterialMngt
                |              Set ObjStrMaterialMngt = ObjSfdStiffenerOnFreeEdge.StrMaterialMngt
                |              StrMaterial = ObjStrMaterialMngt.GetMaterial

        :return: str
        """
        return self.com_object.GetMaterial()

    def set_material(self, i_material_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMaterial(CATBSTR iMaterialName)
                |     Sets the material and grade as a string on this function.
                | 
                |     Parameters:
                | 
                |         iMaterialName
                |             Material name. 
                | 
                |     Example:
                | 
                | 
                |              This example sets the material of the object
                |              
                | 
                |              ObjStrMaterialMngt.SetMaterial "Steel A42"

        :param str i_material_name:
        :return: None
        """
        return self.com_object.SetMaterial(i_material_name)

    def __repr__(self):
        return f'StrMaterialMngt(name="{ self.name }")'
