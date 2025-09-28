"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.viewer import Viewer
from pycatia3dx.interfaces.viewpoint_2d import ViewPoint2D


class Viewer2D(Viewer):
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
                |                         Viewer2D
                | 
                | Represents a 2D viewer.
                | The 2D viewer aggregates a 2D viewpoint to display a 2D scene.
    
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
                |     Returns or sets the 2D viewpoint of a 2D viewer.
                | 
                |     Example:
                |         This example retrieves the Nice2DViewpoint 2D viewpoint from the
                |         My2DViewer 2D viewer.
                | 
                |          Dim Nice2DViewpoint As Viewpoint2D
                |          Set Nice2DViewpoint = My2DViewer.Viewpoint2D

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
        return f'Viewer2D(name="{self.name}")'
