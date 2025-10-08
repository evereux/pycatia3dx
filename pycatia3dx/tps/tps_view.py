"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.text import Text
from pycatia3dx.tps.tps_hyper_links_manager import TPSHyperLinksManager

if TYPE_CHECKING:
    from pycatia3dx.tps.annotations import Annotations


class TPSView(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TPSView

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def annotation_plane(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnnotationPlane() As CATSafeArrayVariant (Read Only)
                |     Gets annotation plane of the view.
                | 
                |     Parameters:
                | 
                |         oMathPlane
                |             Mathematical plane definition of the View.

        :return: tuple
        """

        return self.com_object.AnnotationPlane

    @property
    def annotation_sketch(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnnotationSketch(AnyObject Layout2DLView)
                |     Sets / Gets the annotation Sketch associated under the current
                |     View.
                | 
                |     Parameters:
                | 
                |         Layout2DLView
                |             2D Layout View used by current View as annotation sketch.

        :return: AnyObject
        """

        return AnyObject(self.com_object.AnnotationSketch)

    @annotation_sketch.setter
    def annotation_sketch(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.AnnotationSketch = value.com_object

    @property
    def annotations(self) -> 'Annotations':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Annotations() As Annotations (Read Only)
                |     Retrieves the TPS components of the View.
                | 
                |     Parameters:
                | 
                |         oAnnots
                |             Collection of returned component.

        :return: Annotations
        """
        from pycatia3dx.tps.annotations import Annotations
        return Annotations(self.com_object.Annotations)

    @property
    def display_ratio(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DisplayRatio(double RatioValue)
                |     Sets / Gets the ratio of current View.
                | 
                |     Parameters:
                | 
                |         RatioValue
                |             Ratio applied to the View.

        :return: float
        """

        return self.com_object.DisplayRatio

    @display_ratio.setter
    def display_ratio(self, value: float):
        """
        :param False value:
        """

        self.com_object.DisplayRatio = value

    @property
    def view_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ViewType() As long (Read Only)
                |     Gets view type.
                | 
                |     Parameters:
                | 
                |         oViewType
                |             The view type
                |             Legal values:
                | 
                |                 1: Front View
                |                 2: Section View
                |                 3: Cut View

        :return: int
        """

        return self.com_object.ViewType

    def add_view_text(self) -> Text:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddViewText() As Text
                |     Creates a ViewText associated to the CATIAView.
                | 
                |     Parameters:
                | 
                |         oViewText
                |             The new created Viewtext.

        :return: Text
        """
        return Text(self.com_object.AddViewText())

    def get_view_text(self) -> Text:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetViewText() As Text
                |     Gets the viewtext on the View interface.
                | 
                |     Parameters:
                | 
                |         oViewText
                |             The viewtext of the CATIAView.

        :return: Text
        """
        return Text(self.com_object.GetViewText())

    def has_view_text(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasViewText() As boolean
                |     Checks if there is a viewtext in the view.

        :return: bool
        """
        return self.com_object.HasViewText()

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

    def __repr__(self):
        return f'TpsView(name="{self.name}")'
