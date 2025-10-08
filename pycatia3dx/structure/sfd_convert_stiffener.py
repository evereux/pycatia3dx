"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SfdConvertStiffener(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfdConvertStiffener
                | 
                | Object to manage the Structure Functional Modeler ConvertStiffener
                | object.
                | Interface representing Sfd ConvertStiffener. 'SldStiffener' late type
                | implements CATIASfdConvertStiffener. Role: Allows accessing and setting of
                | ConvertStiffener's data. There are 2 types of mode available (Plate/Plate and
                | Plate/FlatBar). PLATE/PLATE 1 PLATE/FLATBAR 2
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def mode(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mode(long iMode) (Write Only)
                |     Sets Mode.
                | 
                |     Parameters:
                | 
                |         iMode
                |             The type of Stiffener Conversion you want to
                |             retreive:
                |             - 1 : PLATE/PLATE
                |             - 2 : PLATE/FLATBAR

        :return: None
        """

        return None

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mode = value

    def category(self, i_category_1: str, i_category_2: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Category(CATBSTR iCategory_1,CATBSTR iCategory_2)
                |     Sets Category.
                | 
                |     Parameters:
                | 
                |         iCategory_1
                |             iCategory_1 - Panel 
                |         iCategory_2
                |             iCategory_2 - Panel

        :param str i_category_1:
        :param str i_category_2:
        :return: None
        """
        return self.com_object.Category(i_category_1, i_category_2)

    def convert_stiffener(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ConvertStiffener()
                |     Once all the above inputs are set ConvertStiffener command will be
                |     executed.

        :return: None
        """
        return self.com_object.ConvertStiffener()

    def flange_state(self, i_flange_state: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub FlangeState(boolean iFlangeState)
                |     Sets Flange State.
                | 
                |     Parameters:
                | 
                |         iFlangeState
                |             Want to convert flange or not:
                |             - TRUE : Convert
                |             - FALSE : Don't Convert

        :param bool i_flange_state:
        :return: None
        """
        return self.com_object.FlangeState(i_flange_state)

    def flat_bar_section_name(self, i_flat_bar_section_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub FlatBarSectionName(CATBSTR iFlatBarSectionName)
                |     Sets FlatBar Section Name.
                | 
                |     Parameters:
                | 
                |         iFlatBarSectionName
                |             iFlatBarSectionName - WT18x179.5

        :param str i_flat_bar_section_name:
        :return: None
        """
        return self.com_object.FlatBarSectionName(i_flat_bar_section_name)

    def material(self, i_material_1: str, i_material_2: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Material(CATBSTR iMaterial_1,CATBSTR iMaterial_2)
                |     Sets Material.
                | 
                |     Parameters:
                | 
                |         iMaterial_1
                |             iMaterial_1 - Steel A42 
                |         iMaterial_2
                |             iMaterial_2 - Steel A42

        :param str i_material_1:
        :param str i_material_2:
        :return: None
        """
        return self.com_object.Material(i_material_1, i_material_2)

    def panel_names(self, i_name_1: str, i_name_2: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PanelNames(CATBSTR iName_1,CATBSTR iName_2)
                |     Sets Panel Names.
                | 
                |     Parameters:
                | 
                |         iName_1
                |             iName_1 - Panel 
                |         iName_2
                |             iName_2 - Flange

        :param str i_name_1:
        :param str i_name_2:
        :return: None
        """
        return self.com_object.PanelNames(i_name_1, i_name_2)

    def remove_stiffener(self, i_remove_stiffener_state: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveStiffener(boolean iRemoveStiffenerState)
                |     Sets Stiffener State.
                | 
                |     Parameters:
                | 
                |         iRemoveStiffenerState
                |             Want to keep Stiffener after conversion:
                |             - TRUE : Remove Stiffener
                |             - FALSE : Keep Stiffener 

        :param bool i_remove_stiffener_state:
        :return: None
        """
        return self.com_object.RemoveStiffener(i_remove_stiffener_state)

    def __repr__(self):
        return f'SfdConvertStiffener(name="{ self.name }")'
