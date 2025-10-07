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
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable


class OLPFor(OLPInstruction):

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
                |                         OlpFor
                | 
                | A for loop instruction.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def count_up(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CountUp() As boolean
                |     Indicates if the variable is incremented or decremented each iteration.

        :return: bool
        """

        return self.com_object.CountUp

    @count_up.setter
    def count_up(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CountUp = value

    @property
    def end_expr(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndExpr() As OlpAstBranch
                |     The final value of the loop variable.
                |     Looping is terminated when the loop variable is equal to this
                |     expression.
                |     When set, the OlpAstBranch.Value of the AST tree is used for the
                |     expression. When retrieved, the DELMIA expression is parsed and is returned in
                |     the format expected by OlpExpressionFixerDownload. You can find more
                |     information on the OLP Expression AST format in the documentation under
                |     Automation | Robotics | Robotics Offline Programming | Offline Programming
                |     Expression Translation.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.EndExpr)

    @end_expr.setter
    def end_expr(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.EndExpr = value

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
    def loop_variable(self) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LoopVariable() As OlpVariable (Read Only)
                |     The counter that is incremented or decremented in the
                |     loop.
                |     Inside the loop instructions, it cannot be modified. The variable used
                |     cannot be set, the name can be changed by retrieving the loop variable and then
                |     setting the Name property. On the loop variable the OlpVariable.Scope is the
                |     OlpInstructions in this for loop and OlpVariable.DefaultValue cannot be used.

        :return: OLPVariable
        """

        return OLPVariable(self.com_object.LoopVariable)

    @property
    def start_expr(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartExpr() As OlpAstBranch
                |     The initial value of the loop variable.
                |     When looping starts, the loop variable is assigned this
                |     value.
                |     When set, the OlpAstBranch.Value of the AST tree is used for the
                |     expression. When retrieved, the DELMIA expression is parsed and is returned in
                |     the format expected by OlpExpressionFixerDownload. You can find more
                |     information on the OLP Expression AST format in the documentation under
                |     Automation | Robotics | Robotics Offline Programming | Offline Programming
                |     Expression Translation. 

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.StartExpr)

    @start_expr.setter
    def start_expr(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.StartExpr = value

    def __repr__(self):
        return f'OLPFor(name="{ self.name }")'
