"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.knowledge_interfaces.knowledge_collection import KnowledgeCollection
from pycatia3dx.knowledge_interfaces.units import Units
from pycatia3dx.system.any_object import AnyObject


class KnowledgeServices(Service):

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
                |                         KnowledgeServices
                | 
                | Interface allowing the access to Knowledge services.
                | Example of how to retrieve such an object.
                | 
                |  Dim aKServ as KnowledgeServices
                |  Set aKServ = CATIA.GetSessionService("KnowledgeServices")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def units(self) -> Units:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Units() As Units (Read Only)
                |     Returns the collection of units.

        :return: Units
        """

        return Units(self.com_object.Units)

    def get_knowledge_collection(self, i_root: AnyObject, i_k_set_type: int) -> KnowledgeCollection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetKnowledgeCollection(AnyObject iRoot,KnowledgeSetType iKSetType) As
                | KnowledgeCollection
                |     Retrieves a Knowledge collection-like aspect of an object.
                | 
                |     Parameters:
                | 
                |         iRoot
                |             The object on which to access Knowledge components
                |             
                |         iKSetType
                |             Type of the wanted Knowledge components 
                | 
                |     Returns:
                |         a KnowledgeCollection

        :param AnyObject i_root:
        :param int i_k_set_type:
        :return: KnowledgeCollection
        """
        return KnowledgeCollection(self.com_object.GetKnowledgeCollection(i_root.com_object, i_k_set_type))

    def __repr__(self):
        return f'KnowledgeServices(name="{ self.name }")'
