"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_del_robot_simulation.rsc_assignment import RscAssignment
from pycatia3dx.todo_del_robot_simulation.rsc_break import RscBreak
from pycatia3dx.todo_del_robot_simulation.rsc_condition import RscCondition
from pycatia3dx.todo_del_robot_simulation.rsc_custom_instruction import RscCustomInstruction
from pycatia3dx.todo_del_robot_simulation.rsc_data_entity import RscDataEntity
from pycatia3dx.todo_del_robot_simulation.rsc_for import RscFor
from pycatia3dx.todo_del_robot_simulation.rsc_goto import RscGoto
from pycatia3dx.todo_del_robot_simulation.rsc_instruction import RscInstruction
from pycatia3dx.todo_del_robot_simulation.rsc_loop import RscLoop
from pycatia3dx.todo_del_robot_simulation.rsc_pulse import RscPulse
from pycatia3dx.todo_del_robot_simulation.rsc_return import RscReturn
from pycatia3dx.todo_del_robot_simulation.rsc_run_internal_task import RscRunInternalTask
from pycatia3dx.todo_del_robot_simulation.rsc_run_service_task import RscRunServiceTask
from pycatia3dx.todo_del_robot_simulation.rsc_wait import RscWait


class RscSequence(RscInstruction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DELRobotSimulationIDLItf.RscInstruction
                |                         RscSequence
                | 
                | Interface representing a Resource Sequence Instruction.
                | 
                | Role: This interface is used to create RscSequence Instruction in
                | RobotTask.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def instructions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Instructions() As CATSafeArrayVariant (Read Only)
                |     Retreives the list of instructions from the Sequence.
                | 
                |     Returns:
                |         oInstructions The list of instructions. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim oInstructions
                |            oInstructions = ResourceSequence.Instructions
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
    def runnable_tasks(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RunnableTasks() As CATSafeArrayVariant (Read Only)
                |     Retreives the list of Runnable Tasks from the Sequence.
                | 
                |     Returns:
                |         oRunnableTasks The list of Runnable Taks. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim oRunnableTasks
                |            oRunnableTasks= ResourceSequence.RunnableTasks

        :return: tuple
        """

        return self.com_object.RunnableTasks

    def can_run_service_task(self, i_called_service_task: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CanRunServiceTask(AnyObject iCalledServiceTask) As
                | boolean
                |     Tests if a Service Task can be called from the current
                |     sequence.
                | 
                |     Parameters:
                | 
                |         iCalledServiceTask
                |             The service task to call. 
                |         oCan
                |             TRUE if the service can be called, FALSE else. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iCalledServiceTask As ResourceTask
                |            Dim oCan As Boolean
                |            oCan = ResourceSequence.CanRunServiceTask(iCalledServiceTask)

        :param AnyObject i_called_service_task:
        :return: bool
        """
        return self.com_object.CanRunServiceTask(i_called_service_task.com_object)

    def create_rsc_assignment(self, i_index: int, i_assigned_entity: RscDataEntity, i_assigned_value: str) -> RscAssignment:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscAssignment(short iIndex,RscDataEntity iAssignedEntity,CATBSTR
                | iAssignedValue) As RscAssignment
                |     Assign a value to a Local Variable or a Constant.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |         iAssignedEntity
                |             The Entity to assign (Local Var, Constant). 
                |         iAssignedValue
                |             The Value to assign (must be of compatible type). 
                | 
                |     Returns:
                |         oCreatedAssignment The created Instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iAssignedEntity As RscDataEntity
                |            Dim iAssignedValue As String
                |            ......
                |            Dim oCreatedAssignment As RscAssignment
                |            Set oCreatedAssignment = ResourceSequence.CreateRscAssignment(iIndex, iAssignedEntity, iAssignedValue)
                |            Dim oValue As String
                |            oValue = oCreatedAssignment.Value

        :param int i_index:
        :param RscDataEntity i_assigned_entity:
        :param str i_assigned_value:
        :return: RscAssignment
        """
        return RscAssignment(self.com_object.CreateRscAssignment(i_index, i_assigned_entity.com_object, i_assigned_value))

    def create_rsc_break(self, i_index: int) -> RscBreak:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscBreak(short iIndex) As RscBreak
                |     Creates a break instruction, to leave the current
                |     sequence.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |     Returns:
                |         oCreatedBreak The break Instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedBreak As RscBreak
                |            Set oCreatedBreak = ResourceSequence.CreateRscBreak(iIndex)

        :param int i_index:
        :return: RscBreak
        """
        return RscBreak(self.com_object.CreateRscBreak(i_index))

    def create_rsc_condition(self, i_index: int, i_condition: str) -> RscCondition:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscCondition(short iIndex,CATBSTR iCondition) As
                | RscCondition
                |     Creates a Condition instruction. It is composed of a condition ( = "If") and 2 alternatives: "Then" and "Else".
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |         iCondition
                |             The Condition (must be of boolean type). If true, the branch "Then"
                |             is active; if false, the branch "Else" is active. 
                | 
                |     Returns:
                |         oCreatedCondition The created Instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iCondition As String
                |            ......
                |            Dim oCreatedCondition As RscCondition
                |            Set oCreatedCondition = ResourceSequence.CreateRscCondition(iIndex, iCondition)
                |            Dim Condition
                |            Condition=oCreatedCondition.Condition

        :param int i_index:
        :param str i_condition:
        :return: RscCondition
        """
        return RscCondition(self.com_object.CreateRscCondition(i_index, i_condition))

    def create_rsc_custom_instruction(self, i_index: int) -> RscCustomInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscCustomInstruction(short iIndex) As
                | RscCustomInstruction
                |     Creates RscCustom instruction.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |     Returns:
                |         oCreatedCustom The created Instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedCustom As RscCustomInstruction
                |            Set oCreatedCustom = ResourceSequence.CreateRscCustomInstruction(iIndex)

        :param int i_index:
        :return: RscCustomInstruction
        """
        return RscCustomInstruction(self.com_object.CreateRscCustomInstruction(i_index))

    def create_rsc_for(self, i_index: int, i_for_type: int, i_for_index: str, i_for_from: str, i_for_to: str) -> RscFor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscFor(short iIndex,DELRscForType iForType,CATBSTR iForIndex,CATBSTR
                | iForFrom,CATBSTR iForTo) As RscFor
                |     Creates a For loop instruction.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |         iForType
                |             DELRscForType_Up for increasing index, DELRscForType_Down for
                |             decreasing. 
                |         iForIndex
                |             The index name. 
                |         iForFrom
                |             The starting expression. 
                |         iForTo
                |             The target expression. 
                | 
                |     Returns:
                |         oForInstr The created for loop instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iForIndex As String
                |            Dim iForFrom As String
                |            Dim iForTo As String
                |            DELRscForType iForLoopType
                |            ......
                |            Set  iForLoopType = DELRscForType_Up
                |            Dim oForInstr As RscFor
                |            Set oForInstr = ResourceSequence.CreateRscFor(iIndex, iForLoopType, iForIndex, iForFrom, iForTo)
                |            Dim oForType As DELRscForType
                |            oForType = oForInstr.Type
                |            ......
                |            oForInstr.Type = oForType
                |            
                | 
                | 
                |          
                |          
                | 
                |     See also:
                |         DELRscForType

        :param int i_index:
        :param int i_for_type:
        :param str i_for_index:
        :param str i_for_from:
        :param str i_for_to:
        :return: RscFor
        """
        return RscFor(self.com_object.CreateRscFor(i_index, i_for_type, i_for_index, i_for_from, i_for_to))

    def create_rsc_goto(self, i_index: int, i_label: str) -> RscGoto:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscGoto(short iIndex,CATBSTR iLabel) As RscGoto
                |     Creates a Goto instruction.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |         iLabel
                |             The target label. 
                | 
                |     Returns:
                |         oGoto The created Goto instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iLabel As String
                |            ......
                |            Dim oGoto As RscGoto
                |            Set oGoto = ResourceSequence.CreateRscGoto(iIndex, iLabel)
                |            Dim  oInstr as RscInstruction
                |            ........
                |            Dim oIsVisible As Boolean
                |            oIsVisible = oGoto.IsVisibleTarget(oInstr)

        :param int i_index:
        :param str i_label:
        :return: RscGoto
        """
        return RscGoto(self.com_object.CreateRscGoto(i_index, i_label))

    def create_rsc_loop(self, i_index: int, i_condition: str, i_loop_type: int) -> RscLoop:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscLoop(short iIndex,CATBSTR iCondition,DELRscLoopType iLoopType) As
                | RscLoop
                |     Creates a Loop instruction.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |         iCondition
                |             The condition (must be of boolean type). 
                |         iLoopType
                |             The loop type. 
                | 
                |     Returns:
                |         oLoop The created loop. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iCondition As String
                |            Dim  iLoopType As DELRscLoopType
                |            ......
                |            iLoopType = DELRscLoopType_WhileDo
                |            Dim oLoop As RscLoop
                |            Set  oLoop=
ResourceSequence.CreateRscLoop(iIndex,iCondition,iLoopType                |            Dim Condition
                |            Condition = oLoop.Condition
                |            
                | 
                | 
                |          
                |          
                | 
                |     See also:
                |         DELRscLoopType

        :param int i_index:
        :param str i_condition:
        :param int i_loop_type:
        :return: RscLoop
        """
        return RscLoop(self.com_object.CreateRscLoop(i_index, i_condition, i_loop_type))

    def create_rsc_pulse(self, i_index: int) -> RscPulse:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscPulse(short iIndex) As RscPulse
                |     Creates a pulse instruction.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |     Returns:
                |         ohCreatedPulse The pulse Instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Dim oDuration
                |            oDuration = oCreatedPulse.Duration

        :param int i_index:
        :return: RscPulse
        """
        return RscPulse(self.com_object.CreateRscPulse(i_index))

    def create_rsc_return(self, i_index: int) -> RscReturn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscReturn(short iIndex) As RscReturn
                |     Creates a return instruction to leave the current Task.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |     Returns:
                |         oCreatedReturn The return Instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedReturn As RscReturn
                |            Set oCreatedReturn = ResourceSequence.CreateRscReturn(iIndex)

        :param int i_index:
        :return: RscReturn
        """
        return RscReturn(self.com_object.CreateRscReturn(i_index))

    def create_rsc_run_internal_task(self, i_task: AnyObject, i_index: int) -> RscRunInternalTask:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscRunInternalTask(AnyObject iTask,short iIndex) As
                | RscRunInternalTask
                |     Launches an RscRunInternalTask
                | 
                |     Parameters:
                | 
                |         iTask
                |             The Task to run (Only runnable Task). 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |     Returns:
                |         oCreatedRscRunInternalTask The created Run Task. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iTask
                |            .........
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedRscRunInternalTask
                |            Set oCreatedRscRunInternalTask=
ResourceSequence.CreateRscRunInternalTask(iTask,iIndex)

        :param AnyObject i_task:
        :param int i_index:
        :return: RscRunInternalTask
        """
        return RscRunInternalTask(self.com_object.CreateRscRunInternalTask(i_task.com_object, i_index))

    def create_rsc_run_service_task(self, i_called_service_task: AnyObject, i_index: int) -> RscRunServiceTask:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscRunServiceTask(AnyObject iCalledServiceTask,short iIndex) As
                | RscRunServiceTask
                |     Launches an RscRunServiceTask .
                | 
                |     Parameters:
                | 
                |         ihCalledServiceTask
                |             The service task to launch. 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |     Returns:
                |         oCreatedRscRunServiceTask The created Instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iTask
                |            .....
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedRscRunServiceTask 
                |            Set oCreatedRscRunServiceTask = ResourceSequence.CreateRscRunServiceTask(iTask, iIndex)

        :param AnyObject i_called_service_task:
        :param int i_index:
        :return: RscRunServiceTask
        """
        return RscRunServiceTask(self.com_object.CreateRscRunServiceTask(i_called_service_task.com_object, i_index))

    def create_rsc_wait(self, i_index: int, i_time_out: float, i_boolean_expression: str) -> RscWait:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRscWait(short iIndex,double iTimeOut,CATBSTR iBooleanExpression) As
                | RscWait
                |     Creates RscWait Instruction.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index where to create the Instruction. Legal
                |             values:
                | 
                |                 -1 / neg value : At the end of the Sequence
                |                 0 : At the beginning of the Sequence.
                |                 other : At given index in the Sequence. If higher than available, the method fails
                | 
                |         iTimeOut
                |             The Maximum Duration of this Wait. May be 0 
                |         iBooleanExpression
                |             The Boolean Expression associated to this wait. The wait finishes
                |             when this expression becomes true. 
                | 
                |     Returns:
                |         ohCreatedWait The created Instruction. 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            Dim iTimeOut
                |            iTimeOut=0
                |            iIndex=-1
                |            Dim iBooleanExpression As String
                |            Dim oCreatedWait As RscWait
                |            Set oCreatedWait = ResourceSequence.CreateRscWait(iIndex, iTimeOut, iBooleanExpression)
                |            Call  oCreatedWait.UnsetTimeOut()

        :param int i_index:
        :param float i_time_out:
        :param str i_boolean_expression:
        :return: RscWait
        """
        return RscWait(self.com_object.CreateRscWait(i_index, i_time_out, i_boolean_expression))

    def delete_rsc_instruction(self, i_instruction: RscInstruction) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteRscInstruction(RscInstruction iInstruction)
                |     Deletes a RscInstruction.
                | 
                |     Parameters:
                | 
                |         iInstruction
                |             The instruction to Delete. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim oInstructions
                |            oInstructions = ResourceSequence.Instructions
                |            
                |            Dim oInstr As RscInstruction
                |            Set oInstr = oInstructions(0)
                |            Call  ResourceSequence.DeleteRscInstruction(oInstr)

        :param RscInstruction i_instruction:
        :return: None
        """
        return self.com_object.DeleteRscInstruction(i_instruction.com_object)

    def __repr__(self):
        return f'RscSequence(name="{ self.name }")'
