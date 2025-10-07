"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.know_how.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime
from pycatia3dx.know_how.expert_rule_base_component_runtimes import ExpertRuleBaseComponentRuntimes
from pycatia3dx.know_how.expert_rule_set import ExpertRuleSet


class ExpertRuleSetRuntime(ExpertRuleBaseComponentRuntime):

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
                |                         ExpertRuleSetRuntime
                | 
                | Represents the ExpertRuleSet object in the rule base.
                | Example of how to retrieve a runtime expert rule set.
                | 
                |  Dim RBRO as ExpertRuleBaseRuntime
                |  Set RBRO = ...
                |  Dim RSRO as ExpertRuleSetRuntime
                |  Set RSRO = RBRO.RuleSet.ExpertRuleBaseComponentRuntimes.Item("Rule1")
                |  
                | 
                | See also:
                |     ExpertRuleBaseRuntime.RuleSet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def expert_rule_base_component_runtimes(self) -> ExpertRuleBaseComponentRuntimes:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExpertRuleBaseComponentRuntimes() As ExpertRuleBaseComponentRuntimes
                | (Read Only)
                |     Returns the list of the RuleBaseComponent.

        :return: ExpertRuleBaseComponentRuntimes
        """

        return ExpertRuleBaseComponentRuntimes(self.com_object.ExpertRuleBaseComponentRuntimes)

    @property
    def rule_set_edition(self) -> ExpertRuleSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RuleSetEdition() As ExpertRuleSet (Read Only)
                |     Returns the editable object corresponding to this ruleset. Be careful that,
                |     according to your licence, or the type of ruleset you're handling, you may not
                |     have the right to edit the ruleset.
                | 
                |     Example:
                | 
                |          Dim aRuleSetEdition As ExpertRuleSet
                |          Set aRuleSetEdition = aRuleSetRuntime.RuleSetEdition
                | 
                |          If not(aRuleSetEdition is Nothing) Then
                |            ' .. some actions
                |          End if

        :return: ExpertRuleSet
        """

        return ExpertRuleSet(self.com_object.RuleSetEdition)

    def status(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Status() As long
                |     Returns the Status of the ruleset: 1=OK, 0=KO.
                | 
                |     Example:
                | 
                |          Dim RuleSet1 As ExpertRuleSet 
                |          Set RuleSet1 = RuleSet.ExpertGenericRuleBaseComponentRuntimes.Item("RuleSet1")
                |          status = RuleSet1.Status ()
                |          
                | 
                |     Returns:
                |         Status of the ruleset

        :return: int
        """
        return self.com_object.Status()

    def __repr__(self):
        return f'ExpertRuleSetRuntime(name="{ self.name }")'
