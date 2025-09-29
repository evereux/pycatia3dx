"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sim_rep.sim_import_export_args import SimImportExportArgs
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimManagerSimImport(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimManagerSIMImport
                | 
                | Represents the service to import data into a SIM manager.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def args(self) -> SimImportExportArgs:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Args() As SimImportExportArgs (Read Only)
                |     Gets the current arguments of the import operation.

        :return: SimImportExportArgs
        """

        return SimImportExportArgs(self.com_object.Args)

    def import_(self, i_importer_id: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Import(CATBSTR iImporterId)
                |     Imports data into this SIM manager thanks to a given SIM importer
                |     (identified by its id) using the current import arguments.
                | 
                |     Parameters:
                | 
                |         iImporterId:
                |             The importer id.

        :param str i_importer_id:
        :return: None
        """
        return self.com_object.Import(i_importer_id)

    def __repr__(self):
        return f'SimManagerSimImport()'
