"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_composite_grid import SimCompositeGrid
from pycatia3dx.sma_mpa_structural_mode.sim_composite_laminate import SimCompositeLaminate


class SimCompositeGridCell(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCompositeGridCell
                | 
                | Represents the Composite Grid Cell object.
                | Given a SimCompositeGrid object, you can retrieve a SimCompositeGridCell as below: Dim myCompShellSection As SimCompositeShellSection .... Refer SMAIAMpaCompositeGrid.idl to create/retrieve a SimCompositeGrid .... Dim myCompositeGrid As SimCompositeGrid ... Dim myCompositeGridCell As SimCompositeGridCell i) Dim myCompositeGridCellList 'As SimCompositeGridCellList //Do not use type myCompositeGridCellList = myCompositeGrid.GetCells ...Loop for listSize = UBound(myCompositeGridCellList) - LBound(myCompositeGridCellList) + 1 if needed.. Set myCompositeGridCell = myCompositeGridCellList(0) or ii) Set myCompositeGridCell = myCompositeGrid.GetCell iIndex
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_cell_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCellName() As CATBSTR
                |     Retreives the name of the grid cell.
                | 
                |     Returns:
                |         Name of the cell.

        :return: str
        """
        return self.com_object.GetCellName()

    def get_grid(self) -> SimCompositeGrid:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGrid() As SimCompositeGrid
                |     Retreives the Grid associated to the cell.
                | 
                |     Returns:
                |         Grid that holds the cell.

        :return: SimCompositeGrid
        """
        return SimCompositeGrid(self.com_object.GetGrid())

    def get_laminate_on_cell(self) -> SimCompositeLaminate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLaminateOnCell() As SimCompositeLaminate
                |     Retreives the laminate.
                | 
                |     Returns:
                |         Laminate on the cell.

        :return: SimCompositeLaminate
        """
        return SimCompositeLaminate(self.com_object.GetLaminateOnCell())

    def set_cell_name(self, i_cell_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCellName(CATBSTR iCellName)
                |     Sets the name of the grid cell.
                | 
                |     Parameters:
                | 
                |         iCellName
                |             [in] Name to be set to the cell.

        :param str i_cell_name:
        :return: None
        """
        return self.com_object.SetCellName(i_cell_name)

    def set_laminate_on_cell(self, i_laminate: SimCompositeLaminate) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLaminateOnCell(SimCompositeLaminate iLaminate)
                |     Sets the laminate.
                | 
                |     Parameters:
                | 
                |         iLaminate
                |             [in] Laminate to be set on the cell. 

        :param SimCompositeLaminate i_laminate:
        :return: None
        """
        return self.com_object.SetLaminateOnCell(i_laminate.com_object)

    def __repr__(self):
        return f'SimCompositeGridCell(name="{ self.name }")'
