"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class ListObject(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ListObject
                | 
                | Specializes Collection for Material.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=PLMEntity)
        self.com_object = com_object

    def add(self, i_item_value: PLMEntity) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(PLMEntity iItemValue)
                |     Allow to add an object in list.
                | 
                |     Parameters:
                | 
                |         iItemValue
                |             the object to add 
                | 
                |     Example:
                | 
                |          This example shows you how to add an object in list.
                |            
                | 
                |            Dim myListObject As CATIAListObject
                |            Dim iMyObject As CATIAPLMEntity
                |            ...
                |            myListObject.Add iMyObject

        :param PLMEntity i_item_value:
        :return: None
        """
        return self.com_object.Add(i_item_value.com_object)

    def get(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Get(CATVariant iIndex) As CATBaseDispatch
                |     Retrieves a Material object from the list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index in the list 
                |         oObject
                |             the retrieved object 
                | 
                |     Example:
                | 
                |          This example shows you how to get an object in list.
                |            
                | 
                |            Dim myListObject As CATIAListObject
                |            Dim oMyObject As CATBaseDispatch
                |            ...
                |            Set oMyObject = myListObject.Get (1)

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Get(i_index)

    def item(self, i_index: CATVariant) -> PLMEntity:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As PLMEntity
                |     Allow to get an object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index in the list 
                |         oObject
                |             the retrieved object 
                | 
                |     Example:
                | 
                |          This example shows you how to get an object in list.
                |            
                | 
                |            Dim myListObject As CATIAListObject
                |            Dim oMyObject As CATIAPLMEntity
                |            ...
                |            Set oMyObject = myListObject.Item (1)

        :param CATVariant i_index:
        :return: PLMEntity
        """
        return PLMEntity(self.com_object.Item(i_index))

    def remove(self, i_item_value: PLMEntity) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(PLMEntity iItemValue)
                |     Allow to remove an object.
                | 
                |     Parameters:
                | 
                |         iItemValue
                |             the object to remove 
                | 
                |     Example:
                | 
                |          This example shows you how to remove an object in
                |          list.
                |            
                | 
                |            Dim myListObject As CATIAListObject
                |            Dim iMyObject As CATIAPLMEntity
                |            ...
                |            myListObject.Remove iMyObject

        :param PLMEntity i_item_value:
        :return: None
        """
        return self.com_object.Remove(i_item_value.com_object)

    def __getitem__(self, n: int) -> PLMEntity:
        if (n + 1) > self.count:
            raise StopIteration

        return PLMEntity(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[PLMEntity]:
        for i in range(self.count):
            yield PLMEntity(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'ListObject(name="{self.name}")'
