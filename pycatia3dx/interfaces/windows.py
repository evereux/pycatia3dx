"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx import CatArrangeStyle
from pycatia3dx.interfaces.window import Window
from pycatia3dx.system.collection import Collection


class Windows(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Windows
                | 
                | A collection of all the Window objects currently managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Window)
        self.com_object = com_object

    def arrange(self, i_style: CatArrangeStyle) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Arrange(CatArrangeStyle iStyle)
                |     Arranges all the windows of the collection.
                | 
                |     Parameters:
                | 
                |         iStyle
                |             The arrangement style to take into account to arrange the windows
                |             
                | 
                |     Example:
                |         The following example arranges all the windows in the Windows
                |         collection, according to the catArrangeCascade style.
                | 
                |          CATIA.Windows.Arrange(catArrangeCascade)

        :param CatArrangeStyle i_style:
        :return: None
        """
        return self.com_object.Arrange(i_style)

    def item(self, i_index: int) -> Window:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(CATVariant iIndex) As Window
                |     Returns a window using its index or its name from the Windows
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the window to retrieve from the collection
                |             of windows. As a numerics, this index is the rank of the window in the
                |             collection. The index of the first window in the collection is 1, and the index
                |             of the last window is Count. As a string, it is the name you assigned to the
                |             window using the AnyObject.Name property. 
                | 
                |     Returns:
                |         The retrieved window 
                |     Example:
                |         This example returns in ThisWindow the third window in the collection,
                |         and in ThatWindow the window named MyWindow.
                | 
                |          Dim ThisWindow As Window
                |          Set ThisWindow = CATIA.Windows.Item(3)
                |          Dim ThatWindow As Window
                |          Set ThatWindow = CATIA.Windows.Item("MyWindow")

        :param CATVariant i_index:
        :return: Window
        """
        return Window(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> Window:
        if (n + 1) > self.count:
            raise StopIteration

        return Window(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Window]:
        for i in range(self.count):
            yield Window(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Windows(name="{self.name}")'
