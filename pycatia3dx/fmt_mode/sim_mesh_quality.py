"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimMeshQuality(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimMeshQuality
                | 
                | Interface representing mesh quality.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_csv_file(self, i_path: str, i_overwrite: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateCSVFile(CATBSTR iPath,boolean iOverwrite)
                |     Creates a CSV (comma-separated value) report file containing all the
                |     quality data.

        :param str i_path:
        :param bool i_overwrite:
        :return: None
        """
        return self.com_object.CreateCSVFile(i_path, i_overwrite)

    def __repr__(self):
        return f'SimMeshQuality()'
