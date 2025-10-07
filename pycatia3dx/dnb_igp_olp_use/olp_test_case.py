"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_cases import OLPCases
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction
from pycatia3dx.dnb_igp_olp_use.olp_instructions import OLPInstructions


class OLPTestCase(OLPInstruction):

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
                |                         OlpTestCase
                | 
                | A test case instruction (TEST, SELECT, SWITCH, CASE).
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def cases(self) -> OLPCases:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Cases() As OlpCases (Read Only)
                |     The list of cases.

        :return: OLPCases
        """

        return OLPCases(self.com_object.Cases)

    @property
    def default_case_instructions(self) -> OLPInstructions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DefaultCaseInstructions() As OlpInstructions (Read
                | Only)
                |     The default case if no other case is matched.
                |     This method will return Nothing if there is no default case.

        :return: OLPInstructions
        """

        return OLPInstructions(self.com_object.DefaultCaseInstructions)

    @property
    def expression(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Expression() As OlpAstBranch
                |     The expression that determines which branch is executed.
                |     When set, the OlpAstBranch.Value of the AST tree is used for the
                |     expression. When retrieved, the DELMIA expression is parsed and is returned in
                |     the format expected by OlpExpressionFixerDownload. You can find more
                |     information on the OLP Expression AST format in the documentation under
                |     Automation | Robotics | Robotics Offline Programming | Offline Programming
                |     Expression Translation.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Expression)

    @expression.setter
    def expression(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.Expression = value

    @property
    def has_default_case(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HasDefaultCase() As boolean
                |     Get/Set whether the test case instruction has a default
                |     case.
                |     The default case is executed if no other case matches. 

        :return: bool
        """

        return self.com_object.HasDefaultCase

    @has_default_case.setter
    def has_default_case(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.HasDefaultCase = value

    def __repr__(self):
        return f'OLPTestCase(name="{ self.name }")'
