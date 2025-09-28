"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.knowledge_services import KnowledgeServices
from pycatia3dx.knowledge_interfaces.knowledge_set import KnowledgeSet


class KnowledgeObjects(KnowledgeServices):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         KnowledgeIDLItf.KnowledgeServices
                |                             KnowledgeObjects
                | 
                | Interface allowing the access to Knowledge objects.
                | Example of how to retrieve such an object.
                | 
                |  Dim aRepRef as VPMRepReference
                |  Set aRepRef = ...
                |  Dim aKOs as KnowledgeObjects
                |  Set aKOs = aRepRef.GetItem("KnowledgeObjects")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_knowledge_root_set(self, i_create_or_not: bool, i_k_set_type: int) -> KnowledgeSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetKnowledgeRootSet(boolean iCreateOrNot,KnowledgeSetType iKSetType) As
                | KnowledgeSet
                |     Retrieves (or creates) a root Knowledge set of a certain
                |     type.
                | 
                |     Parameters:
                | 
                |         iCreateOrNot
                |             True or False 
                |         iKSetType
                |             Type of the wanted set 
                | 
                |     Returns:
                |         the set

        :param bool i_create_or_not:
        :param int i_k_set_type:
        :return: KnowledgeSet
        """
        return KnowledgeSet(self.com_object.GetKnowledgeRootSet(i_create_or_not, i_k_set_type))

    def __repr__(self):
        return f'KnowledgeObjects(name="{ self.name }")'
