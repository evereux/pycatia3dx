"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.sim_rep.sim_excitations import SimExcitations
from pycatia3dx.sim_rep.sim_probe import SimProbe
from pycatia3dx.sim_rep.sim_probes import SimProbes
from pycatia3dx.sim_rep.sim_scenario_result import SimScenarioResult
from pycatia3dx.system.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia3dx.sim_rep.sim_excitation import SimExcitation


class SimScenarioSpec(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimScenarioSpec
                | 
                | Represents the Scenario Specification
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def excitations(self) -> SimExcitations:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Excitations() As SimExcitations (Read Only)
                |     Retrieves the collection of all Excitations. SimExcitations

        :return: SimExcitations
        """

        return SimExcitations(self.com_object.Excitations)

    @property
    def is_current(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsCurrent() As boolean (Read Only)
                |     Returns the current state of a scenario.

        :return: bool
        """

        return self.com_object.IsCurrent

    @property
    def probes(self) -> SimProbes:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Probes() As SimProbes (Read Only)
                |     Retrieves the collection of all Excitations. SimProbes

        :return: SimProbes
        """

        return SimProbes(self.com_object.Probes)

    @property
    def scenario_result(self) -> SimScenarioResult:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScenarioResult() As SimScenarioResult (Read Only)
                |     Retrieves the Scenario Result associated to the scenario.

        :return: SimScenarioResult
        """

        return SimScenarioResult(self.com_object.ScenarioResult)

    @property
    def solver_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SolverType() As CATBSTR (Read Only)
                |     Returns the Solver Type of a scenario.

        :return: str
        """

        return self.com_object.SolverType

    def add_excitation(self, i_excitation: 'SimExcitation') -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddExcitation(SimExcitation iExcitation)
                |     Reference an Excitation to the scenario SimExcitation

        :param SimExcitation i_excitation:
        :return: None
        """
        return self.com_object.AddExcitation(i_excitation.com_object)

    def add_probe(self, i_probe: SimProbe) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddProbe(SimProbe iProbe)
                |     Reference a Probe to the scenario SimProbe

        :param SimProbe i_probe:
        :return: None
        """
        return self.com_object.AddProbe(i_probe.com_object)

    def get_behaviors(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBehaviors() As CATSafeArrayVariant
                |     Gets behavior links.

        :return: tuple
        """
        return self.com_object.GetBehaviors()

    def remove_excitation(self, i_excitation: 'SimExcitation') -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveExcitation(SimExcitation iExcitation)
                |     Unreference an Excitation to the scenario SimExcitation

        :param SimExcitation i_excitation:
        :return: None
        """
        return self.com_object.RemoveExcitation(i_excitation.com_object)

    def remove_probe(self, i_probe: SimProbe) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveProbe(SimProbe iProbe)
                |     Unreference a Probe to the scenario SimProbe

        :param SimProbe i_probe:
        :return: None
        """
        return self.com_object.RemoveProbe(i_probe.com_object)

    def set_current(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCurrent()
                |     Sets the scenario as current.

        :return: None
        """
        return self.com_object.SetCurrent()

    def __repr__(self):
        return f'SimScenarioSpec(name="{self.name}")'
