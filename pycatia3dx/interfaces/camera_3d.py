"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.camera import Camera
from pycatia3dx.interfaces.viewpoint_3d import ViewPoint3D


class Camera3D(Camera):
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
                |                         Camera3D
                | 
                | Represents a 3D camera.
                | The 3D camera stores a 3D viewpoint, that is a Viewpoint3D
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def viewpoint_3d(self) -> ViewPoint3D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Viewpoint3D() As Viewpoint3D
                |     Returns or sets the 3D viewpoint of a 3D camera.
                | 
                |     Example:
                |         Assume the active window is a SpecsAndGeomWindow object. This example
                |         retrieves the Viewpoint3D of the active 3D viewer and creates from it a
                |         Camera3D you handle using the MyCamera variable. Then the camera zoom is set to
                |         2, and the camera's viewpoint is assigned to the active
                |         viewer.
                | 
                |          Dim MyCamera As Camera3D
                |          Set MyCamera = CATIA.ActiveWindow.ActiveViewer.NewCamera()
                |          MyCamera.Viewpoint3D.Zoom = 2
                |          CATIA.ActiveWindow.ActiveViewer.Viewpoint3D = MyCamera.Viewpoint3D

        :return: Viewpoint3D
        """

        return ViewPoint3D(self.com_object.ViewPoint3D)

    @viewpoint_3d.setter
    def viewpoint_3d(self, value: ViewPoint3D):
        """
        :param ViewPoint3D value:
        """

        self.com_object.ViewPoint3D = value

    def __repr__(self):
        return f'Camera3D(name="{self.name}")'
