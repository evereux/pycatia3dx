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


class OLPIf(OLPInstruction):

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
                |                         OlpIf
                | 
                | A conditional instruction.
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
                |     The expression that determines which branch is executed.
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
    def else_instructions(self) -> OLPInstructions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ElseInstructions() As OlpInstructions (Read Only)
                |     The list of instructions executed if the condition is false.

        :return: OLPInstructions
        """

        return OLPInstructions(self.com_object.ElseInstructions)

    @property
    def then_instructions(self) -> OLPInstructions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThenInstructions() As OlpInstructions (Read Only)
                |     The list of instructions executed if the condition is true.

        :return: OLPInstructions
        """

        return OLPInstructions(self.com_object.ThenInstructions)

    def __repr__(self):
        return f'OLPIf(name="{ self.name }")'
