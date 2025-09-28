"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.knowledge_collection import KnowledgeCollection
from pycatia3dx.knowledge_interfaces.knowledge_factory import KnowledgeFactory
from pycatia3dx.system.any_object import AnyObject


class KnowledgeSet(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeSet
                | 
                | Base interface for Knowledge sets.
                | 
                | See also:
                |     KnowledgeObjects.GetKnowledgeRootSet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def collection(self) -> KnowledgeCollection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Collection() As KnowledgeCollection (Read Only)
                |     Returns a collection for accessing objects of the kind of the set.

        :return: KnowledgeCollection
        """

        return KnowledgeCollection(self.com_object.Collection)

    @property
    def factory(self) -> KnowledgeFactory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Factory() As KnowledgeFactory (Read Only)
                |     Returns a factory for creating objects of the kind of the set.

        :return: KnowledgeFactory
        """

        return KnowledgeFactory(self.com_object.Factory)

    def __repr__(self):
        return f'KnowledgeSet(name="{ self.name }")'
