"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.specs_viewer import SpecsViewer
from pycatia3dx.interfaces.window import Window


class SpecsAndGeomWindow(Window):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Window
                |                         SpecsAndGeomWindow
                | 
                | Represents a window featuring a specification viewer and a geometry
                | viewer.
                | The specification viewer is located in the left part of the window and displays
                | the document's specification tree. The geometry viewer is located in the right
                | part of the window and displays the document's geometry, and can thus be a
                | Viewer2D or a Viewer3D, according to the document type. Even if generally the
                | two viewers are simultaneously displayed, one viewer or the other can be hidden
                | thanks to the CatSpecsAndGeomWindowLayout enumeration.
                | 
                | See also:
                |     CatSpecsAndGeomWindowLayout
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def layout(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Layout() As CatSpecsAndGeomWindowLayout
                |     Returns or sets the specification and geometry window
                |     layout.
                | 
                |     Example:
                |         This example sets the specification and geometry window layout for the
                |         MyCADWindow window to catWindowGeomOnly.
                | 
                |          MyCADWindow.Layout = catWindowGeomOnly

        :return: int
        """

        return self.com_object.Layout

    @layout.setter
    def layout(self, value: int):
        """
        :param int value:
        """

        self.com_object.Layout = value

    @property
    def specs_viewer(self) -> SpecsViewer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property SpecsViewer() As SpecsViewer (Read Only)
                |     Returns the specifications viewer.
                | 
                |     Example:
                |         This example retrieves the specification viewer for the MyCADWindow
                |         window.
                | 
                |          Dim MyViewer As Viewer
                |          Set MyViewer = MyCADWindow.SpecsViewer

        :return: SpecsViewer
        """

        return SpecsViewer(self.com_object.SpecsViewer)

    def __repr__(self):
        return f'SpecsAndGeomWindow(name="{self.name}")'
