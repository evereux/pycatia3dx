"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_know_how.expert_rule_runtime import ExpertRuleRuntime


class ExpertRule(ExpertRuleRuntime):

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
                |                         KnowHowIDLItf.ExpertRuleRuntime
                |                             ExpertRule
                | 
                | Represents the edition part of a rule.
                | 
                | See also:
                |     ExpertRuleRuntime.RuleEdition, ExpertRuleSet.CreateRule
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def body(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Body() As CATBSTR
                |     Returns or sets the string that defines the body of a Rule.
                |     For instance: "if ( H\\Diameter > 20mm ) H\\Activity = FALSE"
                |     To modify the variable, you need to have the Knowledge Expert
                |     Buildtime license.

        :return: str
        """

        return self.com_object.Body

    @body.setter
    def body(self, value: str):
        """
        :param str value:
        """

        self.com_object.Body = value

    @property
    def language(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Language() As long
                |     Returns or sets the language of a rule.

        :return: int
        """

        return self.com_object.Language

    @language.setter
    def language(self, value: int):
        """
        :param int value:
        """

        self.com_object.Language = value

    @property
    def variables(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Variables() As CATBSTR
                |     Returns or sets the variables scope of the Rule. For instance: "H:Hole;
                |     P: Pad" To modify the variable, you need to have the Knowledge Expert Buildtime
                |     license.

        :return: str
        """

        return self.com_object.Variables

    @variables.setter
    def variables(self, value: str):
        """
        :param str value:
        """

        self.com_object.Variables = value

    def __repr__(self):
        return f'ExpertRule(name="{ self.name }")'
