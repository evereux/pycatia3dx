"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_know_how.expert_rule_base_runtime import ExpertRuleBaseRuntime


class ExpertRuleBase(ExpertRuleBaseRuntime):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                        
                |                        KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                KnowHowIDLItf.ExpertRuleBaseRuntime
                |                                     ExpertRuleBase
                | 
                | Represents the RuleBase object that can be edited.
                | 
                | See also:
                |     ExpertRuleBaseRuntime.RuleBaseEdition,
                |     ExpertRuleBasesFactory.CreateRuleBase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def volatile_copy(self) -> ExpertRuleBaseRuntime:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func VolatileCopy() As ExpertRuleBaseRuntime
                |     Copy the persistent rulebase in a unpersistent unchangeable
                |     rulebase.
                | 
                |     Returns:
                |         A volatile copy of the rulebase To use this method, you must have the
                |         Knowledge Expert 1 license (runtime)

        :return: ExpertRuleBaseRuntime
        """
        return ExpertRuleBaseRuntime(self.com_object.VolatileCopy())

    def __repr__(self):
        return f'ExpertRuleBase(name="{ self.name }")'
