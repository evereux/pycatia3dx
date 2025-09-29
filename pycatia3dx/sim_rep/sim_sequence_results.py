"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sim_rep.sim_scenario_results import SimScenarioResults
from pycatia3dx.sim_rep.sim_scenario_spec import SimScenarioSpec
from pycatia3dx.sim_rep.sim_sequence import SimSequence
from pycatia3dx.system.any_object import AnyObject


class SimSequenceResults(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSequenceResults
                | 
                | Interface representing Simulation Sequence Results.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def is_current(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsCurrent() As boolean (Read Only)
                |     Retrieves the current status of the sequence results.

        :return: bool
        """

        return self.com_object.IsCurrent

    @property
    def is_successfully_computed(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsSuccessfullyComputed() As boolean (Read Only)
                |     Retrieves the compute status of the sequence results.

        :return: bool
        """

        return self.com_object.IsSuccessfullyComputed

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

    @property
    def scenario_to_compute(self) -> SimScenarioSpec:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScenarioToCompute() As SimScenarioSpec
                |     Sets or retrieves the scenario to compute.

        :return: SimScenarioSpec
        """

        return SimScenarioSpec(self.com_object.ScenarioToCompute)

    @scenario_to_compute.setter
    def scenario_to_compute(self, value: SimScenarioSpec):
        """
        :param SimScenarioSpec value:
        """

        self.com_object.ScenarioToCompute = value

    @property
    def sequence(self) -> SimSequence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Sequence() As SimSequence (Read Only)
                |     Retrieves the sequence associated to this sequence results. SimSequence

        :return: SimSequence
        """

        return SimSequence(self.com_object.Sequence)

    def update(self, isp_scenario_to_compute: SimScenarioSpec) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update(SimScenarioSpec ispScenarioToCompute)
                |     Updates and computes the specified scenario. SimScenarioSpec

        :param SimScenarioSpec isp_scenario_to_compute:
        :return: None
        """
        return self.com_object.Update(isp_scenario_to_compute.com_object)

    def __repr__(self):
        return f'SimSequenceResults(name="{self.name}")'
