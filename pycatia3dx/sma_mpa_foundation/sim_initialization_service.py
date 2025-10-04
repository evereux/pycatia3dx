"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service


class SimInitializationService(Service):

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
                |                         SimInitializationService
                | 
                | Represents the Service to initialize simulation.
                | 
                | Example:
                |     Given a CATIA application object you can retrieve a
                |     SimInitializationService object as following:
                | 
                |      Dim MyInitializationService As SimInitializationService
                |      Set MyInitializationService = CATIA.GetSessionService("SimInitializationService")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def set_simulation_initialization(self, i_app_name: str, i_type_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSimulationInitialization(CATBSTR iAppName,CATBSTR
                | iTypeName)
                |     Initializes the simulation object for the specified simulation app and
                |     type. This method must be called prior to the creation of the simulation. This
                |     method will fail if the simulation object already contains an analysis case.
                |     The simulation cannot be opened interactively if a product is not assigned. The
                |     product must be assigned directly during the simulation
                |     creation.
                | 
                |     Parameters:
                | 
                |         iAppName
                |             The simulation app expected to open the
                |             simulation.
                |             Valid App Names
                | 
                |                 "SimMechanicalScenarioCreation"
                |                 "SimStructuralScenarioCreation"
                |                 "SimLinearStructuralScenarioCreation"
                |                 "SimLinearStructuralValidation"
                | 
                |         iTypeName
                |             The simulation type expected.
                |             Valid Simulation Type Names
                | 
                |                 "SimGeneral"
                |                 "SimStructural"
                |                 "SimThermal"
                |                 "SimThermalStructural"

        :param str i_app_name:
        :param str i_type_name:
        :return: None
        """
        return self.com_object.SetSimulationInitialization(i_app_name, i_type_name)

    def set_simulation_method(self, ip_simulation_method: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSimulationMethod(SimInitializationServiceSimulationMethod
                | ipSimulationMethod)
                | 
                |     Deprecated:
                |         R422 See SetSimulationInitialization
                | 
                |         Initializes the simulation object per the specified simulation method.
                |         This method must be called prior to the creation of the simulation. This
                |         involves the modification of simulation object so that it opens up in the
                |         corresponding App as well as creation of an analysis case corresponding to the
                |         simulation method. This method will fail if the simulation object already
                |         contains an analysis case. The simulation cannot be opened interactively if a
                |         product is not assigned. The product must be assigned directly during the
                |         simulation creation. 
                |     Parameters:
                | 
                |         ipSimulationMethod
                |             The simulation method used for initialization. 

        :param int ip_simulation_method:
        :return: None
        """
        return self.com_object.SetSimulationMethod(ip_simulation_method)

    def __repr__(self):
        return f'SimInitializationService(name="{ self.name }")'
