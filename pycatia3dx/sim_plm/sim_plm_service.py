"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.sim_plm.simulation_reference import SimulationReference


class SimPLMService(Service):

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
                |                         SIMPLMService
                | 
                | Interface representing the PLMNew service.
                | It can be retrieves using the
                | Application.GetSessionService("SimPLMService")
                | Role: provides the services to create and edit in authoring session a new PLM
                | entity. In case this material is not granted the PLMCreate method of the
                | interface fails. The data are created in the default authoring customization
                | domain (environment).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def plm_create(self, i_simulation_name: str, i_simulation_type: str, i_context: PLMEntity, o_sim_object: SimulationReference, o_editor: Editor) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PLMCreate(CATBSTR iSimulationName,CATBSTR iSimulationType,PLMEntity
                | iContext,SimulationReference oSimObject,Editor oEditor)
                |     Method which allows to create a new Simulation object .
                | 
                |     Parameters:
                | 
                |         iSimulationName
                |             The newly Simulation's Name. 
                |         iSimulationType
                |             Indicates the type of simulation to create.
                |             Legal values: SMAFeaPLMNewSimu: to create a Multiphysics
                |             simulation. DELPLMSimulation: to create a Manufacturing simulation.
                |             DELPSSSimulation: to create a Production simulation. CATKinPLMNew: to create a
                |             Kinematics simulation. LogicalSimulation: to create a Logical simulation.
                |             LogicalSimulation: to create a Functional simulation. LogicalSimulation: to
                |             create a Behavior simulation. For other simulation types, contact the
                |             responsible team. 
                |         iContext
                |             The Context simulated. 
                |         oSimObject
                |             [out, CATBaseUnknown#Release] The newly Simulation created.
                |             
                |         oEditor
                |             [out, CATBaseUnknown#Release] The resulting editor on the newly
                |             created data. 
                | 
                |     Example:
                | 
                |          This example shows you how to create a new Kinematics Simulation
                |          reference.
                |            
                | 
                |            Dim SimService As SIMPLMService
                |            Dim oSimlEditor As Editor
                |            Dim oPLMSimObject As SimulationObject
                |            Set SimService = CATIA.GetSessionService("SimPLMService")
                |            ...
                |            SimService.PLMCreate "MySimulation","CATKinPLMNew", iContext ,
                |            oPLMSimObject, oSimlEditor

        :param str i_simulation_name:
        :param str i_simulation_type:
        :param PLMEntity i_context:
        :param SimulationReference o_sim_object:
        :param Editor o_editor:
        :return: None
        """
        return self.com_object.PLMCreate(i_simulation_name, i_simulation_type, i_context.com_object, o_sim_object.com_object, o_editor.com_object)

    def __repr__(self):
        return f'SimplmService(name="{ self.name }")'
