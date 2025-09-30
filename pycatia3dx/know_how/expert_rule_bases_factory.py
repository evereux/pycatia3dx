"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.knowledge_factory import KnowledgeFactory
from pycatia3dx.todo_know_how.expert_rule_base import ExpertRuleBase


class ExpertRuleBasesFactory(KnowledgeFactory):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeFactory
                |                         ExpertRuleBasesFactory
                | 
                | Interface representing the factory for rule bases.
                | Example of how to retrieve an ExpertRuleBasesFactory.
                | 
                |  Dim part As VPMRepReference
                |  Set part = ...
                |  Dim rulebasesset As ExpertRuleBasesSet
                |  Set rulebasesset = part.GetItem("KnowledgeObjects").GetKnowledgeRootSet(False, 3)
                |  Dim RulebaseFact As ExpertRuleBasesFactory
                |  If not(rulebasesset is nothing) Then
                |    Set RulebaseFact = rulebasesset.Factory
                |    ...
                |  End If
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_rule_base(self, i_name: str) -> ExpertRuleBase:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRuleBase(CATBSTR iName) As ExpertRuleBase
                |     Creates a rulebase.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the rulebase. 
                | 
                |     Returns:
                |         The created rulebase. The following example shows how to create the
                |         Rule Base RB1 in a product representation reference :
                | 
                |          Dim RulebaseFact As ExpertRuleBasesFactory
                |          Set RulebaseFact = ...
                |          Set RuleBase = RulebaseFact.CreateRuleBase("RB1")
                |          
                | 
                |     See also:
                |         CATIAExpertRuleBase To use this method, you must have the Knowledge
                |         Expert license (buildtime)

        :param str i_name:
        :return: ExpertRuleBase
        """
        return ExpertRuleBase(self.com_object.CreateRuleBase(i_name))

    def __repr__(self):
        return f'ExpertRuleBasesFactory(name="{ self.name }")'
