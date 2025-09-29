"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sim_rep.sim_scenario_results import SimScenarioResults
from pycatia3dx.system.any_object import AnyObject


class SimResultRepManager(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimResultRepManager
                | 
                | Represents the Result Rep Manager.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def scenario_results(self) -> SimScenarioResults:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScenarioResults() As SimScenarioResults (Read Only)
                |     Retrieves the collection of all scenario results. SimScenarioResults

        :return: SimScenarioResults
        """

        return SimScenarioResults(self.com_object.ScenarioResults)

    def __repr__(self):
        return f'SimResultRepManager(name="{self.name}")'
