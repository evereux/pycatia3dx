"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.drafting.drawing_sheet import DrawingSheet
from pycatia3dx.drafting.drawing_sheets import DrawingSheets
from pycatia3dx.knowledge_interfaces.parameters import Parameters
from pycatia3dx.knowledge_interfaces.relations import Relations
from pycatia3dx.system.any_object import AnyObject


class DrawingRoot(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingRoot
                | 
                | Represents the drawing object in drawing representation.
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
                | Property ActiveSheet() As DrawingSheet
                |     Retrieves or sets the active sheet of the drawing.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example retrieves the active sheet in the drawing of the active
                |          representation, supposed to be a drawing
                |          representation.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          MyDrawing.GetActiveSheet

        :return: DrawingSheet
        """

        return DrawingSheet(self.com_object.ActiveSheet)

    @active_sheet.setter
    def active_sheet(self, value: DrawingSheet):
        """
        :param DrawingSheet value:
        """

        self.com_object.ActiveSheet = value

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parameters() As Parameters (Read Only)
                |     Returns the collection of parameters of the drawing
                |     representation.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example retrieves in DrawingParameters the collection
                |          of
                |          parameters currently managed by the active representation, supposed to
                |          be a
                |          drawing representation.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim DrawingParameters As Parameters
                |          Set DrawingParameters = MyDrawing.Parameters

        :return: Parameters
        """

        return Parameters(self.com_object.Parameters)

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Relations() As Relations (Read Only)
                |     Returns the collection of relations of the drawing
                |     representation.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example retrieves in DrawingRelations the collection
                |          of
                |          relations currently managed by the active representation, supposed to
                |          be a
                |          drawing representation.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim DrawingRelations As Relations
                |          Set DrawingRelations = MyDrawing.Relations

        :return: Relations
        """

        return Relations(self.com_object.Relations)

    @property
    def sheets(self) -> DrawingSheets:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Sheets() As DrawingSheets (Read Only)
                |     Returns the collection of drawing sheets of the drawing
                |     representation.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example retrieves in SheetCollection the collection
                |          of
                |          sheets currently managed by the active representation, supposed to be
                |          a
                |          drawing representation.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Dim SheetCollection As DrawingSheets
                |          Set SheetCollection = MyDrawing.Sheets

        :return: DrawingSheets
        """

        return DrawingSheets(self.com_object.Sheets)

    @property
    def standard(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Standard() As CATBSTR
                |     Returns or sets the drawing standard name of the drawing
                |     representation.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example sets the drawing standard of the active
                |          representation,
                |          supposed to be a drawing representation, to ISO.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          MyDrawing.Standard = "ISO"

        :return: str
        """

        return self.com_object.Standard

    @standard.setter
    def standard(self, value: str):
        """
        :param str value:
        """

        self.com_object.Standard = value

    def isolate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Isolate()
                |     Isolates all the drawing views of all the drawing sheets of the drawing
                |     representation.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example isolates all the drawing views of all the drawing sheets
                |          of the active representation, supposed to be a drawing
                |          representation.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          MyDrawing.Isolate

        :return: None
        """
        return self.com_object.Isolate()

    def load_3d_data(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Load3DData()
                |     Loads 3D data pointed by the drawing representation in the
                |     session.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example loads the 3D data pointed by the MyDrawing drawing
                |          representation in the session.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          MyDrawing.Load3DData

        :return: None
        """
        return self.com_object.Load3DData()

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Update()
                |     Updates all the drawing sheets of the drawing
                |     representation.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                | 
                |          This example updates the active representation, supposed to be a
                |          drawing representation.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          MyDrawing.Update

        :return: None
        """
        return self.com_object.Update()

    def reorder_sheets(self, i_ordered_sheets: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub reorder_Sheets(CATSafeArrayVariant iOrderedSheets)
                |     Changes the positions of the sheets in this drawing according to the given
                |     ordered list. iOrderedSheets is the result of a permutation applied to the list
                |     of all the sheets of this drawing, with the following constraint: For every
                |     non-detail sheet, there is not any detail sheet appearing before in
                |     iOrderedSheets.
                | 
                |     Example:
                | 
                |          This example inverts the sheet order of a drawing made of exactly two
                |          
                |          regular sheets.
                |          
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Set drwsheets = MyDrawing.Sheets
                |          Set drwsheetsorder =  MyDrawing.DrawingRoot
                |          Set sheet1 = drwsheets.item(1)
                |          Set sheet2 = drwsheets.item(2)
                |          newsheetorder = Array(sheet2, sheet1)
                |          drwsheetsorder.reorder_Sheets(newsheetorder)

        :param tuple i_ordered_sheets:
        :return: None
        """
        return self.com_object.reorder_Sheets(i_ordered_sheets)

    def __repr__(self):
        return f'DrawingRoot(name="{ self.name }")'
