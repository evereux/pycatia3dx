"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.annotation.drawing_table import DrawingTable
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DrawingTables(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingTables
                | 
                | A collection of all the drawing tables currently managed by a drawing view of
                | drawing sheet in a drawing representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DrawingTable)
        self.com_object = com_object

    def add(
            self, i_position_x: float,
            i_position_y: float,
            i_number_of_row: int,
            i_number_of_column: int,
            i_row_height: float,
            i_column_width: float
    ) -> DrawingTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(double iPositionX,double iPositionY,long iNumberOfRow,long
                | iNumberOfColumn,double iRowHeight,double iColumnWidth) As
                | DrawingTable
                |     Creates a drawing table and adds it to the DrawingTables collection.
                |     
                |     Notice that an authoring product licence is required.
                | 
                |     Parameters:
                | 
                |         iPositionX,iPositionY
                |             The drawing table x and y coordinates, expressed in millimeters,
                |             with respect to the drawing view coordinate system
                |             
                |         iNumberOfRow,iNumberOfColumn
                |             The drawing table number of rows and columns 
                |         iRowHeight,iColumnWidth
                |             The row height and the column width 
                | 
                |     Returns:
                |         The created drawing table 
                | 
                | Example:
                |     The following example creates an empty drawing table and retrieves it in
                |     MyTable in the drawing table collection of the active view MyView of the
                |     drawing sheet MySheet.
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyTable As DrawingTable
                |      Set MyTable = MyView.Tables.Add(100., 100., 2, 2, 20., 50.)

        :param float i_position_x:
        :param float i_position_y:
        :param int i_number_of_row:
        :param int i_number_of_column:
        :param float i_row_height:
        :param float i_column_width:
        :return: DrawingTable
        """
        return DrawingTable(
            self.com_object.Add(i_position_x, i_position_y, i_number_of_row, i_number_of_column, i_row_height,
                                i_column_width))

    def item(self, i_index: CATVariant) -> DrawingTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As DrawingTable
                |     Returns a drawing table using its index from the DrawingTables
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing table to retrieve from the collection of
                |             drawing tables. As a numerics, this index is the rank of the drawing table in
                |             the collection. The index of the first drawing table in the collection is 1,
                |             and the index of the last drawing table is Count. As a string, it is the name
                |             you assigned to the drawing table using the AnyObject.Name property or when
                |             creating it using the Add method. 
                | 
                |     Returns:
                |         The retrieved drawing table 
                |     Example:
                |         This example retrieves in ThisDrawingTable the second drawing table, in
                |         the drawing view collection of the active view in the active sheet, in the
                |         active representation supposed to be a drawing
                |         representation.
                | 
                |          Dim MyView  As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          Dim ThisDrawingTable As DrawingTable
                |          Set ThisDrawingTable = MyView.Tables.Item(2)

        :param CATVariant i_index:
        :return: DrawingTable
        """
        return DrawingTable(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a drawing table from the DrawingTables collection.
                |     
                |     Notice that an authoring product licence is required.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing table to remove from the collection of
                |             drawing tables. As a numerics, this index is the rank of the drawing table in
                |             the collection. The index of the first drawing table in the collection is 1,
                |             and the index of the last drawing table is Count. 
                | 
                |     Example:
                |         The following example removes the third drawing table in the drawing
                |         table collection of the active view of the active representation, supposed to
                |         be a drawing representation.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.DrawingTables.Remove(3)

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'DrawingTables(name="{self.name}")'
