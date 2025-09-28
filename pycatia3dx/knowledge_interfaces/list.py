"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class List(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     List
                | 
                | Represents the value of a list parameter.
                | 
                | See also:
                |     ListParameter.ValueList
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_item_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Add(AnyObject iItemValue)
                |     Adds an item at the end of the list. Does an AddRef on the item. Returns
                |     E_FAIL if the object type is not correct. Will return E_FAIL if trying to set
                |     an already existing element while IsDuplicateElementsAllowed is false. The
                |     object must be in the same container as the list. This will be enforced in the
                |     future.
                | 
                |     Parameters:
                | 
                |         iItemValue
                |             vqlue added

        :param AnyObject i_item_value:
        :return: None
        """
        return self.com_object.Add(i_item_value.com_object)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As AnyObject
                |     Retrieves a Feature using its index or its name from the Features
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Feature to retrieve from the
                |             collection of Features. As a numerics, this index is the rank of the Feature in
                |             the collection. The index of the first Feature in the collection is 1, and the
                |             index of the last Feature is Count. As a string, it is the name you assigned to
                |             the Feature using the AnyObject.Name property or when creating the Feature.
                |             
                | 
                |     Returns:
                |         The retrieved Feature 
                |     Example:
                |         This example retrieves the last Feature in the Features
                |         collection.
                | 
                |          Dim lastFeature As CATIABase
                |          Set lastFeature = Features.Item(Features.Count)

        :param CATVariant i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Feature from the Features collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Feature to retrieve from the
                |             collection of Features. As a numerics, this index is the rank of the Feature in
                |             the collection. The index of the first Feature in the collection is 1, and the
                |             index of the last Feature is Count. As a string, it is the name you assigned to
                |             the Feature using the AnyObject.Name property or when creating the Feature.
                |             
                | 
                |     Example:
                |         This example removes the Feature named density from the Features
                |         collection.
                | 
                |          Features.Remove("density")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def reorder(self, i_index_current: CATVariant, i_index_target: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Reorder(CATVariant iIndexCurrent,CATVariant iIndexTarget)
                |     Reorders an element by moving it from the current position to the target
                |     position. Doesn't change the list if either position is out of the list. Return
                |     E_FAIL if cannot reorder.
                | 
                |     Parameters:
                | 
                |         iIndexCurrent
                |             current position of the item to reorder. 
                |         iIndexTarget
                |             target position.

        :param CATVariant i_index_current:
        :param CATVariant i_index_target:
        :return: None
        """
        return self.com_object.Reorder(i_index_current, i_index_target)

    def replace(self, i_index: CATVariant, i_item_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Replace(CATVariant iIndex,AnyObject iItemValue)
                |     Sets an item in the list at a position. Does an AddRef on the item. Returns
                |     E_FAIL if the object type is not correct or the index is out of bounds. Returns
                |     E_FAIL if trying to set an already existing element while
                |     IsDuplicateElementsAllowed is false.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index in the list (starts at 1). 
                |         iItemValue
                |             item to replace The object must be in the same container as the
                |             list. This will be enforced in the future.

        :param CATVariant i_index:
        :param AnyObject i_item_value:
        :return: None
        """
        return self.com_object.Replace(i_index, i_item_value.com_object)

    def __repr__(self):
        return f'List(name="{ self.name }")'
