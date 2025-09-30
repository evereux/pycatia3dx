"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_modeller_base.plm_entities import PLMEntities


class PLMAppContext(Service):

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
                |                         PLMAppContext
                | 
                | Interface representing abstract service to manage Editors.
                | This object can only be accessed through inherited objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def edited_content(self) -> PLMEntities:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EditedContent() As PLMEntities (Read Only)
                |     Returns Root entities of active Editor.

        :return: PLMEntities
        """

        return PLMEntities(self.com_object.EditedContent)

    def __repr__(self):
        return f'PlmAppContext(name="{ self.name }")'
