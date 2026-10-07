"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.material.material import Material
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Materials(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Materials
                | 
                | Represents a collection of Material Entities.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Material)
        self.com_object = com_object

    def add(self, i_material: Material) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(Material iMaterial)
                |     Allow to add a material in list.
                | 
                |     Parameters:
                | 
                |         iMaterial
                |             the material to add 
                | 
                |     Example:
                | 
                |          This example shows you how to add a material in list.
                |            
                | 
                |            Dim myMatRef As Material
                |            Dim myListMatRef As Materials
                |            ...
                |            myListMatRef.Add myMatRef

        :param Material i_material:
        :return: None
        """
        return self.com_object.Add(i_material.com_object)

    def item(self, i_index: CATVariant) -> Material:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As Material
                |     Allow to get a material.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index in the list 
                |         oMaterial
                |             the retrieved material 
                | 
                |     Example:
                | 
                |          This example shows you how to get a material in list.
                |            
                | 
                |            Dim myListMatRef As Materials
                |            Dim myMatRef As Material
                |            ...
                |            Set myMatRef = myListMatRef.Item (1)

        :param CATVariant i_index:
        :return: Material
        """
        return Material(self.com_object.Item(i_index))

    def remove(self, i_material: Material) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(Material iMaterial)
                |     Allow to remove a material.
                | 
                |     Parameters:
                | 
                |         iItemValue
                |             the material to remove 
                | 
                |     Example:
                | 
                |          This example shows you how to remove a material in
                |          list.
                |            
                | 
                |            Dim myListMatRef As Materials
                |            Dim myMatRef As Material
                |            ...
                |            myListMatRef.Remove myMatRef

        :param Material i_material:
        :return: None
        """
        return self.com_object.Remove(i_material.com_object)

    def __getitem__(self, n: int) -> Material:
        if (n + 1) > self.count:
            raise StopIteration

        return Material(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Material]:
        for i in range(self.count):
            yield Material(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Materials(name="{self.name}")'
