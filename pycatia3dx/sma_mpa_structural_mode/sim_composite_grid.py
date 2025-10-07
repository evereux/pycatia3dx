"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_composite_grid_elem_ref_group import SimCompositeGridElemRefGroup
from pycatia3dx.sma_mpa_structural_mode.sim_composite_rosette import SimCompositeRosette


class SimCompositeGrid(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCompositeGrid
                | 
                | Represents the Composite Grid object.
                | Given a SimCompositeShellSection object, you can retrieve a SimCompositeCells as below: Dim myCompShellSection As SimCompositeShellSection .... Refer SMAIAMpaCompositeShellSection.idl to create/retrieve a SimCompositeShellSection. .... i)Dim myCompositeGrid As SimCompositeGrid Set myCompositeGrid = myCompShellSection.CreateGrid or ii) Dim MyLinkServices As SimLinkServices ... Set MyLinkServices = oEditor.GetService("SimLinkServices") Dim myCPDSupport As SimCompositeSupportDefinition Set myCPDSupport = myCompShellSection.CompositeSupport Dim mycpdLinkAccess As SimLinkAccess Set mycpdLinkAccess = myCPDSupport.GetItem("SimLinkAccess") Dim AllLinks AllLinks = mycpdLinkAccess.GetAllLinks("ConnectorList") ...Loop for listSize = UBound(AllLinks) - LBound(AllLinks) + 1 if needed.. Set CompSupport = AllLinks(0) Dim myCompositeGrid As SimCompositeGrid Set myCompositeGrid = MyLinkServices.GetTarget(CompSupport)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_new_ref_group(self) -> SimCompositeGridElemRefGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddNewRefGroup() As SimCompositeGridElemRefGroup
                |     Creates a new element reference group for the grid.
                | 
                |     Returns:
                |         Created element reference group.

        :return: SimCompositeGridElemRefGroup
        """
        return SimCompositeGridElemRefGroup(self.com_object.AddNewRefGroup())

    def create_cells_from_file(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateCellsFromFile(CATBSTR iPath)
                |     Creates cells in the grid with the reference elements and laminate from a
                |     file
                | 
                |     Parameters:
                | 
                |         iPath
                |             [in] Path to read the data eg. D:\\GridData\\GridData.xls

        :param str i_path:
        :return: None
        """
        return self.com_object.CreateCellsFromFile(i_path)

    def create_file_from_cells(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateFileFromCells(CATBSTR iPath)
                |     Writes the all the cells in the grid with the reference elements and lamina
                |     to a file.
                | 
                |     Parameters:
                | 
                |         iPath
                |             [in] Path to write the data eg. D:\\GridData\\GridData.xls

        :param str i_path:
        :return: None
        """
        return self.com_object.CreateFileFromCells(i_path)

    def get_cell(self, i_cell_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCell(short iCellIndex) As CATBaseDispatch
                |     Retreives the cell in the grid corresponding to te index.
                | 
                |     Parameters:
                | 
                |         iCellIndex
                |             [in] Index of the cell in Grid. 
                | 
                |     Returns:
                |         Grid cell correcponding to the index.

        :param int i_cell_index:
        :return: AnyObject
        """
        return self.com_object.GetCell(i_cell_index)

    def get_cells(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCells() As CATSafeArrayVariant
                |     Retreives the list of all the cells in the grid.
                | 
                |     Returns:
                |         All grid cells in the grid.

        :return: tuple
        """
        return self.com_object.GetCells()

    def get_cells_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCellsCount() As short
                |     Retreives the count of cells in the grid.
                | 
                |     Returns:
                |         Number of cells in the grid.

        :return: int
        """
        return self.com_object.GetCellsCount()

    def get_draping_direction(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDrapingDirection() As boolean
                |     Retreives the draping direction.
                | 
                |     Returns:
                |         Draping direction of grid.

        :return: bool
        """
        return self.com_object.GetDrapingDirection()

    def get_element_ref_groups(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetElementRefGroups() As CATSafeArrayVariant
                |     Retreives all the element reference group of the grid.
                | 
                |     Returns:
                |         List of all element reference group of the grid.

        :return: tuple
        """
        return self.com_object.GetElementRefGroups()

    def get_rosette(self) -> SimCompositeRosette:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRosette() As SimCompositeRosette
                |     Retreives the Rosette of the grid.
                | 
                |     Returns:
                |         Rosette of the grid.

        :return: SimCompositeRosette
        """
        return SimCompositeRosette(self.com_object.GetRosette())

    def get_surface(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSurface() As CATBaseDispatch
                |     Retreives the surface of the grid.
                | 
                |     Returns:
                |         Surface of the grid.

        :return: AnyObject
        """
        return self.com_object.GetSurface()

    def set_draping_direction(self, i_draping_direcion: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDrapingDirection(boolean iDrapingDirecion)
                |     Sets the draping direction.
                | 
                |     Parameters:
                | 
                |         iDrapingDirecion
                |             [in] Draping direction to be set to the grid.

        :param bool i_draping_direcion:
        :return: None
        """
        return self.com_object.SetDrapingDirection(i_draping_direcion)

    def set_rosette(self, i_rosette: SimCompositeRosette) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRosette(SimCompositeRosette iRosette)
                |     Sets the Rosette of the grid.
                | 
                |     Parameters:
                | 
                |         iRosette
                |             [in] Rosette of the grid.

        :param SimCompositeRosette i_rosette:
        :return: None
        """
        return self.com_object.SetRosette(i_rosette.com_object)

    def set_split_element(self, i_split_elem: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSplitElement(CATBaseDispatch iSplitElem)
                |     Split the cell in the grid with respect to the specified reference
                |     element.
                | 
                |     Parameters:
                | 
                |         iSplitElem
                |             [in] Reference/cutting geometry. 

        :param AnyObject i_split_elem:
        :return: None
        """
        return self.com_object.SetSplitElement(i_split_elem.com_object)

    def __repr__(self):
        return f'SimCompositeGrid(name="{ self.name }")'
