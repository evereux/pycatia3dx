"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.opns_inertial.inertia_box import InertiaBox
from pycatia3dx.system.any_object import AnyObject


class InertiaBoxService(Service):
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
                |                         InertiaBoxService
                | 
                | Object representing the service to retrieve an inertia box
                | element.
                | 
                | See also:
                |     Editor.GetService
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_inertia_box_element(self, i_selected_item: AnyObject) -> InertiaBox:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInertiaBoxElement(AnyObject iSelectedItem) As
                | InertiaBox
                |     Retrieves the Inertia box object.
                | 
                |     Example:
                | 
                |            This example retrieves an Inertia box object.
                |            
                | 
                |              Set theInertiaBoxService = CATIA.ActiveEditor.GetService("InertiaBoxService")
                |              Dim theInertiaBox As InertiaBox
                |              Set theInertiaBox = theInertiaBoxService.GetInertiaBoxElement(theSelection)

        :param AnyObject i_selected_item:
        :return: InertiaBox
        """
        return InertiaBox(self.com_object.GetInertiaBoxElement(i_selected_item.com_object))

    def __repr__(self):
        return f'InertiaBoxService(name="{self.name}")'
