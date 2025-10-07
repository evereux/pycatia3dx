"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sim_plm.simulation_object import SimulationObject


class SimulationRepresentation(SimulationObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         CATSimPLMIDLItf.SimulationObject
                |                             SimulationRepresentation
                | 
                | Interface representing SIMULATION data referenced by a
                | category.
                | Objects that can implement this interface are Authoring Simulation
                | representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def root(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Root() As AnyObject (Read Only)
                |     Retrieves Root Feature of a Simlation representation.
                |     Role: This method retrieves a pointer on the Root Feature of a Simlation
                |     representation
                | 
                |     Parameters:
                | 
                |         oRepRoot
                | 
                |     Returns:
                |         An HRESULT value
                | 
                |             S_OK The pointer on the Root Feature is correctly
                |             retrieved
                |             E_FAIL Otherwise.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Root)

    def __repr__(self):
        return f'SimulationRepresentation(name="{ self.name }")'
