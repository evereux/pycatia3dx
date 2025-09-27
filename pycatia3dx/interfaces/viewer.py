"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.camera import Camera
from pycatia3dx.system.any_object import AnyObject


class Viewer(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Viewer
                | 
                | Represents the viewer.
                | The viewer is the object that makes your objects display on the
                | screen.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def full_screen(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property FullScreen() As boolean
                |     Returns or sets the state of a viewer to occupy the whole
                |     screen.
                |     True if the viewer occupies the whole screen.
                | 
                |     Example:
                |         This example retrieves in IsFullScreen whether the MyViewer viewer
                |         occupies the whole screen.
                | 
                |          IsFullScreen = MyViewer.FullScreen

        :return: bool
        """

        return self.com_object.FullScreen

    @full_screen.setter
    def full_screen(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FullScreen = value

    @property
    def height(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Height() As long (Read Only)
                |     Returns the viewer's height, in pixels.
                | 
                |     Example:
                |         This example retrieves the height of the MyViewer
                |         viewer.
                | 
                |          h = MyViewer.Height

        :return: int
        """

        return self.com_object.Height

    @property
    def width(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Width() As long (Read Only)
                |     Returns the viewer's width, in pixels.
                | 
                |     Example:
                |         This example retrieves the width of the MyViewer
                |         viewer.
                | 
                |          w = MyViewer.Width

        :return: int
        """

        return self.com_object.Width

    def abort_all_animations(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub AbortAllAnimations()
                |     Abort all the running animations and go directly to their final
                |     state
                | 
                |     Example:
                |         This example aborts the animations of the MyViewer
                |         viewer.
                | 
                |          MyViewer.AbortAllAnimations()

        :return: None
        """
        return self.com_object.AbortAllAnimations()

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Activate()
                |     Activates the viewer in the window.
                | 
                |     Example:
                |         This example activates Viewers(1) in the window
                |         MyWindow.
                | 
                |          MyWindow.Viewers(1).Activate()

        :return: None
        """
        return self.com_object.Activate()

    def capture_to_file(self, i_format: int, i_file: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub CaptureToFile(CatCaptureFormat iFormat,CATBSTR iFile)
                |     Captures the actually displayed scene by the viewer as an image, and stores
                |     the image in a file. Clipped parts of the scene are also clipped in the
                |     captured image. Images can be captured as CGM, EMF, TIFF, TIFF Greyscale, BMP,
                |     and JPEG images.
                | 
                |     Parameters:
                | 
                |         iFormat
                |             The format in which the image will be created 
                |         iFile
                |             The full pathname of the file into which you want to store the
                |             captured image 
                |         Example:
                |             This example captures the displayed part of the MyViewer viewer as
                |             a BMP image, and stores it in the e:\MyImage.bmp
                |             file.
                | 
                |              MyViewer.CaptureToFile catCaptureFormatBMP, "e:\MyImage.bmp"

        :param CatCaptureFormat i_format:
        :param str i_file:
        :return: None
        """
        return self.com_object.CaptureToFile(i_format, i_file)

    def get_background_color(self, color: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetBackgroundColor(CATSafeArrayVariant color)
                |     Gets the viewer's background color. The color is expressed in the RGB color
                |     mode, as a triplet of coordinates ranging from 0 to 1 for the red, green, and
                |     blue colors respectively.
                | 
                |     Example:
                |         This example gets the background color of the MyViewer
                |         viewer.
                | 
                |          Dim color(2)
                |          MyViewer.GetBackgroundColor color

        :param tuple color:
        :return: None
        """
        return self.com_object.GetBackgroundColor(color)

    def new_camera(self) -> Camera:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func NewCamera() As Camera
                |     Creates a new camera from the viewpoint of the viewer.
                | 
                |     Example:
                |         This example creates the MyCamera new camera by using the current
                |         viewpoint of the MyViewer viewer.
                | 
                |          Dim MyCamera As Camera
                |          Set MyCamera = MyViewer.NewCamera()

        :return: Camera
        """
        return Camera(self.com_object.NewCamera())

    def put_background_color(self, color: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PutBackgroundColor(CATSafeArrayVariant color)
                |     Sets the viewer's background color. The color is expressed in the RGB color
                |     mode, as a triplet of coordinates ranging from 0 to 1 for the red, green, and
                |     blue colors respectively. This method is working only with "None" design
                |     ambience.
                | 
                |     Example:
                |         This example sets the background color of the MyViewer viewer to blue,
                |         that is the color with (0.,0.,1.) coordinates
                | 
                |          MyViewer.PutBackgroundColor Array(0, 0, 1)

        :param tuple color:
        :return: None
        """
        return self.com_object.PutBackgroundColor(color)

    def reframe(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Reframe()
                |     Reframes the viewer's contents (Fits all in). Reframing means that the
                |     viewer's contents is zoomed in or out to enable every object of the scene to be
                |     displayed in such a way that most of the space available in the viewer is used,
                |     just leaving a thin empty strip around the scene.
                | 
                |     Example:
                |         This example reframes the contents of the MyViewer
                |         viewer.
                | 
                |          MyViewer.Reframe()

        :return: None
        """
        return self.com_object.Reframe()

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Update()
                |     Updates the viewer's contents. Since the viewer is not automatically
                |     updated after a viewpoint modification (for performance reasons), it must be
                |     explicitely redrawn when needed.
                | 
                |     Example:
                |         This example updates the contents of the MyViewer
                |         viewer.
                | 
                |          MyViewer.Update()

        :return: None
        """
        return self.com_object.Update()

    def zoom_in(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub ZoomIn()
                |     Zooms in the viewer's contents.
                | 
                |     Example:
                |         This example zooms in the contents of the MyViewer
                |         viewer.
                | 
                |          MyViewer.ZoomIn()

        :return: None
        """
        return self.com_object.ZoomIn()

    def zoom_out(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub ZoomOut()
                |     Zooms out the viewer's contents.
                | 
                |     Example:
                |         This example zooms out the contents of the MyViewer
                |         viewer.
                | 
                |          MyViewer.ZoomOut()

        :return: None
        """
        return self.com_object.ZoomOut()

    def __repr__(self):
        return f'Viewer(name="{self.name}")'
