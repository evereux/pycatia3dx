"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.cameras import Cameras
from pycatia3dx.interfaces.service import Service
from pycatia3dx.interfaces.window import Window


class VisuServices(Service):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         VisuServices
                | 
                | Represents the visualizations services.
                | It gathers all the commands to retrieve the camera collection, create a new
                | window, manage the model hidden element visibility and manage the filters and
                | layers. This service can be retrieve from an Editor
                | 
                | Example:
                | 
                |  Dim Editor1 as Editor
                |  Dim VisuServices1 as VisuServices
                |  
                |  Set Editor1 = CATIA.ActiveEditor
                |  Set VisuServices1 = Editor1.GetService("VisuServices")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def cameras(self) -> Cameras:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Cameras() As Cameras (Read Only)
                |     Returns the model collection of cameras.
                | 
                |     Example:
                |         This example retrieves in CameraCollection the collection of cameras
                |         attached to the ViuServices1 VisuServices.
                | 
                |          Dim CameraCollection As Cameras
                |          Set CameraCollection = ViuServices1.Cameras

        :return: Cameras

        """

        return Cameras(self.com_object.Cameras)

    @property
    def current_filter(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property CurrentFilter() As CATBSTR
                |     Returns or sets the current visualization filter. CurrentFilter uses the
                |     filter name and not its definition. The "All visible" filter means that all
                |     layers are visible. For all filters, remind that the current layer is always
                |     visible.
                | 
                |     Example:
                |         This example makes the filter named "Filter001" as the current
                |         visualization filter for the ViuServices1
                |         VisuServices.
                | 
                |          VisuServices1.CurrentFilter = "Filter001"

        :return: str
        """

        return self.com_object.CurrentFilter

    @current_filter.setter
    def current_filter(self, value: str):
        """
        :param str value:
        """

        self.com_object.CurrentFilter = value

    @property
    def current_layer(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property CurrentLayer() As CATBSTR
                |     Returns or sets the current layer. CurrentLayer uses the layer name and not
                |     its number. The "None" layer means that there is no current
                |     layer.
                | 
                |     Example:
                |         This example makes the layer named "Layer 3" as the current layer for
                |         the ViuServices1 VisuServices.
                | 
                |          VisuServices.CurrentLayer = "Layer 3"

        :return: str
        """

        return self.com_object.CurrentLayer

    @current_layer.setter
    def current_layer(self, value: str):
        """
        :param str value:
        """

        self.com_object.CurrentLayer = value

    @property
    def see_hidden_elements(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property SeeHiddenElements() As boolean
                |     Returns or sets the model hidden elements visibility.
                |     True if the model hidden elements are visible for the
                |     user.
                | 
                |     Example:
                |         This example makes the VisuService model's hidden elements
                |         visible.
                | 
                |          VisuService.SeeHiddenElements = True

        :return: bool
        """

        return self.com_object.SeeHiddenElements

    @see_hidden_elements.setter
    def see_hidden_elements(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SeeHiddenElements = value

    def create_filter(self, i_filter_name: str, i_filter_definition: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub CreateFilter(CATBSTR iFilterName,CATBSTR
                | iFilterDefinition)
                |     Creates a new visualization filter from a name and a definition. Fails if
                |     there is already a filter named iFilterName.
                | 
                |     Parameters:
                | 
                |         iFilterName
                |             The filter name. 
                |         iFilterDefinition
                |             The filter definition 
                |         Example:
                |             This example creates the filter named "Filter001" and with "layer=
                |             2 & layer= 1" definition for the ViuServices1
                |             VisuServices.
                | 
                |              ViuServices1.CreateFilter ("Filter001", "layer= 2 & layer=
                |              1")

        :param str i_filter_name:
        :param str i_filter_definition:
        :return: None
        """
        return self.com_object.CreateFilter(i_filter_name, i_filter_definition)

    def new_window(self) -> Window:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func NewWindow() As Window
                |     Creates a new window for the model. This implies creating a window,
                |     displaying the model in this window, making this model the active one if it was
                |     not, making this window the active one, and adding the window to the collection
                |     of windows.
                | 
                |     Example:
                |         This example creates the MyWindow new window for the VisuServ model
                |         visualization services.
                | 
                |          Dim MyWindow As Window
                |          Set MyWindow = VisuServ.NewWindow()

        :return: Window
        """
        return Window(self.com_object.NewWindow())

    def remove_filter(self, i_filter_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub RemoveFilter(CATBSTR iFilterName)
                |     Removes an existing visualization filter. Fails if the filter to be removed
                |     is the current filter.
                | 
                |     Parameters:
                | 
                |         iFilterName
                |             The filter name. 
                |         Example:
                |             This example removes the filter named "Filter001" for the
                |             ViuServices1 VisuServices.
                | 
                |              ViuServices1.RemoveFilter ("Filter001")

        :param str i_filter_name:
        :return: None
        """
        return self.com_object.RemoveFilter(i_filter_name)

    def __repr__(self):
        return f'VisuServices(name="{self.name}")'
