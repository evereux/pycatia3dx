"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.light_sources import LightSources
from pycatia3dx.interfaces.viewer import Viewer
from pycatia3dx.interfaces.viewpoint_3d import ViewPoint3D


class Viewer3D(Viewer):
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
                |                         Viewer3D
                | 
                | Represents a 3D viewer.
                | The 3D viewer aggregates a 3D viewpoint to display a 3D scene. In addition, the
                | Viewer3D object manages the lighting, the depth effects, the navigation style,
                | and the rendering mode.
                | 
                | See also:
                |     Viewpoint3D, CatLightingMode, CatNavigationStyle,
                |     CatRenderingMode
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def clipping_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ClippingMode() As CatClippingMode
                |     Returns or sets the clipping mode.
                | 
                |     Example:
                |         This example sets the depth effect for the My3DViewer 3D viewer to
                |         catClippingModeNearAndFar.
                | 
                |          My3DViewer.ClippingMode = catClippingModeNearAndFar

        :return: int
        """

        return self.com_object.ClippingMode

    @clipping_mode.setter
    def clipping_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ClippingMode = value

    @property
    def far_limit(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property FarLimit() As double
                |     Returns or sets the far limit for the far clipping plane. The distance is
                |     measured from the eye location, that is the origin of the viewpoint, and is
                |     expressed in model unit. The far clipping plane is available with the
                |     catClippingModeFar and catClippingModeNearAndFar values of the CatClippingMode
                |     enumeration only.
                | 
                |     Example:
                |         This example sets the far limit for the far clipping plane of the
                |         My3DViewer 3D viewer to 150 model units.
                | 
                |          My3DViewer.FarLimit = 150

        :return: float
        """

        return self.com_object.FarLimit

    @far_limit.setter
    def far_limit(self, value: float):
        """
        :param float value:
        """

        self.com_object.FarLimit = value

    @property
    def foggy(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Foggy() As boolean
                |     Returns or sets the fog mode. Useful when clipping is
                |     enabled.
                | 
                |     Example:
                |         This example sets the fog on for the My3DViewer 3D
                |         viewer:
                | 
                |          My3DViewer.Foggy = True

        :return: bool
        """

        return self.com_object.Foggy

    @foggy.setter
    def foggy(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Foggy = value

    @property
    def ground(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Ground() As boolean
                |     Returns or sets the ground displaying mode.
                | 
                |     Example:
                |         This example makes the ground visible for the My3DViewer 3D
                |         viewer:
                | 
                |          My3DViewer.Ground = True

        :return: bool
        """

        return self.com_object.Ground

    @ground.setter
    def ground(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Ground = value

    @property
    def light_sources(self) -> LightSources:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property LightSources() As LightSources (Read Only)
                |     Returns the viewer's light source collection.
                | 
                |     Example:
                |         This example retrieves the light source collection for the My3DViewer
                |         3D viewer in VPLightSources.
                | 
                |          Set VPLightSources = My3DViewer.LightSources

        :return: LightSources
        """

        return LightSources(self.com_object.LightSources)

    @property
    def lighting_intensity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property LightingIntensity() As double
                |     Returns or sets the lighting intensity. The lighting intensity ranges
                |     between 0 and 1.
                | 
                |     Example:
                |         This example sets the lighting intensity for the My3DViewer 3D viewer
                |         to 0.35.
                | 
                |          My3DViewer.LightingIntensity = 0.35

        :return: float
        """

        return self.com_object.LightingIntensity

    @lighting_intensity.setter
    def lighting_intensity(self, value: float):
        """
        :param float value:
        """

        self.com_object.LightingIntensity = value

    @property
    def lighting_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property LightingMode() As CatLightingMode
                |     Returns or sets the lighting mode.
                | 
                |     Example:
                |         This example sets the lighting mode for the My3DViewer 3D viewer to
                |         catInfiniteLightSource.
                | 
                |          My3DViewer.LightingMode = catInfiniteLightSource

        :return: int
        """

        return self.com_object.LightingMode

    @lighting_mode.setter
    def lighting_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.LightingMode = value

    @property
    def navigation_style(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property NavigationStyle() As CatNavigationStyle
                |     Returns or sets the navigation style.
                | 
                |     Example:
                |         This example sets the navigation style for the My3DViewer 3D viewer to
                |         catNavigationWalk.
                | 
                |          My3DViewer.NavigationStyle = catNavigationWalk

        :return: int
        """

        return self.com_object.NavigationStyle

    @navigation_style.setter
    def navigation_style(self, value: int):
        """
        :param int value:
        """

        self.com_object.NavigationStyle = value

    @property
    def near_limit(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property NearLimit() As double
                |     Returns or sets the near limit for the near clipping plane. The distance is
                |     measured from the eye location, that is the origin of the viewpoint, and is
                |     expressed in model unit. The near clipping plane is available with the
                |     catClippingModeNear and catClippingModeNearAndFar values of the CatClippingMode
                |     enumeration only.
                | 
                |     Example:
                |         This example sets the near limit for the near clipping plane of the
                |         My3DViewer 3D viewer to 75 model units.
                | 
                |          My3DViewer.NearLimit = 75

        :return: float
        """

        return self.com_object.NearLimit

    @near_limit.setter
    def near_limit(self, value: float):
        """
        :param float value:
        """

        self.com_object.NearLimit = value

    @property
    def rendering_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property RenderingMode() As CatRenderingMode
                |     Returns or sets the rendering mode.
                | 
                |     Example:
                |         This example sets the rendering mode for the My3DViewer 3D viewer to
                |         catRenderShadingWithEdges.
                | 
                |          My3DViewer.RenderingMode = catRenderShadingWithEdges

        :return: int
        """

        return int(self.com_object.RenderingMode)

    @rendering_mode.setter
    def rendering_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.RenderingMode = value

    @property
    def viewpoint_3d(self) -> ViewPoint3D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Viewpoint3D() As Viewpoint3D
                |     Returns or sets the 3D viewpoint of a 3D viewer.
                | 
                |     Example:
                |         This example retrieves the Nice3DViewpoint 3D viewpoint from the
                |         My3DViewer 3D viewer.
                | 
                |          Dim Nice3DViewpoint As Viewpoint3D
                |          Set Nice3DViewpoint = My3DViewer.Viewpoint3D

        :return: Viewpoint3D
        """

        return ViewPoint3D(self.com_object.ViewPoint3D)

    @viewpoint_3d.setter
    def viewpoint_3d(self, value: ViewPoint3D):
        """
        :param ViewPoint3D value:
        """

        self.com_object.ViewPoint3D = value

    def rotate(self, i_axis: tuple, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub Rotate(CATSafeArrayVariant iAxis,double iAngle)
                |     Applies a rotation. The rotation of iAngle degrees is applied to the
                |     viewer's contents around the axis iAxis (an array of 3 Variants), the invariant
                |     point being the target (ie: Origin +
                |     FocusDistance*SightDirection).
                |
                |     Example:
                |         This applies a rotation of 10 degrees around the Up Direction to the
                |         contents of the MyViewer3D viewer.
                |
                |          MyViewer3D.Rotate MyViewer3D.UpDirection, 10

        :param tuple i_axis:
        :param float i_angle:
        :return: None
        """
        return self.com_object.Rotate(i_axis, i_angle)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'rotate'
        # vba_code = """
        # Public Function rotate(viewer3_d)
        #     Dim iAxis (2)
        #     viewer3_d.Rotate iAxis
        #     rotate = iAxis
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def translate(self, i_vector: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub Translate(CATSafeArrayVariant iVector)
                |     Applies a translation. The translation vector is iVector (an array of 3
                |     Variants).
                |
                |     Example:
                |         This applies a translation along (1, 1, 1) to the contents of the
                |         MyViewer3D viewer.
                |
                |          MyViewer3D.Translate Array(1, 1, 1)

        :param tuple i_vector:
        :return: None
        """
        return self.com_object.Translate(i_vector)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'translate'
        # vba_code = """
        # Public Function translate(viewer3_d)
        #     Dim iVector (2)
        #     viewer3_d.Translate iVector
        #     translate = iVector
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Viewer3D(name="{self.name}")'
