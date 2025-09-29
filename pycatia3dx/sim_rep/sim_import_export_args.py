"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sim_rep.sim_parameter_set import SimParameterSet
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimImportExportArgs(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimImportExportArgs
                | 
                | Represents the arguments used to import/export data to/from a SIM
                | manager.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def parameters(self) -> SimParameterSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parameters() As SimParameterSet (Read Only)
                |     Gets the parameters of the import/export operation.

        :return: SimParameterSet
        """

        return SimParameterSet(self.com_object.Parameters)

    def set_path(self, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPath(CATBSTR iPath)
                |     Sets the path from/to which data is imported/exported.
                | 
                |     Parameters:
                | 
                |         iPath:
                |             Imported/exported data path.

        :param str i_path:
        :return: None
        """
        return self.com_object.SetPath(i_path)

    def set_units(self, i_magnitudes: tuple, i_units: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUnits(CATSafeArrayVariant iMagnitudes,CATSafeArrayVariant
                | iUnits)
                |     Sets the units of the base magnitudes (length, mass, time, ...) of the
                |     imported/exported data.
                |     Note: by default, MKS units are assumed and only those of the provided
                |     magnitudes are overloaded.
                | 
                |     Parameters:
                | 
                |         iMagnitudes:
                |             Imported/exported data base magnitudes. 
                |         iUnits:
                |             Imported/exported data base units.

        :param tuple i_magnitudes:
        :param tuple i_units:
        :return: None
        """
        return self.com_object.SetUnits(i_magnitudes, i_units)

    def __repr__(self):
        return f'SimImportExportArgs()'
