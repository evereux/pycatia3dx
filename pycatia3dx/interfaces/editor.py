"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.selection import Selection
from pycatia3dx.interfaces.service import Service
from pycatia3dx.system.any_object import AnyObject


class Editor(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Editor
                | 
                | Represents an editor.
                | In the Model View Controller paradigm, the editor plays the Controller role.
                | The editor federates all the objects that can be interactively edited in the
                | same window. It holds the current workbench and thus maintains the list of all
                | the commands that can be launched from menus and toolbars when this window is
                | active to edit the objects it controls according to the root object PLM
                | type.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ActiveObject() As AnyObject (Read Only)
                |     Returns the active object.
                |     The active object provides editing commands for itself or its content.
                |     There is only one active object at a time per editor.

        :return: AnyObject
        """

        return AnyObject(self.com_object.ActiveObject)

    @property
    def selection(self) -> Selection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Selection() As Selection (Read Only)
                |     Returns the selection object.
                |     The selection object contains the objects the end user selected, usually
                |     with the mouse, and which are candidates as subjects for the next
                |     action.
                | 
                |     Example:
                |         This example returns in Select1 the selection object of the active
                |         editor.
                | 
                |          Dim Select1 As Selection
                |          Set Select1 = CATIA.ActiveEditor.Selection

        :return: Selection
        """

        return Selection(self.com_object.Selection)

    def get_service(self, i_service: str) -> Service:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetService(CATBSTR iService) As Service
                |     Returns the specified service.
                | 
                |     Parameters:
                | 
                |         iService
                |             The identifier of the service to be retrieved 
                | 
                |     Returns:
                |         The specified service
                | 
                |         Example:
                |             This example retrieves in Service1 the VisuServices editor's
                |             visualization service from the active editor.
                | 
                |              Dim Service1 As Service
                |              Set Service1 = CATIA.ActiveEditor.GetService("VisuServices")

        :param str i_service:
        :return: Service
        """
        return Service(self.com_object.GetService(i_service))

    def __repr__(self):
        return f'Editor(name="{self.name}")'
