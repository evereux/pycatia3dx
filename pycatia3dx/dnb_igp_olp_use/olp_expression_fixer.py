"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction


class OLPExpressionFixer(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpExpressionFixer
                | 
                | The common functionality used to translate expressions.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | see OlpExpressionFixerDownload and OlpExpressionFixerUpload.
                | You can find more information on the OLP Expression AST format in the
                | documentation under Automation | Robotics | Robotics Offline Programming |
                | Offline Programming Expression Translation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def fix_subscripted_variables(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FixSubscriptedVariables() As boolean
                |     Get/Set fixing of subscripted(array) variables.
                |     A subscripted(array) variable is one that has dimensions defined (i.e.
                |     [2,3]). If fixing of subscripted variables is true (the default) then the
                |     entire name varname[2,3] will be fixed. If it is false (for translators that
                |     support array variables) only the name of the array variable (varname) will be
                |     fixed.

        :return: bool
        """

        return self.com_object.FixSubscriptedVariables

    @fix_subscripted_variables.setter
    def fix_subscripted_variables(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FixSubscriptedVariables = value

    @property
    def functions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Functions() As CATSafeArrayVariant (Read Only)
                |     The list of all functions in the expression.
                |     Each item in the list is a DELMIAOlpAstBranch. This property must be used
                |     after setting OlpExpressionFixer.SetExpression but before and
                |     OlpExpressionFixer.Fix. The substitution rules for function names have already
                |     been applied to this list. The functions appear once for each time the function
                |     is used. You can use this list to transform a function into an operator or to
                |     change the argument order etc. by manipulating the AST.

        :return: tuple
        """

        return self.com_object.Functions

    @property
    def literals(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Literals() As CATSafeArrayVariant (Read Only)
                |     The list of all literal values in the expression.
                |     Each item in the list is a DELMIAOlpAstNode. This property must be used
                |     after setting OlpExpressionFixer.SetExpression but before and
                |     OlpExpressionFixer.Fix. A literal value is a Boolean, integer, double or
                |     string. The values appear in this list in the order they appear in the
                |     expression. For example this list will contain "1 true 7.1" for the expression
                |     "(y>3) and (x==true) and (7.1<=z)". You can use this list to transform a
                |     literal value.

        :return: tuple
        """

        return self.com_object.Literals

    @property
    def operators(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Operators() As CATSafeArrayVariant (Read Only)
                |     The list of all operators in the expression.
                |     Each item in the list is a DELMIAOlpAstNode. This property must be used
                |     after setting OlpExpressionFixer.SetExpression but before and
                |     OlpExpressionFixer.Fix. The substitution rules for operators have already been
                |     applied to this list. The operators appear in this list in the order they
                |     appear in the expression. For example this list will contain + * + for the
                |     expression "x+2*(y-3)". You can use this list to transform an operator into a
                |     function call by calling AnyObject.parent on the operator to get its parent
                |     expression and manipulating the AST.

        :return: tuple
        """

        return self.com_object.Operators

    @property
    def variables(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Variables() As CATSafeArrayVariant (Read Only)
                |     The list of all unique variables in the expression.
                |     This property must be used after setting OlpExpressionFixer.SetExpression
                |     but before and OlpExpressionFixer.Fix. Each item in the list is a
                |     DELMIAOlpAstNode on upload or a DELMIAOlpVariable on download. If the variable
                |     is used more than once it is only in the list once. On uplaod, any AST branch
                |     of type delAstVARIABLE or leaf of type delAstIDENTIFIER will be included in
                |     this list. Although any delAstIDENTIFIER nodes inside of functions or inside of
                |     variable nodes will not be included. The value of the node will be used to
                |     determine if 2 variables are the same. But this means that "R[1]" and "R[ 1]"
                |     would both appear in the list and would both need to be substituted separately.
                |     You can loop through all variables in this list and then call the appropriate
                |     SubstituteVariable function for download or upload.

        :return: tuple
        """

        return self.com_object.Variables

    def fix(self, o_expr: OLPAstBranch) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Fix(OlpAstBranch oExpr) As boolean
                |     Translates the expression.
                |     For upload or download, call this method to retrieved the fixed expression.
                |     You should call this method after calling the upload or download
                |     SubstituteVariable methods for each variable. Before calling this method you
                |     can also do any manual fixing of functions, operators, or literal
                |     values.
                |     You can find more information on the OLP Expression AST format in the
                |     documentation under Automation | Robotics | Robotics Offline Programming |
                |     Offline Programming Expression Translation.
                | 
                |     Parameters:
                | 
                |         oExpr
                |             The fixed expression. 
                |         oIsValid
                |             If this method returns FALSE, then there was a problem fixing the
                |             expression. In the case of upload, you should not upload the instruction and
                |             instead create a custom instruction since the resulting DELMIA expression will
                |             not execute. In the case of download, you should skip the instruction because
                |             it will result in a compilation error in the program.

        :param OLPAstBranch o_expr:
        :return: bool
        """
        return self.com_object.Fix(o_expr.com_object)

    def set_expression(self, i_expr: OLPAstBranch, i_instr: OLPInstruction) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetExpression(OlpAstBranch iExpr,OlpInstruction iInstr)
                |     Set the expression to be translated.
                |     You can find more information on the OLP Expression AST format in the
                |     documentation under Automation | Robotics | Robotics Offline Programming |
                |     Offline Programming Expression Translation.
                | 
                |     Parameters:
                | 
                |         iExpr
                |             The expression to fix. 
                |         iInstr
                |             The DELMIA instruction this expression is or will be associated
                |             with.

        :param OLPAstBranch i_expr:
        :param OLPInstruction i_instr:
        :return: None
        """
        return self.com_object.SetExpression(i_expr.com_object, i_instr.com_object)

    def subsitute_function_name(self, i_find_function: str, i_replace_function: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SubsituteFunctionName(CATBSTR iFindFunction,CATBSTR
                | iReplaceFunction)
                |     Set an operator substitution.
                |     This only needs to be called 1 time per function before the 1st call to
                |     SetExpression. This should not be used if the argument order or other things
                |     need to be changed on the functions (use Functions for that). On download, you
                |     may want to set the value of OlpExpressionFixerDownload.EnforceValidFunctions
                |     if you want to ensure that only supported functions exist in the
                |     expression.
                | 
                |     Parameters:
                | 
                |         iFindFunction
                |             The function name to find. 
                |         iReplaceFunction
                |             The function name to replace it with.

        :param str i_find_function:
        :param str i_replace_function:
        :return: None
        """
        return self.com_object.SubsituteFunctionName(i_find_function, i_replace_function)

    def substitute_operator(self, i_find_operator: str, i_replace_operator: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SubstituteOperator(CATBSTR iFindOperator,CATBSTR
                | iReplaceOperator)
                |     Set an operator substitution.
                |     This only needs to be called 1 time per operator before the 1st call to
                |     SetExpression. For upload you only need to call this for operators that are
                |     different between your language and the DELMIA expression syntax because the
                |     substitution list is initialized with all valid DELMIA operators. On download
                |     you must call this for all operators supported by your language. This way if an
                |     invalid operator is encountered, a warning can be generated. In that case
                |     OlpExpressionFixer.Fix will return FALSE and you should skip downloading the
                |     instruction because it will result in a compilation error in the
                |     program.
                | 
                |     Parameters:
                | 
                |         iFindOperator
                |             The operator to find. 
                |         iReplaceOperator
                |             The operator to replace it with. 

        :param str i_find_operator:
        :param str i_replace_operator:
        :return: None
        """
        return self.com_object.SubstituteOperator(i_find_operator, i_replace_operator)

    def __repr__(self):
        return f'OLPExpressionFixer(name="{ self.name }")'
