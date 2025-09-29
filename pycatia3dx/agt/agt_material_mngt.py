"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class AGTMaterialMngt(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AGTMaterialMngt
                | 
                | Object to manage material.
                | To access material of structure object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_material(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetMaterial() As CATBSTR
                |     Returns the material as a string on this function.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the material of object.
                |              
                | 
                |              Dim ObjAGTMaterialMngt As AGTMaterialMngt
                |              Set ObjAGTMaterialMngt = ObjAGTInsulation.AGTMaterialMngt
                |              AGTMaterial = ObjAGTMaterialMngt.GetMaterial

        :return: str
        """
        return self.com_object.GetMaterial()

    def get_sub_material(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetSubMaterial() As CATBSTR
                |     Returns the material as a string on this function.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the material of object.
                |              
                | 
                |              Dim ObjAGTMaterialMngt As AGTMaterialMngt
                |              Set ObjAGTMaterialMngt = ObjAGTInsulation.AGTMaterialMngt
                |              AGTMaterial = ObjAGTMaterialMngt.GetSubMaterial

        :return: str
        """
        return self.com_object.GetSubMaterial()

    def set_material(self, i_material_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetMaterial(CATBSTR iMaterialName)
                |     Sets the material as a string on this function.
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
                |              ObjAGTMaterialMngt.SetMaterial "A-800"

        :param str i_material_name:
        :return: None
        """
        return self.com_object.SetMaterial(i_material_name)

    def set_sub_material(self, i_material_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetSubMaterial(CATBSTR iMaterialName)
                |     Sets the material as a string on this function.
                | 
                |     Parameters:
                | 
                |         iMaterialName
                |             Material name. 
                | 
                |     Example:
                |
                |              This example sets the material of the object
                |
                |              ObjAGTMaterialMngt.SetSubMaterial "A-800"

        :param str i_material_name:
        :return: None
        """
        return self.com_object.SetSubMaterial(i_material_name)

    def __repr__(self):
        return f'AgtMaterialMngt(name="{self.name}")'
