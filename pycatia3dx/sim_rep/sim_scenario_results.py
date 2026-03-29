"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.sim_rep.sim_scenario_result import SimScenarioResult
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimScenarioResults(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimScenarioResults
                | 
                | Represents the collection of Scenario Results.
                | 
                | See also:
                |     SimScenarioResult
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimScenarioResult)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SimScenarioResult:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimScenarioResult
                |     Returns a scenario result using its index from the scenario result
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the scenario result to retrieve from the collection of
                |             scenario results.
                |             This index is the rank of the scenario result in the collection.
                |             The index of the first scenario result in the collection is 1, and the index of
                |             the last scenario result is Count. 
                | 
                |     Returns:
                |         The retrieved scenario result.

        :param CATVariant i_index:
        :return: SimScenarioResult
        """
        return SimScenarioResult(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> SimScenarioResult:
        if (n + 1) > self.count:
            raise StopIteration

        return SimScenarioResult(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SimScenarioResult]:
        for i in range(self.count):
            yield SimScenarioResult(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SimScenarioResults(name="{self.name}")'
