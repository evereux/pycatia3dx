"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_procedure import OLPProcedure
from pycatia3dx.dnb_igp_olp_use.olp_trigger_action import OLPTriggerAction


class OLPActionPRun(OLPTriggerAction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpTriggerAction
                |                         OlpActionPRun
                | 
                | A trigger Action for calling a task in parallel.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def arguments(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Arguments() As OlpAstBranch
                |     The arguments passed to the procedure.
                |     Procedures called in parallel can only have input arguments, no output
                |     arguments. The order of the arguments corresponds to the order of the procedure
                |     inputs retrieved from OlpProcedure.LocalVariables. The AST format is an
                |     "Arguments" node which contains a list of "Expression" and "Operator" nodes.
                |     Each "Expression" node has the id "Argument" and is in the proper format to be
                |     used with OlpExpressionFixerDownload. The operator nodes are just
                |     commas.
                |     When set, each child node with id="Argument" will be taken as an argument,
                |     in order. You can find more information on the OLP Expression AST format in the
                |     documentation under Automation | Robotics | Robotics Offline Programming |
                |     Offline Programming Expression Translation. The AST Arguments format used in
                |     function expressions as described in that document is the same as the AST
                |     Arguments format used here.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Arguments)

    @arguments.setter
    def arguments(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.Arguments = value

    @property
    def job_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property JobId() As CATBSTR
                |     The parallel job ID. If waiting for the parallel task to finish, this ID is
                |     used to identify the other thread.

        :return: str
        """

        return self.com_object.JobId

    @job_id.setter
    def job_id(self, value: str):
        """
        :param str value:
        """

        self.com_object.JobId = value

    @property
    def procedure(self) -> OLPProcedure:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Procedure() As OlpProcedure
                |     The procedure that is run from this instruction.

        :return: OLPProcedure
        """

        return OLPProcedure(self.com_object.Procedure)

    @procedure.setter
    def procedure(self, value: OLPProcedure):
        """
        :param OLPProcedure value:
        """

        self.com_object.Procedure = value

    @property
    def sustain_simulation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SustainSimulation() As boolean
                |     Get/Set whether to continue simulation if the parallel task has not yet
                |     finished. If not set, the simulation will not be sustained.

        :return: bool
        """

        return self.com_object.SustainSimulation

    @sustain_simulation.setter
    def sustain_simulation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SustainSimulation = value

    def assign_undefined_procedure(self, i_name: str, i_data_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AssignUndefinedProcedure(CATBSTR iName,DELOlpDataType
                | iDataType)
                |     Assign a procedure that is not defined in the robot
                |     program.
                |     This method is used to assign a procedure to this run instruction which is
                |     not defined in the robot programs selected for upload. If a procedure with this
                |     name already exists that has the correct number of arguments, it will be
                |     reused. If it does not exists, it will be created. When created, the procedure
                |     will have the same number of arguments as those set on this instruction. You
                |     must have set the arguments before calling this method.
                |     Note: Do not use this method to create a procedure which you will upload as
                |     normal. That will bypass any user options for creating new tasks on upload vs.
                |     overwriting existing tasks. Note: Do not use this method to assign a procedure
                |     that you have already uploaded by name. The name assigned to procedures you
                |     upload may not match if there was already an existing procedure with that
                |     name.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the procedure. 
                |         iDataType
                |             The data type to use for all arguments.
                |             This is only used when creating a new procedure.

        :param str i_name:
        :param int i_data_type:
        :return: None
        """
        return self.com_object.AssignUndefinedProcedure(i_name, i_data_type)

    def assign_undefined_procedure_in_string_type(self, i_name: str, i_data_type: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AssignUndefinedProcedureInStringType(CATBSTR iName,CATBSTR
                | iDataType)
                |     Assign a procedure that is not defined in the robot
                |     program.
                |     This method is used to assign a procedure to this run instruction which is
                |     not defined in the robot programs selected for upload. If a procedure with this
                |     name already exists that has the correct number of arguments, it will be
                |     reused. If it does not exists, it will be created. When created, the procedure
                |     will have the same number of arguments as those set on this instruction. You
                |     must have set the arguments before calling this method.
                |     Note: Do not use this method to create a procedure which you will upload as
                |     normal. That will bypass any user options for creating new tasks on upload vs.
                |     overwriting existing tasks. Note: Do not use this method to assign a procedure
                |     that you have already uploaded by name. The name assigned to procedures you
                |     upload may not match if there was already an existing procedure with that
                |     name.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the procedure. 
                |         iDataType
                |             The data type to use for all arguments. Note that the other method
                |             with the same name cannot be used for Position
                |             type.
                |             This is only used when creating a new procedure. 

        :param str i_name:
        :param str i_data_type:
        :return: None
        """
        return self.com_object.AssignUndefinedProcedureInStringType(i_name, i_data_type)

    def __repr__(self):
        return f'OLPActionPRun(name="{ self.name }")'
