"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.interfaces.camera_3d import Camera3D
from pycatia3dx.interfaces.viewpoint_3d import ViewPoint3D
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.annotations import Annotations
from pycatia3dx.tps.tps_hyper_links_manager import TPSHyperLinksManager
from pycatia3dx.tps.tps_parallel_on_screen import TPSParallelOnScreen
from pycatia3dx.tps.tps_view import TPSView
from pycatia3dx.tps.tps_views import TPSViews

if TYPE_CHECKING:
    from pycatia3dx.tps.annotation_set import AnnotationSet


class Capture(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Capture
                | 
                | The interface to access a CATIACapture
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_view(self) -> TPSView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActiveView() As TPSView
                |     Retrieves the active view for the capture.

        :return: TpsView
        """

        return TPSView(self.com_object.ActiveView)

    @active_view.setter
    def active_view(self, value: TPSView):
        """
        :param TPSView value:
        """

        self.com_object.ActiveView = value

    @property
    def active_view_state(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActiveViewState() As boolean
                |     Retrieves the Active View state, saved or Not. The Active View state
                |     describes what happens when Capture is displayed, if TRUE, the active view of
                |     the tolerancing set is replaced by the active view of the capture.

        :return: bool
        """

        return self.com_object.ActiveViewState

    @active_view_state.setter
    def active_view_state(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ActiveViewState = value

    @property
    def annotations(self) -> Annotations:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Annotations() As Annotations
                |     Retrieves the TPSs that are visualy managed by this Capture.

        :return: Annotations
        """

        return Annotations(self.com_object.Annotations)

    @annotations.setter
    def annotations(self, value: Annotations):
        """
        :param Annotations value:
        """

        self.com_object.Annotations = value

    @property
    def camera(self) -> Camera3D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Camera() As Camera3D
                |     Retrieves or sets a camera. Deprecated usage: please prefer
                |     Capture.AddViewPoint3D.

        :return: Camera3D
        """

        return Camera3D(self.com_object.Camera)

    @camera.setter
    def camera(self, value: Camera3D):
        """
        :param Camera3D value:
        """

        self.com_object.Camera = value

    @property
    def clipping_plane(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ClippingPlane() As boolean
                |     Retrieves the clipping plane state, activated or Not. The Clipping plane
                |     state describes what happens when Capture is displayed, if TRUE, the active
                |     view is used to define a clipping plane. If FALSE, there is no clipping plane
                |     applied.
                | 
                |     Parameters:
                | 
                |         oClipPlane
                |             The clipping plane state.

        :return: bool
        """

        return self.com_object.ClippingPlane

    @clipping_plane.setter
    def clipping_plane(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ClippingPlane = value

    @property
    def current(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Current() As boolean
                |     Retrieves the Capture state, current or Not.
                | 
                |     Parameters:
                | 
                |         oCurrentState
                |             Capture state. if TRUE the capture is current.that means that after
                |             the creation of the capture, the future TPSs that would be added to the 3D
                |             Shape Representation will belong to the capture.

        :return: bool
        """

        return self.com_object.Current

    @current.setter
    def current(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Current = value

    @property
    def manage_hide_show_body(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ManageHideShowBody() As boolean
                |     Manages the visibility of Part instances, bodies and geometrical sets
                |     across the Capture.
                | 
                |     Parameters:
                | 
                |         obManageHideShowBody
                |             TRUE: If Hide/Show of these elements will be managed FALSE: If
                |             Hide/Show of these elements will not be managed

        :return: bool
        """

        return self.com_object.ManageHideShowBody

    @manage_hide_show_body.setter
    def manage_hide_show_body(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ManageHideShowBody = value

    @property
    def set(self) -> 'AnnotationSet':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Set() As AnnotationSet (Read Only)
                |     Retrieves tolerancing set the Capture belongs too.

        :return: AnnotationSet
        """
        from pycatia3dx.tps.annotation_set import AnnotationSet
        return AnnotationSet(self.com_object.Set)

    @property
    def tps_views(self) -> TPSViews:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TPSViews() As TPSViews
                |     Retrieves the TPS Views that are visualy managed by this Capture.

        :return: TPSViews
        """

        return TPSViews(self.com_object.TPSViews)

    @tps_views.setter
    def tps_views(self, value: TPSViews):
        """
        :param TPSViews value:
        """

        self.com_object.TPSViews = value

    @property
    def view_point(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ViewPoint() As boolean
                |     Retrieves the ViewPoint state, saved or Not. The ViewPoint state describes
                |     what happens when Capture is displayed, if TRUE, the 3D Camera of the Capture
                |     is used to change the 3D ViewPoint.

        :return: bool
        """

        return self.com_object.ViewPoint

    @view_point.setter
    def view_point(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ViewPoint = value

    # todo:
    @property
    def view_point_3d(self) -> ViewPoint3D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ViewPoint3D() As Viewpoint3D
                |     Retrieves or sets the 3D ViewPoint definition.

        :return: ViewPoint3D
        """

        return ViewPoint3D(self.com_object.ViewPoint3D)

    @view_point_3d.setter
    def view_point_3d(self, value: ViewPoint3D):
        """
        :param ViewPoint3D value:
        """

        self.com_object.ViewPoint3D = value

    def add_view_point3_d(self, i_view_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddViewPoint3D(CATBSTR iViewName)
                |     Adds an explicit 3D ViewPoint to the Capture; one can then edit Viewpoint3D
                |     thanks to the property Capture.ViewPoint3D.
                |     The input string is used to search for a view with the same
                |     name.
                |     If found, the Capture is assigned with a 3D ViewPoint that corresponds to
                |     the view point defined by the view.
                | 
                |     See also:
                |         CATIAView
                |     Parameters:
                | 
                |         iViewName
                |             Name of the first view with the same name searched under the
                |             Annotation Set to initialize the 3D ViewPoint with the annotation plane
                |             definition of the retrieved view. When no View is found, the ViewPoint
                |             definition corresponds to any default. 
                | 
                |     See also:
                |         Viewpoint3D

        :param str i_view_name:
        :return: None
        """
        return self.com_object.AddViewPoint3D(i_view_name)

    def display_capture(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DisplayCapture()
                |     Displays the Capture.

        :return: None
        """
        return self.com_object.DisplayCapture()

    def display_capture2(self, ib_apply_mirror: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DisplayCapture2(boolean ibApplyMirror)
                |     Displays the Capture with mirroring annotations
                |     management.
                | 
                |     Parameters:
                | 
                |         out
                |             boolean ibApplyMirror [out] Annotations mirroring management: TRUE:
                |             The annotations mirroring is activated. FALSE: The annotations mirroring is
                |             desactivated.

        :param bool ib_apply_mirror:
        :return: None
        """
        return self.com_object.DisplayCapture2(ib_apply_mirror)

    def get_nbr_of_part_inst_and_body(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbrOfPartInstAndBody() As long
                |     Reads the number of Body and Part Instances assigned to this Capture. This
                |     call is to be called just before @GetPartInstAndBody to allocate the array with
                |     the accurate size. This call is working properly only if ManageHideShowBody is
                |     set to True.
                | 
                |     Parameters:
                | 
                |         oEntityCount
                |             The number of Part Instance(s) and/or Body(ies) associated with the
                |             Capture.

        :return: int
        """
        return self.com_object.GetNbrOfPartInstAndBody()

    def get_part_inst_and_body(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetPartInstAndBody(CATSafeArrayVariant oListOfElements)
                |     Returns the list of Body and Part Instances. This call is working properly
                |     only if ManageHideShowBody is set to True.
                |
                |     Parameters:
                |
                |         oListOfElements
                |             The list of Part Instance(s) and Body(s) bound to this Capture. It
                |             is returned as an array of SafeArrayVariant whose size is given by
                |             GetNbrOfPartInstAndBody.
                |
                |             Note: You can access each constraint as follows:
                |
                |                 1 is in oListOfElements(0)
                |                 2 is in oListOfElements(1)
                |                 oEntityCount is in oListOfElements(oEntityCount-1)

        :return: tuple
        """
        return self.com_object.GetPartInstAndBody(tuple)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_part_inst_and_body'
        # vba_code = """
        # Public Function get_part_inst_and_body(capture)
        #     Dim oListOfElements (2)
        #     capture.GetPartInstAndBody oListOfElements
        #     get_part_inst_and_body = oListOfElements
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def hyper_link_manager(self) -> TPSHyperLinksManager:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HyperLinkManager() As TPSHyperLinksManager
                |     Gets the annotation on HyperLinks manager interface.

        :return: TPSHyperLinksManager
        """
        return TPSHyperLinksManager(self.com_object.HyperLinkManager())

    def remove_view_point3_d(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveViewPoint3D()
                |     Removes any 3D ViewPoint set to the Capture.

        :return: None
        """
        return self.com_object.RemoveViewPoint3D()

    def set_part_inst_and_body(self, i_list_of_elements: tuple, i_entity_count: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetPartInstAndBody(CATSafeArrayVariant iListOfElements,long
                | iEntityCount)
                |     Sets the list of Body and Part Instances. This call is working properly
                |     only if ManageHideShowBody is set to True.
                |
                |     Parameters:
                |
                |         iListOfElements
                |             The list of Part Instance(s) and Body(s) to assign to this Capture.
                |             iEntityCount of elements are taken for the SafeArrayVariant.
                |
                |         iEntityCount
                |             The number of items in the given stack.

        :param tuple i_list_of_elements:
        :param int i_entity_count:
        :return: None
        """
        return self.com_object.SetPartInstAndBody(i_list_of_elements, i_entity_count)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_part_inst_and_body'
        # vba_code = """
        # Public Function set_part_inst_and_body(capture)
        #     Dim iListOfElements (2)
        #     capture.SetPartInstAndBody iListOfElements
        #     set_part_inst_and_body = iListOfElements
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TPSParallelOnScreen() As TPSParallelOnScreen
                |     Gets the annotation on TPSParallelOnScreen interface. 

        :return: TPSParallelOnScreen
        """
        return TPSParallelOnScreen(self.com_object.TPSParallelOnScreen())

    def __repr__(self):
        return f'Capture(name="{self.name}")'
