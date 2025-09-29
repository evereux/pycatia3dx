"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sim_rep.sim_probe import SimProbe
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimProbes(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimProbes
                | 
                | Represents the collection of Simulation Probes.
                | 
                | See also:
                |     SimProbe
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str, i_catalog_name: str, i_client_id: str) -> SimProbe:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType,CATBSTR iCatalogName,CATBSTR iClientId) As
                | SimProbe
                |     Creates a new Simulation Probe and adds it to the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iType:
                |             The type of Simulation Probe to create. 
                |         iCatalogName
                |             The catalog base name with its extension. 
                |         iClientId
                |             The client id related to catalog. 
                | 
                |     Returns:
                |         The created Simulation Probe.

        :param str i_type:
        :param str i_catalog_name:
        :param str i_client_id:
        :return: SimProbe
        """
        return SimProbe(self.com_object.Add(i_type, i_catalog_name, i_client_id))

    def item(self, i_index: CATVariant) -> SimProbe:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimProbe
                |     Returns a Simulation Probe using its index from the Simulation Probes
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Simulation Probe to retrieve from the collection
                |             of Simulation Probes.
                |             This index is the rank of the Simulation Probe in the collection.
                |             The index of the first Simulation Probe in the collection is 1, and the index
                |             of the last Simulation Probe is Count. 
                | 
                |     Returns:
                |         The retrieved Simulation Probe.

        :param CATVariant i_index:
        :return: SimProbe
        """
        return SimProbe(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Simulation Probe using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the Simulation Probe to retrieve from the
                |             collection.
                |             As a numeric, this index is the rank of the Simulation Probe in the
                |             collection. The index of the first Simulation Probe in the collection is 1, and
                |             the index of the last Simulation Probe is Count.
                |             As a string, it is the name you assigned to the Simulation Probe
                |             using the Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimProbes(name="{self.name}")'
