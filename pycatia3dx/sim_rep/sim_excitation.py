"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sim_rep.sim_scenario_spec import SimScenarioSpec
from pycatia3dx.system.any_object import AnyObject


class SimExcitation(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimExcitation
                | 
                | Represents the Scenario Excitation
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def scenario_spec(self) -> SimScenarioSpec:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScenarioSpec() As SimScenarioSpec (Read Only)
                |     Gets the scenario aggregating this excitation(return Nothing if the
                |     excitation is not aggregated by a scenario).
                |     SimScenarioSpec
                | 
                |     Parameters:
                | 
                |         oScenarioSpec[out]
                |             The scenario aggregating this excitation.

        :return: SimScenarioSpec
        """

        return SimScenarioSpec(self.com_object.ScenarioSpec)

    def __repr__(self):
        return f'SimExcitation(name="{self.name}")'
