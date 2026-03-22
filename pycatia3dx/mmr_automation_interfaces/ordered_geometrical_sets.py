#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.ordered_geometrical_set import OrderedGeometricalSet
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class OrderedGeometricalSets(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OrderedGeometricalSets
                | 
                | A collection of the OrderedGeometricalSet objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OrderedGeometricalSet)
        self.com_object = com_object

    def add(self) -> OrderedGeometricalSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Add() As OrderedGeometricalSet
                |     Creates a new ordered geometrical set and adds it to the
                |     OrderedGeometricalSets collection. Thisordered geometrical set becomes the
                |     current one
                | 
                |     Returns:
                |         The created ordered geometrical set 
                |     Example:
                |         The following example creates a ordered geometrical set named
                |         newOrderedGeometricalSet in the ordered geometrical set collection of the
                |         rootPart part in the 3D shape. NewPartBody becomes the in work
                |         object.
                | 
                |          Set NewPartBody = rootPart.OrderedGeometricalSets.Add()

        :return: OrderedGeometricalSet
        """
        return OrderedGeometricalSet(self.com_object.Add())

    def item(self, i_index: CATVariant) -> OrderedGeometricalSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As OrderedGeometricalSet
                |     Returns a ordered geometrical set using its index or its name from the
                |     ordered geometrical set collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the ordered geometrical set to retrieve
                |             from the collection of ordered geometrical sets. As a numerics, this index is
                |             the rank of the ordered geometrical set in the collection. The index of the
                |             first ordered geometrical set in the collection is 1, and the index of the last
                |             ordered geometrical set is Count. As a string, it is the name you assigned to
                |             the ordered geometrical set using the AnyObject.Name property.
                |             
                | 
                |     Returns:
                |         The retrieved ordered geometrical set 
                |     Example:
                |         This example retrieves in ThisOrderedGeometricalSet the fifth ordered
                |         geometrical set in the collection and in ThatOrderedGeometricalSet the ordered
                |         geometrical set named MyOrderedGeometricalSet in the ordered geometrical set
                |         collection of the 3D shape.
                | 
                |          Set orderedGeometricalSetColl = Part.OrderedGeometricalSets
                |          Set ThisOrderedGeometricalSet = orderedGeometricalSetColl.Item(5)
                |          Set ThatOrderedGeometricalSet = orderedGeometricalSetColl.Item("MyOrderedGeometricalSet")

        :param CATVariant i_index:
        :return: OrderedGeometricalSet
        """
        return OrderedGeometricalSet(self.com_object.Item(i_index))

    def __repr__(self):
        return f'OrderedGeometricalSets(name="{self.name}")'
