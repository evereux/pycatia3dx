"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimMaterialOption(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMaterialOption
                | 
                | Represents the material option object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimMaterialOption for
                |     any material option as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyPlastic As SimPlastic
                |      Set MyPlastic = MyMaterialOptions.Add("SimPlastic")
                |      ...
                |      Dim MyOption As SimMaterialOption
                |      Set MyOption = MyPlastic.GetItem("SimMaterialOption")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_sub_option(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSubOption(CATBSTR iType) As CATBaseDispatch
                |     Creates a new material suboption under a material option.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of the material suboption. 
                | 
                |     Returns:
                |         Created material option.

        :param str i_type:
        :return: AnyObject
        """
        return self.com_object.CreateSubOption(i_type)

    def get_parent_option(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParentOption() As CATBaseDispatch
                |     Retrieves the parent material option of a suboption.

        :return: AnyObject
        """
        return self.com_object.GetParentOption()

    def get_sub_options(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSubOptions() As CATSafeArrayVariant
                |     Retrieves the suboptions of a material option.

        :return: tuple
        """
        return self.com_object.GetSubOptions()

    def is_sub_option(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsSubOption() As boolean
                |     Checks if a material option is a suboption of other material option.

        :return: bool
        """
        return self.com_object.IsSubOption()

    def remove_sub_option(self, i_material_sub_option: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveSubOption(CATBaseDispatch iMaterialSubOption)
                |     Removes the material suboption from a material option. 

        :param AnyObject i_material_sub_option:
        :return: None
        """
        return self.com_object.RemoveSubOption(i_material_sub_option.com_object)

    def __repr__(self):
        return f'SimMaterialOption(name="{ self.name }")'
