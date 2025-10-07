"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_robot_simulation.rsc_instruction import RscInstruction


class RscGoto(RscInstruction):

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
                |                         RscGoto
                | 
                | Interface representing a Resource Goto Instruction.
                | 
                | Role: This interface represents a RscGoto Instruction in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def target(self) -> RscInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Target() As RscInstruction
                |     Get/Set the target instruction.
                | 
                |     Returns:
                |         oTarget The accessible labeled instruction. 
                |     Parameters:
                | 
                |         iTarget
                |             The accessible labeled instruction. 
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
                |            Dim iLabel As String
                |            ......
                |            Dim oGoto As RscGoto
                |            Set oGoto = ResourceSequence.CreateRscGoto(iIndex, iLabel)
                |            Dim Target as RscInstruction
                |            Set Target = oGoto.Target
                |            ......
                |            oGoto.Target = Target

        :return: RscInstruction
        """

        return RscInstruction(self.com_object.Target)

    @target.setter
    def target(self, value: RscInstruction):
        """
        :param RscInstruction value:
        """

        self.com_object.Target = value

    @property
    def visible_targets(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VisibleTargets() As CATSafeArrayVariant (Read Only)
                |     List of visible instructions.
                | 
                |     Returns:
                |         oVisibleTargets The list of visible instructions. 
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
                |            Dim VisibleTargets
                |            VisibleTargets = oGoto.VisibleTargets

        :return: tuple
        """

        return self.com_object.VisibleTargets

    def is_visible_target(self, i_instr: RscInstruction) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsVisibleTarget(RscInstruction iInstr) As boolean
                |     Check if a labeled instruction is visible or not.
                | 
                |     Parameters:
                | 
                |         iInstr
                |             The labeled instruction to be checked. 
                | 
                |     Returns:
                |         oIsVisible TRUE : is labeled & visible. FALSE : is not labeled or not visible. 
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

        :param RscInstruction i_instr:
        :return: bool
        """
        return self.com_object.IsVisibleTarget(i_instr.com_object)

    def __repr__(self):
        return f'RscGoto(name="{ self.name }")'
