"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_ast_node import OLPAstNode
from pycatia3dx.dnb_igp_olp_use.olp_expression_fixer import OLPExpressionFixer
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable


class OLPExpressionFixerDownload(OLPExpressionFixer):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpExpressionFixer
                |                         OlpExpressionFixerDownload
                | 
                | An object for translating expressions from DELMIA expressions in the native
                | robot language.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | A new expression fixer can be created with
                | OlpTranslatorHelper.CreateExprFixerDownload.
                | You can find more information on the OLP Expression AST format in the
                | documentation under Automation | Robotics | Robotics Offline Programming |
                | Offline Programming Expression Translation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def allow_binary_numbers(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllowBinaryNumbers(boolean iAllowed) (Write Only)
                |     Set whether integers can be expressed as binary numbers in the
                |     expression.
                |     Only needs to be set once before the first call to set
                |     OlpExpressionFixer.SetExpression If a binary number is found and this is FALSE,
                |     then a warning will be added and OlpExpressionFixer.Fix will return FALSE. In
                |     this case you should skip downloading the instruction because it will result in
                |     a compilation error in the program. Default value is TRUE.

        :return: bool
        """

        return self.com_object.AllowBinaryNumbers

    @allow_binary_numbers.setter
    def allow_binary_numbers(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllowBinaryNumbers = value

    @property
    def allow_conditional_expr(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllowConditionalExpr(boolean iAllowed) (Write Only)
                |     Set whether conditional expressions (if...then...else...) are allowed in
                |     the expression.
                |     Only needs to be set once before the first call to set
                |     OlpExpressionFixer.SetExpression If a conditional expressions is found and this
                |     is FALSE, then a warning will be added and OlpExpressionFixer.Fix will return
                |     FALSE. In this case you should skip downloading the instruction because it will
                |     result in a compilation error in the program. Default value is TRUE.

        :return: bool
        """

        return self.com_object.AllowConditionalExpr

    @allow_conditional_expr.setter
    def allow_conditional_expr(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllowConditionalExpr = value

    @property
    def allow_constants(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllowConstants(boolean iAllowed) (Write Only)
                |     Set whether constants are allowed in the expression.
                |     Only needs to be set once before the first call to set
                |     OlpExpressionFixer.SetExpression If FALSE, then all constants in the expression
                |     are replaced by their literal values. Default value is TRUE.

        :return: bool
        """

        return self.com_object.AllowConstants

    @allow_constants.setter
    def allow_constants(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllowConstants = value

    @property
    def allow_functions(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllowFunctions(boolean iAllowed) (Write Only)
                |     Set whether function calls are allowed in the expression.
                |     Only needs to be set once before the first call to set
                |     OlpExpressionFixer.SetExpression If a function is found and this is FALSE, then
                |     a warning will be added and OlpExpressionFixer.Fix will return FALSE. In this
                |     case you should skip downloading the instruction because it will result in a
                |     compilation error in the program. Default value is TRUE.

        :return: bool
        """

        return self.com_object.AllowFunctions

    @allow_functions.setter
    def allow_functions(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllowFunctions = value

    @property
    def allow_hex_numbers(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllowHexNumbers(boolean iAllowed) (Write Only)
                |     Set whether integers can be expressed as hexadecimal numbers in the
                |     expression.
                |     Only needs to be set once before the first call to set
                |     OlpExpressionFixer.SetExpression If a hexadecimal number is found and this is
                |     FALSE, then a warning will be added and OlpExpressionFixer.Fix will return
                |     FALSE. In this case you should skip downloading the instruction because it will
                |     result in a compilation error in the program. Default value is TRUE.

        :return: bool
        """

        return self.com_object.AllowHexNumbers

    @allow_hex_numbers.setter
    def allow_hex_numbers(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllowHexNumbers = value

    @property
    def allow_parentheses(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllowParentheses(boolean iAllowed) (Write Only)
                |     Set whether parentheses are allowed in the expression.
                |     Only needs to be set once before the first call to set
                |     OlpExpressionFixer.SetExpression If parentheses are found and this is FALSE,
                |     then a warning will be added and OlpExpressionFixer.Fix will return FALSE. In
                |     this case you should skip downloading the instruction because it will result in
                |     a compilation error in the program. Default value is TRUE.

        :return: bool
        """

        return self.com_object.AllowParentheses

    @allow_parentheses.setter
    def allow_parentheses(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllowParentheses = value

    @property
    def allow_scientific_notation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllowScientificNotation(boolean iAllowed) (Write
                | Only)
                |     Set whether doubles can be expressed in scientific notation in the
                |     expression.
                |     Only needs to be set once before the first call to set
                |     OlpExpressionFixer.SetExpression If a number in scientific notation is found
                |     and this is FALSE, then a warning will be added and OlpExpressionFixer.Fix will
                |     return FALSE. In this case you should skip downloading the instruction because
                |     it will result in a compilation error in the program. Default value is TRUE.

        :return: bool
        """

        return self.com_object.AllowScientificNotation

    @allow_scientific_notation.setter
    def allow_scientific_notation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AllowScientificNotation = value

    @property
    def enforce_valid_functions(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EnforceValidFunctions(boolean iEnforce) (Write Only)
                |     Set whether all valid function calls must be added to the
                |     SubsituteFunctionName list.
                |     If TRUE and a function that is not in the list is encountered, then a
                |     warning will be added and OlpExpressionFixer.Fix will return FALSE. In this
                |     case you should skip downloading the instruction because it will result in a
                |     compilation error in the program. Default value is TRUE.

        :return: bool
        """

        return self.com_object.EnforceValidFunctions

    @enforce_valid_functions.setter
    def enforce_valid_functions(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.EnforceValidFunctions = value

    def substitute_variable(self, i_bm_var: OLPVariable, i_nrl_var: OLPAstNode) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SubsituteVariable(OlpVariable iBMVar,OlpAstNode iNRLVar)
                |     Set the variable substitutions to make.
                |     You only need to set a variable substitution for a variable one time and
                |     all instances of the variable in the expression will be substituted. You can
                |     find all variables in the expression using OlpExpressionFixer.Variables. This
                |     function must be called after setting OlpExpressionFixer.SetExpression but
                |     before and OlpExpressionFixer.Fix. Any variable substitutions are cleared after
                |     calling Fix.
                | 
                |     Parameters:
                | 
                |         iBMVar
                |             The DELMIA variable to replace. 
                |         iBMVar
                |             The robot language variable to replace it with.
                |             This AST node will be cloned to replace all variables of this type.
                |             The original AST node will not be used, so you can use it over and over again.

        :param OlpVariable i_bm_var:
        :param OlpAstNode i_nrl_var:
        :return: None
        """
        return self.com_object.SubsituteVariable(i_bm_var.com_object, i_nrl_var.com_object)

    def __repr__(self):
        return f'OLPExpressionFixerDownload(name="{ self.name }")'
