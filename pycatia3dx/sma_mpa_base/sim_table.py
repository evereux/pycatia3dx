"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_base.sim_table_columns import SimTableColumns


class SimTable(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimTable
                | 
                | Represents the Table object.
                | 
                | Example:
                |     Given a SimTabularAmplitude object with an attribute Table of type
                |     SimTable, you can retrieve SimTable object as following:
                | 
                |      Dim MyTabularAmplitude As SimTabularAmplitude
                |      ...
                |      Dim MyTable As SimTable
                |      Set MyTable = MyTabularAmplitude.Table
                |      
                | 
                | Example in Python:
                |     Given a SimTabularAmplitude object with an attribute Table of type
                |     SimTable, you can retrieve SimTable object as following:
                | 
                |      ...
                |      myTable = myTabularAmplitude.Table
                |      
                | 
                | See also:
                |     SimTabularAmplitude
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def empty_cells_in_table_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EmptyCellsInTableFlag() As boolean (Read Only)
                |     Retrieves the flag that determines whether table has empty cells. This
                |     boolean will be TRUE if some cells are empty, FALSE otherwise.

        :return: bool
        """

        return self.com_object.EmptyCellsInTableFlag

    @property
    def number_of_columns(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfColumns() As long (Read Only)
                |     Retrieves the number of columns in the table.

        :return: int
        """

        return self.com_object.NumberOfColumns

    @property
    def number_of_rows(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfRows() As long (Read Only)
                |     Retrieves the number of rows in the table.

        :return: int
        """

        return self.com_object.NumberOfRows

    @property
    def table_columns(self) -> SimTableColumns:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TableColumns() As SimTableColumns (Read Only)
                |     Retrieves the table columns. Each item of the returned list adheres to the
                |     CATISimTableColumn interface.

        :return: SimTableColumns
        """

        return SimTableColumns(self.com_object.TableColumns)

    def delete_row(self, i_row: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteRow(long iRow)
                |     Deletes the specified row.
                | 
                |     Parameters:
                | 
                |         iRow[in]
                |             The row number. To delete the first row iRow should be 1.

        :param int i_row:
        :return: None
        """
        return self.com_object.DeleteRow(i_row)

    def insert_row(self, i_row: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InsertRow(long iRow)
                |     Inserts a row at the specified location.
                |     Newly created cells will have an illegal value. They will return True using
                |     the GetEmptyCellFlag method. This method will fail if multiple rows are not
                |     allowed for the specific table.
                | 
                |     Parameters:
                | 
                |         iRow[in]
                |             The row number at which a new row is inserted. To insert the row at
                |             the top of the table iRow should be 1. 

        :param int i_row:
        :return: None
        """
        return self.com_object.InsertRow(i_row)

    def __repr__(self):
        return f'SimTable(name="{ self.name }")'
