"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service


class PlayerServices(Service):
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
                |                         PlayerServices
                | 
                | Represents the PLM Player services.
                | This service can be retrieve from an Editor
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def play(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Play()
                |     Launches the Play function of the PLM PLayer.

        :return: None
        """
        return self.com_object.Play()

    def stop(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Stop()
                |     Launches the Stop function of the PLM PLayer.

        :return: None
        """
        return self.com_object.Stop()

    def __repr__(self):
        return f'PlayerServices(name="{self.name}")'
