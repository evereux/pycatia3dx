"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service


class PLMPropagateService(Service):

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
                |                         PLMPropagateService
                | 
                | Interface representing the Save service.
                | It can be retreives using the
                | Application.GetSessionService("PLMPropagateService")
                | Role: provides the service to propagate modifications to the PLM provider
                | repository.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def plm_propagate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PLMPropagate()
                |     Propagate CATIAEditor modifications to the PLM provider repository.

        :return: None
        """
        return self.com_object.PLMPropagate()

    def save(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Save()
                | 
                |     Deprecated:
                |         V6R2011x

        :return: None
        """
        return self.com_object.Save()

    def get_last_error(self, o_error_message: str, o_error_code: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub getLastError(CATBSTR oErrorMessage,long oErrorCode)
                |     Retrieves the diagnosis related to the last call to Save.
                | 
                |     Parameters:
                | 
                |         oErrorMessage
                |             The error message. 
                |         oErrorCode
                |             The error code.
                |             Legal values: 0: action successfully performed, other values:
                |             action failed.

        :param str o_error_message:
        :param int o_error_code:
        :return: None
        """
        return self.com_object.getLastError(o_error_message, o_error_code)

    def __repr__(self):
        return f'PlmPropagateService(name="{ self.name }")'
