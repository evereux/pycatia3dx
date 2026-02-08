"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.inertia.inertia import Inertia
from pycatia3dx.interfaces.service import Service
from pycatia3dx.system.any_object import AnyObject


class InertiaService(Service):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         InertiaService
                | 
                | Object representing the service to retrieve an inertia
                | element.
                | 
                | See also:
                |     Editor.GetService
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_inertia_element(self, i_selected_item: AnyObject) -> Inertia:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInertiaElement(AnyObject iSelectedItem) As Inertia
                |     Retrieves the Inertia object.
                | 
                |     Example:
                | 
                |            This example retrieves an Inertia object.
                |            
                | 
                |              Set theInertiaService = CATIA.ActiveEditor.GetService("InertiaService")
                |              Dim theInertia As Inertia
                |              Set theInertia = theInertiaService.GetInertiaElement(theSelection)

        :param AnyObject i_selected_item:
        :return: Inertia
        """
        return Inertia(self.com_object.GetInertiaElement(i_selected_item.com_object))

    def __repr__(self):
        return f'InertiaService(name="{self.name}")'
