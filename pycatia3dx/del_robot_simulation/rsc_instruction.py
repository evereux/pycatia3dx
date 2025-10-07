"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_robot_simulation.rsc_data_entity import RscDataEntity


class RscInstruction(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscInstruction
                | 
                | Interface representing a Resource Instruction.
                | 
                | Role: This interface represents a Resource Instruction in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def father_instruction(self) -> 'RscInstruction':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FatherInstruction() As RscInstruction (Read Only)
                |     Retrieve the Father Sequence.
                | 
                |     Returns:
                |         oFatherInstr The returned Father Sequence. 
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
                |            Dim FatherInstruction As RscInstruction
                |            Set FatherInstruction = oInstr.FatherInstruction

        :return: RscInstruction
        """

        return RscInstruction(self.com_object.FatherInstruction)

    @property
    def goto_instructions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GotoInstructions() As CATSafeArrayVariant (Read Only)
                |     Get all Goto instruction pointing to this label.
                | 
                |     Returns:
                |         oList The list of instructions. 
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
                |            Dim GotoInstructions
                |            GotoInstructions = oInstr.GotoInstructions

        :return: tuple
        """

        return self.com_object.GotoInstructions

    @property
    def index(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Index() As short (Read Only)
                |     Retrieve the index in the father Sequence.
                | 
                |     Returns:
                |         oIndex The returned Index. 
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
                |            Dim Index
                |            Index = oInstr.Index

        :return: int
        """

        return self.com_object.Index

    @property
    def label(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Label() As CATBSTR
                |     Get/Set the label associated to this instruction.
                |     Role: label are target of Goto instruction
                | 
                |     Returns:
                |         oLabel The label 
                |     Parameters:
                | 
                |         iLabel
                |             The label 
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
                |            ......
                |            Dim oInstr As RscInstruction
                |            Set oInstr = oInstructions(0)
                |            Dim sLabel
                |            sLabel = oInstr.Label
                |            ......
                |            oInstr.Label = sLabel

        :return: str
        """

        return self.com_object.Label

    @label.setter
    def label(self, value: str):
        """
        :param str value:
        """

        self.com_object.Label = value

    def get_data_entity_from_name(self, i_name: str) -> RscDataEntity:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDataEntityFromName(CATBSTR iName) As RscDataEntity
                |     Retrieve a data entity from its name.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the data entity that is visible from the current
                |             instruction. 
                | 
                |     Returns:
                |         oEntity The retrieved data entity. 
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
                |            Dim iName
                |            ...
                |            Dim oEntity As RscDataEntity
                |            Set  oEntity= oInstr.GetDataEntityFromName(iName)

        :param str i_name:
        :return: RscDataEntity
        """
        return RscDataEntity(self.com_object.GetDataEntityFromName(i_name))

    def move(self, i_param: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Move(DELRscMoveParameter iParam)
                |     Move the current instruction in the parent sequence.
                | 
                |     Parameters:
                | 
                |         iParam
                |             The move parameter. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            ResourceSequence = oResourceTask.RscSequence
                |            ......
                |            Dim oInstructions
                |            oInstructions = ResourceSequence.Instructions
                |            
                |            Dim oInstr As RscInstruction
                |            Set oInstr = oInstructions(0)
                |            Dim iParam As DELRscMoveParameter
                |            Set iParam = DELRscMoveParameter_Forward
                |            ...
                |            Call  oInstr.Move(iParam)
                |            
                | 
                | 
                |          
                |          
                | 
                |     See also:
                |         DELRscMoveParameter

        :param int i_param:
        :return: None
        """
        return self.com_object.Move(i_param)

    def move_to_other_sequence(self, i_in_sequence: 'RscInstruction', i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MoveToOtherSequence(RscInstruction iInSequence,short
                | iIndex)
                |     Move the current instruction in a target sequence.
                |     Note:The target sequence must be in the same Task as the current
                |     instruction
                | 
                |     Parameters:
                | 
                |         iInSequence
                |             The target sequence. 
                |         iIndex
                |             The index in the sequence where to move the instruction.
                |             
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
                |            Dim iInSequence
                |            Dim iIndex
                |            ...
                |            Call 
                |            oInstr.MoveToOtherSequence(iInSequence,iIndex)

        :param RscInstruction i_in_sequence:
        :param int i_index:
        :return: None
        """
        return self.com_object.MoveToOtherSequence(i_in_sequence.com_object, i_index)

    def remove_label(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveLabel()
                |     Remove the label associated to this instruction.
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
                |            Call  oInstr.RemoveLabel()

        :return: None
        """
        return self.com_object.RemoveLabel()

    def __repr__(self):
        return f'RscInstruction(name="{ self.name }")'
