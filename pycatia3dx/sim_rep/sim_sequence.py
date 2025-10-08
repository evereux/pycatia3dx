"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.sim_rep.sim_excitations import SimExcitations
from pycatia3dx.sim_rep.sim_probes import SimProbes
from pycatia3dx.sim_rep.sim_scenario_specs import SimScenarioSpecs
from pycatia3dx.system.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia3dx.sim_rep.sim_sequence_results import SimSequenceResults


class SimSequence(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSequence
                | 
                | Interface representing Simulation Sequence.
    
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
    def scenario_specs(self) -> SimScenarioSpecs:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScenarioSpecs() As SimScenarioSpecs (Read Only)
                |     Retrieves the collection of all Scenarios. SimScenarioSpecs

        :return: SimScenarioSpecs
        """

        return SimScenarioSpecs(self.com_object.ScenarioSpecs)

    @property
    def sequence_results(self) -> 'SimSequenceResults':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SequenceResults() As SimSequenceResults (Read Only)
                |     Retrieves the sequence results associated to this sequence.
                |     SimSequenceResults

        :return: SimSequenceResults
        """
        from pycatia3dx.sim_rep.sim_sequence_results import SimSequenceResults
        return SimSequenceResults(self.com_object.SequenceResults)

    def add_behavior(self, i_behavior: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddBehavior(AnyObject iBehavior)
                |     Adds behavior links.

        :param AnyObject i_behavior:
        :return: None
        """
        return self.com_object.AddBehavior(i_behavior.com_object)

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

    def remove_behavior(self, i_behavior: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveBehavior(AnyObject iBehavior)
                |     Removes behavior links.

        :param AnyObject i_behavior:
        :return: None
        """
        return self.com_object.RemoveBehavior(i_behavior.com_object)

    def __repr__(self):
        return f'SimSequence(name="{self.name}")'
