"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.know_how.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime

if TYPE_CHECKING:
    from pycatia3dx.know_how.expert_rule import ExpertRule


class ExpertRuleRuntime(ExpertRuleBaseComponentRuntime):
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
                |                         ExpertRuleRuntime
                | 
                | Represents the ExpertRuleRuntime object.
                | 
                |  Dim RSet as CATIAExpertRuleSetRuntime
                |  Set RSet = ...
                |  Dim CR as ExpertRuleRuntime
                |  Set CR = RSet.ExpertRuleBaseComponentRuntimes.Item(1)
                |  
                | 
                | See also:
                |     ExpertRuleSetRuntime.ExpertRuleBaseComponentRuntimes
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def priority(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Priority() As double
                |     Returns or sets the priority of the rule. The priority of expert rules
                |     indicates the order in which the rules are evaluated. Rules with the same
                |     priority are evaluated in the order of their creation.

        :return: float
        """

        return self.com_object.Priority

    @priority.setter
    def priority(self, value: float):
        """
        :param float value:
        """

        self.com_object.Priority = value

    @property
    def rule_edition(self) -> 'ExpertRule':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RuleEdition() As ExpertRule (Read Only)
                |     Returns the editable object corresponding to this rule. Be careful that,
                |     according to your licence, or the type of rule you're handling, you may not
                |     have the right to edit the rule.
                | 
                |      Dim aRuleEdition As ExpertRule
                |      Set aRuleEdition = aRuleRuntime.RuleEdition
                | 
                |      If not(aRuleEdition is Nothing) Then
                |        CATIA.SystemService.Print aRuleEdition.Body
                |      End if

        :return: ExpertRule
        """
        from pycatia3dx.know_how.expert_rule import ExpertRule
        return ExpertRule(self.com_object.RuleEdition)

    def __repr__(self):
        return f'ExpertRuleRuntime(name="{self.name}")'
