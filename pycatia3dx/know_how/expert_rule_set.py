"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.know_how.expert_check import ExpertCheck
from pycatia3dx.know_how.expert_rule import ExpertRule
from pycatia3dx.know_how.expert_rule_set_runtime import ExpertRuleSetRuntime




class ExpertRuleSet(ExpertRuleSetRuntime):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    KnowHowIDLItf.ExpertRuleBaseComponentRuntime
                |                         KnowHowIDLItf.ExpertRuleSetRuntime
                |                             ExpertRuleSet
                | 
                | Represents the ExpertRuleSet object which is the editable part of a RuleSet or
                | a RuleBase.
                | 
                | See also:
                |     ExpertRuleSetRuntime.RuleSetEdition,
                |     ExpertRuleSet.CreateRuleSet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_check(self, i_name: str, i_check_variables: str, i_check_body: str, i_rule_set: str) -> ExpertCheck:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateCheck(CATBSTR iName,CATBSTR iCheckVariables,CATBSTR
                | iCheckBody,CATBSTR iRuleSet) As ExpertCheck
                |     Creates a check and adds it to the RuleSet.
                | 
                |     Parameters:
                | 
                |         iName
                |             The check name 
                |         iCheckVariables
                |             define variables of the check. 
                |         iCheckBody
                |             The check definition 
                |         iRuleSet
                |             The ruleset name where the check is to be aggregated.
                |             If this macro is used from the RuleSet where we want
                |             to create the check, the param must be equal to value : "".
                | 
                |     Returns:
                |         The created check 
                |     Example:
                |         This example creates the SolidActivity check and adds it to the newly
                |         created RuleSet.1 RuleSet then creates the HoleActivity check and adds it to
                |         the newly created RuleSet.2 RuleSet
                | 
                |          Dim aRuleBase as ExpertRuleBase
                |          Set aRuleBase = ...
                |          Set CheckSolid = aRuleBase.RuleSet.CreateCheck
                |                             ("SolidActivity",
                |                              "Sol : Solid",
                |                              "Sol.Activity == True",
                |                              "RuleSet.1")
                |          Dim ruleset2 as ExpertRuleSet
                |          Set ruleset2 = aRuleBase.RuleSet.CreateRuleSet ("RuleSet.2", "")
                |          Dim CheckHole as ExpertCheck
                |          Set CheckHole = ruleset2.CreateCheck
                |                              ("HoleActivity",
                |                               "H : Hole",
                |                               "H.Activity == True",
                |                               "")
                |          
                | 
                |     To use this method, you need to have the Knowledge Expert Buildtime
                |     license.

        :param str i_name:
        :param str i_check_variables:
        :param str i_check_body:
        :param str i_rule_set:
        :return: ExpertCheck
        """
        return ExpertCheck(self.com_object.CreateCheck(i_name, i_check_variables, i_check_body, i_rule_set))

    def create_rule(self, i_name: str, i_rule_variables: str, i_rule_body: str, i_rule_set: str) -> ExpertRule:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRule(CATBSTR iName,CATBSTR iRuleVariables,CATBSTR iRuleBody,CATBSTR
                | iRuleSet) As ExpertRule
                |     Creates a rule and adds it to the RuleSet.
                | 
                |     Parameters:
                | 
                |         iName
                |             The rule name 
                |         iRuleVariables
                |             define variables of the rule. 
                |         iRuleBody
                |             The check definition 
                |         iRuleSet
                |             The RuleSet name where this rule aggregated. If this
                |             macro is used from the ruleset where we want to aggregate
                |             the rule, the param must be equal to value : "".
                | 
                |     Returns:
                |         The created rule 
                |     Example:
                |         This example creates the DesactivateIfActivatedOnSolid rule and adds it
                |         to the newly created RuleSet.1 RuleSet then creates the
                |         DesactivateIfActivatedOnHole rule and adds it to the newly created RuleSet.2
                |         RuleSet
                | 
                |          Dim aRuleBase as ExpertRuleBase
                |          Set aRuleBase = ...
                |          Dim rulesolid as ExpertRule
                |          Set rulesolid = aRuleBase.RuleSet.CreateRule
                |                              ("DesactivateIfActivatedOnSolid",
                |                              "Sol : Solid",
                |                              "Sol.Activity == True then Sol.Activity = False",
                |                              "RuleSet.1")
                |          Dim ruleset2 as ExpertRuleSet
                |          Set ruleset2 = aRuleBase.RuleSet.CreateRuleSet
                |                             ("RuleSet.2",
                |                              "")
                |          Dim rulehole as ExpertRule
                |          Set rulehole = ruleset2.CreateRule
                |                             ("DesactivateIfActivatedOnHole",
                |                              "H : Hole",
                |                              "H.Activity == True then H.Activity = False",
                |                              "")
                |          
                | 
                |     To use this method, you need to have the Knowledge Expert Buildtime
                |     license.

        :param str i_name:
        :param str i_rule_variables:
        :param str i_rule_body:
        :param str i_rule_set:
        :return: ExpertRule
        """
        return ExpertRule(self.com_object.CreateRule(i_name, i_rule_variables, i_rule_body, i_rule_set))

    def create_rule_set(self, i_name: str, i_rule_set: str) -> 'ExpertRuleSet':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRuleSet(CATBSTR iName,CATBSTR iRuleSet) As
                | ExpertRuleSet
                |     Creates a RuleSet and adds it to the RuleSet.
                | 
                |     Parameters:
                | 
                |         iName
                |             The ruleset name 
                |         iRuleSet
                |             The ruleset name where this ruleset is to be aggregated.
                |             If this macro is used from the ruleset or the rulebase
                |             where we want to aggregate the ruleset, the param must
                |             be equal to value : "".
                | 
                |     Returns:
                |         The created ruleset 
                |     Example:
                |         This example, firstly, creates the RuleSet.1 RuleSet and adds it to the
                |         newly created RuleBase. Secondly, it creates RuleSet.2 RuleSet and adds it to
                |         the ruleset RuleSet.1
                | 
                |          Dim aRuleBase as ExpertRuleBase
                |          Set aRuleBase = ...
                |          Dim RS1 as ExpertRuleSet
                |          RS1 = aRuleBase.RuleSet.CreateRuleSet
                |                             ("RuleSet.1",
                |                              "")
                |          Dim RS2 as ExpertRuleSet
                |          Set RS2 = aRuleBase.RuleSet.CreateRuleSet
                |                             ("RuleSet.2",
                |                              "RuleSet.1")
                |          
                | 
                |     To use this method, you need to have the Knowledge Expert Buildtime
                |     license.

        :param str i_name:
        :param str i_rule_set:
        :return: ExpertRuleSet
        """
        return ExpertRuleSet(self.com_object.CreateRuleSet(i_name, i_rule_set))

    def __repr__(self):
        return f'ExpertRuleSet(name="{ self.name }")'
