"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.unit import Unit
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Units(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Units
                | 
                | Represents the collection of Units.
                | 
                | See also:
                |     KnowledgeObjects.Units
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Unit)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> Unit:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As Unit
                |     Returns a unit using its index or its name from the Parameters
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the unit to retrieve from the collection
                |             of parameters. As a numerics, this index is the rank of the unit in the
                |             collection. The index of the first unit in the collection is 1, and the index
                |             of the last parameter is Count. As a string, it is the name you assigned to the
                |             parameter using the AnyObject.Name property or when creating the parameter.
                |             
                | 
                |     Returns:
                |         Unit retrieved 
                |     Example:
                |         This example retrieves the millimeter unit in the units
                |         collection:
                | 
                |          Set unitmm = units.Item("mm")

        :param CATVariant i_index:
        :return: Unit
        """
        return Unit(self.com_object.Item(i_index))

    def __repr__(self):
        return f'Units(name="{self.name}")'
