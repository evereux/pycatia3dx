"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service


class ElecImportFinalizerService(Service):

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
                |                         ElecImportFinalizerService
                | 
                | The interface to access a CATIAElecImportFinalizerService.
                | 
                | This interface perform the POST PROCESS of Electrical Entities after FBDI
                | Command is complete. Performs Actions equivalent to Finalize Import in
                | Electrical Harness WB
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def finalize(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Finalize()
                |     Performs Actions equivalent to Finalize Import in Electrical Harness WB.

        :return: None
        """
        return self.com_object.Finalize()

    def __repr__(self):
        return f'ElecImportFinalizerService(name="{ self.name }")'
