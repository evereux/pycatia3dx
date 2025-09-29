"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimManagerSimAccess(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimManagerSIMAccess
                | 
                | Interface to access the SIM document of a SIM manager.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def manifest_path(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ManifestPath() As CATBSTR (Read Only)
                |     Returns the manifest path of the SIM document of this SIM
                |     manager.
                |     Role: if necessary, this method will download and check out the SIM files
                |     of the SIM document so that it can be accessed.
                |     Warning:
                | 
                |         Do NOT write to the SIM document if it is currently accessed by this
                |         SIM manager.
                |         The manifest path is NOT guaranteed to be the same on each
                |         call.
                |         The operations performed by this method can NOT be
                |         undone.
                |         The operations performed by this method MAY be time
                |         consuming.
                | 
                |     Note: The returned path can be empty if the SIM document is either
                |     currently accessed by this SIM manager or empty.

        :return: str
        """

        return self.com_object.ManifestPath

    def notify_manifest_modification(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub NotifyManifestModification()
                |     Notifies this SIM manager that the manifest of its SIM document has been
                |     modified.
                |     Role: This method will parse the manifest to detect modifications and make
                |     sure that modified and newly created SIM files of the SIM document get checked
                |     in.
                |     Warning:
                | 
                |         This method will fail if the SIM document is currently accessed by this
                |         SIM manager.
                |         The SIM file paths are NOT guaranteed to be unchanged by this
                |         call.
                |         The operations performed by this method can NOT be
                |         undone.
                |         The operations performed by this method are NOT time
                |         consuming.

        :return: None
        """
        return self.com_object.NotifyManifestModification()

    def __repr__(self):
        return f'SimManagerSimAccess()'
