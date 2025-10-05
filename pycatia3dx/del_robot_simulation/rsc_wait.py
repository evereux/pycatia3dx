"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_del_robot_simulation.rsc_instruction import RscInstruction


class RscWait(RscInstruction):

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
                |                         RscWait
                | 
                | Interface representing a Resource Wait Instruction.
                | 
                | Role: This interface represents a RscWait Instruction in a Resource
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
                | Property Condition(CATBSTR iCondition)
                |     Set/Get the wait condition.
                | 
                |     Parameters:
                | 
                |         iCondition
                |             The condition expression. 
                | 
                |     Returns:
                |         oCondition The condition expression. 
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
                |            Dim Condition
                |            Condition=oCreatedWait.Condition
                |            ......
                |            CreatedWait.Condition = Condition

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
    def time_out(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeOut() As double
                |     Get/Set the wait time out.
                | 
                |     Returns:
                |         oTimeOut The time out (positive or null). 
                |     Parameters:
                | 
                |         iTimeOut
                |             The time out (positive or null). 
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
                |            Dim iTimeOut
                |            iTimeOut=0
                |            iIndex=-1
                |            Dim iBooleanExpression As String
                |            Dim oCreatedWait As RscWait
                |            Set oCreatedWait = ResourceSequence.CreateRscWait(iIndex, iTimeOut, iBooleanExpression)
                |            Dim TimeOut
                |            TimeOut=oCreatedWait.TimeOut
                |            ......
                |            CreatedWait.TimeOut = TimeOut

        :return: float
        """

        return self.com_object.TimeOut

    @time_out.setter
    def time_out(self, value: float):
        """
        :param float value:
        """

        self.com_object.TimeOut = value

    def unset_time_out(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnsetTimeOut()
                |     Remove the wait time out.
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
                |            Dim iTimeOut
                |            iTimeOut=0
                |            iIndex=-1
                |            Dim iBooleanExpression As String
                |            Dim oCreatedWait As RscWait
                |            Set oCreatedWait = ResourceSequence.CreateRscWait(iIndex, iTimeOut, iBooleanExpression)
                |            Call  oCreatedWait.UnsetTimeOut()

        :return: None
        """
        return self.com_object.UnsetTimeOut()

    def __repr__(self):
        return f'RscWait(name="{ self.name }")'
