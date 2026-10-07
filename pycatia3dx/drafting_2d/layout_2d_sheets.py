"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.drafting_2d.layout_2d_sheet import Layout2DSheet
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Layout2DSheets(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Layout2DSheets
                | 
                | A collection of all the Layout sheets 2DL currently managed by the
                | LayoutRoot.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Layout2DSheet)
        self.com_object = com_object

    @property
    def active_sheet(self) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActiveSheet() As Layout2DSheet (Read Only)
                |     Returns the active Layout sheet of the Layout document.
                | 
                |     Example:
                |         The following example shows how to get the active sheet and retrieved
                |         in MySheet in the Layout sheet collection of the layout root of Part supposed
                |         to be in the active 3D shape representation.
                | 
                |          Dim myPart as CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActievObject
                |          Dim MyLayoutRoot As Layout2DRoot
                |          Set MyLayoutRoot = myPart.GetItem("CATLayoutRoot")
                |          Dim MySheet As Layout2DSheet
                |          Set MySheet =  MyLayoutRoot.Sheets.ActiveSheet

        :return: Layout2DSheet
        """

        return Layout2DSheet(self.com_object.ActiveSheet)

    def add(self, i_layout_sheet_name: str) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iLayoutSheetName) As Layout2DSheet
                |     Creates a Layout sheet and adds it to the Layout2DSheets collection. This
                |     Layout sheet becomes the active one.
                | 
                |     Parameters:
                | 
                |         iLayoutSheetName
                |             The name to assign to the created Layout2DSheet object
                |             
                | 
                |     Returns:
                |         The created Layout sheet 
                |     Example:
                |         The following example creates a Layout sheet named FirstSheet and
                |         retrieved in MySheet in the Layout sheet collection of the layout root of Part
                |         supposed to be in the active 3D shape representation.
                | 
                |          Dim myPart as CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActievObject
                |          Dim MyLayoutRoot As Layout2DRoot
                |          Set MyLayoutRoot = myPart.GetItem("CATLayoutRoot")
                |          Dim MySheet As Layout2DSheet
                |          Set MySheet = MyLayoutRoot.Sheets.Add("FirstSheet").

        :param str i_layout_sheet_name:
        :return: Layout2DSheet
        """
        return Layout2DSheet(self.com_object.Add(i_layout_sheet_name))

    def add_detail(self, i_layout_sheet_name: str) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddDetail(CATBSTR iLayoutSheetName) As Layout2DSheet
                |     Creates a detail Layout sheet 2DL and adds it to the LayoutSheets2DL
                |     collection. This detail Layout sheet becomes the active
                |     one.
                | 
                |     Parameters:
                | 
                |         iLayoutSheetName
                |             The name to assign to the created detail LayoutSheet object
                |             
                | 
                |     Returns:
                |         The created layout sheet 
                |     Example:
                |         The following example creates a detail Layout sheet named FirstSheet
                |         and retrieved in MySheet in the Layout sheet collection of the layout root of
                |         Part supposed to be in the active 3D shape
                |         representation.
                | 
                |          Dim myPart as CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActievObject
                |          Dim MyLayoutRoot As Layout2DRoot
                |          Set MyLayoutRoot = myPart.GetItem("CATLayoutRoot")
                |          Dim MySheet As Layout2DSheet
                |          Set MySheet = MyLayoutRoot.Sheets.Add("FirstSheet")

        :param str i_layout_sheet_name:
        :return: Layout2DSheet
        """
        return Layout2DSheet(self.com_object.AddDetail(i_layout_sheet_name))

    def item(self, i_index: CATVariant) -> Layout2DSheet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As Layout2DSheet
                |     Returns a Layout sheet using its index or its name from the Layout2DSheets
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Layout sheet to retrieve from the
                |             collection of Layout sheets. As a numerics, this index is the rank of the
                |             Layout sheet in the collection. The index of the first Layout sheet in the
                |             collection is 1, and the index of the last Layout sheet is Count. As a string,
                |             it is the name you assigned to the Layout sheet using the AnyObject.Name
                |             property or when creating it using the Add method.
                |             
                | 
                |     Returns:
                |         The retrieved Layout sheet 
                |     Example:
                |         This example retrieves in ThisLayoutSheet the third Layout sheet, and
                |         in ThatLayoutSheet the Layout sheet named MySheet in the Layout sheet
                |         collection of the layout root of Part supposed to be in the active 3D shape
                |         representation..
                | 
                |          Dim myPart as CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActievObject
                |          Dim ThisLayoutRoot As Layout2DRoot
                |          Set ThisLayoutRoot = myPart.GetItem("CATLayoutRoot")
                |          Dim ThisLayoutSheet As Layout2DSheet
                |          Set ThisLayoutSheet = ThisLayoutRoot.Sheets.Item(3)
                |          Dim ThatLayoutSheet As Layout2DSheet
                |          Set ThatLayoutSheet = ThisLayoutRoot.Sheets.Item("MySheet")

        :param CATVariant i_index:
        :return: Layout2DSheet
        """
        return Layout2DSheet(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Layout2Dsheet from the Layout2DSheets
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Layout sheet to remove from the
                |             collection of Layout sheets. As a numerics, this index is the rank of the
                |             Layout sheet in the collection. The index of the first Layout sheet in the
                |             collection is 1, and the index of the last Layout sheet is Count. As a string,
                |             it is the name you assigned to the Layout sheet using the AnyObject.Name
                |             property or when creating it using the Add method.
                |             
                |         Example:
                |             The following example removes the second Layout sheet and the
                |             Layout sheet named SheetToBeRemoved in the Layout sheet collection of the
                |             layout root of Part supposed to be in the active 3D shape
                |             representation.
                | 
                |              Dim myPart as CATIAPart
                |              Set myPart = CATIA.ActiveEditor.ActievObject
                |              Dim MyLayoutRoot As Layout2DRoot
                |              Set MyLayoutRoot = myPart.GetItem("CATLayoutRoot")
                |              MyLayoutRoot.Layout2DSheets.Remove("SheetToBeRemoved")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __getitem__(self, n: int) -> Layout2DSheet:
        if (n + 1) > self.count:
            raise StopIteration

        return Layout2DSheet(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Layout2DSheet]:
        for i in range(self.count):
            yield Layout2DSheet(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Layout2DSheets(name="{self.name}")'
