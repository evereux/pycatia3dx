"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sim_rep.sim_scenario_spec import SimScenarioSpec
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimScenarioSpecs(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimScenarioSpecs
                | 
                | Represents the collection of Scenario Specification.
                | 
                | See also:
                |     SimScenarioSpec
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimScenarioSpec)
        self.com_object = com_object

    def add(self, i_type: str, i_catalog_name: str, i_client_id: str, i_behavior_list: tuple) -> SimScenarioSpec:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType,CATBSTR iCatalogName,CATBSTR
                | iClientId,CATSafeArrayVariant iBehaviorList) As
                | SimScenarioSpec
                |     Creates a new scenario specification and adds it to the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iType:
                |             The type of scenario solver to create. 
                |         iCatalogName
                |             The catalog base name with its extension. 
                |         iClientId
                |             The client id related to catalog. 
                |         iBehaviorList
                |             The behavior that is going to be simulated by the scenario with
                |             respect to the applicative Solver object requests.
                |             
                | 
                |     Returns:
                |         The created Simulation Probe.

        :param str i_type:
        :param str i_catalog_name:
        :param str i_client_id:
        :param tuple i_behavior_list:
        :return: SimScenarioSpec
        """
        return SimScenarioSpec(self.com_object.Add(i_type, i_catalog_name, i_client_id, i_behavior_list))

    def item(self, i_index: CATVariant) -> SimScenarioSpec:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimScenarioSpec
                |     Returns a scenario specification using its index from the scenario
                |     specification collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the scenario specification to retrieve from the
                |             collection of scenario specs.
                |             This index is the rank of the scenario specification in the
                |             collection. The index of the first scenario specification in the collection is
                |             1, and the index of the last scenario specification is Count.
                |             
                | 
                |     Returns:
                |         The retrieved scenario specification.

        :param CATVariant i_index:
        :return: SimScenarioSpec
        """
        return SimScenarioSpec(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a scenario specification using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the scenario specification to retrieve
                |             from the collection.
                |             As a numeric, this index is the rank of the scenario specification
                |             in the collection. The index of the first scenario specification in the
                |             collection is 1, and the index of the last scenario specification is
                |             Count.
                |             As a string, it is the name you assigned to the scenario
                |             specification using the Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimScenarioSpecs(name="{self.name}")'
