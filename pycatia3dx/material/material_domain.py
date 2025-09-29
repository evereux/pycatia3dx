"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.material.material_domain_content import MaterialDomainContent
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity


class MaterialDomain(PLMEntity):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         MaterialDomain
                | 
                | Represents a Material applicative Domain.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def material_domain_content(self) -> MaterialDomainContent:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialDomainContent() As MaterialDomainContent (Read
                | Only)
                |     Allow to get material domain content.
                | 
                |     Parameters:
                | 
                |         oMatDomContent
                |             The retrieved material domain content. 
                | 
                |     Example:
                | 
                |          This example shows you how to get all material's
                |          domains.
                |            
                | 
                |            Dim Domain As MaterialDomain
                |            Dim oMaterialDomainContent As MaterialDomainContent
                |            ...
                |            Set oMaterialDomainContent = Domain.MaterialDomainContent

        :return: MaterialDomainContent
        """

        return MaterialDomainContent(self.com_object.MaterialDomainContent)

    def __repr__(self):
        return f'MaterialDomain(name="{self.name}")'
