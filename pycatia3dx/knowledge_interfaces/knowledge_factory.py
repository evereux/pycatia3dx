#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.knowledge_collection import KnowledgeCollection
from pycatia3dx.system.any_object import AnyObject


class KnowledgeFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeFactory
                | 
                | Generic factory for creating Knowledge objects.
                | 
                | See also:
                |     KnowledgeSet.Factory
    
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
                |     Returns the collection of Knowledge objects owned by the root.

        :return: KnowledgeCollection
        """

        return KnowledgeCollection(self.com_object.Collection)

    @property
    def root(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Root() As CATBaseDispatch (Read Only)
                |     Returns the object on which the objects will be created.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Root)

    def __repr__(self):
        return f'KnowledgeFactory(name="{ self.name }")'
