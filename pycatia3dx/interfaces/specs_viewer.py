"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx import CatSpecsLayout
from pycatia3dx.interfaces.viewer_2d import Viewer2D


class SpecsViewer(Viewer2D):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Viewer
                |                         InfInterfaces.Viewer2D
                |                             SpecsViewer
                | 
                | Represents the specification tree viewer.
                | This viewer displays the document's specification tree according to the chosen
                | layout, and can only be included in a SpecsAndGeomWindow
                | object.
                | 
                | See also:
                |     CatSpecsLayout, SpecsAndGeomWindow
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def layout(self) -> CatSpecsLayout:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Layout() As CatSpecsLayout
                |     Returns or sets the specification tree layout.
                | 
                |     Example:
                |         This example sets the specification tree layout for the SpecsTreeViewer
                |         specification tree viewer to
                |         catSpecsViewerHorizontalCentered.
                | 
                |          SpecsTreeViewer.Layout = catSpecsViewerHorizontalCentered

        :return: int
        """

        return self.com_object.Layout

    @layout.setter
    def layout(self, value: int):
        """
        :param int value:
        """

        self.com_object.Layout = value

    def __repr__(self):
        return f'SpecsViewer(name="{self.name}")'
