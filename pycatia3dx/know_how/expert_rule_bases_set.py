"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.knowledge_set import KnowledgeSet


class ExpertRuleBasesSet(KnowledgeSet):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeSet
                |                         ExpertRuleBasesSet
                | 
                | Interface representing the set of rule bases.
                | Example : how to create an ExpertRuleBasesSet
                | 
                |  Dim part As VPMRepReference
                |  Set part = ...
                |  Dim rulebasesset As ExpertRuleBasesSet
                |  Set rulebasesset = part.GetItem("KnowledgeObjects").GetKnowledgeRootSet(True, 3)
                |  
                | 
                | See also:
                |     KnowledgeObjects
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'ExpertRuleBasesSet(name="{ self.name }")'
