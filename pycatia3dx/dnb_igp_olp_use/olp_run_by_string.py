"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction


class OLPRunByString(OLPInstruction):

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
                |                         OlpRunByString
                | 
                | An instruction that calls another procedure by name.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def arguments(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Arguments() As OlpAstBranch
                |     The arguments passed to the procedure.
                |     The order of the arguments corresponds to the order of the procedure inputs
                |     retrieved from OlpProcedure.LocalVariables. The AST format is an "Arguments"
                |     node which contains a list of "Expression" and "Operator" nodes. Each
                |     "Expression" node has the id "Argument" and is in the proper format to be used
                |     with OlpExpressionFixerDownload. The operator nodes are just
                |     commas.
                |     When set, each child node with id="Argument" will be taken as an argument,
                |     in order. You can find more information on the OLP Expression AST format in the
                |     documentation under Automation | Robotics | Robotics Offline Programming |
                |     Offline Programming Expression Translation. The AST Arguments format used in
                |     function expressions as described in that document is the same as the AST
                |     Arguments format used here.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Arguments)

    @arguments.setter
    def arguments(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.Arguments = value

    @property
    def procedure_expression(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProcedureExpression() As OlpAstBranch
                |     The expression that evaluates to a string for the name of the procedure
                |     that is run from this instruction.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.ProcedureExpression)

    @procedure_expression.setter
    def procedure_expression(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.ProcedureExpression = value

    @property
    def runnable_procedure_prefix(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RunnableProcedurePrefix() As CATBSTR
                |     The prefix to identify runnable procedures. During upload, the translator
                |     can set this to filter the list of runnable procedures. If not set we will try
                |     to identify the prefix from the procedure expression.

        :return: str
        """

        return self.com_object.RunnableProcedurePrefix

    @runnable_procedure_prefix.setter
    def runnable_procedure_prefix(self, value: str):
        """
        :param str value:
        """

        self.com_object.RunnableProcedurePrefix = value

    @property
    def runnable_procedure_suffix(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RunnableProcedureSuffix() As CATBSTR
                |     The suffix to identify runnable procedures. During upload, the translator
                |     can set this to filter the list of runnable procedures. If not set we will try
                |     to identify the suffix from the procedure expression.

        :return: str
        """

        return self.com_object.RunnableProcedureSuffix

    @runnable_procedure_suffix.setter
    def runnable_procedure_suffix(self, value: str):
        """
        :param str value:
        """

        self.com_object.RunnableProcedureSuffix = value

    @property
    def runnable_procedures(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RunnableProcedures() As CATSafeArrayVariant
                |     The list of runnable procedures. The procedure to call must be one of the
                |     ones in this list. Each item in the list is a OlpProcedure. During download,
                |     all tasks in this list will have been added to the list of tasks to download if
                |     the user requested a download of all called tasks. During upload, setting this
                |     list is optional. If not set, we will identify all tasks that are valid to be
                |     called (don't result in recursive called) and then filter the list based on a
                |     constant prefix or suffix identified in the procedure expression.

        :return: tuple
        """

        return self.com_object.RunnableProcedures

    @runnable_procedures.setter
    def runnable_procedures(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.RunnableProcedures = value

    def __repr__(self):
        return f'OLPRunByString(name="{ self.name }")'
