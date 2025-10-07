"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_robot_simulation.rsc_instruction import RscInstruction


class RscLoop(RscInstruction):

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
                |                         RscLoop
                | 
                | Interface representing a Resource Loop Instruction.
                | 
                | Role: This interface represents a RscLoop Instruction in a Resource
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
                |     Get/Set loop condition.
                | 
                |     Returns:
                |         oCondition The loop condition 
                |     Parameters:
                | 
                |         iCondition
                |             The loop condition 
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
                |            Dim  iLoopType As DELRscLoopType
                |            ......
                |            iLoopType = DELRscLoopType_WhileDo
                |            Dim oLoop As RscLoop
                |            Set  oLoop=ResourceSequence.CreateRscLoop(iIndex,iCondition,iLoopType
                |            Dim Condition
                |            Condition = oLoop.Condition
                |            ......
                |            oLoop.Condition = Condition

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
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As DELRscLoopType
                |     Get/Set loop type.
                | 
                |     Returns:
                |         oType The loop type 
                |     Parameters:
                | 
                |         iType
                |             The loop type 
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
                |            Dim  iLoopType As DELRscLoopType
                |            ......
                |            iLoopType = DELRscLoopType_WhileDo
                |            Dim oLoop As RscLoop
                |            Set  oLoop=ResourceSequence.CreateRscLoop(iIndex,iCondition,iLoopType
                |            Dim LoopType As DELRscLoopType
                |            LoopType = oLoop.Type
                |            ......
                |            oLoop.Type = LoopType
                |
                |     See also:
                |         DELRscLoopType

        :return: DELRscLoopType
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def __repr__(self):
        return f'RscLoop(name="{ self.name }")'
