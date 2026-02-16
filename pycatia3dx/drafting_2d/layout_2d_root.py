"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.drafting_2d.layout_2d_sheet import Layout2DSheet
from pycatia3dx.drafting_2d.layout_2d_sheets import Layout2DSheets
from pycatia3dx.knowledge_interfaces.parameters import Parameters
from pycatia3dx.knowledge_interfaces.relations import Relations
from pycatia3dx.system.any_object import AnyObject


class Layout2DRoot(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DRoot
                | 
                | Interface to manage the 2D Layout root.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_sheet(self) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActiveSheet() As Layout2DSheet
                |     Retrieves or sets the active sheet of the layout.
                | 
                |     Example:
                |         This example retrieves the active sheet currently managed by the layout
                |         root of an active 3D Shape representation.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = MyRoot.GetItem("CATLayout2DRoot)"
                |          Dim MySheet = MyRoot.GetActiveSheet

        :return: Layout2DSheet
        """

        return Layout2DSheet(self.com_object.ActiveSheet)

    @active_sheet.setter
    def active_sheet(self, value: Layout2DSheet):
        """
        :param Layout2DSheet value:
        """

        self.com_object.ActiveSheet = value

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parameters() As Parameters (Read Only)
                |     Returns the collection of parameters of the layout.
                | 
                |     Example:
                | 
                |          This example retrieves in layoutParameters the collection
                |          of
                |          parameters currently managed by the layout root of an active 3D Shape
                |          representation. 
                |          
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = MyRoot.GetItem("CATLayout2DRoot)"
                |          Dim layoutParameters As Parameters
                |          Set layoutParameters = MyRoot.Parameters

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
                |     Returns the collection of relations of the 3D shape rep
                |     representation.
                | 
                |     Example:
                | 
                |          This example retrieves in layoutRelations the collection
                |          of
                |          relations currently managed by the layout root of an active 3D Shape
                |          representation.
                |          
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = MyRoot.GetItem("CATLayout2DRoot)"
                |          Dim layoutRelations As Relations
                |          Set layoutRelations = MyRoot.Relations

        :return: Relations
        """

        return Relations(self.com_object.Relations)

    @property
    def rendering_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RenderingMode() As CatRenderingMode
                |     Set/Get the rendering mode of Layout2D. get_RenderingMode method can fail
                |     if rendering value stored on Layout is not a value defined in CatRenderingMode
                |     enum.
                | 
                |     Example:
                |         This example sets the rendering mode to catRenderShadingWithEdges for
                |         the layout root of a part of the active document.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = myPart.GetItem("CATLayout2DRoot)"
                |          MyRoot. RenderingMode  = catRenderShadingWithEdges

        :return: int
        """

        return self.com_object.RenderingMode

    @rendering_mode.setter
    def rendering_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.RenderingMode = value

    @property
    def sheets(self) -> Layout2DSheets:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Sheets() As Layout2DSheets (Read Only)
                |     Returns the collection of Layout2D sheets aggregated by the layout
                |     root.
                | 
                |     Example:
                |         This example retrieves in SheetCollection the collection of sheets
                |         currently managed by the layout root of an active 3D Shape
                |         representation.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = MyRoot.GetItem("CATLayout2DRoot)"
                |          Dim SheetCollection As Layout2DSheets
                |          Set SheetCollection = MyRoot.Sheets.

        :return: Layout2DSheets
        """

        return Layout2DSheets(self.com_object.Sheets)

    @property
    def standard(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Standard() As CATBSTR
                |     Returns or sets the DrawingStandard of the part document.
                | 
                |     Example:
                |         This example sets the drawing standard currently managed by the layout
                |         root of a part of the active 3D Shape representation, supposed to be a part
                |         document, to ISO.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = myPart.GetItem("CATLayout2DRoot)"
                |          MyRoot.Standard = ISO

        :return: str
        """

        return self.com_object.Standard

    @standard.setter
    def standard(self, value: str):
        """
        :param str value:
        """

        self.com_object.Standard = value

    @property
    def visu_in_3d(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VisuIn3D() As CatVisuIn3DMode
                |     Set/Get the 3D visualization mode of the layout in the 3D Viewer ie in the
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

    def reorder_sheets(self, i_ordered_sheets: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub reorder_Sheets(CATSafeArrayVariant iOrderedSheets)
                |     Changes the positions of the sheets in this drawing according to the given
                |     ordered list. iOrderedSheets is the result of a permutation applied to the list
                |     of all the sheets of this drawing, with the following constraint: For every
                |     non-detail sheet, there is not any detail sheet appearing before in
                |     iOrderedSheets.
                |
                |     Example:
                |         This example inverts the sheet order of a drawing made of exactly two
                |         regular sheets.
                |
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Set drwsheets = MyRoot.Sheets
                |          Set sheet1 = drwsheets.item(1)
                |          Set sheet2 = drwsheets.item(2)
                |          newsheetorder = Array(sheet2, sheet1)
                |          drwsheetsorder.reorder_Sheets(newsheetorder)

        :param tuple i_ordered_sheets:
        :return: None
        """
        return self.com_object.reorder_Sheets(i_ordered_sheets)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'reorder_sheets'
        # vba_code = """
        # Public Function reorder_sheets(layout2_d_root)
        #     Dim iOrderedSheets (2)
        #     layout2_d_root.reorder_Sheets iOrderedSheets
        #     reorder_sheets = iOrderedSheets
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Layout2DRoot(name="{self.name}")'
