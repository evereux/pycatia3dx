"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.camera import Camera
from pycatia3dx.interfaces.viewpoint_2d import ViewPoint2D


class Camera2D(Camera):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Camera
                |                         Camera2D
                | 
                | Represents a 2D camera.
                | The 2D camera stores a 2D viewpoint, that is a Viewpoint2D
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def viewpoint_2d(self) -> ViewPoint2D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Viewpoint2D() As Viewpoint2D
                |     Returns or sets the 2D viewpoint of a 2D camera.
                | 
                |     Example:
                |         Assume the active window is a SpecsAndGeomWindow object. This example
                |         retrieves the Viewpoint2D of the SpecsViewer and creates from it a Camera2D you
                |         handle using the MyCamera variable. Then the camera zoom is set to 2, and the
                |         camera's viewpoint is assigned to the SpecsViewer.
                | 
                |          Dim MyCamera As Camera
                |          Set MyCamera = CATIA.ActiveWindow.SpecsViewer.NewCamera()
                |          MyCamera.Viewpoint2D.Zoom = 2
                |          CATIA.ActiveWindow.SpecsViewer.Viewpoint2D = MyCamera.Viewpoint2D

        :return: Viewpoint2D
        """

        return ViewPoint2D(self.com_object.ViewPoint2D)

    @viewpoint_2d.setter
    def viewpoint_2d(self, value: ViewPoint2D):
        """
        :param ViewPoint2D value:
        """

        self.com_object.ViewPoint2D = value

    def __repr__(self):
        return f'Camera2D(name="{self.name}")'
