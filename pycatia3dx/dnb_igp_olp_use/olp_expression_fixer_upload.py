"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_ast_node import OLPAstNode
from pycatia3dx.dnb_igp_olp_use.olp_expression_fixer import OLPExpressionFixer
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable


class OLPExpressionFixerUpload(OLPExpressionFixer):

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
                |                         OlpExpressionFixerUpload
                | 
                | An object for translating expressions from the native robot language into
                | DELMIA expressions.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | A new transform can be created with
                | OlpTranslatorHelper.CreateExprFixerUpload.
                | You can find more information on the OLP Expression AST format in the
                | documentation under Automation | Robotics | Robotics Offline Programming |
                | Offline Programming Expression Translation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def subsitute_variable(self, i_nrl_var: OLPAstNode, i_bm_var: OLPVariable) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SubsituteVariable(OlpAstNode iNRLVar,OlpVariable iBMVar)
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
                |         iNRLVar
                |             The robot program variable to replace. 
                |         iBMVar
                |             The DELMIA variable to replace it with.

        :param OLPAstNode i_nrl_var:
        :param OLPVariable i_bm_var:
        :return: None
        """
        return self.com_object.SubsituteVariable(i_nrl_var.com_object, i_bm_var.com_object)

    def substitute_variable_get_or_create(self, i_nrl_var: OLPAstNode, i_name: str, i_type: int, i_data_type: int, i_direction: int, i_scope: AnyObject, i_default_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SubsituteVariableGetOrCreate(OlpAstNode iNRLVar,CATBSTR
                | iName,DELOlpVariableType iType,DELOlpDataType iDataType,DELOlpIODirection
                | iDirection,AnyObject iScope,CATBSTR iDefaultValue)
                |     Set the variable substitutions to make.
                |     See SubsituteVariable for details on variable substitution. Everything from
                |     there applies here.
                |     Set all the variable parameters if the variable may not have been created
                |     yet. This is most common for languages that don't have explicit variable
                |     declarations. It will be created if it does not yet exist.
                | 
                |     Parameters:
                | 
                |         iNRLVar
                |             The robot program variable to replace. 
                |         iName
                |             The new variable name. 
                |         iType
                |             The variable type 
                |         iDataType
                |             The variable data type. 
                |         iDirection
                |             Whether the variable is "in" or "out". 
                |         iScope
                |             The scope is either a DELMIAOlpProcedure or a DELMIAOlpBehavior.
                |             
                |         iDefaultValue
                |             Default value can be an empty string.

        :param OLPAstNode i_nrl_var:
        :param str i_name:
        :param int i_type:
        :param int i_data_type:
        :param int i_direction:
        :param AnyObject i_scope:
        :param str i_default_value:
        :return: None
        """
        return self.com_object.SubsituteVariableGetOrCreate(i_nrl_var.com_object, i_name, i_type, i_data_type, i_direction, i_scope.com_object, i_default_value)

    def substitute_variable_get_or_create_in_string_type(self, i_nrl_var: OLPAstNode, i_name: str, i_type: int, i_data_type: str, i_direction: int, i_scope: AnyObject, i_default_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SubsituteVariableGetOrCreateInStringType(OlpAstNode iNRLVar,CATBSTR
                | iName,DELOlpVariableType iType,CATBSTR iDataType,DELOlpIODirection
                | iDirection,AnyObject iScope,CATBSTR iDefaultValue)
                |     Set the variable substitutions to make.
                |     See SubsituteVariable for details on variable substitution. Everything from
                |     there applies here.
                |     Set all the variable parameters if the variable may not have been created
                |     yet. This is most common for languages that don't have explicit variable
                |     declarations. It will be created if it does not yet exist.
                | 
                |     Parameters:
                | 
                |         iNRLVar
                |             The robot program variable to replace. 
                |         iName
                |             The new variable name. 
                |         iType
                |             The variable type 
                |         iDataType
                |             The data type, in string, to get or create. It is the same as the
                |             DELOlpDataType enum but without the delOlp prefix. For example if the intended
                |             type is delOlpInteger, use string "Integer". Use string "Position" for position
                |             variable 
                |         iDirection
                |             Whether the variable is "in" or "out". 
                |         iScope
                |             The scope is either a DELMIAOlpProcedure or a DELMIAOlpBehavior.
                |             
                |         iDefaultValue
                |             Default value can be an empty string.

        :param OLPAstNode i_nrl_var:
        :param str i_name:
        :param int i_type:
        :param str i_data_type:
        :param int i_direction:
        :param AnyObject i_scope:
        :param str i_default_value:
        :return: None
        """
        return self.com_object.SubsituteVariableGetOrCreateInStringType(i_nrl_var.com_object, i_name, i_type, i_data_type, i_direction, i_scope.com_object, i_default_value)

    def subsitute_variable_name_only(self, i_nrl_var: OLPAstNode, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SubsituteVariableNameOnly(OlpAstNode iNRLVar,CATBSTR
                | iName)
                |     Set the variable substitutions to make.
                |     See SubsituteVariable for details on variable substitution. Everything from
                |     there applies here.
                |     This version of the function allows you to set the name if the variable
                |     that has been already created. This is most likely the case for languages that
                |     have explicit variable declarations. However, if the name used in DELMIA is the
                |     same as the robot program, then you don't need to call this
                |     function.
                | 
                |     Parameters:
                | 
                |         iNRLVar
                |             The robot program variable to replace. 
                |         iName
                |             The new variable name. 

        :param OLPAstNode i_nrl_var:
        :param str i_name:
        :return: None
        """
        return self.com_object.SubsituteVariableNameOnly(i_nrl_var.com_object, i_name)

    def __repr__(self):
        return f'OLPExpressionFixerUpload(name="{ self.name }")'
