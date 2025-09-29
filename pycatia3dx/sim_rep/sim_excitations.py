"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sim_rep.sim_excitation import SimExcitation
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimExcitations(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimExcitations
                | 
                | Represents the collection of Simulation Excitations.
                | 
                | See also:
                |     SimExcitation
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str, i_catalog_name: str, i_client_id: str) -> SimExcitation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType,CATBSTR iCatalogName,CATBSTR iClientId) As
                | SimExcitation
                |     Creates a new Simulation Excitation and adds it to the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iType:
                |             The type of Simulation Excitation to create. 
                |         iCatalogName
                |             The catalog base name with its extension. 
                |         iClientId
                |             The client id related to catalog. 
                | 
                |     Returns:
                |         The created Simulation Excitation.

        :param str i_type:
        :param str i_catalog_name:
        :param str i_client_id:
        :return: SimExcitation
        """
        return SimExcitation(self.com_object.Add(i_type, i_catalog_name, i_client_id))

    def item(self, i_index: CATVariant) -> SimExcitation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimExcitation
                |     Returns a Simulation Excitation using its index from the simulation
                |     excitations collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the simulation excitation to retrieve from the
                |             collection of simulation excitations.
                |             This index is the rank of the simulation excitation in the
                |             collection. The index of the first simulation excitation in the collection is
                |             1, and the index of the last simulation excitation is Count.
                |             
                | 
                |     Returns:
                |         The retrieved simulation excitation.

        :param CATVariant i_index:
        :return: SimExcitation
        """
        return SimExcitation(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Simulation Excitation using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the Simulation Excitation to retrieve from
                |             the collection.
                |             As a numeric, this index is the rank of the Simulation Excitation
                |             in the collection. The index of the first Simulation Excitation in the
                |             collection is 1, and the index of the last Simulation Excitation is
                |             Count.
                |             As a string, it is the name you assigned to the Simulation
                |             Excitation using the Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimExcitations(name="{self.name}")'
