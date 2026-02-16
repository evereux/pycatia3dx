"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.drafting.drawing_page_setup import DrawingPageSetup
from pycatia3dx.drafting.print_area import PrintArea
from pycatia3dx.drafting_2d.layout_2d_views import Layout2DViews
from pycatia3dx.system.any_object import AnyObject


class Layout2DSheet(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DSheet
                | 
                | The interface to access a Layout2D Sheet.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

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
                |         This example sets the paper orientation for the MySheet Layout2D sheet
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
                |         This example returns the page setup for the MySheet Layout2D
                |         sheet.
                | 
                |          Dim MySheetPageSetup As DrawingPageSetup
                |          Set MySheetPageSetup = MySheet.PageSetup

        :return: DrawingPageSetup
        """

        return DrawingPageSetup(self.com_object.PageSetup)

    @property
    def paper_height(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PaperHeight() As double
                |     Gets or Sets the paper width of the layout sheet.
                | 
                |     Parameters:
                | 
                |         oPaperHeight
                | 
                |             Example:
                |                 This example get the height of the
                |                 Layout2DSheet1.
                | 
                |                  Layout2DSheet1.GetPaperHeight oPaperHeight

        :return: float
        """

        return self.com_object.PaperHeight

    @paper_height.setter
    def paper_height(self, value: float):
        """
        :param float value:
        """

        self.com_object.PaperHeight = value

    @property
    def paper_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PaperName() As CATBSTR
                |     Returns or sets the paper format name.
                | 
                |     Example:
                |         This example sets the paper format name for the MySheet Layout2D sheet
                |         to DSFormat1.
                | 
                |          MySheet.PaperName = DSFormat1

        :return: str
        """

        return self.com_object.PaperName

    @paper_name.setter
    def paper_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.PaperName = value

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
                |         This example sets the page size for the MySheet Layout2D sheet to
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
    def paper_width(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PaperWidth() As double
                |     Gets or Sets the paper width of the layout sheet.
                | 
                |     Parameters:
                | 
                |         oPaperWidth
                | 
                |             Example:
                |                 This example get the width of the Sheet1.
                | 
                |                  Sheet1.GetPaperWidth oPaperWidth

        :return: float
        """

        return self.com_object.PaperWidth

    @paper_width.setter
    def paper_width(self, value: float):
        """
        :param float value:
        """

        self.com_object.PaperWidth = value

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
                |         This example returns the print area for the MySheet Layout2D sheet
                |         2DL.
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
                |         This example sets the projection mode of the MySheet Layout2D sheet to
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
    def sheet_scale(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SheetScale() As double
                |     Returns or sets the scale of the Layout2D sheet.
                | 
                |     Example:
                |         This example sets the scale of the MySheet Layout2D sheet to
                |         0.5.
                | 
                |          MySheet.SheetScale = 0.5

        :return: float
        """

        return self.com_object.SheetScale

    @sheet_scale.setter
    def sheet_scale(self, value: float):
        """
        :param float value:
        """

        self.com_object.SheetScale = value

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
                |          myStdname = myLayoutRoot.Standard
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
    def views(self) -> Layout2DViews:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Views() As Layout2DViews (Read Only)
                |     Returns the Layout2D view collection of the Layout2D
                |     sheet.
                | 
                |     Example:
                |         This example retrieves in ViewCollection the collection of views 2DL of
                |         the MySheet Layout2D sheet.
                | 
                |          Dim ViewCollection As Layout2DViews
                |          Set ViewCollection = MySheet.Views.

        :return: Layout2DViews
        """

        return Layout2DViews(self.com_object.Views)

    @property
    def visu_in_3d(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VisuIn3D() As CatVisuIn3DMode
                |     Set/Get the 3D visualization mode of the sheet in the 3D Viewer ie in the
                |     3D windows and in the background of each view in every 2D
                |     context.
                | 
                |     See also:
                |         CatVisuIn3DMode

        :return: int
        """

        return self.com_object.VisuIn3D

    @visu_in_3d.setter
    def visu_in_3d(self, value: int):
        """
        :param int value:
        """

        self.com_object.VisuIn3D = value

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Activate()
                |     Activates the Layout2D sheet. Activating a Layout2D sheet means that this
                |     Layout2D sheet is the one on which the end user is now working. The window in
                |     the application's window collection which contains this Layout2D sheet becomes
                |     the active one.
                | 
                |     Example:
                |         This example activates the MySheet layout2dsheet.
                | 
                |          MySheet.Activate

        :return: None
        """
        return self.com_object.Activate()

    def is_detail(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsDetail() As boolean
                |     Checks whether the sheet is a detail sheet.
                |     TRUE if the sheet is a detail sheet.
                | 
                |     Example:
                |         This example checks whether MySheet is a detail sheet.
                | 
                |          IsDetail = MySheet.IsDetail

        :return: bool
        """
        return self.com_object.IsDetail()

    def print_out(self, i_rendering_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PrintOut(CatRenderingMode iRenderingMode)
                |     Prints the Layout2D sheet according to its page setup on the default
                |     printer.
                | 
                |     Parameters:
                | 
                |         iRenderingMode
                |             The rendering mode to use for the backgrounds of the views in the
                |             sheet.
                | 
                |             Example:
                |                 This example prints the Layout2DSheet1 on the default
                |                 printer.
                | 
                |                  Layout2DSheet1.PrintOut
                |                  catRenderShadingWithEdges

        :param int i_rendering_mode:
        :return: None
        """
        return self.com_object.PrintOut(i_rendering_mode)

    def print_out_2(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PrintOut2()
                |     Prints the Layout2D sheet according to its page setup on the default
                |     printer. If a rendering mode has been stored on the 2D Layout, it is used
                |     during print process for the backgrounds. Otherwise, "Shading with edges"
                |     rendering mode is used.
                | 
                |     Example:
                |         This example prints the Layout2DSheet1 on the default
                |         printer.
                | 
                |          Layout2DSheet1.PrintOut2

        :return: None
        """
        return self.com_object.PrintOut2()

    def print_to_file(self, file_name: str, i_rendering_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PrintToFile(CATBSTR fileName,CatRenderingMode
                | iRenderingMode)
                |     Prints the Layout2D sheet according its page setup in a file instead of
                |     being sent to a printer.
                | 
                |     Parameters:
                | 
                |         fileName
                |             The full pathname of the file receiving the data. 
                |         iRenderingMode
                |             The rendering mode to use for the backgrounds of the views in the
                |             sheet. 
                | 
                |     Example:
                |         This example prints the Layout2DSheet1 in a file.
                | 
                |          Layout2DSheet1.PrintToFile
                |          "e:\\temp\\sheet1.prn",catRenderShadingWithEdges

        :param str file_name:
        :param int i_rendering_mode:
        :return: None
        """
        return self.com_object.PrintToFile(file_name, i_rendering_mode)

    def print_to_file2(self, file_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PrintToFile2(CATBSTR fileName)
                |     Prints the Layout2D sheet according its page setup in a file instead of
                |     being sent to a printer. If a rendering mode has been stored on the 2D Layout,
                |     it is used during print process for the backgrounds. Otherwise, "Shading with
                |     edges" rendering mode is used.
                | 
                |     Parameters:
                | 
                |         fileName
                |             The full pathname of the file receiving the data. 
                | 
                |     Example:
                |         This example prints the Layout2DSheet1 in a file.
                | 
                |          Layout2DSheet1.PrintToFile2 "e:\\temp\\sheet1.prn"

        :param str file_name:
        :return: None
        """
        return self.com_object.PrintToFile2(file_name)

    def reorder_views(self, i_ordered_views: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
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
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Set myLayout =  myPart.GetItem("CATLayoutRoot")
                |          Set drwviewsorder = myLayout.Sheets.ActiveSheet
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
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'reorder_views'
        # vba_code = """
        # Public Function reorder_views(layout2_d_sheet)
        #     Dim iOrderedViews (2)
        #     layout2_d_sheet.reorder_Views iOrderedViews
        #     reorder_views = iOrderedViews
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Layout2DSheet(name="{self.name}")'
