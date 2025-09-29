"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.material.material_domain import MaterialDomain
from pycatia3dx.plm_modeller_base.plm_entities import PLMEntities
from pycatia3dx.system.collection import Collection


class MaterialDomains(PLMEntities):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMModelerBaseIDLItf.PLMEntities
                |                         MaterialDomains
                | 
                | Represents a collection of Material applicative Domains.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_user_discipline: str, o_domain: MaterialDomain) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Add(CATBSTR iUserDiscipline,MaterialDomain oDomain)
                |     Allow to add a domain in list.
                | 
                |     Parameters:
                | 
                |         iUserType
                |             The user discipline to identify the entity to add.
                |             
                |         oDomain
                |             The new created domain. 
                | 
                |     Example:
                | 
                |          This example shows you how to add a domain in list.
                |            
                | 
                |            Dim oMatRef As Material
                |            Dim oListMatDomains As MaterialDomains
                |            Dim oNewDomain As MaterialDomain
                |            ...
                |            oMatRef.GetDomains oListMatDomains
                |            oListMatDomains.Add "dsc_matref_rep_Rendering",
                |            oNewDomain

        :param str i_user_discipline:
        :param MaterialDomain o_domain:
        :return: None
        """
        return self.com_object.Add(i_user_discipline, o_domain.com_object)

    def get_item_by_discipline(self, i_user_discipline: tuple, o_list_domain: Collection) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetItemByDiscipline(CATSafeArrayVariant iUserDiscipline,Collection
                | oListDomain)
                |     Allow to retrieve domains in list.
                | 
                |     Parameters:
                | 
                |         iUserDiscipline
                |             The user discipline to identify the entities to get.
                |             
                |         oListDomain
                |             The list of domains found. 
                | 
                |     Example:
                | 
                |          This example shows you how to retrieve domains in
                |          list.
                |            
                | 
                |            Dim oMatRef As Material
                |            Dim listDomFilt 'As ListObject
                |            ReDim myListDisc(0) 'As Collection
                |            myListDisc(0) = "dsc_matref_rep_Sample"
                |            Dim oListDomains As Object
                |            ...
                |            oMatRef.GetDomains oListDomains
                |            oListDomains.GetItemByDiscipline myListDisc,
                |            listDomFilt

        :param tuple i_user_discipline:
        :param Collection o_list_domain:
        :return: None
        """
        return self.com_object.GetItemByDiscipline(i_user_discipline, o_list_domain.com_object)

    def __repr__(self):
        return f'MaterialDomains(name="{self.name}")'
