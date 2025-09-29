"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.page_setup import PageSetup
from pycatia3dx.interfaces.viewer import Viewer
from pycatia3dx.interfaces.viewers import Viewers
from pycatia3dx.system.any_object import AnyObject


class Window(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Window
                | 
                | Represents the window.
                | The window is the object that accommodates one or several viewers to display
                | your objects, and which makes the link with the windowing
                | system.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_viewer(self) -> Viewer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ActiveViewer() As Viewer (Read Only)
                |     Returns the active viewer in the window.
                | 
                |     Example:
                |         This example retrieves the active viewer in the CADWindow window in
                |         ViewerToWorkIn.
                | 
                |          Dim ViewerToWorkIn As Viewer
                |          Set ViewerToWorkIn = CADWindow.ActiveViewer

        :return: Viewer
        """

        return Viewer(self.com_object.ActiveViewer)

    @property
    def caption(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Caption() As CATBSTR
                |     Returns or sets the window caption. The window caption is displayed in the
                |     title bar.
                | 
                |     Example:
                |         This example sets the window caption for the CADWindow window to: CAD
                |         3D Window.
                | 
                |          CADWindow.Caption = "CAD 3D Window"

        :return: str
        """

        return self.com_object.Caption

    @caption.setter
    def caption(self, value: str):
        """
        :param str value:
        """

        self.com_object.Caption = value

    @property
    def height(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Height() As long
                |     Returns or sets the window height. The window height is expressed in
                |     pixels.
                | 
                |     Example:
                |         This example sets the window height for the CADWindow window to 300
                |         pixels.
                | 
                |          CADWindow.Width = 300

        :return: int
        """

        return self.com_object.Height

    @height.setter
    def height(self, value: int):
        """
        :param int value:
        """

        self.com_object.Height = value

    @property
    def left(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Left() As long
                |     Returns or sets the distance of the window with respect to the inner left
                |     side of the frame. This distance is expressed in pixels.
                | 
                |     Example:
                |         This example sets the distance of the window with respect to the inner
                |         left side of the frame for the CADWindow window to 150
                |         pixels.
                | 
                |          CADWindow.Left = 150

        :return: int
        """

        return self.com_object.Left

    @left.setter
    def left(self, value: int):
        """
        :param int value:
        """

        self.com_object.Left = value

    @property
    def page_setup(self) -> PageSetup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property PageSetup() As PageSetup
                |     Returns or sets the page setup of the window. The page setup includes all
                |     parameters to print the window.
                | 
                |     Example:
                |         This example sets the page setup for the CADWindow window to an
                |         existing page setup for the A4 paper size A4PageSetup.
                | 
                |          CADWindow.PageSetup = A4PageSetup

        :return: PageSetup
        """

        return PageSetup(self.com_object.PageSetup)

    @page_setup.setter
    def page_setup(self, value: PageSetup):
        """
        :param PageSetup value:
        """

        self.com_object.PageSetup = value

    @property
    def top(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Top() As long
                |     Returns or sets the distance of the window with respect to the inner top
                |     side of the frame. This distance is expressed in pixels.
                | 
                |     Example:
                |         This example sets the distance of the window with respect to the inner
                |         top side of the frame for the CADWindow window to 50
                |         pixels.
                | 
                |          CADWindow.Top = 50

        :return: int
        """

        return self.com_object.Top

    @top.setter
    def top(self, value: int):
        """
        :param int value:
        """

        self.com_object.Top = value

    @property
    def viewers(self) -> Viewers:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Viewers() As Viewers (Read Only)
                |     Returns the collection of viewers attached to the window.
                | 
                |     Example:
                |         This example retrieves the collection of viewers attached to the
                |         CADWindow window in ViewerCollection.
                | 
                |          Dim ViewerCollection As Viewers
                |          Set ViewerCollection = CADWindow.Viewers

        :return: Viewers
        """

        return Viewers(self.com_object.Viewers)

    @property
    def width(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Width() As long
                |     Returns or sets the window width. The window width is expressed in
                |     pixels.
                | 
                |     Example:
                |         This example sets the window width for the CADWindow window to 450
                |         pixels.
                | 
                |          CADWindow.Width = 450

        :return: int
        """

        return self.com_object.Width

    @width.setter
    def width(self, value: int):
        """
        :param int value:
        """

        self.com_object.Width = value

    @property
    def window_state(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property WindowState() As CatWindowState
                |     Returns or sets the window state.
                | 
                |     Example:
                |         This example sets the window state for the CADWindow window to
                |         catWindowStateMaximized.
                | 
                |          CADWindow.WindowState = catWindowStateMaximized

        :return: int
        """

        return self.com_object.WindowState

    @window_state.setter
    def window_state(self, value: int):
        """
        :param int value:
        """

        self.com_object.WindowState = value

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Activate()
                |     Activates a window. The active window is deactivated and the window to
                |     which the method applies is activated instead.
                | 
                |     Example:
                |         This example activates the CADWindow window.
                | 
                |          CADWindow.Activate()

        :return: None
        """
        return self.com_object.Activate()

    def activate_next(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub ActivateNext()
                |     Activates the window following the current active one in the window
                |     collection.
                | 
                |     Example:
                |         This example activates the window following the current CADWindow
                |         window in the window collection.
                | 
                |          CADWindow.ActivateNext()

        :return: None
        """
        return self.com_object.ActivateNext()

    def activate_previous(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub ActivatePrevious()
                |     Activates the window preceding the current active one in the window
                |     collection.
                | 
                |     Example:
                |         This example activates the window preceding the current CADWindow
                |         window in the window collection.
                | 
                |          CADWindow.ActivatePrevious()

        :return: None
        """
        return self.com_object.ActivatePrevious()

    def close(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Close()
                |     Closes the window. This method displays the dialog box requesting whether
                |     to save the file if the document was modified, except if the
                |     Application.DisplayFileAlerts property was previously set to
                |     False.
                | 
                |     Example:
                |         This example closes the CADWindow window.
                | 
                |          CADWindow.Close()

        :return: None
        """
        return self.com_object.Close()

    def new_window(self) -> 'Window':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func NewWindow() As Window
                |     Creates a new window. The new window displays the same document with the
                |     same viewers and viewpoints than the window to which the method applies, and
                |     becomes the active one.
                | 
                |     Example:
                |         This example creates a new window named CADNewWindow from the CADWindow
                |         window.
                | 
                |          Dim CADNewWindow As Window
                |          Set CADNewWindow = CADWindow.NewWindow()

        :return: Window
        """
        return Window(self.com_object.NewWindow())

    def print_out(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PrintOut()
                |     Prints the active viewer of the window according to the window's page setup
                |     on the default printer.
                | 
                |     Example:
                |         This example prints the CADWindow window's active viewer on the default
                |         printer.
                | 
                |          CADWindow.PrintOut()

        :return: None
        """
        return self.com_object.PrintOut()

    def print_to_file(self, file_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PrintToFile(CATBSTR fileName)
                |     Prints the active viewer of the window according to the window's page setup
                |     in a file instead of being sent to a printer.
                | 
                |     Parameters:
                | 
                |         fileName
                |             The full pathname of the file receiving the data. 
                | 
                |     Example:
                |         This example prints the CADWindow window's active viewer in a
                |         file.
                | 
                |          CADWindow.PrintToFile("e:\\temp\\cadwin.prn")

        :param str file_name:
        :return: None
        """
        return self.com_object.PrintToFile(file_name)

    def __repr__(self):
        return f'Window(name="{self.name}")'
