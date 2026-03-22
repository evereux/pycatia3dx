"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.sim_plm.simulation_object import SimulationObject
from pycatia3dx.types.general import CATVariant


class SimulationSpecifications(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimulationSpecifications
                | 
                | Interface representing SIMULATION Objects collection.
                | This collection of objects can be associated to specification or result
                | category.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SimulationObject)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SimulationObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimulationObject
                |     Retrieves the Simulation Object under the Scenario
                |     Category.
                |     Role: This method retrieves a pointer on the SimulationObject
                |     .
                | 
                |     Parameters:
                | 
                |         oSimulationObject
                | 
                |     Returns:
                |         An HRESULT value
                | 
                |             S_OK The pointer on the Simulation Objects is correctly
                |             retrieved
                |             E_FAIL Otherwise.

        :param CATVariant i_index:
        :return: SimulationObject
        """
        return SimulationObject(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SimulationSpecifications(name="{self.name}")'
