"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sim_plm.simulation_results import SimulationResults
from pycatia3dx.sim_plm.simulation_specifications import SimulationSpecifications


class SimulationReference(PLMEntity):

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
                |                         SimulationReference
                | 
                | Interface representing SIMULATION Object Reference.
                | This interface enables to retrieve Simulation Entities collection
                | .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def model(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Model() As AnyObject (Read Only)
                |     Retrieves Simulated Model.
                |     Role: This method retrieves a pointer on the simulated Model. It is a
                |     specialized type of Reference PLMEntity.
                | 
                |     Parameters:
                | 
                |         oPLMModel
                | 
                |     Returns:
                |         An HRESULT value
                | 
                |             S_OK The pointer on the Model is correctly
                |             retrieved
                |             E_FAIL Otherwise.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Model)

    @property
    def results(self) -> SimulationResults:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Results() As SimulationResults (Read Only)
                |     Retrieves Collection defines as Results.
                |     Role: This method retrieves a pointer on the Results collection of
                |     objects.
                | 
                |     Parameters:
                | 
                |         Results
                | 
                |     Returns:
                |         An HRESULT value
                | 
                |             S_OK The pointer on the Simulation Objects is correctly
                |             retrieved
                |             E_FAIL Otherwise.

        :return: SimulationResults
        """

        return SimulationResults(self.com_object.Results)

    @property
    def specifications(self) -> SimulationSpecifications:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Specifications() As SimulationSpecifications (Read
                | Only)
                |     Retrieves Collection defines as Specifications.
                |     Role: This method retrieves a pointer on the Specifications collection of
                |     objects.
                | 
                |     Parameters:
                | 
                |         oSpecifications
                | 
                |     Returns:
                |         An HRESULT value
                | 
                |             S_OK The pointer on the Simulation Objects is correctly
                |             retrieved
                |             E_FAIL Otherwise.

        :return: SimulationSpecifications
        """

        return SimulationSpecifications(self.com_object.Specifications)

    def __repr__(self):
        return f'SimulationReference(name="{ self.name }")'
