"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity


class PLMOpenService(Service):
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
                |                         PLMOpenService
                | 
                | Interface representing the Open service.
                | It can be retreives using the
                | Application.GetSessionService("PLMOpenService")
                | Role: provides the services to Open in authoring session the result of a
                | PLMQuery. The result is loaded in VISU mode.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def plm_open(self, i_plm_entity: PLMEntity) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PLMOpen(PLMEntity iPLMEntity,Editor oEditor)
                |     Opens in the authoring session the result of a PLMQuery. The result is
                |     loaded in VISU mode. This method should be used on Navigation components. It
                |     fails if the entity does not exist in the database.
                | 
                |     Parameters:
                | 
                |         iPLMEntity
                |             The PLMEntity to be opened. Must exist in the database.
                |             
                |         oEditor
                |             The editor of the opened PLMEntity.

        :param PLMEntity i_plm_entity:
        :return: None
        """
        return self.com_object.PLMOpen(i_plm_entity.com_object)

    def plm_open_in_new_window(self, i_plm_entity: PLMEntity, o_editor: Editor) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PLMOpenInNewWindow(PLMEntity iPLMEntity,Editor oEditor)
                |     Opens in a new window the provided entity already loaded in session. This
                |     method should be used on Authoring components. It fails if the provided entity
                |     is not loaded in session.
                | 
                |     Parameters:
                | 
                |         iPLMEntity
                |             The PLMEntity to be opened. Must be opened in session.
                |             
                |         oEditor
                |             The new editor of the opened PLMEntity.

        :param PLMEntity i_plm_entity:
        :param Editor o_editor:
        :return: None
        """
        return self.com_object.PLMOpenInNewWindow(i_plm_entity.com_object, o_editor.com_object)

    def get_last_error(self, o_error_message: str, o_error_code: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub getLastError(CATBSTR oErrorMessage,long oErrorCode)
                |     Retrieves the diagnosis related to the last call to
                |     PLMOpen.
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
        return f'PLMOpenService(name="{self.name}")'
