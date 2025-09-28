"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ViewPoint2D(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Viewpoint2D
                | 
                | Represents the 2D viewpoint.
                | The 2D viewpoint is the object that stores data which defines how your objects
                | are seen to enable their display by a 2D viewer. This data includes namely the
                | origin of the scene, that is the center of the displayed area, and the zoom
                | factor.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def zoom(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Zoom() As double
                |     Returns or sets the zoom factor associated with the
                |     viewpoint.
                | 
                |     Example:
                |         This example retrieves in ZoomFactor the zoom factor associated with
                |         the NiceViewpoint viewpoint, tests if it is less than 1, and if so, sets it to
                |         one and applies it to the viewpoint.
                | 
                |          ZoomFactor = NiceViewpoint.Zoom
                |          If ZoomFactor < 1 Then
                |           ZoomFactor = 1
                |           NiceViewpoint.Zoom(ZoomFactor)
                |          End If

        :return: float
        """

        return self.com_object.Zoom

    @zoom.setter
    def zoom(self, value: float):
        """
        :param float value:
        """

        self.com_object.Zoom = value

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetOrigin(CATSafeArrayVariant oOrigin)
                |     Gets the coordinates of the origin of the viewpoint.
                | 
                |     Example:
                |         This example Gets the origin of the NiceViewpoint
                |         viewpoint.
                | 
                |          Dim origin(1)
                |          NiceViewpoint.GetOrigin origin

        :param tuple o_origin:
        :return: None
        """
        return self.com_object.GetOrigin(o_origin)

    def put_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PutOrigin(CATSafeArrayVariant oOrigin)
                |     Sets the coordinates of the origin of the viewpoint.
                | 
                |     Example:
                |         This example sets the origin of the NiceViewpoint viewpoint to the
                |         point with coordinates (5, 8).
                | 
                |          NiceViewpoint.PutOrigin Array(5, 8)

        :param tuple o_origin:
        :return: None
        """
        return self.com_object.PutOrigin(o_origin)

    def __repr__(self):
        return f'Viewpoint2D(name="{self.name}")'
