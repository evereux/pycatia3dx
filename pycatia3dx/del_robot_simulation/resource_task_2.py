"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.del_robot_simulation.rsc_const import RscConst
from pycatia3dx.del_robot_simulation.rsc_local_var import RscLocalVar
from pycatia3dx.del_robot_simulation.rsc_sequence import RscSequence
from pycatia3dx.system.any_object import AnyObject


class ResourceTask2(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ResourceTask2
                | 
                | Interface representing a Resource Task.
                | 
                | Role: This interface is used to create Task-specific objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    # todo: what is DELRscTaskExecutionType?
    @property
    def execution_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExecutionType() As DELRscTaskExecutionType (Read
                | Only)
                |     The Type of Task execution
                | 
                |     Returns:
                |         oTaskExecutionType The Type of execution of the current Task. Legal
                |         values:
                | 
                |             DELRscTaskExecutionType_Internal : Internal Task
                |             DELRscTaskExecutionType_Service : Service Task
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            'Display DELRscTaskExecutionType
                |            If (DELRscTaskExecutionType_Internal = oResourceTask.RscTaskExecutionType) Then
                |            MsgBox "Execution type =  Internal"
                |            Else
                |            MsgBox "Execution type =  Service"
                |            End If 
                |
                |     See also:
                |         DELRscTaskExecutionType

        :return: int
        """

        return self.com_object.ExecutionType

    @property
    def instructions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Instructions() As CATSafeArrayVariant (Read Only)
                |     Retreives the list of instructions from the task.
                | 
                |     Returns:
                |         oInstructions The list of instructions. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim oInstructions
                |            oInstructions = oResourceTask.Instructions
                |            
                |            Dim oInstr As RscInstruction
                |            Set oInstr = oInstructions(0)
                |            oInstr.Name = "ResourceInstructionVB"
                |            
                |            Dim oCustomInstr As RscCustomInstruction
                |            Set oCustomInstr = oInstructions(1)
                |            oCustomInstr.Name = "ResourceCustomInstructionVB"
                |            
                |            Dim oMotionAct As RobotMotion
                |            Set oMotionAct = oInstructions(2)
                |            oMotionAct.Name = "RobotMotionVB"

        :return: tuple
        """

        return self.com_object.Instructions

    @property
    def main_rsc_sequence(self) -> RscSequence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MainRscSequence() As RscSequence (Read Only)
                |     Retreives the main RscSequence of the task.
                | 
                |     Returns:
                |         oMainSequence The Main Sequence. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim oMainSequence As RscSequence
                |            Set oMainSequence = oResourceTask.MainRscSequence

        :return: RscSequence
        """

        return RscSequence(self.com_object.MainRscSequence)

    @property
    def rsc_const_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RscConstList() As CATSafeArrayVariant (Read Only)
                |     List all the constants in the current ResourceTask.
                | 
                |     Returns:
                |         oList The list. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim oListOfConst
                |            oListOfConst=oResourceTask.Const
                | 
                |            Dim Const As RscConst
                |            Set Const = oListOfConst(0)
                | 
                |            Const.Value="5"

        :return: tuple
        """

        return self.com_object.RscConstList

    @property
    def rsc_local_var_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RscLocalVarList() As CATSafeArrayVariant (Read Only)
                |     List all the local variables in the current ResourceTask.
                | 
                |     Returns:
                |         oListOfLocalVar The list. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim oListOfLocalVar
                |            oListOfLocalVar=oResourceTask.RscLocalVarList
                | 
                |            Dim LocalVar As RscLocalVar
                |            Set LocalVar = oListOfLocalVar(0)
                | 
                |            LocalVar.DefaultValue="5"

        :return: tuple
        """

        return self.com_object.RscLocalVarList

    def create_rsc_const(self, i_name: str, i_type: int, i_val: str) -> RscConst:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscConst(CATBSTR iName,DELRscDataEntityType iType,CATBSTR iVal) As
                | RscConst
                |     Create a constant in the current ResourceTask.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the constant to create. 
                |         iType
                |             The type of the constant to create. 
                |         iVal
                |             The value of the constant to create. 
                | 
                |     Returns:
                |         oConst The created constant. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim iName As String
                |            iName = "MyConst"
                |            Dim iVal As String 
                |            iVal = "MyVal"
                |            Dim oConst As RscConst
                |            Dim iType As DELRscDataEntityType
                |            iType = DELRscDataEntityType_Integer
                |            Set oConst = oResourceTask.CreateRscConst(iName, iType, iVal)
                |            
                | 
                | 
                |          
                |          
                | 
                |     See also:
                |         DELRscDataEntityType

        :param str i_name:
        :param int i_type:
        :param str i_val:
        :return: RscConst
        """
        return RscConst(self.com_object.CreateRscConst(i_name, i_type, i_val))

    def create_rsc_local_var(self, i_name: str, i_type: int) -> RscLocalVar:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscLocalVar(CATBSTR iName,DELRscDataEntityType iType) As
                | RscLocalVar
                |     Create a local variable in the current ResourceTask.
                |     Note: This variable won't be visible outside the current
                |     ResourceTask.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the variable to create. 
                |         iType
                |             The type of the variable to create. 
                | 
                |     Returns:
                |         oLocalVar The created variable. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim iName As String
                |            iName = "MyLocalVar"
                |            Dim oLocalVar As RscLocalVar
                |            Dim iType As DELRscDataEntityType
                |            iType = DELRscDataEntityType_Integer
                |            Set oLocalVar = oResourceTask.CreateRscLocalVar(iName, iType)
                |            
                | 
                | 
                |          
                |          
                | 
                |     See also:
                |         DELRscDataEntityType

        :param str i_name:
        :param int i_type:
        :return: RscLocalVar
        """
        return RscLocalVar(self.com_object.CreateRscLocalVar(i_name, i_type))

    def create_spm_operation(self, i_before: bool, i_reference_instruction: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSPMOperation(boolean iBefore,AnyObject iReferenceInstruction) As
                | AnyObject
                |     Creates an SPMOperation under a DeviceTask (not supported for
                |     RobotTask)
                | 
                |     Returns:
                |         oCreatedSPMOp The created SPMOperation. 
                |     Parameters:
                | 
                |         iBefore
                |             Create before the reference instruction or not. 
                |         iReferenceInstruction
                |             The reference instruction before/after which the SPMOperation has
                |             to be created. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objResTask As ResourceTask2
                |                   ......
                |            Dim  objNewSPMOp As SPMOperation
                |            Dim  objRefAct As DeviceMotion
                |            Dim  CreateBefore As Boolean
                |            CreateBefore = FALSE
                |                   ......
                |            Call objResTask.CreateSPMOperation(CreateBefore, objRefAct,
                |            objNewSPMOp)

        :param bool i_before:
        :param AnyObject i_reference_instruction:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateSPMOperation(i_before, i_reference_instruction.com_object))

    def delete_rsc_const(self, i_const: RscConst) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteRscConst(RscConst iConst)
                |     Deletes a RscConst.
                | 
                |     Parameters:
                | 
                |         iConst
                |             The constant to Delete. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim iName As String
                |            iName = "MyConst"
                |            Dim iVal As String 
                |            iVal = "MyVal"
                |            Dim oConst As RscConst
                |            Dim iType As DELRscDataEntityType
                |            iType = DELRscDataEntityType_Integer
                |            Set oConst = oResourceTask.CreateRscConst(iName, iType, iVal)
                |            Call oResourceTask.DeleteRscConst(oConst)

        :param RscConst i_const:
        :return: None
        """
        return self.com_object.DeleteRscConst(i_const.com_object)

    def delete_rsc_local_var(self, i_local_var: RscLocalVar) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteRscLocalVar(RscLocalVar iLocalVar)
                |     Deletes a RscLocalVar.
                | 
                |     Parameters:
                | 
                |         iLocalVar
                |             The local variable to Delete. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim iName As String
                |            iName = "MyLocalVar"
                |            Dim oLocalVar As RscLocalVar
                |            Dim iType As DELRscDataEntityType
                |            iType = DELRscDataEntityType_Integer
                |            Set oLocalVar = oResourceTask.CreateRscLocalVar(iName, iType)
                |            Call oResourceTask.DeleteRscLocalVar(oLocalVar)

        :param RscLocalVar i_local_var:
        :return: None
        """
        return self.com_object.DeleteRscLocalVar(i_local_var.com_object)

    def move_after(self, i_relative: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MoveAfter(AnyObject iRelative)
                |     Move a ResourceTask after another one inside the same
                |     father.
                | 
                |     Parameters:
                | 
                |         iRelative
                |             The relative ResourceTask. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            Dim iRelative As ResourceTask2
                |            ......
                |           Call oResourceTask.MoveAfter(iRelative);

        :param AnyObject i_relative:
        :return: None
        """
        return self.com_object.MoveAfter(i_relative.com_object)

    def move_before(self, i_relative: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MoveBefore(AnyObject iRelative)
                |     Move a ResourceTask before another one inside the same
                |     father.
                | 
                |     Parameters:
                | 
                |         iRelative
                |             The relative ResourceTask. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            Dim iRelative As ResourceTask2
                |            ......
                |           Call oResourceTask.MoveBefore(iRelative);

        :param AnyObject i_relative:
        :return: None
        """
        return self.com_object.MoveBefore(i_relative.com_object)

    def __repr__(self):
        return f'ResourceTask2(name="{self.name}")'
