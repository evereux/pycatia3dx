"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.system.any_object import AnyObject


class SimExecutionService(Service):

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
                |                         SimExecutionService
                | 
                | Represents the Service to perform simulation execution.
                | 
                | Example:
                |     Given a CATIA application object you can retrieve a SimExecutionService
                |     object as following:
                | 
                |      Dim MyExecutionService As SimExecutionService
                |      Set MyExecutionService = CATIA.GetSessionService("SimExecutionSerivce")
                |      
                | 
                | Example in Python:
                |     Given a CATIA application object you can retrieve a SimExecutionService
                |     object as following:
                | 
                |      myExecutionService = CATIA.GetSessionService("SimExecutionSerivce")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def basic_execute_all(self, i_simulation_reference: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func BasicExecuteAll(AnyObject iSimulationReference) As
                | boolean
                |     Executes all analysis cases within a simulation reference.
                | 
                |     Parameters:
                | 
                |         iSimulationReference[in]
                |             The simulation object. 
                | 
                |     Returns:
                |         Boolean execution status TRUE if the simulation ran successfully. FALSE
                |         if did not. 

        :param AnyObject i_simulation_reference:
        :return: bool
        """
        return self.com_object.BasicExecuteAll(i_simulation_reference.com_object)

    def __repr__(self):
        return f'SimExecutionService(name="{ self.name }")'
