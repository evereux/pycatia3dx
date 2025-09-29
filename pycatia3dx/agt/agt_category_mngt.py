"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class AGTCategoryMngt(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AGTCategoryMngt
                | 
                | Object to manage category.
                | To access category of structure object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCategory() As CATBSTR
                |     Returns the category of this object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in category of insulation
                |              object.
                |              
                | 
                |              Dim ObjAGTCategoryMngt As AGTMaterialMngt
                |              Set ObjAGTCategoryMngt = ObjAGTInsulation.AGTCategoryMngt
                |              AGTCategory = ObjAGTCategoryMngt.GetCategory

        :return: str
        """
        return self.com_object.GetCategory()

    def set_category(self, i_category: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCategory(CATBSTR iCategory)
                |     Sets the category of this object.
                | 
                |     Parameters:
                | 
                |         iCategory
                |             New category of the object. 
                | 
                |     Example:
                | 
                | 
                |              This example sets category of object.
                |              
                | 
                |              ObjAGTCategoryMngt.SetCategory "AGTInsulation"

        :param str i_category:
        :return: None
        """
        return self.com_object.SetCategory(i_category)

    def __repr__(self):
        return f'AgtCategoryMngt(name="{self.name}")'
