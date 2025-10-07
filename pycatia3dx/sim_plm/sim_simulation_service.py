"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.product_structure_client.vpm_root_occurrence import VPMRootOccurrence
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sim_plm.simulation_reference import SimulationReference


class SimSimulationService(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SimSimulationService
                | 
                | Represents the Service to return the root occurrence of the product referred by
                | the simulation.
                | 
                | Example:
                |     Given a CATIA application object you can retrieve a SimSimulationService
                |     object as following:
                | 
                |      Dim MySimulationService As SimSimulationService
                |      Set MySimulationService = CATIA.GetSessionService("SimSimulationService")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_product_root_occurrence(self, ip_simulation_reference: SimulationReference) -> VPMRootOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProductRootOccurrence(SimulationReference ipSimulationReference) As
                | VPMRootOccurrence
                |     Method to return the root occurrence of the product referred by the
                |     simulation.
                | 
                |     Parameters:
                | 
                |         ipSimulationReference
                |             The simulation whose product's root occurrence needs to be
                |             determined. 
                | 
                |     Returns:
                |         The VPMRootOccurrence object

        :param SimulationReference ip_simulation_reference:
        :return: VPMRootOccurrence
        """
        return VPMRootOccurrence(self.com_object.GetProductRootOccurrence(ip_simulation_reference.com_object))

    def get_simulation_reference_from_object(self, i_object: AnyObject) -> SimulationReference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSimulationReferenceFromObject(AnyObject iObject) As
                | SimulationReference
                |     Retrieves the Simulation object that aggregates a simulation
                |     feature.
                |     This service is valid only for Object stored in Scenario or Result
                |     representation.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The Object stored in Scenario or Result representation.
                |             
                | 
                |     Returns:
                |         The simulation reference object 

        :param AnyObject i_object:
        :return: SimulationReference
        """
        return SimulationReference(self.com_object.GetSimulationReferenceFromObject(i_object.com_object))

    def __repr__(self):
        return f'SimSimulationService(name="{ self.name }")'
