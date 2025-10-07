"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction
from pycatia3dx.dnb_igp_olp_use.olp_instructions import OLPInstructions


class OLPLoop(OLPInstruction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpInstruction
                |                         OlpLoop
                | 
                | A do while OR while do instruction.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def condition(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Condition() As OlpAstBranch
                |     The expression that if true causes looping to continue.
                |     When set, the OlpAstBranch.Value of the AST tree is used for the
                |     expression. When retrieved, the DELMIA expression is parsed and is returned in
                |     the format expected by OlpExpressionFixerDownload. You can find more
                |     information on the OLP Expression AST format in the documentation under
                |     Automation | Robotics | Robotics Offline Programming | Offline Programming
                |     Expression Translation.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Condition)

    @condition.setter
    def condition(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.Condition = value

    @property
    def instructions(self) -> OLPInstructions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Instructions() As OlpInstructions (Read Only)
                |     The list of instructions in the loop.

        :return: OLPInstructions
        """

        return OLPInstructions(self.com_object.Instructions)

    @property
    def is_while_do(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsWhileDo() As boolean
                |     Indicates whether this loop is a "do-while" or a
                |     "while-do".
                |     If True this is a "while()do{...}" loop. In this type of a loop, the loop
                |     instructions are not executed the 1st time if the condition is false. If False,
                |     this is a "do{...}while()" loop. In that case, the loop is always executed at
                |     least 1 time, even if the condition is false. 

        :return: bool
        """

        return self.com_object.IsWhileDo

    @is_while_do.setter
    def is_while_do(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IsWhileDo = value

    def __repr__(self):
        return f'OLPLoop(name="{ self.name }")'
