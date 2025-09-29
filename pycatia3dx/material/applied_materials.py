"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.material.applied_material import AppliedMaterial
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class AppliedMaterials(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AppliedMaterials
                | 
                | Manages material application collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_applied_material: AppliedMaterial) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(AppliedMaterial iAppliedMaterial)
                |     Allow to add an applied-material.
                | 
                |     Parameters:
                | 
                |         iAppliedMaterial
                |             the applied-material to add 
                | 
                |     Example:
                | 
                |          This example shows you how to add an
                |          applied-material.
                |            
                | 
                |            Dim ListAppliedMaterial As CATIAAppliedMaterials
                |            Dim iAppliedMaterial As CATIAAppliedMaterial
                |            ...
                |            ListAppliedMaterial.Add iAppliedMaterial

        :param AppliedMaterial i_applied_material:
        :return: None
        """
        return self.com_object.Add(i_applied_material.com_object)

    def item(self, i_index: CATVariant) -> AppliedMaterial:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As AppliedMaterial
                |     Allow to get an applied-material.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index in the list 
                |         oAppliedMaterial
                |             the retrieved applied-material 
                | 
                |     Example:
                | 
                |          This example shows you how to get an
                |          applied-material.
                |            
                | 
                |            Dim ListAppliedMaterial As CATIAAppliedMaterials
                |            Dim oAppliedMaterial As CATIAAppliedMaterial
                |            ...
                |            Set oAppliedMaterial = ListAppliedMaterial.Item (1)

        :param CATVariant i_index:
        :return: AppliedMaterial
        """
        return AppliedMaterial(self.com_object.Item(i_index))

    def remove(self, i_applied_material: AppliedMaterial) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(AppliedMaterial iAppliedMaterial)
                |     Allow to remove an applied-material.
                | 
                |     Parameters:
                | 
                |         iAppliedMaterial
                |             the applied-material to remove 
                | 
                |     Example:
                | 
                |          This example shows you how to remove an
                |          applied-material.
                |            
                | 
                |            Dim ListAppliedMaterial As CATIAAppliedMaterials
                |            Dim iAppliedMaterial As CATIAAppliedMaterial
                |            ...
                |            ListAppliedMaterial.Remove iAppliedMaterial

        :param AppliedMaterial i_applied_material:
        :return: None
        """
        return self.com_object.Remove(i_applied_material.com_object)

    def __repr__(self):
        return f'AppliedMaterials(name="{self.name}")'
