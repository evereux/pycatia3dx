"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_del_robot_simulation.rsc_instruction import RscInstruction


class RscCondition(RscInstruction):

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
                |                         RscCondition
                | 
                | Interface representing a Resource Condition Instruction.
                | 
                | Role: This interface represents a RscCondition Instruction in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def condition(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Condition() As CATBSTR
                |     Returns/Sets the condition associated to this
                |     If/Then/Else.
                | 
                |     Returns:
                |         oCondition The returned Condition. 
                |     Parameters:
                | 
                |         iCondition
                |             The new Condition. 
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
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iCondition As String
                |            ......
                |            Dim oCreatedCondition As RscCondition
                |            Set oCreatedCondition = ResourceSequence.CreateRscCondition(iIndex, iCondition)
                |            Dim Condition
                |            Condition=oCreatedCondition.Condition
                |            ......
                |            oCreatedCondition.Condition = Condition

        :return: str
        """

        return self.com_object.Condition

    @condition.setter
    def condition(self, value: str):
        """
        :param str value:
        """

        self.com_object.Condition = value

    @property
    def else_sequence(self) -> RscInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ElseSequence() As RscInstruction (Read Only)
                |     Returns the Else Branch. It is by default an empty
                |     sequence.
                | 
                |     Returns:
                |         oElseSequence The returned Else RscSequence 
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
                |            Dim ElseSequence as RscSequence
                |            ElseSequence=oCreatedCondition.ElseSequence

        :return: RscInstruction
        """

        return RscInstruction(self.com_object.ElseSequence)

    @property
    def then_sequence(self) -> RscInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThenSequence() As RscInstruction (Read Only)
                |     Returns the Then Branch. It is by default an empty
                |     sequence.
                | 
                |     Returns:
                |         oThenSequence The returned Then RscSequence 
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
                |            Dim ThenSequence as RscSequence
                |            ThenSequence=oCreatedCondition.ThenSequence

        :return: RscInstruction
        """

        return RscInstruction(self.com_object.ThenSequence)

    def __repr__(self):
        return f'RscCondition(name="{ self.name }")'
