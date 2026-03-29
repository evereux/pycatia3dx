"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction


class OLPInstructions(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpInstructions
                | 
                | Represents a list of instructions.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | The instructions are in execution order. You must use the For Each instruction
                | to loop through this collection. Random access via an "Item" method is not
                | available. "Count" is also not implemented since this would be a time consuming
                | function.
                | 
                | Example: (VB.NET)
                | 
                |  Dim Task As OlpProcedure
                |  Dim Instructions As OlpInstructions = Task.Instructions
                |  For Each Instruction As OlpInstruction In Instructions
                |     'Do Something
                |  Next
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OLPInstruction)
        self.com_object = com_object

    def create_instruction(
            self,
            i_type:
            int,
            i_relative_instruction: OLPInstruction,
            i_after_instruction: bool
    ) -> OLPInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateInstruction(DELOlpInstructionType iType,OlpInstruction
                | iRelativeInstruction,boolean iAfterInstruction) As
                | OlpInstruction
                |     Creates a new instruction in this list of instructions.
                | 
                |         If iRelativeInstruction is not NULL and iAfterInstruction is FALSE, the
                |         instruction is created before iRelativeInstruction.
                |         If iRelativeInstruction is not NULL and iAfterInstruction is TRUE, the
                |         instruction is created after iRelativeInstruction.
                |         If iRelativeInstruction is NULL and iAfterInstruction is FALSE, the
                |         instruction is created at the beginning.
                |         If iRelativeInstruction is NULL and iAfterInstruction is TRUE, the
                |         instruction is created at the end.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of instruction to create 
                |         iRelativeInstruction
                |             The new instruction will be created before or after this
                |             instruction. This input can be either NULL or an instruction in this list.
                |             
                |         iAfterInstruction
                |             If true, the new instruction will be created after the
                |             iRelativeInstruction. 
                | 
                |     Returns:
                |         The new instruction

        :param int i_type:
        :param OLPInstruction i_relative_instruction:
        :param bool i_after_instruction:
        :return: OLPInstruction
        """
        return OLPInstruction(
            self.com_object.CreateInstruction(i_type, i_relative_instruction.com_object, i_after_instruction))

    def create_instruction_from_template(self, i_library: str, i_template: str, i_type: str, i_sub_type: str,
                                         i_relative_instruction: OLPInstruction,
                                         i_after_instruction: bool) -> OLPInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateInstructionFromTemplate(CATBSTR iLibrary,CATBSTR iTemplate,CATBSTR
                | iType,CATBSTR iSubType,OlpInstruction iRelativeInstruction,boolean
                | iAfterInstruction) As OlpInstruction
                |     Creates a new instruction from a template in this list of
                |     instructions.
                | 
                |         If iRelativeInstruction is not NULL and iAfterInstruction is FALSE, the
                |         instruction is created before iRelativeInstruction.
                |         If iRelativeInstruction is not NULL and iAfterInstruction is TRUE, the
                |         instruction is created after iRelativeInstruction.
                |         If iRelativeInstruction is NULL and iAfterInstruction is FALSE, the
                |         instruction is created at the beginning.
                |         If iRelativeInstruction is NULL and iAfterInstruction is TRUE, the
                |         instruction is created at the end.
                | 
                |     Parameters:
                | 
                |         iLibrary
                |             The name of the template library 
                |         iTemplate
                |             The name of template 
                |         iType
                |             The type of template 
                |         iSubType
                |             The subtype of template 
                |         iRelativeInstruction
                |             The new instruction will be created before or after this
                |             instruction. This input can be either NULL or an instruction in this list.
                |             
                |         iAfterInstruction
                |             If true, the new instruction will be created after the
                |             iRelativeInstruction. 
                | 
                |     Returns:
                |         The new instruction

        :param str i_library:
        :param str i_template:
        :param str i_type:
        :param str i_sub_type:
        :param OLPInstruction i_relative_instruction:
        :param bool i_after_instruction:
        :return: OLPInstruction
        """
        return OLPInstruction(self.com_object.CreateInstructionFromTemplate(i_library, i_template, i_type, i_sub_type,
                                                                            i_relative_instruction.com_object,
                                                                            i_after_instruction))

    def create_instruction_type_string(self, i_type: str, i_relative_instruction: OLPInstruction,
                                       i_after_instruction: bool) -> OLPInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateInstructionTypeString(CATBSTR iType,OlpInstruction
                | iRelativeInstruction,boolean iAfterInstruction) As
                | OlpInstruction
                |     Creates a new instruction in this list of instructions.
                | 
                |         If iRelativeInstruction is not NULL and iAfterInstruction is FALSE, the
                |         instruction is created before iRelativeInstruction.
                |         If iRelativeInstruction is not NULL and iAfterInstruction is TRUE, the
                |         instruction is created after iRelativeInstruction.
                |         If iRelativeInstruction is NULL and iAfterInstruction is FALSE, the
                |         instruction is created at the beginning.
                |         If iRelativeInstruction is NULL and iAfterInstruction is TRUE, the
                |         instruction is created at the end.
                | 
                |     Parameters:
                | 
                |         iType
                |             The string type of instruction to create. The type is the same as
                |             the DELOlpInstructionType enum but without the delOlp prefix. For example if
                |             the type is delOlpRobotMotion, this property returns "RobotMotion".
                |             
                |         iRelativeInstruction
                |             The new instruction will be created before or after this
                |             instruction. This input can be either NULL or an instruction in this list.
                |             
                |         iAfterInstruction
                |             If true, the new instruction will be created after the
                |             iRelativeInstruction. 
                | 
                |     Returns:
                |         The new instruction

        :param str i_type:
        :param OLPInstruction i_relative_instruction:
        :param bool i_after_instruction:
        :return: OLPInstruction
        """
        return OLPInstruction(
            self.com_object.CreateInstructionTypeString(i_type, i_relative_instruction.com_object, i_after_instruction))

    def delete_instruction(self, i_instruction: OLPInstruction) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteInstruction(OlpInstruction iInstruction)
                |     Deletes an instruction from this instruction list.
                | 
                |     Parameters:
                | 
                |         iInstruction
                |             The instruction to delete.

        :param OLPInstruction i_instruction:
        :return: None
        """
        return self.com_object.DeleteInstruction(i_instruction.com_object)

    def item(self, i_index: int) -> OLPInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(long iIndex) As OlpInstruction
                |     Retrieves a instruction by its index.
                |     This method should be used sparingly as it is much faster to loop through
                |     all instructions using a "For Each" loop than to loop through them by calling
                |     Item.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the first instruction is 1, and the index of the last
                |             instruction is Count. If the index is out of bounds, the function fails.
                |             
                | 
                |     Returns:
                |         The instruction.

        :param int i_index:
        :return: OLPInstruction
        """
        return OLPInstruction(self.com_object.Item(i_index))

    def next(self, i_relative_instruction: OLPInstruction) -> OLPInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Next(OlpInstruction iRelativeInstruction) As
                | OlpInstruction
                |     Returns the next instruction in the collection.
                |     This method should be used sparingly as it is much faster to loop through
                |     all instructions using a "For Each" loop.
                | 
                |     Parameters:
                | 
                |         iRelativeInstruction
                |             The current instruction. Cannot be NULL. 
                | 
                |     Returns:
                |         The next instruction.
                |         This is NULL if iRelativeInstruction is the last instruction in the
                |         list.

        :param OLPInstruction i_relative_instruction:
        :return: OLPInstruction
        """
        return OLPInstruction(self.com_object.Next(i_relative_instruction.com_object))

    def previous(self, i_relative_instruction: OLPInstruction) -> OLPInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Previous(OlpInstruction iRelativeInstruction) As
                | OlpInstruction
                |     Returns the previous instruction in the collection.
                |     This method should be used sparingly as it is much faster to loop through
                |     all instructions using a "For Each" loop.
                | 
                |     Parameters:
                | 
                |         iRelativeInstruction
                |             The current instruction. Cannot be NULL. 
                | 
                |     Returns:
                |         The next instruction.
                |         This is NULL if iRelativeInstruction is the first instruction in the
                |         list. 

        :param OLPInstruction i_relative_instruction:
        :return: OLPInstruction
        """
        return OLPInstruction(self.com_object.Previous(i_relative_instruction.com_object))

    def __getitem__(self, n: int) -> OLPInstruction:
        if (n + 1) > self.count:
            raise StopIteration

        return OLPInstruction(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[OLPInstruction]:
        for i in range(self.count):
            yield OLPInstruction(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'OLPInstructions(name="{self.name}")'
