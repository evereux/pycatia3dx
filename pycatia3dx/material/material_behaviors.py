"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.material.material_behavior import MaterialBehavior
from pycatia3dx.plm_modeller_base.plm_entities import PLMEntities
from pycatia3dx.types.general import CATVariant


class MaterialBehaviors(PLMEntities):
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
                |                         MaterialBehaviors
                | 
                | Represents a Material Behavior Collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_simulation_behavior(self) -> MaterialBehavior:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func AddSimulationBehavior() As MaterialBehavior
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
                |            Dim oListBehavior As MaterialBehaviors
                |            ...
                |            oMatRef.GetSimulationBehaviors oListBehavior
                |            oListMatDomains.AddSimulationBehavior oBehavior

        :return: MaterialBehavior
        """
        return MaterialBehavior(self.com_object.AddSimulationBehavior())

    def get_behavior(self, i_index: CATVariant) -> MaterialBehavior:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetBehavior(CATVariant iIndex) As MaterialBehavior
                |     Allow to get a Behavior.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index in the list 
                |         oMaterial
                |             the retrieved behavior 
                | 
                |     Example:
                | 
                |          This example shows you how to get a behavior in list.
                |            
                | 
                |            Dim myBehaviorList As CATIAMaterialBehaviors
                |            Dim myBehavior As MaterialBehavior
                |            ...
                |            Set myBehavior = myBehaviorList.Item (1)

        :param CATVariant i_index:
        :return: MaterialBehavior
        """
        return MaterialBehavior(self.com_object.GetBehavior(i_index))

    def remove(self, i_behavior: MaterialBehavior) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Remove(MaterialBehavior iBehavior)
                |     Allow to remove a material.
                | 
                |     Parameters:
                | 
                |         iBehavior
                |             the behavior to remove 
                | 
                |     Example:
                | 
                |          This example shows you how to remove a material in
                |          list.
                |            
                | 
                |            Dim myBehaviorList As CATIAMaterialBehaviors
                |            Dim myBehavior As MaterialBehavior
                |            ...
                |            myBehaviorList.Remove myBehavior

        :param MaterialBehavior i_behavior:
        :return: None
        """
        return self.com_object.Remove(i_behavior.com_object)

    def __repr__(self):
        return f'MaterialBehaviors(name="{self.name}")'
