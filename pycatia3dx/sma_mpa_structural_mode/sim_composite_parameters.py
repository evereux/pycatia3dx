"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_composite_laminate import SimCompositeLaminate
from pycatia3dx.sma_mpa_structural_mode.sim_composite_rosette import SimCompositeRosette


class SimCompositeParameters(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCompositeParameters
                | 
                | Represents the Composite Parameters object.
                | Given a SimCompositeShellSection object, you can create/retrieve a SimCompositeParameters as below: Dim myCompShellSection As SimCompositeShellSection .... Refer SMAIAMpaCompositeShellSection.idl to create/retrieve a SimCompositeShellSection. .... Dim myCompositeParameters As SimCompositeParameters Set myCompositeParameters = myCompShellSection.GetCompositeParameters
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_material(self, i_material: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddMaterial(CATBaseDispatch iMaterial)
                |     Adds material to Composite Parameters.
                | 
                |     Parameters:
                | 
                |         iMaterial
                |             [in] The material to add.

        :param AnyObject i_material:
        :return: None
        """
        return self.com_object.AddMaterial(i_material.com_object)

    def create_file_from_laminates(self, i_laminate_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateFileFromLaminates(CATBSTR iLaminatePath)
                |     Writes the current laminates in Composite Parameters to the file
                |     path.
                | 
                |     Parameters:
                | 
                |         iLaminatePath
                |             [in] Path of the file.

        :param str i_laminate_path:
        :return: None
        """
        return self.com_object.CreateFileFromLaminates(i_laminate_path)

    def create_laminate(self, i_laminate_name: str) -> SimCompositeLaminate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateLaminate(CATBSTR iLaminateName) As
                | SimCompositeLaminate
                |     Creates a new laminate in Composite Parameters.
                | 
                |     Parameters:
                | 
                |         iLaminateName
                |             [in] Name of the laminate 
                | 
                |     Returns:
                |         The created laminate

        :param str i_laminate_name:
        :return: SimCompositeLaminate
        """
        return SimCompositeLaminate(self.com_object.CreateLaminate(i_laminate_name))

    def create_laminates_from_file(self, i_laminate_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateLaminatesFromFile(CATBSTR iLaminatePath)
                |     Creates laminates from file path in Composite Parameters.
                | 
                |     Parameters:
                | 
                |         iLaminatePath
                |             [in] Path of the file.

        :param str i_laminate_path:
        :return: None
        """
        return self.com_object.CreateLaminatesFromFile(i_laminate_path)

    def create_orientation(self, i_orientation_name: str, i_val: float, i_red: int, i_green: int, i_blue: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateOrientation(CATBSTR iOrientationName,double iVal,short iRed,short
                | iGreen,short iBlue)
                |     Creates a Orientation with the specified name, value and color at the end
                |     of the list of Orientations in Composite Parameters.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Value of orientation in Composite Parameters.
                |             
                |         iRed
                |             [in] Red value of the Orientation color. 
                |         iGreen
                |             [in] Green value of the Orientation color. 
                |         iBlue
                |             [in] Blue value of the Orientation color.

        :param str i_orientation_name:
        :param float i_val:
        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :return: None
        """
        return self.com_object.CreateOrientation(i_orientation_name, i_val, i_red, i_green, i_blue)

    def create_rosette(self) -> SimCompositeRosette:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRosette() As SimCompositeRosette
                |     Creates a new rosette in Composite Parameters.
                | 
                |     Returns:
                |         The created rosette.

        :return: SimCompositeRosette
        """
        return SimCompositeRosette(self.com_object.CreateRosette())

    def get_laminate_by_index(self, i_index: int) -> SimCompositeLaminate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLaminateByIndex(short iIndex) As SimCompositeLaminate
                |     Retrieves the laminate for given index name from Composite
                |     Parameters.
                | 
                |     Parameters:
                | 
                |         iLaminate
                |             [in] Index of the laminate in Composite Parameters.
                |             
                | 
                |     Returns:
                |         Laminate with the specified iIndex.

        :param int i_index:
        :return: SimCompositeLaminate
        """
        return SimCompositeLaminate(self.com_object.GetLaminateByIndex(i_index))

    def get_laminate_by_name(self, i_laminate_name: str) -> SimCompositeLaminate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLaminateByName(CATBSTR iLaminateName) As
                | SimCompositeLaminate
                |     Retrieves the laminate for given laminate name from Composite
                |     Parameters.
                | 
                |     Parameters:
                | 
                |         iLaminate
                |             [in] Name of the Laminate in Composite Parameters.
                |             
                | 
                |     Returns:
                |         Laminate with the specified oLaminate.

        :param str i_laminate_name:
        :return: SimCompositeLaminate
        """
        return SimCompositeLaminate(self.com_object.GetLaminateByName(i_laminate_name))

    def get_list_of_laminates(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetListOfLaminates() As CATSafeArrayVariant
                |     Gets the list of Laminates from Composite Parameters.
                | 
                |     Returns:
                |         List of Lamiantes.

        :return: tuple
        """
        return self.com_object.GetListOfLaminates()

    def get_list_of_orientations(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetListOfOrientations() As CATSafeArrayVariant
                |     Gets the list of Orientations from Composite parameters.
                | 
                |     Returns:
                |         List of Orientations as double.

        :return: tuple
        """
        return self.com_object.GetListOfOrientations()

    def get_list_of_rosettes(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetListOfRosettes() As CATSafeArrayVariant
                |     Gets the list of Rosettes from Composite Parameters
                | 
                |     Returns:
                |         List of all Rosettes in Composite Parameters

        :return: tuple
        """
        return self.com_object.GetListOfRosettes()

    def get_material_by_index(self, i_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialByIndex(short iIndex) As CATBaseDispatch
                |     Retrieves Material for given index if exists from Composite
                |     Parameters.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             [in] Index of the Material in Composite Parameters.
                |             
                | 
                |     Returns:
                |         Material at the specified iIndex.

        :param int i_index:
        :return: AnyObject
        """
        return self.com_object.GetMaterialByIndex(i_index)

    def get_material_by_name(self, i_material_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialByName(CATBSTR iMaterialName) As
                | CATBaseDispatch
                |     Retrieves Material for given Material name if exists from Composite
                |     Parameters.
                | 
                |     Parameters:
                | 
                |         iMaterialName
                |             [in] Name of the Material in Composite Parameters.
                |             
                | 
                |     Returns:
                |         Material with the specified iMaterialName.

        :param str i_material_name:
        :return: AnyObject
        """
        return self.com_object.GetMaterialByName(i_material_name)

    def get_material_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialList() As CATSafeArrayVariant
                |     Retrieves list of materials from Composite Parameters.
                | 
                |     Returns:
                |         List of materials in Composite Parameters.

        :return: tuple
        """
        return self.com_object.GetMaterialList()

    def get_orientation_by_index(self, i_index: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrientationByIndex(short iIndex) As double
                |     Retrieves Orientation for given index if exists from Composite
                |     Parameters.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             [in] Index of orientation in Composite Parameters.
                |             
                | 
                |     Returns:
                |         Orientation value at the specified index.

        :param int i_index:
        :return: float
        """
        return self.com_object.GetOrientationByIndex(i_index)

    def get_orientation_by_name(self, i_orientation_name: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrientationByName(CATBSTR iOrientationName) As double
                |     Retrieves Orientation for given orientation name if exists from Composite
                |     Parameters.
                | 
                |     Parameters:
                | 
                |         iOrientationName
                |             [in] Name of the orientation in Composite Parameters.
                |             
                | 
                |     Returns:
                |         Orientation value with the specified name.

        :param str i_orientation_name:
        :return: float
        """
        return self.com_object.GetOrientationByName(i_orientation_name)

    def get_rosette_by_index(self, i_index: int) -> SimCompositeRosette:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRosetteByIndex(short iIndex) As SimCompositeRosette
                |     Retrieves Rosette for given index if exists from Composite
                |     Parameters.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             [in] Index of the Rosette in Composite Parameters.
                |             
                | 
                |     Returns:
                |         Rosette at the specified iIndex.

        :param int i_index:
        :return: SimCompositeRosette
        """
        return SimCompositeRosette(self.com_object.GetRosetteByIndex(i_index))

    def get_rosette_by_name(self, i_rosette_name: str) -> SimCompositeRosette:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRosetteByName(CATBSTR iRosetteName) As
                | SimCompositeRosette
                |     Retrieves Rosette for given Rosette name if exists from Composite
                |     Parameters.
                | 
                |     Parameters:
                | 
                |         iRosetteName
                |             [in] Name of the Rosette in Composite Parameters. 
                | 
                |     Returns:
                |         Rosette with the specified iRosetteName.

        :param str i_rosette_name:
        :return: SimCompositeRosette
        """
        return SimCompositeRosette(self.com_object.GetRosetteByName(i_rosette_name))

    def remove_laminate(self, i_laminate: SimCompositeLaminate) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveLaminate(SimCompositeLaminate iLaminate)
                |     Removes the laminate from Composite Parameters.
                | 
                |     Parameters:
                | 
                |         iLaminate
                |             [in] Laminate to remove from Composite Parameters.

        :param SimCompositeLaminate i_laminate:
        :return: None
        """
        return self.com_object.RemoveLaminate(i_laminate.com_object)

    def remove_material(self, i_material: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveMaterial(CATBaseDispatch iMaterial)
                |     Removes material from Composite Parameters.
                | 
                |     Parameters:
                | 
                |         iMaterial
                |             [in] The material to remove.

        :param AnyObject i_material:
        :return: None
        """
        return self.com_object.RemoveMaterial(i_material.com_object)

    def remove_rosette(self, i_rosette: SimCompositeRosette) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveRosette(SimCompositeRosette iRosette)
                |     Removes the Rosette from Composite Parameters.
                | 
                |     Parameters:
                | 
                |         iRosette
                |             [in] The rosette to remove.

        :param SimCompositeRosette i_rosette:
        :return: None
        """
        return self.com_object.RemoveRosette(i_rosette.com_object)

    def set_color(self, i_orientation_name: str, i_val: float, i_red: int, i_green: int, i_blue: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetColor(CATBSTR iOrientationName,double iVal,short iRed,short iGreen,short
                | iBlue)
                |     Modifies the color of the Orientation associated with the specified
                |     name.
                | 
                |     Parameters:
                | 
                |         iOrientationName
                |             [in] Name of orientation in Composite Parameters. 
                |         iRed
                |             [in] Red value of the Orientation color. 
                |         iGreen
                |             [in] Green value of the Orientation color. 
                |         iBlue
                |             [in] Blue value of the Orientation color. 

        :param str i_orientation_name:
        :param float i_val:
        :param int i_red:
        :param int i_green:
        :param int i_blue:
        :return: None
        """
        return self.com_object.SetColor(i_orientation_name, i_val, i_red, i_green, i_blue)

    def __repr__(self):
        return f'SimCompositeParameters(name="{ self.name }")'
