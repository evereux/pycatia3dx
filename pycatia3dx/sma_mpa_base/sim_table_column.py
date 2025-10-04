"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimTableColumn(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimTableColumn
                | 
                | Represents the Table-Column object.
                | 
                | Example:
                |     Given a SimTabularAmplitude object with a method GetTableColumn, you can
                |     retrieve SimTableColumn object as following:
                | 
                |      Dim MyTabularAmplitude As SimTabularAmplitude
                |      ...
                |      Dim MyTableColumn As SimTableColumn
                |      Set MyTable = MyTabularAmplitude.GetTableColumn(SimTabularAmplitudeAmplitude)
                |      
                | 
                | Example in Python:
                |     Given a SimTabularAmplitude object with a method GetTableColumn, you can
                |     retrieve SimTableColumn object as following:
                | 
                |      ...
                |      myTable = myTabularAmplitude.GetTableColumn(SimTabularAmplitudeAmplitude)
                |      
                | 
                | See also:
                |     SimTabularAmplitude
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def data(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Data() As CATSafeArrayVariant
                |     The data in the column. This method gives better performance than calling
                |     GetCellData/SetCellData on each cell within a column. Invalid value will be
                |     present in the data if there are blank cells in the specified column. Use the
                |     GetEmptyCellsInTableFlag method prior to using this method.

        :return: tuple
        """

        return self.com_object.Data

    @data.setter
    def data(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.Data = value

    @property
    def number_of_rows(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfRows() As long (Read Only)
                |     The number of rows in the coulumn.

        :return: int
        """

        return self.com_object.NumberOfRows

    def get_cell_data(self, i_row: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCellData(long iRow) As double
                |     Retrieves the specified cell data.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The row number (Starting from 1). 
                | 
                |     Returns:
                |         The value stored in the cell. The value will be an invalid value if the
                |         cell is empty. Use the GetEmptyCellFlag method prior to using this method.

        :param int i_row:
        :return: float
        """
        return self.com_object.GetCellData(i_row)

    def get_cell_long_data(self, i_row: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCellLongData(long iRow) As long
                |     Retrieves the specified cell data.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The row number (Starting from 1). 
                | 
                |     Returns:
                |         The value stored in the cell. The value will be an invalid value if the
                |         cell is empty. Use the GetEmptyCellFlag method prior to using this method.

        :param int i_row:
        :return: int
        """
        return self.com_object.GetCellLongData(i_row)

    def get_cell_string_data(self, i_row: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCellStringData(long iRow) As CATBSTR
                |     Retrieves the specified cell data.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The row number (Starting from 1). 
                | 
                |     Returns:
                |         The value stored in the cell. The value will be an invalid value if the
                |         cell is empty. Use the GetEmptyCellFlag method prior to using this method.

        :param int i_row:
        :return: str
        """
        return self.com_object.GetCellStringData(i_row)

    def get_empty_cell_flag(self, i_row: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEmptyCellFlag(long iRow) As boolean
                |     Retrieves the flag that determines whether the cell is
                |     empty.
                | 
                |     Parameters:
                | 
                |         iRow[in]
                |             The row number (Starting from 1). 
                | 
                |     Returns:
                |         This boolean will be TRUE if the cell is empty, FALSE otherwise.

        :param int i_row:
        :return: bool
        """
        return self.com_object.GetEmptyCellFlag(i_row)

    def set_cell_data(self, i_row: int, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCellData(long iRow,double iValue)
                |     Sets the specified cell data.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The row number (Starting from 1). The row number can be between 1
                |             to the current number of rows + 1, the current number of rows will be returned
                |             by the method GetNumberOfRows(). If the row number is current number of rows +
                |             1 then a new row is inserted at that position using InsertRow().
                |             
                |         iValue
                |             The value to be stored in the cell.

        :param int i_row:
        :param float i_value:
        :return: None
        """
        return self.com_object.SetCellData(i_row, i_value)

    def set_cell_long_data(self, i_row: int, i_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCellLongData(long iRow,long iValue)
                |     Sets the specified cell data.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The row number (Starting from 1). The row number can be between 1
                |             to the current number of rows + 1, the current number of rows will be returned
                |             by the method GetNumberOfRows(). If the row number is current number of rows +
                |             1 then a new row is inserted at that position using InsertRow().
                |             
                |         iValue
                |             The value to be stored in the cell.

        :param int i_row:
        :param int i_value:
        :return: None
        """
        return self.com_object.SetCellLongData(i_row, i_value)

    def set_cell_string_data(self, i_row: int, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCellStringData(long iRow,CATBSTR iValue)
                |     Sets the specified cell data.
                | 
                |     Parameters:
                | 
                |         iRow
                |             The row number (Starting from 1). The row number can be between 1
                |             to the current number of rows + 1, the current number of rows will be returned
                |             by the method GetNumberOfRows(). If the row number is current number of rows +
                |             1 then a new row is inserted at that position using InsertRow().
                |             
                |         iValue
                |             The value to be stored in the cell. 

        :param int i_row:
        :param str i_value:
        :return: None
        """
        return self.com_object.SetCellStringData(i_row, i_value)

    def __repr__(self):
        return f'SimTableColumn(name="{ self.name }")'
