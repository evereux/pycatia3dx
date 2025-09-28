"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.knowledge_factory import KnowledgeFactory
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class KnowledgeCollection(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     KnowledgeCollection
                | 
                | Collection of Knowledge objects.
                | 
                | See also:
                |     KnowledgeSet.Collection, KnowledgeCollection.Find
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def factory(self) -> KnowledgeFactory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Factory() As KnowledgeFactory (Read Only)
                |     Returns a Knowledge factory for creating objects in this collection.

        :return: KnowledgeFactory
        """

        return KnowledgeFactory(self.com_object.Factory)

    def find(self, i_object_type: int, i_recursively: bool) -> 'KnowledgeCollection':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Find(KnowledgeObjectType iObjectType,boolean iRecursively) As
                | KnowledgeCollection
                |     Finds objects under the current collection, responding to the given
                |     type.
                | 
                |     Parameters:
                | 
                |         iObjectType
                |             Type of the wanted objects 
                |         iRecursively
                |             Recursive traversal or not 
                | 
                |     Returns:
                |         a collection of found objects

        :param int i_object_type:
        :param bool i_recursively:
        :return: KnowledgeCollection
        """
        return KnowledgeCollection(self.com_object.Find(i_object_type, i_recursively))

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Retrieves a direct child using its index or its name.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of the wanted object 
                | 
                |     Returns:
                |         the wanted object

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Remove(CATVariant iIndex)
                |     Removes a direct child using its index or its name.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of the object to remove

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'KnowledgeCollection(name="{ self.name }")'
