"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class StrCategoryMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrCategoryMngt
                | 
                | Object to manage Str functions category.
                | Role: To access category of structure object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def automatic_name(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AutomaticName() As boolean
                |     Returns or Sets the naming mode of this object: automatic or manual. (TRUE = automatic, FALSE = manual)
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in whether object has AutomaticName mode or
                |              not.
                |              
                | 
                |              StrAutomaticName = ObjStrCategoryMngt.AutomaticName

        :return: bool
        """

        return self.com_object.AutomaticName

    @automatic_name.setter
    def automatic_name(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AutomaticName = value

    @property
    def category_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CategoryName() As CATBSTR
                |     Returns or Sets the CategoryName of this object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves CategoryName of the panel or
                |              profile.
                |              
                | 
                |              Dim ObjStrCategoryMngt As StrCategoryMngt
                |              Set ObjStrCategoryMngt = ObjSfdPanel.StrCategoryMngt
                |              StrCategoryName = ObjStrCategoryMngt.CategoryName

        :return: str
        """

        return self.com_object.CategoryName

    @category_name.setter
    def category_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.CategoryName = value

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
                |              This example retrieves in category of object.
                |              
                | 
                |              StrCategory = ObjStrCategoryMngt.GetCategory

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
                |         iCategory
                |             New category of the object. 
                | 
                |     Example:
                |              This example sets category of object.
                |
                |              ObjStrCategoryMngt.SetCategory "SldPanel"

        :param str i_category:
        :return: None
        """
        return self.com_object.SetCategory(i_category)

    def __repr__(self):
        return f'StrCategoryMngt(name="{ self.name }")'
