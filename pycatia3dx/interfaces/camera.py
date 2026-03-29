"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx import CatCameraType
from pycatia3dx.system.any_object import AnyObject


class Camera(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Camera
                | 
                | Represents the camera.
                | The camera is the object that stores a viewpoint saved from a viewer at a given
                | moment using the Viewer.NewCamera method of the Viewer object. The viewpoint
                | stored in the camera can then be applied to another viewer to display the
                | document in this viewer according to this viewpoint.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> CatCameraType:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Type() As CatCameraType (Read Only)
                |     Returns the camera's type.
                | 
                |     Example:
                |         This example retrieves in MyCameraType the type of the MyCamera 3D
                |         camera and applies the viewpoint stored in this camera to the active
                |         viewer.
                | 
                |          MyCameraType = MyCamera.Type
                |          CATIA.ActiveWindow.ActiveViewer.Viewpoint3D = MyCamera.Viewpoint3D
                |          
                | 
                |         The value returned by the Type property in MyCameraType is catCamera3D

        :return: CatCameraType
        """

        return self.com_object.Type

    def __repr__(self):
        return f'Camera(name="{self.name}")'
