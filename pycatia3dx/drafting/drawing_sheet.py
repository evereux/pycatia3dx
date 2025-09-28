"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.drafting.drawing_page_setup import DrawingPageSetup
from pycatia3dx.drafting.drawing_views import DrawingViews
from pycatia3dx.drafting.print_area import PrintArea
from pycatia3dx.system.any_object import AnyObject


class DrawingSheet(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingSheet
                | 
                | Represents a drawing sheet of the drawing representation.
                | 
                | The drawing sheet is included in a drawing representation and contains drawing
                | views.
                | Warning: This interface is not available with 2D Layout for 3D
                | Design.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def gen_views_pos_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GenViewsPosMode() As CatSheetGenViewsPosMode
                |     Returns or sets the generative views position stability
                |     mode.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example sets the stability mode of the MySheet drawing sheet so
                |         that after an update, existing and unmodified geometries don't move
                |         globally.
                | 
                |          MySheet.GenViewsPosMode = catFixedAxis

        :return: int
        """

        return self.com_object.GenViewsPosMode

    @gen_views_pos_mode.setter
    def gen_views_pos_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.GenViewsPosMode = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Orientation() As CatPaperOrientation
                |     Returns or sets the paper orientation.
                | 
                |     Example:
                |         This example sets the paper orientation for the MySheet drawing sheet
                |         to catPaperLandscape.
                | 
                |          MySheet.Orientation = catPaperLandscape

        :return: int
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation = value

    @property
    def page_setup(self) -> DrawingPageSetup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PageSetup() As DrawingPageSetup (Read Only)
                |     Returns the page setup.
                | 
                |     Example:
                |         This example returns the page setup for the MySheet drawing
                |         sheet.
                | 
                |          Dim MySheetPageSetup As DrawingPageSetup
                |          Set MySheetPageSetup = MySheet.PageSetup

        :return: DrawingPageSetup
        """

        return DrawingPageSetup(self.com_object.PageSetup)

    @property
    def paper_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PaperSize() As CatPaperSize
                |     Returns or sets the paper size.
                | 
                |     Example:
                |         This example sets the page size for the MySheet drawing sheet to
                |         catPaperA4.
                | 
                |          MySheet.PaperSize = catPaperA4

        :return: int
        """

        return self.com_object.PaperSize

    @paper_size.setter
    def paper_size(self, value: int):
        """
        :param int value:
        """

        self.com_object.PaperSize = value

    @property
    def print_area(self) -> PrintArea:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PrintArea() As PrintArea (Read Only)
                |     Returns the print area definition object.
                | 
                |     Example:
                |         This example returns the print area for the MySheet drawing
                |         sheet.
                | 
                |          Dim MyPrintArea As PrintArea
                |          Set MyPrintArea = MySheet.PrintArea

        :return: PrintArea
        """

        return PrintArea(self.com_object.PrintArea)

    @property
    def projection_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProjectionMethod() As CatSheetProjectionMethod
                |     Returns or sets the sheet projection mode .
                | 
                |     Example:
                |         This example sets the projection mode of the MySheet drawing sheet to
                |         catFirstAngle.
                | 
                |          MySheet.ProjectionMethod = catFirstAngle

        :return: int
        """

        return self.com_object.ProjectionMethod

    @projection_method.setter
    def projection_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.ProjectionMethod = value

    @property
    def scale(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Scale() As double
                |     Returns or sets the scale of the drawing sheet.
                | 
                |     Example:
                |         This example sets the scale of the MySheet drawing sheet to
                |         0.5.
                | 
                |          MySheet.Scale = 0.5

        :return: float
        """

        return self.com_object.Scale

    @scale.setter
    def scale(self, value: float):
        """
        :param float value:
        """

        self.com_object.Scale = value

    @property
    def scale2(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Scale2() As double
                |     Returns or sets the scale of the drawing sheet (Workaround for VBA
                |     keyword).
                | 
                |     Example:
                |         This example sets the scale of the MySheet drawing sheet to
                |         0.5.
                | 
                |          MySheet.Scale2 = 0.5

        :return: float
        """

        return self.com_object.Scale2

    @scale2.setter
    def scale2(self, value: float):
        """
        :param float value:
        """

        self.com_object.Scale2 = value

    @property
    def sheet_style(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SheetStyle(CATBSTR iSheetStyleName) (Write Only)
                |     Sets the sheet Style. The available Sheet style name is obtained from
                |     CATIADrawingService
                | 
                |     Example:
                |         This example sets the sheet Style for the MySheet drawing
                |         sheet.
                | 
                |          myDrawingService As DrawingService 
                |          Set myDrawingService = CATIA.ActiveEditor.GetService("CATDrawingService")
                |          Set myDrawingRoot = CATIA.ActiveEditor.ActiveObject
                |          myStdname = myDrawingRoot.Standard
                |          nbsheetStyle = myDrawingService.NumberOfSheetStyle(myStdname)
                |          Dim mylstSheetStyle(0) 'as CATSafeArrayVariant
                |          ReDim mylstSheetStyle(nbsheetStyle - 1)
                |          myNewSheetStyle = mylstSheetStyle(nbsheetStyle-1)
                |          MySheet.SheetStyle = myNewSheetStyle
                |          
                | 
                |     See also:
                |         DrawingService

        :return: bool
        """

        return self.com_object.SheetStyle

    @sheet_style.setter
    def sheet_style(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SheetStyle = value

    @property
    def views(self) -> DrawingViews:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Views() As DrawingViews (Read Only)
                |     Returns the drawing view collection of the drawing sheet.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example retrieves in ViewCollection the collection of views of the
                |         MySheet drawing sheet.
                | 
                |          Dim ViewCollection As DrawingViews
                |          Set ViewCollection = MySheet.Views

        :return: DrawingViews
        """

        return DrawingViews(self.com_object.Views)

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Activate()
                |     Activates the drawing sheet. Activating a drawing sheet means that this
                |     drawing sheet is the one on which the end user is now working. The window in
                |     the application's window collection which contains this drawing sheet becomes
                |     the active one.
                | 
                |     Example:
                |         This example activates the MySheet drawing sheet.
                | 
                |          MySheet.Activate

        :return: None
        """
        return self.com_object.Activate()

    def force_update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub ForceUpdate()
                |     Forces the update of all the drawing views of the drawing sheet. This
                |     update redraws all the views, whether their pointed objects have been modified
                |     since the drawing sheet creation or last update or not. These pointed objects
                |     can be CATIA Version 4 models, or CATIA Version 5 parts or
                |     assemblies.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example forces the update of all the dawing views in the MySheet
                |         drawing sheet.
                | 
                |          MySheet.ForceUpdate

        :return: None
        """
        return self.com_object.ForceUpdate()

    def generate_dimensions(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GenerateDimensions()
                |     Generates dimensions in all the drawing views of the drawing sheet. These
                |     dimensions are generated from the constraints of the pointed 3D part(s). One
                |     dimension only is generated for a given constraint. Only dimensions for the
                |     following constraints are generated: distance, length, angle, radius, and
                |     diameter.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example generates the dimensions for all the views in the MySheet
                |         drawing sheet.
                | 
                |          MySheet.GenerateDimensions

        :return: None
        """
        return self.com_object.GenerateDimensions()

    def get_paper_height(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetPaperHeight() As double
                |     Gets the paper width of the drawing sheet.
                | 
                |     Parameters:
                | 
                |         oPaperHeight
                | 
                |             Example:
                |                 This example get the height of the
                |                 DrawingSheet1.
                | 
                |                  DrawingSheet1.GetPaperHeight oPaperHeight

        :return: float
        """
        return self.com_object.GetPaperHeight()

    def get_paper_width(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetPaperWidth() As double
                |     Gets the paper width of the drawing sheet.
                | 
                |     Parameters:
                | 
                |         oPaperWidth
                | 
                |             Example:
                |                 This example get the width of the
                |                 DrawingSheet1.
                | 
                |                  DrawingSheet1.GetPaperWidth oPaperWidth

        :return: float
        """
        return self.com_object.GetPaperWidth()

    def is_detail(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func IsDetail() As boolean
                |     Checks whether the sheet is a detail sheet.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                |     TRUE if the sheet is a detail sheet.
                | 
                |     Example:
                |         This example checks whether MySheet is a detail sheet.
                | 
                |          IsDetail = MySheet.IsDetail

        :return: bool
        """
        return self.com_object.IsDetail()

    def isolate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Isolate()
                |     Isolates the drawing sheet.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example isolates the MySheet drawing sheet.
                | 
                |          MySheet.Isolate

        :return: None
        """
        return self.com_object.Isolate()

    def print_out(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub PrintOut()
                |     Prints the drawing sheet according to its page setup on the default
                |     printer.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example prints the DrawingSheet1 on the default
                |         printer.
                | 
                |          DrawingSheet1.PrintOut

        :return: None
        """
        return self.com_object.PrintOut()

    def print_to_file(self, file_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub PrintToFile(CATBSTR fileName)
                |     Prints the drawing sheet according its page setup in a file instead of
                |     being sent to a printer.
                | 
                |     Parameters:
                | 
                |         fileName
                |             The full pathname of the file receiving the data.
                |             Warning: This method is not available with 2D Layout for 3D Design.
                |             
                | 
                |     Example:
                |         This example prints the DrawingSheet1 in a file.
                | 
                |          DrawingSheet1.PrintToFile "e:\temp\sheet1.prn"

        :param str file_name:
        :return: None
        """
        return self.com_object.PrintToFile(file_name)

    def set_as_detail(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetAsDetail()

        :return: None
        """
        return self.com_object.SetAsDetail()

    def set_paper_height(self, o_paper_height: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetPaperHeight(double oPaperHeight)
                |     Sets the paper width of the drawing sheet, avalaible on user
                |     format.
                | 
                |     Parameters:
                | 
                |         iPaperHeight
                | 
                |             Example:
                |                 This example set the height of the
                |                 DrawingSheet1.
                | 
                |                  DrawingSheet1.PaperSize = catPaperUser
                |                  DrawingSheet1.SetPaperHeight iPaperHeight

        :param float o_paper_height:
        :return: None
        """
        return self.com_object.SetPaperHeight(o_paper_height)

    def set_paper_width(self, o_paper_width: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetPaperWidth(double oPaperWidth)
                |     Sets the paper width of the drawing sheet, avalaible on user
                |     format.
                | 
                |     Parameters:
                | 
                |         iPaperWidth
                | 
                |             Example:
                |                 This example set the width of the
                |                 DrawingSheet1.
                | 
                |                  DrawingSheet1.PaperSize = catPaperUser
                |                  DrawingSheet1.SetPaperWidth iPaperWidth

        :param float o_paper_width:
        :return: None
        """
        return self.com_object.SetPaperWidth(o_paper_width)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Update()
                |     Updates the drawing views of the drawing sheet. This update redraws all the
                |     views whose pointed objects have been modified since the drawing sheet creation
                |     or last update, but do not redraw the views whose pointed have not been
                |     modifed. These pointed objects can be CATIA Version 4 models, or CATIA Version
                |     5 parts or assemblies.
                |     Warning: This method is not available with 2D Layout for 3D
                |     Design.
                | 
                |     Example:
                |         This example updates the drawing views in the MySheet drawing
                |         sheet.
                | 
                |          MySheet.Update

        :return: None
        """
        return self.com_object.Update()

    def reorder_views(self, i_ordered_views: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub reorder_Views(CATSafeArrayVariant iOrderedViews)
                |     Changes the positions of the views in this sheet according to the given
                |     ordered list. iOrderedViews is the result of a permutation applied to the list
                |     of all the views of this sheet with the following constraint: the two first
                |     elements of the list must be respectively the sheet's mainview and background
                |     view.
                | 
                |     Example:
                |         This example modifies the views order of a sheet made of a mainview, a
                |         backgroundview and two user-created views. (user-created views are
                |         inverted).
                | 
                |          Dim MyDrawing as DrawingDrawing
                |          Set MyDrawing = CATIA.ActiveEditor.ActiveObject
                |          Set drwviewsorder = MyDrawing.Sheets.ActiveSheet
                |          Set drwviews = drwviewsorder.Views
                |          Set mainview = drwviews.item(1)
                |          Set backview = drwviews.item(2)
                |          Set view1 = drwviews.item(3)
                |          Set view2 = drwviews.item(4)
                |          newvieworder = Array(mainview, backview, view2, view1)
                |          drwviewsorder.reorder_Views(newvieworder)

        :param tuple i_ordered_views:
        :return: None
        """
        return self.com_object.reorder_Views(i_ordered_views)

    def __repr__(self):
        return f'DrawingSheet(name="{ self.name }")'
