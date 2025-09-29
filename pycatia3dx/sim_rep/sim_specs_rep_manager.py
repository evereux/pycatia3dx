"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sim_rep.sim_excitations import SimExcitations
from pycatia3dx.sim_rep.sim_probes import SimProbes
from pycatia3dx.sim_rep.sim_scenario_specs import SimScenarioSpecs
from pycatia3dx.system.any_object import AnyObject


class SimSpecsRepManager(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSpecsRepManager
                | 
                | Interface representing Specifications Rep Manager.
    
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
                |     Retrieves the collection of all scenario specifications. SimScenarioSpecs

        :return: SimScenarioSpecs
        """

        return SimScenarioSpecs(self.com_object.ScenarioSpecs)

    def __repr__(self):
        return f'SimSpecsRepManager(name="{self.name}")'
