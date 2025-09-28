"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.drafting.drawing_sheet import DrawingSheet
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DrawingSheets(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingSheets
                | 
                | A collection of all the drawing sheets currently managed by the drawing
                | representation.
                | 
                | Warning: This interface is not available with 2D Layout for 3D
                | Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_sheet(self) -> DrawingSheet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActiveSheet() As DrawingSheet (Read Only)
                |     Returns the active drawing sheet of the drawing
                |     representation.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         The following example retrieves in SheetToWorkIn the active drawing
                |         sheet of the active drawing representation.
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim SheetToWorkIn As DrawingSheet
                |          Set SheetToWorkIn =  MyDrawing.Sheets.ActiveSheet

        :return: DrawingSheet
        """

        return DrawingSheet(self.com_object.ActiveSheet)

    def add(self, i_drawing_sheet_name: str) -> DrawingSheet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Add(CATBSTR iDrawingSheetName) As DrawingSheet
                |     Creates a drawing sheet and adds it to the DrawingSheets collection. This
                |     drawing sheet becomes the active one.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iDrawingSheetName
                |             The name to assign to the created DrawingSheet object
                |             
                | 
                |     Returns:
                |         The created drawing sheet 
                |     Example:
                |         The following example creates a drawing sheet named FirstSheet and
                |         retrieved in MySheet in the drawing sheet collection of the active draing
                |         representation.
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim MySheet As DrawingSheet
                |          Set MySheet = MyDrawing.Sheets.Add("FirstSheet")

        :param str i_drawing_sheet_name:
        :return: DrawingSheet
        """
        return DrawingSheet(self.com_object.Add(i_drawing_sheet_name))

    def add_detail(self, i_drawing_sheet_name: str) -> DrawingSheet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func AddDetail(CATBSTR iDrawingSheetName) As DrawingSheet
                |     Creates a detail drawing sheet and adds it to the DrawingSheets collection.
                |     This detail drawing sheet becomes the active one.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iDrawingSheetName
                |             The name to assign to the created detail DrawingSheet object
                |             
                | 
                |     Returns:
                |         The created drawing sheet 
                |     Example:
                |         The following example creates a detail drawing sheet named FirstSheet
                |         and retrieved in MySheet in the drawing sheet collection of the active drawing
                |         representation.
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim MySheet As DrawingSheet
                |          Set MySheet = MyDrawing.Sheets.Add("FirstSheet")

        :param str i_drawing_sheet_name:
        :return: DrawingSheet
        """
        return DrawingSheet(self.com_object.AddDetail(i_drawing_sheet_name))

    def item(self, i_index: CATVariant) -> DrawingSheet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Item(CATVariant iIndex) As DrawingSheet
                |     Returns a drawing sheet using its index or its name from the DrawingSheets
                |     collection.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing sheet to retrieve from the
                |             collection of drawing sheets. As a numerics, this index is the rank of the
                |             drawing sheet in the collection. The index of the first drawing sheet in the
                |             collection is 1, and the index of the last drawing sheet is Count. As a string,
                |             it is the name you assigned to the drawing sheet using the AnyObject.Name
                |             property or when creating it using the Add method.
                |             
                | 
                |     Returns:
                |         The retrieved drawing sheet 
                |     Example:
                |         This example retrieves in ThisDrawingSheet the third drawing sheet, and
                |         in ThatDrawingSheet the drawing sheet named MySheet in the drawing sheet
                |         collection of the active representation, supposed to be a drawing
                |         representation.
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim ThisDrawingSheet As DrawingSheet
                |          Set ThisDrawingSheet = MyDrawing.Sheets.Item(3)
                |          Dim ThatDrawingSheet As DrawingSheet
                |          Set ThatDrawingSheet = MyDrawing.Sheets.Item("MySheet")

        :param CATVariant i_index:
        :return: DrawingSheet
        """
        return DrawingSheet(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Remove(CATVariant iIndex)
                |     Removes a drawing sheet from the DrawingSheets collection.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the drawing sheet to remove from the
                |             collection of drawing sheets. As a numerics, this index is the rank of the
                |             drawing sheet in the collection. The index of the first drawing sheet in the
                |             collection is 1, and the index of the last drawing sheet is Count. As a string,
                |             it is the name you assigned to the drawing sheet using the AnyObject.Name
                |             property or when creating it using the Add method.
                |             
                |         Example:
                |             The following example removes the second drawing sheet and the
                |             drawing sheet named SheetToBeRemoved in the drawing sheet collection of the
                |             active representation, supposed to be a drawing
                |             representation.
                | 
                |              Dim MyDrawing as DrawingDrawing
                |              Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |              MyDrawing.Sheets.Remove(2)

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'DrawingSheets(name="{ self.name }")'
