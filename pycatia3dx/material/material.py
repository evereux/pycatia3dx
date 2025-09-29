"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.material.material_behaviors import MaterialBehaviors
from pycatia3dx.material.material_domains import MaterialDomains
from pycatia3dx.material.material_generic import MaterialGeneric


class Material(MaterialGeneric):
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
                |                         CATMaterialIDLItf.MaterialGeneric
                |                             Material
                | 
                | Represents a Material Entity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_domains(self, o_list_domain: MaterialDomains) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetDomains(MaterialDomains oListDomain)
                |     Allow to get all material's domains.
                | 
                |     Parameters:
                | 
                |         oListDomain
                |             List of domains 
                | 
                |     Example:
                | 
                |          This example shows you how to get all material's
                |          domains.
                |            
                | 
                |            Dim MatRef As Material
                |            Dim ListDomain As MaterialDomains
                |            ...
                |            MatRef.GetDomains ListDomain

        :param MaterialDomains o_list_domain:
        :return: None
        """
        return self.com_object.GetDomains(o_list_domain.com_object)

    def get_simulation_behaviors(self, o_list_behavior: MaterialBehaviors) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetSimulationBehaviors(MaterialBehaviors oListBehavior)
                |     Allow to get all material's simulation behaviors.
                | 
                |     Parameters:
                | 
                |         oListBehavior
                |             List of behaviors 
                | 
                |     Example:
                | 
                |          This example shows you how to get all material's simulation
                |          behaviors.
                |            
                | 
                |            Dim MatRef As Material
                |            Dim ListBehavior As MaterialBehaviors
                |            ...

        :param MaterialBehaviors o_list_behavior:
        :return: None
        """
        return self.com_object.GetSimulationBehaviors(o_list_behavior.com_object)

    def __repr__(self):
        return f'Material(name="{self.name}")'
